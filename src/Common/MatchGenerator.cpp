#ifdef __clang__
#  pragma clang diagnostic push
#  pragma clang diagnostic ignored "-Wzero-as-null-pointer-constant"
#  pragma clang diagnostic ignored "-Wgnu-anonymous-struct"
#  pragma clang diagnostic ignored "-Wnested-anon-types"
#  pragma clang diagnostic ignored "-Wunused-parameter"
#  pragma clang diagnostic ignored "-Wshadow-field-in-constructor"
#  pragma clang diagnostic ignored "-Wdtor-name"
#endif
#include <re2/re2.h>
#include <re2/regexp.h>
#include <re2/walker-inl.h>
#ifdef __clang__
#  pragma clang diagnostic pop
#endif

#ifdef LOG_INFO
#undef LOG_INFO
#undef LOG_WARNING
#undef LOG_ERROR
#undef LOG_FATAL
#endif

#include "MatchGenerator.h"

#include <Common/Exception.h>
#include <Common/logger_useful.h>
#include <Common/thread_local_rng.h>
#include <random>
#include <map>
#include <functional>
#include <magic_enum.hpp>

namespace DB
{
namespace ErrorCodes
{
extern const int BAD_ARGUMENTS;
extern const int LOGICAL_ERROR;
}
}


namespace re2
{

class RandomStringPrepareWalker : public Regexp::Walker<Regexp *>
{
private:
    static constexpr int ImplicitMax = 100;

    using Children = std::vector<Regexp *>;

    class Generators;

    /// This function objects look much prettier than lambda expression when stack traces are printed
    class NodeFunction
    {
    public:
        virtual String operator() () = 0;
        virtual ~NodeFunction() = default;
    };

    using NodeFunctionPtr = std::shared_ptr<NodeFunction>;
    using NodeFuncs = std::vector<NodeFunctionPtr>;

    static NodeFuncs getFuncs(Children children_, const Generators & generators_)
    {
        NodeFuncs result;
        result.reserve(children_.size());

        for (auto * child: children_)
        {
            result.push_back(generators_.at(child));
        }

        return result;
    }

    class Generators: public std::map<re2::Regexp *, NodeFunctionPtr> {};

    class RegexpConcatFunction : public NodeFunction
    {
    public:
        RegexpConcatFunction(Children children_, const Generators & generators_)
            : children(getFuncs(children_, generators_))
        {
        }

        String operator () () override
        {
            size_t total_size = 0;

            std::vector<String> part_result;
            part_result.reserve(children.size());
            for (auto & child: children)
            {
                part_result.push_back(child->operator()());
                total_size += part_result.back().size();
            }

            String result;
            result.reserve(total_size);
            for (auto & part: part_result)
            {
                result += part;
            }

            return result;
        }

    private:
        NodeFuncs children;
    };

    class RegexpAlternateFunction : public NodeFunction
    {
    public:
        RegexpAlternateFunction(Children children_, const Generators & generators_)
            : children(getFuncs(children_, generators_))
        {
        }

        String operator () () override
        {
            std::uniform_int_distribution<int> distribution(0, static_cast<int>(children.size()-1));
            int chosen = distribution(thread_local_rng);
            return children[chosen]->operator()();
        }

    private:
        NodeFuncs children;
    };

    class RegexpRepeatFunction : public NodeFunction
    {
    public:
        RegexpRepeatFunction(Regexp * re_, const Generators & generators_, int min_repeat_, int max_repeat_)
            : func(generators_.at(re_))
            , min_repeat(min_repeat_)
            , max_repeat(max_repeat_)
        {
        }

        String operator () () override
        {
            std::uniform_int_distribution<int> distribution(min_repeat, max_repeat);
            int chosen = distribution(thread_local_rng);

            String result;
            for (int i = 0; i < chosen; ++i)
                result += func->operator()();
            return result;
        }

    private:
        NodeFunctionPtr func;
        int min_repeat = 0;
        int max_repeat = 0;
    };

    class RegexpCharClassFunction : public NodeFunction
    {
        using CharRanges = std::vector<std::pair<re2::Rune, re2::Rune>>;

    public:
        RegexpCharClassFunction(Regexp * re_)
        {
            CharClass * cc = re_->cc();
            chassert(cc);
            if (cc->empty())
                throw DB::Exception(DB::ErrorCodes::BAD_ARGUMENTS, "kRegexpCharClass is empty");

            char_count = cc->size();
            char_ranges.reserve(std::distance(cc->begin(), cc->end()));

            for (auto it = cc->begin(); it != cc->end(); ++it)
            {
                char_ranges.emplace_back(it->lo, it->hi);
            }
        }

        String operator () () override
        {
            std::uniform_int_distribution<int> distribution(1, char_count);
            int chosen = distribution(thread_local_rng);
            int count_down = chosen;

            auto it = char_ranges.begin();
            for (; it != char_ranges.end(); ++it)
            {
                auto [lo, hi] = *it;
                auto range_len = hi - lo + 1;
                if (count_down <= range_len)
                    break;
                count_down -= range_len;
            }

            if (it == char_ranges.end())
                throw DB::Exception(DB::ErrorCodes::LOGICAL_ERROR,
                                    "Unable to choose the rune. Runes {}, ranges {}, chosen {}",
                                    char_count, char_ranges.size(), chosen);

            auto [lo, _] = *it;
            Rune r = lo + count_down - 1;
            int n = re2::runetochar(buffer, &r);
            return String(buffer, n);
        }

    private:
        char buffer[UTFmax];
        int char_count = 0;
        CharRanges char_ranges;
    };

    class RegexpLiteralStringFunction : public NodeFunction
    {
    public:
        RegexpLiteralStringFunction(Regexp * re_)
        {
            if (re_->nrunes() == 0)
                return;

            char buffer[UTFmax];
            for (int i = 0; i < re_->nrunes(); ++i)
            {
                int n = re2::runetochar(buffer, &re_->runes()[i]);
                literal_string += String(buffer, n);
            }
        }

        String operator () () override
        {
            return literal_string;
        }

    private:
        String literal_string;
    };

    class RegexpLiteralFunction : public NodeFunction
    {
    public:
        RegexpLiteralFunction(Regexp * re_)
        {
            char buffer[UTFmax];

            Rune r = re_->rune();
            int n = re2::runetochar(buffer, &r);
            literal = String(buffer, n);
        }

        String operator () () override
        {
            return literal;
        }

    private:
        String literal;
    };

    class ThrowExceptionFunction : public NodeFunction
    {
    public:
        ThrowExceptionFunction(Regexp * re_)
            : operation(magic_enum::enum_name(re_->op()))
        {
        }

        String operator () () override
        {
            throw DB::Exception(
                DB::ErrorCodes::BAD_ARGUMENTS,
                "RandomStringPrepareWalker: regexp node '{}' is not supported for generating a random match",
                operation);
        }

    private:
        String operation;
    };


public:
    RandomStringPrepareWalker(bool logging)
        : logger(logging ? &Poco::Logger::get("GeneratorCombiner") : nullptr)
    {
        if (logger)
            LOG_DEBUG(logger, "GeneratorCombiner");
    }

    std::function<String()> getGenerator()
    {
        if (root == nullptr)
            throw DB::Exception(DB::ErrorCodes::LOGICAL_ERROR, "no root has been set");

        if (generators.size() == 0)
            throw DB::Exception(DB::ErrorCodes::LOGICAL_ERROR, "no generators");

        auto result = [root_func = generators.at(root)] () -> String {
            return root_func->operator()();
        };

        root = nullptr;
        generators.clear();

        return std::move(result);
    }

private:
    Children CopyChildrenArgs(Regexp** children, int nchild)
    {
        Children result;
        result.reserve(nchild);
        for (int i = 0; i < nchild; ++i)
            result.push_back(Copy(children[i]));
        return result;
    }

    Regexp * ShortVisit(Regexp* /*re*/, Regexp * /*parent_arg*/) override
    {
        if (logger)
            LOG_DEBUG(logger, "ShortVisit");
        throw DB::Exception(DB::ErrorCodes::LOGICAL_ERROR, "should not be call");
    }

    Regexp * PreVisit(Regexp * re, Regexp* parent_arg, bool* /*stop*/) override /*noexcept*/
    {
        if (logger)
            LOG_DEBUG(logger, "GeneratorCombiner PreVisit node {}", magic_enum::enum_name(re->op()));

        if (parent_arg == nullptr)
        {
            chassert(root == nullptr);
            chassert(re != nullptr);
            root = re;
        }

        return re;
    }

    Regexp * PostVisit(Regexp * re, Regexp* /*parent_arg*/, Regexp* pre_arg,
                       Regexp ** child_args, int nchild_args) override /*noexcept*/
    {
        if (logger)
            LOG_DEBUG(logger, "GeneratorCombiner PostVisit node {}",
                      magic_enum::enum_name(re->op()));

        switch (re->op())
        {
            case kRegexpConcat: // Matches concatenation of sub_[0..nsub-1].
                generators[re] = std::make_shared<RegexpConcatFunction>(CopyChildrenArgs(child_args, nchild_args), generators);
                break;
            case kRegexpAlternate: // Matches union of sub_[0..nsub-1].
                generators[re] = std::make_shared<RegexpAlternateFunction>(CopyChildrenArgs(child_args, nchild_args), generators);
                break;
            case kRegexpQuest: // Matches sub_[0] zero or one times.
                chassert(nchild_args == 1);
                generators[re] = std::make_shared<RegexpRepeatFunction>(child_args[0], generators, 0, 1);
                break;
            case kRegexpStar: // Matches sub_[0] zero or more times.
                chassert(nchild_args == 1);
                generators[re] = std::make_shared<RegexpRepeatFunction>(child_args[0], generators, 0, ImplicitMax);
                break;
            case kRegexpPlus: // Matches sub_[0] one or more times.
                chassert(nchild_args == 1);
                generators[re] = std::make_shared<RegexpRepeatFunction>(child_args[0], generators, 1, ImplicitMax);
                break;
            case kRegexpCharClass: // Matches character class given by cc_.
                chassert(nchild_args == 0);
                generators[re] = std::make_shared<RegexpCharClassFunction>(re);
                break;
            case kRegexpLiteralString: // Matches runes_.
                chassert(nchild_args == 0);
                generators[re] = std::make_shared<RegexpLiteralStringFunction>(re);
                break;
            case kRegexpLiteral: // Matches rune_.
                chassert(nchild_args == 0);
                generators[re] = std::make_shared<RegexpLiteralFunction>(re);
                break;
            case kRegexpCapture: // Parenthesized (capturing) subexpression.
                chassert(nchild_args == 1);
                generators[re] = generators.at(child_args[0]);
                break;

            case kRegexpNoMatch: // Matches no strings.
            case kRegexpEmptyMatch: // Matches empty string.
            case kRegexpRepeat: // Matches sub_[0] at least min_ times, at most max_ times.
            case kRegexpAnyChar: // Matches any character.
            case kRegexpAnyByte: // Matches any byte [sic].
            case kRegexpBeginLine: // Matches empty string at beginning of line.
            case kRegexpEndLine: // Matches empty string at end of line.
            case kRegexpWordBoundary: // Matches word boundary "\b".
            case kRegexpNoWordBoundary: // Matches not-a-word boundary "\B".
            case kRegexpBeginText: // Matches empty string at beginning of text.
            case kRegexpEndText: // Matches empty string at end of text.
            case kRegexpHaveMatch: // Forces match of entire expression
                generators[re] = std::make_shared<ThrowExceptionFunction>(re);
        }

        return pre_arg;
    }

private:
    Poco::Logger * logger = nullptr;

    Regexp * root = nullptr;
    Generators generators;
};

}


namespace DB
{

void RandomStringGeneratorByRegexp::RegexpPtrDeleter::operator() (re2::Regexp * re) const noexcept
{
    re->Decref();
}

RandomStringGeneratorByRegexp::RandomStringGeneratorByRegexp(String re_str, bool logging)
{
    re2::RE2::Options options;
    options.set_case_sensitive(true);
    options.set_encoding(re2::RE2::Options::EncodingLatin1);
    auto flags = static_cast<re2::Regexp::ParseFlags>(options.ParseFlags());

    re2::RegexpStatus status;
    regexp.reset(re2::Regexp::Parse(re_str, flags, &status));

    if (!regexp)
        throw DB::Exception(DB::ErrorCodes::BAD_ARGUMENTS,
                            "Error parsing regexp '{}': {}",
                            re_str, status.Text());

    regexp.reset(regexp->Simplify());

    auto walker = re2::RandomStringPrepareWalker(logging);
    walker.Walk(regexp.get(), {});
    generatorFunc = walker.getGenerator();

    {
        auto test_check = generate();
        auto matched = RE2::FullMatch(test_check, re2::RE2(re_str));
        if (!matched)
            throw DB::Exception(DB::ErrorCodes::BAD_ARGUMENTS,
                                "Generator is unable to produce random string for regexp '{}': {}",
                                re_str, test_check);
    }
}

String RandomStringGeneratorByRegexp::generate() const
{
    chassert(generatorFunc);
    return generatorFunc();
}

}
