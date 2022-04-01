# These requirements were auto generated
# from software requirements specification (SRS)
# document by TestFlows v1.6.210101.1235930.
# Do not edit by hand but re-generate instead
# using 'tfs requirements generate' command.
from testflows.core import Specification
from testflows.core import Requirement

Heading = Specification.Heading

RQ_SRS008_AES_Functions = Requirement(
    name="RQ.SRS008.AES.Functions",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support [AES] encryption functions to encrypt and decrypt data.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.1.1",
)

RQ_SRS008_AES_Functions_Compatibility_MySQL = Requirement(
    name="RQ.SRS008.AES.Functions.Compatibility.MySQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support [AES] encryption functions compatible with [MySQL 5.7].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.1",
)

RQ_SRS008_AES_Functions_Compatibility_Dictionaries = Requirement(
    name="RQ.SRS008.AES.Functions.Compatibility.Dictionaries",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support encryption and decryption of data accessed on remote\n"
        "[MySQL] servers using [MySQL Dictionary].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.2",
)

RQ_SRS008_AES_Functions_Compatibility_Engine_Database_MySQL = Requirement(
    name="RQ.SRS008.AES.Functions.Compatibility.Engine.Database.MySQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support encryption and decryption of data accessed using [MySQL Database Engine],\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.3",
)

RQ_SRS008_AES_Functions_Compatibility_Engine_Table_MySQL = Requirement(
    name="RQ.SRS008.AES.Functions.Compatibility.Engine.Table.MySQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support encryption and decryption of data accessed using [MySQL Table Engine].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.4",
)

RQ_SRS008_AES_Functions_Compatibility_TableFunction_MySQL = Requirement(
    name="RQ.SRS008.AES.Functions.Compatibility.TableFunction.MySQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support encryption and decryption of data accessed using [MySQL Table Function].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.5",
)

RQ_SRS008_AES_Functions_DifferentModes = Requirement(
    name="RQ.SRS008.AES.Functions.DifferentModes",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL allow different modes to be supported in a single SQL statement\n"
        "using explicit function parameters.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.3.1",
)

RQ_SRS008_AES_Functions_DataFromMultipleSources = Requirement(
    name="RQ.SRS008.AES.Functions.DataFromMultipleSources",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support handling encryption and decryption of data from multiple sources\n"
        "in the `SELECT` statement, including [ClickHouse] [MergeTree] table as well as [MySQL Dictionary],\n"
        "[MySQL Database Engine], [MySQL Table Engine], and [MySQL Table Function]\n"
        "with possibly different encryption schemes.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.1",
)

RQ_SRS008_AES_Functions_SuppressOutputOfSensitiveValues = Requirement(
    name="RQ.SRS008.AES.Functions.SuppressOutputOfSensitiveValues",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL suppress output of [AES] `string` and `key` parameters to the system log,\n"
        "error log, and `query_log` table to prevent leakage of sensitive values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.5.1",
)

RQ_SRS008_AES_Functions_InvalidParameters = Requirement(
    name="RQ.SRS008.AES.Functions.InvalidParameters",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when parameters are invalid.\n" "\n"
    ),
    link=None,
    level=3,
    num="4.6.1",
)

RQ_SRS008_AES_Functions_Mismatched_Key = Requirement(
    name="RQ.SRS008.AES.Functions.Mismatched.Key",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] SHALL return garbage for mismatched keys.\n" "\n"),
    link=None,
    level=3,
    num="4.7.1",
)

RQ_SRS008_AES_Functions_Mismatched_IV = Requirement(
    name="RQ.SRS008.AES.Functions.Mismatched.IV",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return garbage for mismatched initialization vector for the modes that use it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.7.2",
)

RQ_SRS008_AES_Functions_Mismatched_AAD = Requirement(
    name="RQ.SRS008.AES.Functions.Mismatched.AAD",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return garbage for mismatched additional authentication data for the modes that use it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.7.3",
)

RQ_SRS008_AES_Functions_Mismatched_Mode = Requirement(
    name="RQ.SRS008.AES.Functions.Mismatched.Mode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error or garbage for mismatched mode.\n" "\n"
    ),
    link=None,
    level=3,
    num="4.7.4",
)

RQ_SRS008_AES_Functions_Check_Performance = Requirement(
    name="RQ.SRS008.AES.Functions.Check.Performance",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("Performance of [AES] encryption functions SHALL be measured.\n" "\n"),
    link=None,
    level=3,
    num="4.8.1",
)

RQ_SRS008_AES_Function_Check_Performance_BestCase = Requirement(
    name="RQ.SRS008.AES.Function.Check.Performance.BestCase",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "Performance of [AES] encryption functions SHALL be checked for the best case\n"
        "scenario where there is one key, one initialization vector, and one large stream of data.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.8.2",
)

RQ_SRS008_AES_Function_Check_Performance_WorstCase = Requirement(
    name="RQ.SRS008.AES.Function.Check.Performance.WorstCase",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "Performance of [AES] encryption functions SHALL be checked for the worst case\n"
        "where there are `N` keys, `N` initialization vectors and `N` very small streams of data.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.8.3",
)

RQ_SRS008_AES_Functions_Check_Compression = Requirement(
    name="RQ.SRS008.AES.Functions.Check.Compression",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "Effect of [AES] encryption on column compression SHALL be measured.\n" "\n"
    ),
    link=None,
    level=3,
    num="4.8.4",
)

RQ_SRS008_AES_Functions_Check_Compression_LowCardinality = Requirement(
    name="RQ.SRS008.AES.Functions.Check.Compression.LowCardinality",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "Effect of [AES] encryption on the compression of a column with [LowCardinality] data type\n"
        "SHALL be measured.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.8.5",
)

RQ_SRS008_AES_Encrypt_Function = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `encrypt` function to encrypt data using [AES].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.1",
)

RQ_SRS008_AES_Encrypt_Function_Syntax = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Syntax",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the following syntax for the `encrypt` function\n"
        "\n"
        "```sql\n"
        "encrypt(mode, plaintext, key, [iv, aad])\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.2",
)

RQ_SRS008_AES_Encrypt_Function_NIST_TestVectors = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.NIST.TestVectors",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] `encrypt` function output SHALL produce output that matches [NIST test vectors].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.3",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_PlainText = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.PlainText",
    version="2.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `plaintext` with `String`, `FixedString`, `Nullable(String)`,\n"
        "`Nullable(FixedString)`, `LowCardinality(String)`, or `LowCardinality(FixedString(N))` data types as\n"
        "the second parameter to the `encrypt` function that SHALL specify the data to be encrypted.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.4",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_Key = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.Key",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `key` with `String` or `FixedString` data types\n"
        "as the  parameter to the `encrypt` function that SHALL specify the encryption key.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.5",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_Mode = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.Mode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `mode` with `String` or `FixedString` data types as the first parameter\n"
        "to the `encrypt` function that SHALL specify encryption key length and block encryption mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.6",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_Mode_ValuesFormat = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.ValuesFormat",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support values of the form `aes-[key length]-[mode]` for the `mode` parameter\n"
        "of the `encrypt` function where\n"
        "the `key_length` SHALL specifies the length of the key and SHALL accept\n"
        "`128`, `192`, or `256` as the values and the `mode` SHALL specify the block encryption\n"
        "mode and SHALL accept [ECB], [CBC], [CFB128], or [OFB] as well as\n"
        "[CTR] and [GCM] as the values. For example, `aes-256-ofb`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.7",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_Mode_Value_Invalid = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.Value.Invalid",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the specified value for the `mode` parameter of the `encrypt`\n"
        "function is not valid with the exception where such a mode is supported by the underlying\n"
        "[OpenSSL] implementation.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.8",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_Mode_Values = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.Values",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the following [AES] block encryption modes as the value for the `mode` parameter\n"
        "of the `encrypt` function:\n"
        "\n"
        "* `aes-128-ecb` that SHALL use [ECB] block mode encryption with 128 bit key\n"
        "* `aes-192-ecb` that SHALL use [ECB] block mode encryption with 192 bit key\n"
        "* `aes-256-ecb` that SHALL use [ECB] block mode encryption with 256 bit key\n"
        "* `aes-128-cbc` that SHALL use [CBC] block mode encryption with 128 bit key\n"
        "* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 192 bit key\n"
        "* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 256 bit key\n"
        "* `aes-128-cfb128` that SHALL use [CFB128] block mode encryption with 128 bit key\n"
        "* `aes-192-cfb128` that SHALL use [CFB128] block mode encryption with 192 bit key\n"
        "* `aes-256-cfb128` that SHALL use [CFB128] block mode encryption with 256 bit key\n"
        "* `aes-128-ofb` that SHALL use [OFB] block mode encryption with 128 bit key\n"
        "* `aes-192-ofb` that SHALL use [OFB] block mode encryption with 192 bit key\n"
        "* `aes-256-ofb` that SHALL use [OFB] block mode encryption with 256 bit key\n"
        "* `aes-128-gcm` that SHALL use [GCM] block mode encryption with 128 bit key\n"
        "   and [AEAD] 16-byte tag is appended to the resulting ciphertext according to\n"
        "   the [RFC5116]\n"
        "* `aes-192-gcm` that SHALL use [GCM] block mode encryption with 192 bit key\n"
        "   and [AEAD] 16-byte tag is appended to the resulting ciphertext according to\n"
        "   the [RFC5116]\n"
        "* `aes-256-gcm` that SHALL use [GCM] block mode encryption with 256 bit key\n"
        "   and [AEAD] 16-byte tag is appended to the resulting ciphertext according to\n"
        "   the [RFC5116]\n"
        "*  `aes-128-ctr` that SHALL use [CTR] block mode encryption with 128 bit key\n"
        "*  `aes-192-ctr` that SHALL use [CTR] block mode encryption with 192 bit key\n"
        "*  `aes-256-ctr` that SHALL use [CTR] block mode encryption with 256 bit key\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.9",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_InitializationVector = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.InitializationVector",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `iv` with `String` or `FixedString` data types as the optional fourth\n"
        "parameter to the `encrypt` function that SHALL specify the initialization vector for block modes that require\n"
        "it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.10",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_AdditionalAuthenticatedData = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.AdditionalAuthenticatedData",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `aad` with `String` or `FixedString` data types as the optional fifth\n"
        "parameter to the `encrypt` function that SHALL specify the additional authenticated data\n"
        "for block modes that require it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.11",
)

RQ_SRS008_AES_Encrypt_Function_Parameters_ReturnValue = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Parameters.ReturnValue",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return the encrypted value of the data\n"
        "using `String` data type as the result of `encrypt` function.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.12",
)

RQ_SRS008_AES_Encrypt_Function_Key_Length_InvalidLengthError = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.Key.Length.InvalidLengthError",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `key` length is not exact for the `encrypt` function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.13",
)

RQ_SRS008_AES_Encrypt_Function_InitializationVector_Length_InvalidLengthError = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.InitializationVector.Length.InvalidLengthError",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `iv` length is specified and not of the exact size for the `encrypt` function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.14",
)

RQ_SRS008_AES_Encrypt_Function_InitializationVector_NotValidForMode = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.InitializationVector.NotValidForMode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `iv` is specified for the `encrypt` function for a mode that does not need it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.15",
)

RQ_SRS008_AES_Encrypt_Function_AdditionalAuthenticationData_NotValidForMode = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.AdditionalAuthenticationData.NotValidForMode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `aad` is specified for the `encrypt` function for a mode that does not need it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.16",
)

RQ_SRS008_AES_Encrypt_Function_AdditionalAuthenticationData_Length = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.AdditionalAuthenticationData.Length",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL not limit the size of the `aad` parameter passed to the `encrypt` function.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.17",
)

RQ_SRS008_AES_Encrypt_Function_NonGCMMode_KeyAndInitializationVector_Length = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.NonGCMMode.KeyAndInitializationVector.Length",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when the `encrypt` function is called with the following parameter values\n"
        "when using non-GCM modes\n"
        "\n"
        "* `aes-128-ecb` mode and `key` is not 16 bytes or `iv` or `aad` is specified\n"
        "* `aes-192-ecb` mode and `key` is not 24 bytes or `iv` or `aad` is specified\n"
        "* `aes-256-ecb` mode and `key` is not 32 bytes or `iv` or `aad` is specified\n"
        "* `aes-128-cbc` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-192-cbc` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-cbc` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-cfb1` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-192-cfb1` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-cfb1` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-cfb8` mode and `key` is not 16 bytes and if specified `iv` is not 16 bytes\n"
        "* `aes-192-cfb8` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-cfb8` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-cfb128` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-192-cfb128` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-cfb128` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-ofb` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-192-ofb` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-ofb` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-ctr` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes\n"
        "* `aes-192-ctr` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes\n"
        "* `aes-256-ctr` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.18",
)

RQ_SRS008_AES_Encrypt_Function_GCMMode_KeyAndInitializationVector_Length = Requirement(
    name="RQ.SRS008.AES.Encrypt.Function.GCMMode.KeyAndInitializationVector.Length",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when the `encrypt` function is called with the following parameter values\n"
        "when using GCM modes\n"
        "\n"
        "* `aes-128-gcm` mode and `key` is not 16 bytes or `iv` is not specified\n"
        "* `aes-192-gcm` mode and `key` is not 24 bytes or `iv` is not specified\n"
        "* `aes-256-gcm` mode and `key` is not 32 bytes or `iv` is not specified\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.9.19",
)

RQ_SRS008_AES_Decrypt_Function = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `decrypt` function to decrypt data using [AES].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.1",
)

RQ_SRS008_AES_Decrypt_Function_Syntax = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Syntax",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the following syntax for the `decrypt` function\n"
        "\n"
        "```sql\n"
        "decrypt(mode, ciphertext, key, [iv, aad])\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.2",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_CipherText = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.CipherText",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `ciphertext` accepting `FixedString` or `String` data types as\n"
        "the second parameter to the `decrypt` function that SHALL specify the data to be decrypted.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.3",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_Key = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.Key",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `key` with `String` or `FixedString` data types\n"
        "as the third parameter to the `decrypt` function that SHALL specify the encryption key.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.4",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_Mode = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.Mode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `mode` with `String` or `FixedString` data types as the first parameter\n"
        "to the `decrypt` function that SHALL specify encryption key length and block encryption mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.5",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_Mode_ValuesFormat = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.ValuesFormat",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support values of the form `aes-[key length]-[mode]` for the `mode` parameter\n"
        "of the `decrypt` function where\n"
        "the `key_length` SHALL specifies the length of the key and SHALL accept\n"
        "`128`, `192`, or `256` as the values and the `mode` SHALL specify the block encryption\n"
        "mode and SHALL accept [ECB], [CBC], [CFB128], or [OFB] as well as\n"
        "[CTR] and [GCM] as the values. For example, `aes-256-ofb`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.6",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_Mode_Value_Invalid = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.Value.Invalid",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the specified value for the `mode` parameter of the `decrypt`\n"
        "function is not valid with the exception where such a mode is supported by the underlying\n"
        "[OpenSSL] implementation.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.7",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_Mode_Values = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.Values",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the following [AES] block encryption modes as the value for the `mode` parameter\n"
        "of the `decrypt` function:\n"
        "\n"
        "* `aes-128-ecb` that SHALL use [ECB] block mode encryption with 128 bit key\n"
        "* `aes-192-ecb` that SHALL use [ECB] block mode encryption with 192 bit key\n"
        "* `aes-256-ecb` that SHALL use [ECB] block mode encryption with 256 bit key\n"
        "* `aes-128-cbc` that SHALL use [CBC] block mode encryption with 128 bit key\n"
        "* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 192 bit key\n"
        "* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 256 bit key\n"
        "* `aes-128-cfb128` that SHALL use [CFB128] block mode encryption with 128 bit key\n"
        "* `aes-192-cfb128` that SHALL use [CFB128] block mode encryption with 192 bit key\n"
        "* `aes-256-cfb128` that SHALL use [CFB128] block mode encryption with 256 bit key\n"
        "* `aes-128-ofb` that SHALL use [OFB] block mode encryption with 128 bit key\n"
        "* `aes-192-ofb` that SHALL use [OFB] block mode encryption with 192 bit key\n"
        "* `aes-256-ofb` that SHALL use [OFB] block mode encryption with 256 bit key\n"
        "* `aes-128-gcm` that SHALL use [GCM] block mode encryption with 128 bit key\n"
        "   and [AEAD] 16-byte tag is expected present at the end of the ciphertext according to\n"
        "   the [RFC5116]\n"
        "* `aes-192-gcm` that SHALL use [GCM] block mode encryption with 192 bit key\n"
        "   and [AEAD] 16-byte tag is expected present at the end of the ciphertext according to\n"
        "   the [RFC5116]\n"
        "* `aes-256-gcm` that SHALL use [GCM] block mode encryption with 256 bit key\n"
        "   and [AEAD] 16-byte tag is expected present at the end of the ciphertext according to\n"
        "   the [RFC5116]\n"
        "*  `aes-128-ctr` that SHALL use [CTR] block mode encryption with 128 bit key\n"
        "*  `aes-192-ctr` that SHALL use [CTR] block mode encryption with 192 bit key\n"
        "*  `aes-256-ctr` that SHALL use [CTR] block mode encryption with 256 bit key\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.8",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_InitializationVector = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.InitializationVector",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `iv` with `String` or `FixedString` data types as the optional fourth\n"
        "parameter to the `decrypt` function that SHALL specify the initialization vector for block modes that require\n"
        "it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.9",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_AdditionalAuthenticatedData = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.AdditionalAuthenticatedData",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `aad` with `String` or `FixedString` data types as the optional fifth\n"
        "parameter to the `decrypt` function that SHALL specify the additional authenticated data\n"
        "for block modes that require it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.10",
)

RQ_SRS008_AES_Decrypt_Function_Parameters_ReturnValue = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Parameters.ReturnValue",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return the decrypted value of the data\n"
        "using `String` data type as the result of `decrypt` function.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.11",
)

RQ_SRS008_AES_Decrypt_Function_Key_Length_InvalidLengthError = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.Key.Length.InvalidLengthError",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `key` length is not exact for the `decrypt` function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.12",
)

RQ_SRS008_AES_Decrypt_Function_InitializationVector_Length_InvalidLengthError = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.InitializationVector.Length.InvalidLengthError",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `iv` is specified and the length is not exact for the `decrypt` function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.13",
)

RQ_SRS008_AES_Decrypt_Function_InitializationVector_NotValidForMode = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.InitializationVector.NotValidForMode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `iv` is specified for the `decrypt` function\n"
        "for a mode that does not need it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.14",
)

RQ_SRS008_AES_Decrypt_Function_AdditionalAuthenticationData_NotValidForMode = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.AdditionalAuthenticationData.NotValidForMode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `aad` is specified for the `decrypt` function\n"
        "for a mode that does not need it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.15",
)

RQ_SRS008_AES_Decrypt_Function_AdditionalAuthenticationData_Length = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.AdditionalAuthenticationData.Length",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL not limit the size of the `aad` parameter passed to the `decrypt` function.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.16",
)

RQ_SRS008_AES_Decrypt_Function_NonGCMMode_KeyAndInitializationVector_Length = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.NonGCMMode.KeyAndInitializationVector.Length",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when the `decrypt` function is called with the following parameter values\n"
        "when using non-GCM modes\n"
        "\n"
        "* `aes-128-ecb` mode and `key` is not 16 bytes or `iv` or `aad` is specified\n"
        "* `aes-192-ecb` mode and `key` is not 24 bytes or `iv` or `aad` is specified\n"
        "* `aes-256-ecb` mode and `key` is not 32 bytes or `iv` or `aad` is specified\n"
        "* `aes-128-cbc` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-192-cbc` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-cbc` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-cfb1` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-192-cfb1` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-cfb1` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-cfb8` mode and `key` is not 16 bytes and if specified `iv` is not 16 bytes\n"
        "* `aes-192-cfb8` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-cfb8` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-cfb128` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-192-cfb128` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-cfb128` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-ofb` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-192-ofb` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-256-ofb` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified\n"
        "* `aes-128-ctr` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes\n"
        "* `aes-192-ctr` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes\n"
        "* `aes-256-ctr` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.17",
)

RQ_SRS008_AES_Decrypt_Function_GCMMode_KeyAndInitializationVector_Length = Requirement(
    name="RQ.SRS008.AES.Decrypt.Function.GCMMode.KeyAndInitializationVector.Length",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when the `decrypt` function is called with the following parameter values\n"
        "when using GCM modes\n"
        "\n"
        "* `aes-128-gcm` mode and `key` is not 16 bytes or `iv` is not specified\n"
        "* `aes-192-gcm` mode and `key` is not 24 bytes or `iv` is not specified\n"
        "* `aes-256-gcm` mode and `key` is not 32 bytes or `iv` is not specified\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.18",
)

RQ_SRS008_AES_MySQL_Encrypt_Function = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `aes_encrypt_mysql` function to encrypt data using [AES].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.1",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Syntax = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Syntax",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the following syntax for the `aes_encrypt_mysql` function\n"
        "\n"
        "```sql\n"
        "aes_encrypt_mysql(mode, plaintext, key, [iv])\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.2",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_PlainText = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.PlainText",
    version="2.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `plaintext` with `String`, `FixedString`, `Nullable(String)`,\n"
        "`Nullable(FixedString)`, `LowCardinality(String)`, or `LowCardinality(FixedString(N))` data types as\n"
        "the second parameter to the `aes_encrypt_mysql` function that SHALL specify the data to be encrypted.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.3",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Key = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Key",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `key` with `String` or `FixedString` data types\n"
        "as the third parameter to the `aes_encrypt_mysql` function that SHALL specify the encryption key.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.4",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `mode` with `String` or `FixedString` data types as the first parameter\n"
        "to the `aes_encrypt_mysql` function that SHALL specify encryption key length and block encryption mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.5",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_ValuesFormat = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.ValuesFormat",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support values of the form `aes-[key length]-[mode]` for the `mode` parameter\n"
        "of the `aes_encrypt_mysql` function where\n"
        "the `key_length` SHALL specifies the length of the key and SHALL accept\n"
        "`128`, `192`, or `256` as the values and the `mode` SHALL specify the block encryption\n"
        "mode and SHALL accept [ECB], [CBC], [CFB128], or [OFB]. For example, `aes-256-ofb`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.6",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_Value_Invalid = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Value.Invalid",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the specified value for the `mode` parameter of the `aes_encrypt_mysql`\n"
        "function is not valid with the exception where such a mode is supported by the underlying\n"
        "[OpenSSL] implementation.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.7",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_Values = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the following [AES] block encryption modes as the value for the `mode` parameter\n"
        "of the `aes_encrypt_mysql` function:\n"
        "\n"
        "* `aes-128-ecb` that SHALL use [ECB] block mode encryption with 128 bit key\n"
        "* `aes-192-ecb` that SHALL use [ECB] block mode encryption with 192 bit key\n"
        "* `aes-256-ecb` that SHALL use [ECB] block mode encryption with 256 bit key\n"
        "* `aes-128-cbc` that SHALL use [CBC] block mode encryption with 128 bit key\n"
        "* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 192 bit key\n"
        "* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 256 bit key\n"
        "* `aes-128-cfb128` that SHALL use [CFB128] block mode encryption with 128 bit key\n"
        "* `aes-192-cfb128` that SHALL use [CFB128] block mode encryption with 192 bit key\n"
        "* `aes-256-cfb128` that SHALL use [CFB128] block mode encryption with 256 bit key\n"
        "* `aes-128-ofb` that SHALL use [OFB] block mode encryption with 128 bit key\n"
        "* `aes-192-ofb` that SHALL use [OFB] block mode encryption with 192 bit key\n"
        "* `aes-256-ofb` that SHALL use [OFB] block mode encryption with 256 bit key\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.8",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_Values_GCM_Error = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values.GCM.Error",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if any of the following [GCM] modes are specified as the value \n"
        "for the `mode` parameter of the `aes_encrypt_mysql` function\n"
        "\n"
        "* `aes-128-gcm`\n"
        "* `aes-192-gcm`\n"
        "* `aes-256-gcm`\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.9",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_Values_CTR_Error = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values.CTR.Error",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if any of the following [CTR] modes are specified as the value \n"
        "for the `mode` parameter of the `aes_encrypt_mysql` function\n"
        "\n"
        "* `aes-128-ctr`\n"
        "* `aes-192-ctr`\n"
        "* `aes-256-ctr`\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.10",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_InitializationVector = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.InitializationVector",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `iv` with `String` or `FixedString` data types as the optional fourth\n"
        "parameter to the `aes_encrypt_mysql` function that SHALL specify the initialization vector for block modes that require\n"
        "it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.11",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_ReturnValue = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.ReturnValue",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return the encrypted value of the data\n"
        "using `String` data type as the result of `aes_encrypt_mysql` function.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.12",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Key_Length_TooShortError = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Key.Length.TooShortError",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `key` length is less than the minimum for the `aes_encrypt_mysql`\n"
        "function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.13",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Key_Length_TooLong = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Key.Length.TooLong",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL use folding algorithm specified below if the `key` length is longer than required\n"
        "for the `aes_encrypt_mysql` function for a given block mode.\n"
        "\n"
        "```python\n"
        "def fold_key(key, cipher_key_size):\n"
        "    key = list(key) if not isinstance(key, (list, tuple)) else key\n"
        "\t  folded_key = key[:cipher_key_size]\n"
        "\t  for i in range(cipher_key_size, len(key)):\n"
        "\t\t    print(i % cipher_key_size, i)\n"
        "\t\t    folded_key[i % cipher_key_size] ^= key[i]\n"
        "\t  return folded_key\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.14",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_InitializationVector_Length_TooShortError = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.Length.TooShortError",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `iv` length is specified and is less than the minimum\n"
        "that is required for the `aes_encrypt_mysql` function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.15",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_InitializationVector_Length_TooLong = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.Length.TooLong",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL use the first `N` bytes that are required if the `iv` is specified and\n"
        "its length is longer than required for the `aes_encrypt_mysql` function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.16",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_InitializationVector_NotValidForMode = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.NotValidForMode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `iv` is specified for the `aes_encrypt_mysql`\n"
        "function for a mode that does not need it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.17",
)

RQ_SRS008_AES_MySQL_Encrypt_Function_Mode_KeyAndInitializationVector_Length = Requirement(
    name="RQ.SRS008.AES.MySQL.Encrypt.Function.Mode.KeyAndInitializationVector.Length",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when the `aes_encrypt_mysql` function is called with the following parameter values\n"
        "\n"
        "* `aes-128-ecb` mode and `key` is less than 16 bytes or `iv` is specified\n"
        "* `aes-192-ecb` mode and `key` is less than 24 bytes or `iv` is specified\n"
        "* `aes-256-ecb` mode and `key` is less than 32 bytes or `iv` is specified\n"
        "* `aes-128-cbc` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-192-cbc` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-cbc` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-128-cfb1` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-192-cfb1` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-cfb1` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-128-cfb8` mode and `key` is less than 16 bytes and if specified `iv` is less than 16 bytes\n"
        "* `aes-192-cfb8` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-cfb8` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-128-cfb128` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-192-cfb128` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-cfb128` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-128-ofb` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-192-ofb` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-ofb` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.11.18",
)

RQ_SRS008_AES_MySQL_Decrypt_Function = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `aes_decrypt_mysql` function to decrypt data using [AES].\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.1",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Syntax = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Syntax",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the following syntax for the `aes_decrypt_mysql` function\n"
        "\n"
        "```sql\n"
        "aes_decrypt_mysql(mode, ciphertext, key, [iv])\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.2",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_CipherText = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.CipherText",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `ciphertext` accepting any data type as\n"
        "the second parameter to the `aes_decrypt_mysql` function that SHALL specify the data to be decrypted.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.3",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Key = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Key",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `key` with `String` or `FixedString` data types\n"
        "as the third parameter to the `aes_decrypt_mysql` function that SHALL specify the encryption key.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.4",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `mode` with `String` or `FixedString` data types as the first parameter\n"
        "to the `aes_decrypt_mysql` function that SHALL specify encryption key length and block encryption mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.5",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_ValuesFormat = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.ValuesFormat",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support values of the form `aes-[key length]-[mode]` for the `mode` parameter\n"
        "of the `aes_decrypt_mysql` function where\n"
        "the `key_length` SHALL specifies the length of the key and SHALL accept\n"
        "`128`, `192`, or `256` as the values and the `mode` SHALL specify the block encryption\n"
        "mode and SHALL accept [ECB], [CBC], [CFB128], or [OFB]. For example, `aes-256-ofb`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.6",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_Value_Invalid = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Value.Invalid",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the specified value for the `mode` parameter of the `aes_decrypt_mysql`\n"
        "function is not valid with the exception where such a mode is supported by the underlying\n"
        "[OpenSSL] implementation.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.7",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_Values = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the following [AES] block encryption modes as the value for the `mode` parameter\n"
        "of the `aes_decrypt_mysql` function:\n"
        "\n"
        "* `aes-128-ecb` that SHALL use [ECB] block mode encryption with 128 bit key\n"
        "* `aes-192-ecb` that SHALL use [ECB] block mode encryption with 192 bit key\n"
        "* `aes-256-ecb` that SHALL use [ECB] block mode encryption with 256 bit key\n"
        "* `aes-128-cbc` that SHALL use [CBC] block mode encryption with 128 bit key\n"
        "* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 192 bit key\n"
        "* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 256 bit key\n"
        "* `aes-128-cfb128` that SHALL use [CFB128] block mode encryption with 128 bit key\n"
        "* `aes-192-cfb128` that SHALL use [CFB128] block mode encryption with 192 bit key\n"
        "* `aes-256-cfb128` that SHALL use [CFB128] block mode encryption with 256 bit key\n"
        "* `aes-128-ofb` that SHALL use [OFB] block mode encryption with 128 bit key\n"
        "* `aes-192-ofb` that SHALL use [OFB] block mode encryption with 192 bit key\n"
        "* `aes-256-ofb` that SHALL use [OFB] block mode encryption with 256 bit key\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.8",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_Values_GCM_Error = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values.GCM.Error",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if any of the following [GCM] modes are specified as the value \n"
        "for the `mode` parameter of the `aes_decrypt_mysql` function\n"
        "\n"
        "* `aes-128-gcm`\n"
        "* `aes-192-gcm`\n"
        "* `aes-256-gcm`\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.9",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_Values_CTR_Error = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values.CTR.Error",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if any of the following [CTR] modes are specified as the value \n"
        "for the `mode` parameter of the `aes_decrypt_mysql` function\n"
        "\n"
        "* `aes-128-ctr`\n"
        "* `aes-192-ctr`\n"
        "* `aes-256-ctr`\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.10",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_InitializationVector = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.InitializationVector",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `iv` with `String` or `FixedString` data types as the optional fourth\n"
        "parameter to the `aes_decrypt_mysql` function that SHALL specify the initialization vector for block modes that require\n"
        "it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.11",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_ReturnValue = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.ReturnValue",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return the decrypted value of the data\n"
        "using `String` data type as the result of `aes_decrypt_mysql` function.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.12",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Key_Length_TooShortError = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Key.Length.TooShortError",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `key` length is less than the minimum for the `aes_decrypt_mysql`\n"
        "function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.13",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Key_Length_TooLong = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Key.Length.TooLong",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL use folding algorithm specified below if the `key` length is longer than required\n"
        "for the `aes_decrypt_mysql` function for a given block mode.\n"
        "\n"
        "```python\n"
        "def fold_key(key, cipher_key_size):\n"
        "    key = list(key) if not isinstance(key, (list, tuple)) else key\n"
        "\t  folded_key = key[:cipher_key_size]\n"
        "\t  for i in range(cipher_key_size, len(key)):\n"
        "\t\t    print(i % cipher_key_size, i)\n"
        "\t\t    folded_key[i % cipher_key_size] ^= key[i]\n"
        "\t  return folded_key\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.14",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_InitializationVector_Length_TooShortError = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.Length.TooShortError",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `iv` length is specified and is less than the minimum\n"
        "that is required for the `aes_decrypt_mysql` function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.15",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_InitializationVector_Length_TooLong = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.Length.TooLong",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL use the first `N` bytes that are required if the `iv` is specified and\n"
        "its length is longer than required for the `aes_decrypt_mysql` function for a given block mode.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.16",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_InitializationVector_NotValidForMode = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.NotValidForMode",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error if the `iv` is specified for the `aes_decrypt_mysql`\n"
        "function for a mode that does not need it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.17",
)

RQ_SRS008_AES_MySQL_Decrypt_Function_Mode_KeyAndInitializationVector_Length = Requirement(
    name="RQ.SRS008.AES.MySQL.Decrypt.Function.Mode.KeyAndInitializationVector.Length",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when the `aes_decrypt_mysql` function is called with the following parameter values\n"
        "\n"
        "* `aes-128-ecb` mode and `key` is less than 16 bytes or `iv` is specified\n"
        "* `aes-192-ecb` mode and `key` is less than 24 bytes or `iv` is specified\n"
        "* `aes-256-ecb` mode and `key` is less than 32 bytes or `iv` is specified\n"
        "* `aes-128-cbc` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-192-cbc` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-cbc` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-128-cfb1` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-192-cfb1` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-cfb1` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-128-cfb8` mode and `key` is less than 16 bytes and if specified `iv` is less than 16 bytes\n"
        "* `aes-192-cfb8` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-cfb8` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-128-cfb128` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-192-cfb128` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-cfb128` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-128-ofb` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-192-ofb` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes\n"
        "* `aes-256-ofb` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.12.18",
)

SRS_008_ClickHouse_AES_Encryption_Functions = Specification(
    name="SRS-008 ClickHouse AES Encryption Functions",
    description=None,
    author=None,
    date=None,
    status=None,
    approved_by=None,
    approved_date=None,
    approved_version=None,
    version=None,
    group=None,
    type=None,
    link=None,
    uid=None,
    parent=None,
    children=None,
    headings=(
        Heading(name="Revision History", level=1, num="1"),
        Heading(name="Introduction", level=1, num="2"),
        Heading(name="Terminology", level=1, num="3"),
        Heading(name="AES", level=2, num="3.1"),
        Heading(name="AEAD", level=2, num="3.2"),
        Heading(name="Requirements", level=1, num="4"),
        Heading(name="Generic", level=2, num="4.1"),
        Heading(name="RQ.SRS008.AES.Functions", level=3, num="4.1.1"),
        Heading(name="Compatibility", level=2, num="4.2"),
        Heading(
            name="RQ.SRS008.AES.Functions.Compatibility.MySQL", level=3, num="4.2.1"
        ),
        Heading(
            name="RQ.SRS008.AES.Functions.Compatibility.Dictionaries",
            level=3,
            num="4.2.2",
        ),
        Heading(
            name="RQ.SRS008.AES.Functions.Compatibility.Engine.Database.MySQL",
            level=3,
            num="4.2.3",
        ),
        Heading(
            name="RQ.SRS008.AES.Functions.Compatibility.Engine.Table.MySQL",
            level=3,
            num="4.2.4",
        ),
        Heading(
            name="RQ.SRS008.AES.Functions.Compatibility.TableFunction.MySQL",
            level=3,
            num="4.2.5",
        ),
        Heading(name="Different Modes", level=2, num="4.3"),
        Heading(name="RQ.SRS008.AES.Functions.DifferentModes", level=3, num="4.3.1"),
        Heading(name="Multiple Sources", level=2, num="4.4"),
        Heading(
            name="RQ.SRS008.AES.Functions.DataFromMultipleSources", level=3, num="4.4.1"
        ),
        Heading(name="Suppressing Sensitive Values", level=2, num="4.5"),
        Heading(
            name="RQ.SRS008.AES.Functions.SuppressOutputOfSensitiveValues",
            level=3,
            num="4.5.1",
        ),
        Heading(name="Invalid Parameters", level=2, num="4.6"),
        Heading(name="RQ.SRS008.AES.Functions.InvalidParameters", level=3, num="4.6.1"),
        Heading(name="Mismatched Values", level=2, num="4.7"),
        Heading(name="RQ.SRS008.AES.Functions.Mismatched.Key", level=3, num="4.7.1"),
        Heading(name="RQ.SRS008.AES.Functions.Mismatched.IV", level=3, num="4.7.2"),
        Heading(name="RQ.SRS008.AES.Functions.Mismatched.AAD", level=3, num="4.7.3"),
        Heading(name="RQ.SRS008.AES.Functions.Mismatched.Mode", level=3, num="4.7.4"),
        Heading(name="Performance", level=2, num="4.8"),
        Heading(name="RQ.SRS008.AES.Functions.Check.Performance", level=3, num="4.8.1"),
        Heading(
            name="RQ.SRS008.AES.Function.Check.Performance.BestCase",
            level=3,
            num="4.8.2",
        ),
        Heading(
            name="RQ.SRS008.AES.Function.Check.Performance.WorstCase",
            level=3,
            num="4.8.3",
        ),
        Heading(name="RQ.SRS008.AES.Functions.Check.Compression", level=3, num="4.8.4"),
        Heading(
            name="RQ.SRS008.AES.Functions.Check.Compression.LowCardinality",
            level=3,
            num="4.8.5",
        ),
        Heading(name="Encrypt Function", level=2, num="4.9"),
        Heading(name="RQ.SRS008.AES.Encrypt.Function", level=3, num="4.9.1"),
        Heading(name="RQ.SRS008.AES.Encrypt.Function.Syntax", level=3, num="4.9.2"),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.NIST.TestVectors", level=3, num="4.9.3"
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.PlainText",
            level=3,
            num="4.9.4",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.Key", level=3, num="4.9.5"
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.Mode", level=3, num="4.9.6"
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.ValuesFormat",
            level=3,
            num="4.9.7",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.Value.Invalid",
            level=3,
            num="4.9.8",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.Values",
            level=3,
            num="4.9.9",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.InitializationVector",
            level=3,
            num="4.9.10",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.AdditionalAuthenticatedData",
            level=3,
            num="4.9.11",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Parameters.ReturnValue",
            level=3,
            num="4.9.12",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.Key.Length.InvalidLengthError",
            level=3,
            num="4.9.13",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.InitializationVector.Length.InvalidLengthError",
            level=3,
            num="4.9.14",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.InitializationVector.NotValidForMode",
            level=3,
            num="4.9.15",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.AdditionalAuthenticationData.NotValidForMode",
            level=3,
            num="4.9.16",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.AdditionalAuthenticationData.Length",
            level=3,
            num="4.9.17",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.NonGCMMode.KeyAndInitializationVector.Length",
            level=3,
            num="4.9.18",
        ),
        Heading(
            name="RQ.SRS008.AES.Encrypt.Function.GCMMode.KeyAndInitializationVector.Length",
            level=3,
            num="4.9.19",
        ),
        Heading(name="Decrypt Function", level=2, num="4.10"),
        Heading(name="RQ.SRS008.AES.Decrypt.Function", level=3, num="4.10.1"),
        Heading(name="RQ.SRS008.AES.Decrypt.Function.Syntax", level=3, num="4.10.2"),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.CipherText",
            level=3,
            num="4.10.3",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.Key", level=3, num="4.10.4"
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.Mode", level=3, num="4.10.5"
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.ValuesFormat",
            level=3,
            num="4.10.6",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.Value.Invalid",
            level=3,
            num="4.10.7",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.Values",
            level=3,
            num="4.10.8",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.InitializationVector",
            level=3,
            num="4.10.9",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.AdditionalAuthenticatedData",
            level=3,
            num="4.10.10",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Parameters.ReturnValue",
            level=3,
            num="4.10.11",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.Key.Length.InvalidLengthError",
            level=3,
            num="4.10.12",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.InitializationVector.Length.InvalidLengthError",
            level=3,
            num="4.10.13",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.InitializationVector.NotValidForMode",
            level=3,
            num="4.10.14",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.AdditionalAuthenticationData.NotValidForMode",
            level=3,
            num="4.10.15",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.AdditionalAuthenticationData.Length",
            level=3,
            num="4.10.16",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.NonGCMMode.KeyAndInitializationVector.Length",
            level=3,
            num="4.10.17",
        ),
        Heading(
            name="RQ.SRS008.AES.Decrypt.Function.GCMMode.KeyAndInitializationVector.Length",
            level=3,
            num="4.10.18",
        ),
        Heading(name="MySQL Encrypt Function", level=2, num="4.11"),
        Heading(name="RQ.SRS008.AES.MySQL.Encrypt.Function", level=3, num="4.11.1"),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Syntax", level=3, num="4.11.2"
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.PlainText",
            level=3,
            num="4.11.3",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Key",
            level=3,
            num="4.11.4",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode",
            level=3,
            num="4.11.5",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.ValuesFormat",
            level=3,
            num="4.11.6",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Value.Invalid",
            level=3,
            num="4.11.7",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values",
            level=3,
            num="4.11.8",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values.GCM.Error",
            level=3,
            num="4.11.9",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values.CTR.Error",
            level=3,
            num="4.11.10",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.InitializationVector",
            level=3,
            num="4.11.11",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.ReturnValue",
            level=3,
            num="4.11.12",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Key.Length.TooShortError",
            level=3,
            num="4.11.13",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Key.Length.TooLong",
            level=3,
            num="4.11.14",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.Length.TooShortError",
            level=3,
            num="4.11.15",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.Length.TooLong",
            level=3,
            num="4.11.16",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.NotValidForMode",
            level=3,
            num="4.11.17",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Encrypt.Function.Mode.KeyAndInitializationVector.Length",
            level=3,
            num="4.11.18",
        ),
        Heading(name="MySQL Decrypt Function", level=2, num="4.12"),
        Heading(name="RQ.SRS008.AES.MySQL.Decrypt.Function", level=3, num="4.12.1"),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Syntax", level=3, num="4.12.2"
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.CipherText",
            level=3,
            num="4.12.3",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Key",
            level=3,
            num="4.12.4",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode",
            level=3,
            num="4.12.5",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.ValuesFormat",
            level=3,
            num="4.12.6",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Value.Invalid",
            level=3,
            num="4.12.7",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values",
            level=3,
            num="4.12.8",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values.GCM.Error",
            level=3,
            num="4.12.9",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values.CTR.Error",
            level=3,
            num="4.12.10",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.InitializationVector",
            level=3,
            num="4.12.11",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.ReturnValue",
            level=3,
            num="4.12.12",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Key.Length.TooShortError",
            level=3,
            num="4.12.13",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Key.Length.TooLong",
            level=3,
            num="4.12.14",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.Length.TooShortError",
            level=3,
            num="4.12.15",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.Length.TooLong",
            level=3,
            num="4.12.16",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.NotValidForMode",
            level=3,
            num="4.12.17",
        ),
        Heading(
            name="RQ.SRS008.AES.MySQL.Decrypt.Function.Mode.KeyAndInitializationVector.Length",
            level=3,
            num="4.12.18",
        ),
        Heading(name="References", level=1, num="5"),
    ),
    requirements=(
        RQ_SRS008_AES_Functions,
        RQ_SRS008_AES_Functions_Compatibility_MySQL,
        RQ_SRS008_AES_Functions_Compatibility_Dictionaries,
        RQ_SRS008_AES_Functions_Compatibility_Engine_Database_MySQL,
        RQ_SRS008_AES_Functions_Compatibility_Engine_Table_MySQL,
        RQ_SRS008_AES_Functions_Compatibility_TableFunction_MySQL,
        RQ_SRS008_AES_Functions_DifferentModes,
        RQ_SRS008_AES_Functions_DataFromMultipleSources,
        RQ_SRS008_AES_Functions_SuppressOutputOfSensitiveValues,
        RQ_SRS008_AES_Functions_InvalidParameters,
        RQ_SRS008_AES_Functions_Mismatched_Key,
        RQ_SRS008_AES_Functions_Mismatched_IV,
        RQ_SRS008_AES_Functions_Mismatched_AAD,
        RQ_SRS008_AES_Functions_Mismatched_Mode,
        RQ_SRS008_AES_Functions_Check_Performance,
        RQ_SRS008_AES_Function_Check_Performance_BestCase,
        RQ_SRS008_AES_Function_Check_Performance_WorstCase,
        RQ_SRS008_AES_Functions_Check_Compression,
        RQ_SRS008_AES_Functions_Check_Compression_LowCardinality,
        RQ_SRS008_AES_Encrypt_Function,
        RQ_SRS008_AES_Encrypt_Function_Syntax,
        RQ_SRS008_AES_Encrypt_Function_NIST_TestVectors,
        RQ_SRS008_AES_Encrypt_Function_Parameters_PlainText,
        RQ_SRS008_AES_Encrypt_Function_Parameters_Key,
        RQ_SRS008_AES_Encrypt_Function_Parameters_Mode,
        RQ_SRS008_AES_Encrypt_Function_Parameters_Mode_ValuesFormat,
        RQ_SRS008_AES_Encrypt_Function_Parameters_Mode_Value_Invalid,
        RQ_SRS008_AES_Encrypt_Function_Parameters_Mode_Values,
        RQ_SRS008_AES_Encrypt_Function_Parameters_InitializationVector,
        RQ_SRS008_AES_Encrypt_Function_Parameters_AdditionalAuthenticatedData,
        RQ_SRS008_AES_Encrypt_Function_Parameters_ReturnValue,
        RQ_SRS008_AES_Encrypt_Function_Key_Length_InvalidLengthError,
        RQ_SRS008_AES_Encrypt_Function_InitializationVector_Length_InvalidLengthError,
        RQ_SRS008_AES_Encrypt_Function_InitializationVector_NotValidForMode,
        RQ_SRS008_AES_Encrypt_Function_AdditionalAuthenticationData_NotValidForMode,
        RQ_SRS008_AES_Encrypt_Function_AdditionalAuthenticationData_Length,
        RQ_SRS008_AES_Encrypt_Function_NonGCMMode_KeyAndInitializationVector_Length,
        RQ_SRS008_AES_Encrypt_Function_GCMMode_KeyAndInitializationVector_Length,
        RQ_SRS008_AES_Decrypt_Function,
        RQ_SRS008_AES_Decrypt_Function_Syntax,
        RQ_SRS008_AES_Decrypt_Function_Parameters_CipherText,
        RQ_SRS008_AES_Decrypt_Function_Parameters_Key,
        RQ_SRS008_AES_Decrypt_Function_Parameters_Mode,
        RQ_SRS008_AES_Decrypt_Function_Parameters_Mode_ValuesFormat,
        RQ_SRS008_AES_Decrypt_Function_Parameters_Mode_Value_Invalid,
        RQ_SRS008_AES_Decrypt_Function_Parameters_Mode_Values,
        RQ_SRS008_AES_Decrypt_Function_Parameters_InitializationVector,
        RQ_SRS008_AES_Decrypt_Function_Parameters_AdditionalAuthenticatedData,
        RQ_SRS008_AES_Decrypt_Function_Parameters_ReturnValue,
        RQ_SRS008_AES_Decrypt_Function_Key_Length_InvalidLengthError,
        RQ_SRS008_AES_Decrypt_Function_InitializationVector_Length_InvalidLengthError,
        RQ_SRS008_AES_Decrypt_Function_InitializationVector_NotValidForMode,
        RQ_SRS008_AES_Decrypt_Function_AdditionalAuthenticationData_NotValidForMode,
        RQ_SRS008_AES_Decrypt_Function_AdditionalAuthenticationData_Length,
        RQ_SRS008_AES_Decrypt_Function_NonGCMMode_KeyAndInitializationVector_Length,
        RQ_SRS008_AES_Decrypt_Function_GCMMode_KeyAndInitializationVector_Length,
        RQ_SRS008_AES_MySQL_Encrypt_Function,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Syntax,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_PlainText,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Key,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_ValuesFormat,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_Value_Invalid,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_Values,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_Values_GCM_Error,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_Mode_Values_CTR_Error,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_InitializationVector,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Parameters_ReturnValue,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Key_Length_TooShortError,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Key_Length_TooLong,
        RQ_SRS008_AES_MySQL_Encrypt_Function_InitializationVector_Length_TooShortError,
        RQ_SRS008_AES_MySQL_Encrypt_Function_InitializationVector_Length_TooLong,
        RQ_SRS008_AES_MySQL_Encrypt_Function_InitializationVector_NotValidForMode,
        RQ_SRS008_AES_MySQL_Encrypt_Function_Mode_KeyAndInitializationVector_Length,
        RQ_SRS008_AES_MySQL_Decrypt_Function,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Syntax,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_CipherText,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Key,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_ValuesFormat,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_Value_Invalid,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_Values,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_Values_GCM_Error,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_Mode_Values_CTR_Error,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_InitializationVector,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Parameters_ReturnValue,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Key_Length_TooShortError,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Key_Length_TooLong,
        RQ_SRS008_AES_MySQL_Decrypt_Function_InitializationVector_Length_TooShortError,
        RQ_SRS008_AES_MySQL_Decrypt_Function_InitializationVector_Length_TooLong,
        RQ_SRS008_AES_MySQL_Decrypt_Function_InitializationVector_NotValidForMode,
        RQ_SRS008_AES_MySQL_Decrypt_Function_Mode_KeyAndInitializationVector_Length,
    ),
    content="""
# SRS-008 ClickHouse AES Encryption Functions
# Software Requirements Specification

## Table of Contents

* 1 [Revision History](#revision-history)
* 2 [Introduction](#introduction)
* 3 [Terminology](#terminology)
  * 3.1 [AES](#aes)
  * 3.2 [AEAD](#aead)
* 4 [Requirements](#requirements)
  * 4.1 [Generic](#generic)
    * 4.1.1 [RQ.SRS008.AES.Functions](#rqsrs008aesfunctions)
  * 4.2 [Compatibility](#compatibility)
    * 4.2.1 [RQ.SRS008.AES.Functions.Compatibility.MySQL](#rqsrs008aesfunctionscompatibilitymysql)
    * 4.2.2 [RQ.SRS008.AES.Functions.Compatibility.Dictionaries](#rqsrs008aesfunctionscompatibilitydictionaries)
    * 4.2.3 [RQ.SRS008.AES.Functions.Compatibility.Engine.Database.MySQL](#rqsrs008aesfunctionscompatibilityenginedatabasemysql)
    * 4.2.4 [RQ.SRS008.AES.Functions.Compatibility.Engine.Table.MySQL](#rqsrs008aesfunctionscompatibilityenginetablemysql)
    * 4.2.5 [RQ.SRS008.AES.Functions.Compatibility.TableFunction.MySQL](#rqsrs008aesfunctionscompatibilitytablefunctionmysql)
  * 4.3 [Different Modes](#different-modes)
    * 4.3.1 [RQ.SRS008.AES.Functions.DifferentModes](#rqsrs008aesfunctionsdifferentmodes)
  * 4.4 [Multiple Sources](#multiple-sources)
    * 4.4.1 [RQ.SRS008.AES.Functions.DataFromMultipleSources](#rqsrs008aesfunctionsdatafrommultiplesources)
  * 4.5 [Suppressing Sensitive Values](#suppressing-sensitive-values)
    * 4.5.1 [RQ.SRS008.AES.Functions.SuppressOutputOfSensitiveValues](#rqsrs008aesfunctionssuppressoutputofsensitivevalues)
  * 4.6 [Invalid Parameters](#invalid-parameters)
    * 4.6.1 [RQ.SRS008.AES.Functions.InvalidParameters](#rqsrs008aesfunctionsinvalidparameters)
  * 4.7 [Mismatched Values](#mismatched-values)
    * 4.7.1 [RQ.SRS008.AES.Functions.Mismatched.Key](#rqsrs008aesfunctionsmismatchedkey)
    * 4.7.2 [RQ.SRS008.AES.Functions.Mismatched.IV](#rqsrs008aesfunctionsmismatchediv)
    * 4.7.3 [RQ.SRS008.AES.Functions.Mismatched.AAD](#rqsrs008aesfunctionsmismatchedaad)
    * 4.7.4 [RQ.SRS008.AES.Functions.Mismatched.Mode](#rqsrs008aesfunctionsmismatchedmode)
  * 4.8 [Performance](#performance)
    * 4.8.1 [RQ.SRS008.AES.Functions.Check.Performance](#rqsrs008aesfunctionscheckperformance)
    * 4.8.2 [RQ.SRS008.AES.Function.Check.Performance.BestCase](#rqsrs008aesfunctioncheckperformancebestcase)
    * 4.8.3 [RQ.SRS008.AES.Function.Check.Performance.WorstCase](#rqsrs008aesfunctioncheckperformanceworstcase)
    * 4.8.4 [RQ.SRS008.AES.Functions.Check.Compression](#rqsrs008aesfunctionscheckcompression)
    * 4.8.5 [RQ.SRS008.AES.Functions.Check.Compression.LowCardinality](#rqsrs008aesfunctionscheckcompressionlowcardinality)
  * 4.9 [Encrypt Function](#encrypt-function)
    * 4.9.1 [RQ.SRS008.AES.Encrypt.Function](#rqsrs008aesencryptfunction)
    * 4.9.2 [RQ.SRS008.AES.Encrypt.Function.Syntax](#rqsrs008aesencryptfunctionsyntax)
    * 4.9.3 [RQ.SRS008.AES.Encrypt.Function.NIST.TestVectors](#rqsrs008aesencryptfunctionnisttestvectors)
    * 4.9.4 [RQ.SRS008.AES.Encrypt.Function.Parameters.PlainText](#rqsrs008aesencryptfunctionparametersplaintext)
    * 4.9.5 [RQ.SRS008.AES.Encrypt.Function.Parameters.Key](#rqsrs008aesencryptfunctionparameterskey)
    * 4.9.6 [RQ.SRS008.AES.Encrypt.Function.Parameters.Mode](#rqsrs008aesencryptfunctionparametersmode)
    * 4.9.7 [RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.ValuesFormat](#rqsrs008aesencryptfunctionparametersmodevaluesformat)
    * 4.9.8 [RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.Value.Invalid](#rqsrs008aesencryptfunctionparametersmodevalueinvalid)
    * 4.9.9 [RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.Values](#rqsrs008aesencryptfunctionparametersmodevalues)
    * 4.9.10 [RQ.SRS008.AES.Encrypt.Function.Parameters.InitializationVector](#rqsrs008aesencryptfunctionparametersinitializationvector)
    * 4.9.11 [RQ.SRS008.AES.Encrypt.Function.Parameters.AdditionalAuthenticatedData](#rqsrs008aesencryptfunctionparametersadditionalauthenticateddata)
    * 4.9.12 [RQ.SRS008.AES.Encrypt.Function.Parameters.ReturnValue](#rqsrs008aesencryptfunctionparametersreturnvalue)
    * 4.9.13 [RQ.SRS008.AES.Encrypt.Function.Key.Length.InvalidLengthError](#rqsrs008aesencryptfunctionkeylengthinvalidlengtherror)
    * 4.9.14 [RQ.SRS008.AES.Encrypt.Function.InitializationVector.Length.InvalidLengthError](#rqsrs008aesencryptfunctioninitializationvectorlengthinvalidlengtherror)
    * 4.9.15 [RQ.SRS008.AES.Encrypt.Function.InitializationVector.NotValidForMode](#rqsrs008aesencryptfunctioninitializationvectornotvalidformode)
    * 4.9.16 [RQ.SRS008.AES.Encrypt.Function.AdditionalAuthenticationData.NotValidForMode](#rqsrs008aesencryptfunctionadditionalauthenticationdatanotvalidformode)
    * 4.9.17 [RQ.SRS008.AES.Encrypt.Function.AdditionalAuthenticationData.Length](#rqsrs008aesencryptfunctionadditionalauthenticationdatalength)
    * 4.9.18 [RQ.SRS008.AES.Encrypt.Function.NonGCMMode.KeyAndInitializationVector.Length](#rqsrs008aesencryptfunctionnongcmmodekeyandinitializationvectorlength)
    * 4.9.19 [RQ.SRS008.AES.Encrypt.Function.GCMMode.KeyAndInitializationVector.Length](#rqsrs008aesencryptfunctiongcmmodekeyandinitializationvectorlength)
  * 4.10 [Decrypt Function](#decrypt-function)
    * 4.10.1 [RQ.SRS008.AES.Decrypt.Function](#rqsrs008aesdecryptfunction)
    * 4.10.2 [RQ.SRS008.AES.Decrypt.Function.Syntax](#rqsrs008aesdecryptfunctionsyntax)
    * 4.10.3 [RQ.SRS008.AES.Decrypt.Function.Parameters.CipherText](#rqsrs008aesdecryptfunctionparametersciphertext)
    * 4.10.4 [RQ.SRS008.AES.Decrypt.Function.Parameters.Key](#rqsrs008aesdecryptfunctionparameterskey)
    * 4.10.5 [RQ.SRS008.AES.Decrypt.Function.Parameters.Mode](#rqsrs008aesdecryptfunctionparametersmode)
    * 4.10.6 [RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.ValuesFormat](#rqsrs008aesdecryptfunctionparametersmodevaluesformat)
    * 4.10.7 [RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.Value.Invalid](#rqsrs008aesdecryptfunctionparametersmodevalueinvalid)
    * 4.10.8 [RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.Values](#rqsrs008aesdecryptfunctionparametersmodevalues)
    * 4.10.9 [RQ.SRS008.AES.Decrypt.Function.Parameters.InitializationVector](#rqsrs008aesdecryptfunctionparametersinitializationvector)
    * 4.10.10 [RQ.SRS008.AES.Decrypt.Function.Parameters.AdditionalAuthenticatedData](#rqsrs008aesdecryptfunctionparametersadditionalauthenticateddata)
    * 4.10.11 [RQ.SRS008.AES.Decrypt.Function.Parameters.ReturnValue](#rqsrs008aesdecryptfunctionparametersreturnvalue)
    * 4.10.12 [RQ.SRS008.AES.Decrypt.Function.Key.Length.InvalidLengthError](#rqsrs008aesdecryptfunctionkeylengthinvalidlengtherror)
    * 4.10.13 [RQ.SRS008.AES.Decrypt.Function.InitializationVector.Length.InvalidLengthError](#rqsrs008aesdecryptfunctioninitializationvectorlengthinvalidlengtherror)
    * 4.10.14 [RQ.SRS008.AES.Decrypt.Function.InitializationVector.NotValidForMode](#rqsrs008aesdecryptfunctioninitializationvectornotvalidformode)
    * 4.10.15 [RQ.SRS008.AES.Decrypt.Function.AdditionalAuthenticationData.NotValidForMode](#rqsrs008aesdecryptfunctionadditionalauthenticationdatanotvalidformode)
    * 4.10.16 [RQ.SRS008.AES.Decrypt.Function.AdditionalAuthenticationData.Length](#rqsrs008aesdecryptfunctionadditionalauthenticationdatalength)
    * 4.10.17 [RQ.SRS008.AES.Decrypt.Function.NonGCMMode.KeyAndInitializationVector.Length](#rqsrs008aesdecryptfunctionnongcmmodekeyandinitializationvectorlength)
    * 4.10.18 [RQ.SRS008.AES.Decrypt.Function.GCMMode.KeyAndInitializationVector.Length](#rqsrs008aesdecryptfunctiongcmmodekeyandinitializationvectorlength)
  * 4.11 [MySQL Encrypt Function](#mysql-encrypt-function)
    * 4.11.1 [RQ.SRS008.AES.MySQL.Encrypt.Function](#rqsrs008aesmysqlencryptfunction)
    * 4.11.2 [RQ.SRS008.AES.MySQL.Encrypt.Function.Syntax](#rqsrs008aesmysqlencryptfunctionsyntax)
    * 4.11.3 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.PlainText](#rqsrs008aesmysqlencryptfunctionparametersplaintext)
    * 4.11.4 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Key](#rqsrs008aesmysqlencryptfunctionparameterskey)
    * 4.11.5 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode](#rqsrs008aesmysqlencryptfunctionparametersmode)
    * 4.11.6 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.ValuesFormat](#rqsrs008aesmysqlencryptfunctionparametersmodevaluesformat)
    * 4.11.7 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Value.Invalid](#rqsrs008aesmysqlencryptfunctionparametersmodevalueinvalid)
    * 4.11.8 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values](#rqsrs008aesmysqlencryptfunctionparametersmodevalues)
    * 4.11.9 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values.GCM.Error](#rqsrs008aesmysqlencryptfunctionparametersmodevaluesgcmerror)
    * 4.11.10 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values.CTR.Error](#rqsrs008aesmysqlencryptfunctionparametersmodevaluesctrerror)
    * 4.11.11 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.InitializationVector](#rqsrs008aesmysqlencryptfunctionparametersinitializationvector)
    * 4.11.12 [RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.ReturnValue](#rqsrs008aesmysqlencryptfunctionparametersreturnvalue)
    * 4.11.13 [RQ.SRS008.AES.MySQL.Encrypt.Function.Key.Length.TooShortError](#rqsrs008aesmysqlencryptfunctionkeylengthtooshorterror)
    * 4.11.14 [RQ.SRS008.AES.MySQL.Encrypt.Function.Key.Length.TooLong](#rqsrs008aesmysqlencryptfunctionkeylengthtoolong)
    * 4.11.15 [RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.Length.TooShortError](#rqsrs008aesmysqlencryptfunctioninitializationvectorlengthtooshorterror)
    * 4.11.16 [RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.Length.TooLong](#rqsrs008aesmysqlencryptfunctioninitializationvectorlengthtoolong)
    * 4.11.17 [RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.NotValidForMode](#rqsrs008aesmysqlencryptfunctioninitializationvectornotvalidformode)
    * 4.11.18 [RQ.SRS008.AES.MySQL.Encrypt.Function.Mode.KeyAndInitializationVector.Length](#rqsrs008aesmysqlencryptfunctionmodekeyandinitializationvectorlength)
  * 4.12 [MySQL Decrypt Function](#mysql-decrypt-function)
    * 4.12.1 [RQ.SRS008.AES.MySQL.Decrypt.Function](#rqsrs008aesmysqldecryptfunction)
    * 4.12.2 [RQ.SRS008.AES.MySQL.Decrypt.Function.Syntax](#rqsrs008aesmysqldecryptfunctionsyntax)
    * 4.12.3 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.CipherText](#rqsrs008aesmysqldecryptfunctionparametersciphertext)
    * 4.12.4 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Key](#rqsrs008aesmysqldecryptfunctionparameterskey)
    * 4.12.5 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode](#rqsrs008aesmysqldecryptfunctionparametersmode)
    * 4.12.6 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.ValuesFormat](#rqsrs008aesmysqldecryptfunctionparametersmodevaluesformat)
    * 4.12.7 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Value.Invalid](#rqsrs008aesmysqldecryptfunctionparametersmodevalueinvalid)
    * 4.12.8 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values](#rqsrs008aesmysqldecryptfunctionparametersmodevalues)
    * 4.12.9 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values.GCM.Error](#rqsrs008aesmysqldecryptfunctionparametersmodevaluesgcmerror)
    * 4.12.10 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values.CTR.Error](#rqsrs008aesmysqldecryptfunctionparametersmodevaluesctrerror)
    * 4.12.11 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.InitializationVector](#rqsrs008aesmysqldecryptfunctionparametersinitializationvector)
    * 4.12.12 [RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.ReturnValue](#rqsrs008aesmysqldecryptfunctionparametersreturnvalue)
    * 4.12.13 [RQ.SRS008.AES.MySQL.Decrypt.Function.Key.Length.TooShortError](#rqsrs008aesmysqldecryptfunctionkeylengthtooshorterror)
    * 4.12.14 [RQ.SRS008.AES.MySQL.Decrypt.Function.Key.Length.TooLong](#rqsrs008aesmysqldecryptfunctionkeylengthtoolong)
    * 4.12.15 [RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.Length.TooShortError](#rqsrs008aesmysqldecryptfunctioninitializationvectorlengthtooshorterror)
    * 4.12.16 [RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.Length.TooLong](#rqsrs008aesmysqldecryptfunctioninitializationvectorlengthtoolong)
    * 4.12.17 [RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.NotValidForMode](#rqsrs008aesmysqldecryptfunctioninitializationvectornotvalidformode)
    * 4.12.18 [RQ.SRS008.AES.MySQL.Decrypt.Function.Mode.KeyAndInitializationVector.Length](#rqsrs008aesmysqldecryptfunctionmodekeyandinitializationvectorlength)
* 5 [References](#references)

## Revision History

This document is stored in an electronic form using [Git] source control management software
hosted in a [GitHub Repository].
All the updates are tracked using the [Revision History].

## Introduction

Users need an ability to encrypt and decrypt column data with tenant specific keys.
Use cases include protection of sensitive column values and [GDPR] right to forget policies.
The implementation will support capabilities of the [MySQL aes_encrypt] and [MySQL aes_decrypt]
functions which encrypt and decrypt values using the [AES] (Advanced Encryption Standard)
algorithm. This functionality will enable encryption and decryption of data
accessed on remote [MySQL] servers via [MySQL Dictionary] or [MySQL Database Engine],
[MySQL Table Engine], or [MySQL Table Function].

## Terminology

### AES

  Advanced Encryption Standard ([AES])

### AEAD

  Authenticated Encryption with Associated Data

## Requirements

### Generic

#### RQ.SRS008.AES.Functions
version: 1.0

[ClickHouse] SHALL support [AES] encryption functions to encrypt and decrypt data.

### Compatibility

#### RQ.SRS008.AES.Functions.Compatibility.MySQL
version: 1.0

[ClickHouse] SHALL support [AES] encryption functions compatible with [MySQL 5.7].

#### RQ.SRS008.AES.Functions.Compatibility.Dictionaries
version: 1.0

[ClickHouse] SHALL support encryption and decryption of data accessed on remote
[MySQL] servers using [MySQL Dictionary].

#### RQ.SRS008.AES.Functions.Compatibility.Engine.Database.MySQL
version: 1.0

[ClickHouse] SHALL support encryption and decryption of data accessed using [MySQL Database Engine],

#### RQ.SRS008.AES.Functions.Compatibility.Engine.Table.MySQL
version: 1.0

[ClickHouse] SHALL support encryption and decryption of data accessed using [MySQL Table Engine].

#### RQ.SRS008.AES.Functions.Compatibility.TableFunction.MySQL
version: 1.0

[ClickHouse] SHALL support encryption and decryption of data accessed using [MySQL Table Function].

### Different Modes

#### RQ.SRS008.AES.Functions.DifferentModes
version: 1.0

[ClickHouse] SHALL allow different modes to be supported in a single SQL statement
using explicit function parameters.

### Multiple Sources

#### RQ.SRS008.AES.Functions.DataFromMultipleSources
version: 1.0

[ClickHouse] SHALL support handling encryption and decryption of data from multiple sources
in the `SELECT` statement, including [ClickHouse] [MergeTree] table as well as [MySQL Dictionary],
[MySQL Database Engine], [MySQL Table Engine], and [MySQL Table Function]
with possibly different encryption schemes.

### Suppressing Sensitive Values

#### RQ.SRS008.AES.Functions.SuppressOutputOfSensitiveValues
version: 1.0

[ClickHouse] SHALL suppress output of [AES] `string` and `key` parameters to the system log,
error log, and `query_log` table to prevent leakage of sensitive values.

### Invalid Parameters

#### RQ.SRS008.AES.Functions.InvalidParameters
version: 1.0

[ClickHouse] SHALL return an error when parameters are invalid.

### Mismatched Values

#### RQ.SRS008.AES.Functions.Mismatched.Key
version: 1.0

[ClickHouse] SHALL return garbage for mismatched keys.

#### RQ.SRS008.AES.Functions.Mismatched.IV
version: 1.0

[ClickHouse] SHALL return garbage for mismatched initialization vector for the modes that use it.

#### RQ.SRS008.AES.Functions.Mismatched.AAD
version: 1.0

[ClickHouse] SHALL return garbage for mismatched additional authentication data for the modes that use it.

#### RQ.SRS008.AES.Functions.Mismatched.Mode
version: 1.0

[ClickHouse] SHALL return an error or garbage for mismatched mode.

### Performance

#### RQ.SRS008.AES.Functions.Check.Performance
version: 1.0

Performance of [AES] encryption functions SHALL be measured.

#### RQ.SRS008.AES.Function.Check.Performance.BestCase
version: 1.0

Performance of [AES] encryption functions SHALL be checked for the best case
scenario where there is one key, one initialization vector, and one large stream of data.

#### RQ.SRS008.AES.Function.Check.Performance.WorstCase
version: 1.0

Performance of [AES] encryption functions SHALL be checked for the worst case
where there are `N` keys, `N` initialization vectors and `N` very small streams of data.

#### RQ.SRS008.AES.Functions.Check.Compression
version: 1.0

Effect of [AES] encryption on column compression SHALL be measured.

#### RQ.SRS008.AES.Functions.Check.Compression.LowCardinality
version: 1.0

Effect of [AES] encryption on the compression of a column with [LowCardinality] data type
SHALL be measured.

### Encrypt Function

#### RQ.SRS008.AES.Encrypt.Function
version: 1.0

[ClickHouse] SHALL support `encrypt` function to encrypt data using [AES].

#### RQ.SRS008.AES.Encrypt.Function.Syntax
version: 1.0

[ClickHouse] SHALL support the following syntax for the `encrypt` function

```sql
encrypt(mode, plaintext, key, [iv, aad])
```

#### RQ.SRS008.AES.Encrypt.Function.NIST.TestVectors
version: 1.0

[ClickHouse] `encrypt` function output SHALL produce output that matches [NIST test vectors].

#### RQ.SRS008.AES.Encrypt.Function.Parameters.PlainText
version: 2.0

[ClickHouse] SHALL support `plaintext` with `String`, `FixedString`, `Nullable(String)`,
`Nullable(FixedString)`, `LowCardinality(String)`, or `LowCardinality(FixedString(N))` data types as
the second parameter to the `encrypt` function that SHALL specify the data to be encrypted.


#### RQ.SRS008.AES.Encrypt.Function.Parameters.Key
version: 1.0

[ClickHouse] SHALL support `key` with `String` or `FixedString` data types
as the  parameter to the `encrypt` function that SHALL specify the encryption key.

#### RQ.SRS008.AES.Encrypt.Function.Parameters.Mode
version: 1.0

[ClickHouse] SHALL support `mode` with `String` or `FixedString` data types as the first parameter
to the `encrypt` function that SHALL specify encryption key length and block encryption mode.

#### RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.ValuesFormat
version: 1.0

[ClickHouse] SHALL support values of the form `aes-[key length]-[mode]` for the `mode` parameter
of the `encrypt` function where
the `key_length` SHALL specifies the length of the key and SHALL accept
`128`, `192`, or `256` as the values and the `mode` SHALL specify the block encryption
mode and SHALL accept [ECB], [CBC], [CFB128], or [OFB] as well as
[CTR] and [GCM] as the values. For example, `aes-256-ofb`.

#### RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.Value.Invalid
version: 1.0

[ClickHouse] SHALL return an error if the specified value for the `mode` parameter of the `encrypt`
function is not valid with the exception where such a mode is supported by the underlying
[OpenSSL] implementation.

#### RQ.SRS008.AES.Encrypt.Function.Parameters.Mode.Values
version: 1.0

[ClickHouse] SHALL support the following [AES] block encryption modes as the value for the `mode` parameter
of the `encrypt` function:

* `aes-128-ecb` that SHALL use [ECB] block mode encryption with 128 bit key
* `aes-192-ecb` that SHALL use [ECB] block mode encryption with 192 bit key
* `aes-256-ecb` that SHALL use [ECB] block mode encryption with 256 bit key
* `aes-128-cbc` that SHALL use [CBC] block mode encryption with 128 bit key
* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 192 bit key
* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 256 bit key
* `aes-128-cfb128` that SHALL use [CFB128] block mode encryption with 128 bit key
* `aes-192-cfb128` that SHALL use [CFB128] block mode encryption with 192 bit key
* `aes-256-cfb128` that SHALL use [CFB128] block mode encryption with 256 bit key
* `aes-128-ofb` that SHALL use [OFB] block mode encryption with 128 bit key
* `aes-192-ofb` that SHALL use [OFB] block mode encryption with 192 bit key
* `aes-256-ofb` that SHALL use [OFB] block mode encryption with 256 bit key
* `aes-128-gcm` that SHALL use [GCM] block mode encryption with 128 bit key
   and [AEAD] 16-byte tag is appended to the resulting ciphertext according to
   the [RFC5116]
* `aes-192-gcm` that SHALL use [GCM] block mode encryption with 192 bit key
   and [AEAD] 16-byte tag is appended to the resulting ciphertext according to
   the [RFC5116]
* `aes-256-gcm` that SHALL use [GCM] block mode encryption with 256 bit key
   and [AEAD] 16-byte tag is appended to the resulting ciphertext according to
   the [RFC5116]
*  `aes-128-ctr` that SHALL use [CTR] block mode encryption with 128 bit key
*  `aes-192-ctr` that SHALL use [CTR] block mode encryption with 192 bit key
*  `aes-256-ctr` that SHALL use [CTR] block mode encryption with 256 bit key

#### RQ.SRS008.AES.Encrypt.Function.Parameters.InitializationVector
version: 1.0

[ClickHouse] SHALL support `iv` with `String` or `FixedString` data types as the optional fourth
parameter to the `encrypt` function that SHALL specify the initialization vector for block modes that require
it.

#### RQ.SRS008.AES.Encrypt.Function.Parameters.AdditionalAuthenticatedData
version: 1.0

[ClickHouse] SHALL support `aad` with `String` or `FixedString` data types as the optional fifth
parameter to the `encrypt` function that SHALL specify the additional authenticated data
for block modes that require it.

#### RQ.SRS008.AES.Encrypt.Function.Parameters.ReturnValue
version: 1.0

[ClickHouse] SHALL return the encrypted value of the data
using `String` data type as the result of `encrypt` function.

#### RQ.SRS008.AES.Encrypt.Function.Key.Length.InvalidLengthError
version: 1.0

[ClickHouse] SHALL return an error if the `key` length is not exact for the `encrypt` function for a given block mode.

#### RQ.SRS008.AES.Encrypt.Function.InitializationVector.Length.InvalidLengthError
version: 1.0

[ClickHouse] SHALL return an error if the `iv` length is specified and not of the exact size for the `encrypt` function for a given block mode.

#### RQ.SRS008.AES.Encrypt.Function.InitializationVector.NotValidForMode
version: 1.0

[ClickHouse] SHALL return an error if the `iv` is specified for the `encrypt` function for a mode that does not need it.

#### RQ.SRS008.AES.Encrypt.Function.AdditionalAuthenticationData.NotValidForMode
version: 1.0

[ClickHouse] SHALL return an error if the `aad` is specified for the `encrypt` function for a mode that does not need it.

#### RQ.SRS008.AES.Encrypt.Function.AdditionalAuthenticationData.Length
version: 1.0

[ClickHouse] SHALL not limit the size of the `aad` parameter passed to the `encrypt` function.

#### RQ.SRS008.AES.Encrypt.Function.NonGCMMode.KeyAndInitializationVector.Length
version: 1.0

[ClickHouse] SHALL return an error when the `encrypt` function is called with the following parameter values
when using non-GCM modes

* `aes-128-ecb` mode and `key` is not 16 bytes or `iv` or `aad` is specified
* `aes-192-ecb` mode and `key` is not 24 bytes or `iv` or `aad` is specified
* `aes-256-ecb` mode and `key` is not 32 bytes or `iv` or `aad` is specified
* `aes-128-cbc` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-192-cbc` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-cbc` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-cfb1` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-192-cfb1` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-cfb1` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-cfb8` mode and `key` is not 16 bytes and if specified `iv` is not 16 bytes
* `aes-192-cfb8` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-cfb8` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-cfb128` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-192-cfb128` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-cfb128` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-ofb` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-192-ofb` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-ofb` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-ctr` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes
* `aes-192-ctr` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes
* `aes-256-ctr` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes

#### RQ.SRS008.AES.Encrypt.Function.GCMMode.KeyAndInitializationVector.Length
version: 1.0

[ClickHouse] SHALL return an error when the `encrypt` function is called with the following parameter values
when using GCM modes

* `aes-128-gcm` mode and `key` is not 16 bytes or `iv` is not specified
* `aes-192-gcm` mode and `key` is not 24 bytes or `iv` is not specified
* `aes-256-gcm` mode and `key` is not 32 bytes or `iv` is not specified

### Decrypt Function

#### RQ.SRS008.AES.Decrypt.Function
version: 1.0

[ClickHouse] SHALL support `decrypt` function to decrypt data using [AES].

#### RQ.SRS008.AES.Decrypt.Function.Syntax
version: 1.0

[ClickHouse] SHALL support the following syntax for the `decrypt` function

```sql
decrypt(mode, ciphertext, key, [iv, aad])
```

#### RQ.SRS008.AES.Decrypt.Function.Parameters.CipherText
version: 1.0

[ClickHouse] SHALL support `ciphertext` accepting `FixedString` or `String` data types as
the second parameter to the `decrypt` function that SHALL specify the data to be decrypted.

#### RQ.SRS008.AES.Decrypt.Function.Parameters.Key
version: 1.0

[ClickHouse] SHALL support `key` with `String` or `FixedString` data types
as the third parameter to the `decrypt` function that SHALL specify the encryption key.

#### RQ.SRS008.AES.Decrypt.Function.Parameters.Mode
version: 1.0

[ClickHouse] SHALL support `mode` with `String` or `FixedString` data types as the first parameter
to the `decrypt` function that SHALL specify encryption key length and block encryption mode.

#### RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.ValuesFormat
version: 1.0

[ClickHouse] SHALL support values of the form `aes-[key length]-[mode]` for the `mode` parameter
of the `decrypt` function where
the `key_length` SHALL specifies the length of the key and SHALL accept
`128`, `192`, or `256` as the values and the `mode` SHALL specify the block encryption
mode and SHALL accept [ECB], [CBC], [CFB128], or [OFB] as well as
[CTR] and [GCM] as the values. For example, `aes-256-ofb`.

#### RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.Value.Invalid
version: 1.0

[ClickHouse] SHALL return an error if the specified value for the `mode` parameter of the `decrypt`
function is not valid with the exception where such a mode is supported by the underlying
[OpenSSL] implementation.

#### RQ.SRS008.AES.Decrypt.Function.Parameters.Mode.Values
version: 1.0

[ClickHouse] SHALL support the following [AES] block encryption modes as the value for the `mode` parameter
of the `decrypt` function:

* `aes-128-ecb` that SHALL use [ECB] block mode encryption with 128 bit key
* `aes-192-ecb` that SHALL use [ECB] block mode encryption with 192 bit key
* `aes-256-ecb` that SHALL use [ECB] block mode encryption with 256 bit key
* `aes-128-cbc` that SHALL use [CBC] block mode encryption with 128 bit key
* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 192 bit key
* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 256 bit key
* `aes-128-cfb128` that SHALL use [CFB128] block mode encryption with 128 bit key
* `aes-192-cfb128` that SHALL use [CFB128] block mode encryption with 192 bit key
* `aes-256-cfb128` that SHALL use [CFB128] block mode encryption with 256 bit key
* `aes-128-ofb` that SHALL use [OFB] block mode encryption with 128 bit key
* `aes-192-ofb` that SHALL use [OFB] block mode encryption with 192 bit key
* `aes-256-ofb` that SHALL use [OFB] block mode encryption with 256 bit key
* `aes-128-gcm` that SHALL use [GCM] block mode encryption with 128 bit key
   and [AEAD] 16-byte tag is expected present at the end of the ciphertext according to
   the [RFC5116]
* `aes-192-gcm` that SHALL use [GCM] block mode encryption with 192 bit key
   and [AEAD] 16-byte tag is expected present at the end of the ciphertext according to
   the [RFC5116]
* `aes-256-gcm` that SHALL use [GCM] block mode encryption with 256 bit key
   and [AEAD] 16-byte tag is expected present at the end of the ciphertext according to
   the [RFC5116]
*  `aes-128-ctr` that SHALL use [CTR] block mode encryption with 128 bit key
*  `aes-192-ctr` that SHALL use [CTR] block mode encryption with 192 bit key
*  `aes-256-ctr` that SHALL use [CTR] block mode encryption with 256 bit key

#### RQ.SRS008.AES.Decrypt.Function.Parameters.InitializationVector
version: 1.0

[ClickHouse] SHALL support `iv` with `String` or `FixedString` data types as the optional fourth
parameter to the `decrypt` function that SHALL specify the initialization vector for block modes that require
it.

#### RQ.SRS008.AES.Decrypt.Function.Parameters.AdditionalAuthenticatedData
version: 1.0

[ClickHouse] SHALL support `aad` with `String` or `FixedString` data types as the optional fifth
parameter to the `decrypt` function that SHALL specify the additional authenticated data
for block modes that require it.

#### RQ.SRS008.AES.Decrypt.Function.Parameters.ReturnValue
version: 1.0

[ClickHouse] SHALL return the decrypted value of the data
using `String` data type as the result of `decrypt` function.

#### RQ.SRS008.AES.Decrypt.Function.Key.Length.InvalidLengthError
version: 1.0

[ClickHouse] SHALL return an error if the `key` length is not exact for the `decrypt` function for a given block mode.

#### RQ.SRS008.AES.Decrypt.Function.InitializationVector.Length.InvalidLengthError
version: 1.0

[ClickHouse] SHALL return an error if the `iv` is specified and the length is not exact for the `decrypt` function for a given block mode.

#### RQ.SRS008.AES.Decrypt.Function.InitializationVector.NotValidForMode
version: 1.0

[ClickHouse] SHALL return an error if the `iv` is specified for the `decrypt` function
for a mode that does not need it.

#### RQ.SRS008.AES.Decrypt.Function.AdditionalAuthenticationData.NotValidForMode
version: 1.0

[ClickHouse] SHALL return an error if the `aad` is specified for the `decrypt` function
for a mode that does not need it.

#### RQ.SRS008.AES.Decrypt.Function.AdditionalAuthenticationData.Length
version: 1.0

[ClickHouse] SHALL not limit the size of the `aad` parameter passed to the `decrypt` function.

#### RQ.SRS008.AES.Decrypt.Function.NonGCMMode.KeyAndInitializationVector.Length
version: 1.0

[ClickHouse] SHALL return an error when the `decrypt` function is called with the following parameter values
when using non-GCM modes

* `aes-128-ecb` mode and `key` is not 16 bytes or `iv` or `aad` is specified
* `aes-192-ecb` mode and `key` is not 24 bytes or `iv` or `aad` is specified
* `aes-256-ecb` mode and `key` is not 32 bytes or `iv` or `aad` is specified
* `aes-128-cbc` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-192-cbc` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-cbc` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-cfb1` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-192-cfb1` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-cfb1` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-cfb8` mode and `key` is not 16 bytes and if specified `iv` is not 16 bytes
* `aes-192-cfb8` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-cfb8` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-cfb128` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-192-cfb128` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-cfb128` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-ofb` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-192-ofb` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-256-ofb` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes or `aad` is specified
* `aes-128-ctr` mode and `key` is not 16 bytes or if specified `iv` is not 16 bytes
* `aes-192-ctr` mode and `key` is not 24 bytes or if specified `iv` is not 16 bytes
* `aes-256-ctr` mode and `key` is not 32 bytes or if specified `iv` is not 16 bytes

#### RQ.SRS008.AES.Decrypt.Function.GCMMode.KeyAndInitializationVector.Length
version: 1.0

[ClickHouse] SHALL return an error when the `decrypt` function is called with the following parameter values
when using GCM modes

* `aes-128-gcm` mode and `key` is not 16 bytes or `iv` is not specified
* `aes-192-gcm` mode and `key` is not 24 bytes or `iv` is not specified
* `aes-256-gcm` mode and `key` is not 32 bytes or `iv` is not specified

### MySQL Encrypt Function

#### RQ.SRS008.AES.MySQL.Encrypt.Function
version: 1.0

[ClickHouse] SHALL support `aes_encrypt_mysql` function to encrypt data using [AES].

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Syntax
version: 1.0

[ClickHouse] SHALL support the following syntax for the `aes_encrypt_mysql` function

```sql
aes_encrypt_mysql(mode, plaintext, key, [iv])
```

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.PlainText
version: 2.0

[ClickHouse] SHALL support `plaintext` with `String`, `FixedString`, `Nullable(String)`,
`Nullable(FixedString)`, `LowCardinality(String)`, or `LowCardinality(FixedString(N))` data types as
the second parameter to the `aes_encrypt_mysql` function that SHALL specify the data to be encrypted.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Key
version: 1.0

[ClickHouse] SHALL support `key` with `String` or `FixedString` data types
as the third parameter to the `aes_encrypt_mysql` function that SHALL specify the encryption key.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode
version: 1.0

[ClickHouse] SHALL support `mode` with `String` or `FixedString` data types as the first parameter
to the `aes_encrypt_mysql` function that SHALL specify encryption key length and block encryption mode.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.ValuesFormat
version: 1.0

[ClickHouse] SHALL support values of the form `aes-[key length]-[mode]` for the `mode` parameter
of the `aes_encrypt_mysql` function where
the `key_length` SHALL specifies the length of the key and SHALL accept
`128`, `192`, or `256` as the values and the `mode` SHALL specify the block encryption
mode and SHALL accept [ECB], [CBC], [CFB128], or [OFB]. For example, `aes-256-ofb`.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Value.Invalid
version: 1.0

[ClickHouse] SHALL return an error if the specified value for the `mode` parameter of the `aes_encrypt_mysql`
function is not valid with the exception where such a mode is supported by the underlying
[OpenSSL] implementation.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values
version: 1.0

[ClickHouse] SHALL support the following [AES] block encryption modes as the value for the `mode` parameter
of the `aes_encrypt_mysql` function:

* `aes-128-ecb` that SHALL use [ECB] block mode encryption with 128 bit key
* `aes-192-ecb` that SHALL use [ECB] block mode encryption with 192 bit key
* `aes-256-ecb` that SHALL use [ECB] block mode encryption with 256 bit key
* `aes-128-cbc` that SHALL use [CBC] block mode encryption with 128 bit key
* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 192 bit key
* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 256 bit key
* `aes-128-cfb128` that SHALL use [CFB128] block mode encryption with 128 bit key
* `aes-192-cfb128` that SHALL use [CFB128] block mode encryption with 192 bit key
* `aes-256-cfb128` that SHALL use [CFB128] block mode encryption with 256 bit key
* `aes-128-ofb` that SHALL use [OFB] block mode encryption with 128 bit key
* `aes-192-ofb` that SHALL use [OFB] block mode encryption with 192 bit key
* `aes-256-ofb` that SHALL use [OFB] block mode encryption with 256 bit key

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values.GCM.Error
version: 1.0

[ClickHouse] SHALL return an error if any of the following [GCM] modes are specified as the value 
for the `mode` parameter of the `aes_encrypt_mysql` function

* `aes-128-gcm`
* `aes-192-gcm`
* `aes-256-gcm`

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.Mode.Values.CTR.Error
version: 1.0

[ClickHouse] SHALL return an error if any of the following [CTR] modes are specified as the value 
for the `mode` parameter of the `aes_encrypt_mysql` function

* `aes-128-ctr`
* `aes-192-ctr`
* `aes-256-ctr`

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.InitializationVector
version: 1.0

[ClickHouse] SHALL support `iv` with `String` or `FixedString` data types as the optional fourth
parameter to the `aes_encrypt_mysql` function that SHALL specify the initialization vector for block modes that require
it.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Parameters.ReturnValue
version: 1.0

[ClickHouse] SHALL return the encrypted value of the data
using `String` data type as the result of `aes_encrypt_mysql` function.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Key.Length.TooShortError
version: 1.0

[ClickHouse] SHALL return an error if the `key` length is less than the minimum for the `aes_encrypt_mysql`
function for a given block mode.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Key.Length.TooLong
version: 1.0

[ClickHouse] SHALL use folding algorithm specified below if the `key` length is longer than required
for the `aes_encrypt_mysql` function for a given block mode.

```python
def fold_key(key, cipher_key_size):
    key = list(key) if not isinstance(key, (list, tuple)) else key
	  folded_key = key[:cipher_key_size]
	  for i in range(cipher_key_size, len(key)):
		    print(i % cipher_key_size, i)
		    folded_key[i % cipher_key_size] ^= key[i]
	  return folded_key
```

#### RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.Length.TooShortError
version: 1.0

[ClickHouse] SHALL return an error if the `iv` length is specified and is less than the minimum
that is required for the `aes_encrypt_mysql` function for a given block mode.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.Length.TooLong
version: 1.0

[ClickHouse] SHALL use the first `N` bytes that are required if the `iv` is specified and
its length is longer than required for the `aes_encrypt_mysql` function for a given block mode.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.InitializationVector.NotValidForMode
version: 1.0

[ClickHouse] SHALL return an error if the `iv` is specified for the `aes_encrypt_mysql`
function for a mode that does not need it.

#### RQ.SRS008.AES.MySQL.Encrypt.Function.Mode.KeyAndInitializationVector.Length
version: 1.0

[ClickHouse] SHALL return an error when the `aes_encrypt_mysql` function is called with the following parameter values

* `aes-128-ecb` mode and `key` is less than 16 bytes or `iv` is specified
* `aes-192-ecb` mode and `key` is less than 24 bytes or `iv` is specified
* `aes-256-ecb` mode and `key` is less than 32 bytes or `iv` is specified
* `aes-128-cbc` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes
* `aes-192-cbc` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-cbc` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes
* `aes-128-cfb1` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes
* `aes-192-cfb1` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-cfb1` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes
* `aes-128-cfb8` mode and `key` is less than 16 bytes and if specified `iv` is less than 16 bytes
* `aes-192-cfb8` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-cfb8` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes
* `aes-128-cfb128` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes
* `aes-192-cfb128` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-cfb128` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes
* `aes-128-ofb` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes
* `aes-192-ofb` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-ofb` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes

### MySQL Decrypt Function

#### RQ.SRS008.AES.MySQL.Decrypt.Function
version: 1.0

[ClickHouse] SHALL support `aes_decrypt_mysql` function to decrypt data using [AES].

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Syntax
version: 1.0

[ClickHouse] SHALL support the following syntax for the `aes_decrypt_mysql` function

```sql
aes_decrypt_mysql(mode, ciphertext, key, [iv])
```

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.CipherText
version: 1.0

[ClickHouse] SHALL support `ciphertext` accepting any data type as
the second parameter to the `aes_decrypt_mysql` function that SHALL specify the data to be decrypted.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Key
version: 1.0

[ClickHouse] SHALL support `key` with `String` or `FixedString` data types
as the third parameter to the `aes_decrypt_mysql` function that SHALL specify the encryption key.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode
version: 1.0

[ClickHouse] SHALL support `mode` with `String` or `FixedString` data types as the first parameter
to the `aes_decrypt_mysql` function that SHALL specify encryption key length and block encryption mode.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.ValuesFormat
version: 1.0

[ClickHouse] SHALL support values of the form `aes-[key length]-[mode]` for the `mode` parameter
of the `aes_decrypt_mysql` function where
the `key_length` SHALL specifies the length of the key and SHALL accept
`128`, `192`, or `256` as the values and the `mode` SHALL specify the block encryption
mode and SHALL accept [ECB], [CBC], [CFB128], or [OFB]. For example, `aes-256-ofb`.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Value.Invalid
version: 1.0

[ClickHouse] SHALL return an error if the specified value for the `mode` parameter of the `aes_decrypt_mysql`
function is not valid with the exception where such a mode is supported by the underlying
[OpenSSL] implementation.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values
version: 1.0

[ClickHouse] SHALL support the following [AES] block encryption modes as the value for the `mode` parameter
of the `aes_decrypt_mysql` function:

* `aes-128-ecb` that SHALL use [ECB] block mode encryption with 128 bit key
* `aes-192-ecb` that SHALL use [ECB] block mode encryption with 192 bit key
* `aes-256-ecb` that SHALL use [ECB] block mode encryption with 256 bit key
* `aes-128-cbc` that SHALL use [CBC] block mode encryption with 128 bit key
* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 192 bit key
* `aes-192-cbc` that SHALL use [CBC] block mode encryption with 256 bit key
* `aes-128-cfb128` that SHALL use [CFB128] block mode encryption with 128 bit key
* `aes-192-cfb128` that SHALL use [CFB128] block mode encryption with 192 bit key
* `aes-256-cfb128` that SHALL use [CFB128] block mode encryption with 256 bit key
* `aes-128-ofb` that SHALL use [OFB] block mode encryption with 128 bit key
* `aes-192-ofb` that SHALL use [OFB] block mode encryption with 192 bit key
* `aes-256-ofb` that SHALL use [OFB] block mode encryption with 256 bit key

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values.GCM.Error
version: 1.0

[ClickHouse] SHALL return an error if any of the following [GCM] modes are specified as the value 
for the `mode` parameter of the `aes_decrypt_mysql` function

* `aes-128-gcm`
* `aes-192-gcm`
* `aes-256-gcm`

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.Mode.Values.CTR.Error
version: 1.0

[ClickHouse] SHALL return an error if any of the following [CTR] modes are specified as the value 
for the `mode` parameter of the `aes_decrypt_mysql` function

* `aes-128-ctr`
* `aes-192-ctr`
* `aes-256-ctr`

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.InitializationVector
version: 1.0

[ClickHouse] SHALL support `iv` with `String` or `FixedString` data types as the optional fourth
parameter to the `aes_decrypt_mysql` function that SHALL specify the initialization vector for block modes that require
it.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Parameters.ReturnValue
version: 1.0

[ClickHouse] SHALL return the decrypted value of the data
using `String` data type as the result of `aes_decrypt_mysql` function.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Key.Length.TooShortError
version: 1.0

[ClickHouse] SHALL return an error if the `key` length is less than the minimum for the `aes_decrypt_mysql`
function for a given block mode.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Key.Length.TooLong
version: 1.0

[ClickHouse] SHALL use folding algorithm specified below if the `key` length is longer than required
for the `aes_decrypt_mysql` function for a given block mode.

```python
def fold_key(key, cipher_key_size):
    key = list(key) if not isinstance(key, (list, tuple)) else key
	  folded_key = key[:cipher_key_size]
	  for i in range(cipher_key_size, len(key)):
		    print(i % cipher_key_size, i)
		    folded_key[i % cipher_key_size] ^= key[i]
	  return folded_key
```

#### RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.Length.TooShortError
version: 1.0

[ClickHouse] SHALL return an error if the `iv` length is specified and is less than the minimum
that is required for the `aes_decrypt_mysql` function for a given block mode.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.Length.TooLong
version: 1.0

[ClickHouse] SHALL use the first `N` bytes that are required if the `iv` is specified and
its length is longer than required for the `aes_decrypt_mysql` function for a given block mode.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.InitializationVector.NotValidForMode
version: 1.0

[ClickHouse] SHALL return an error if the `iv` is specified for the `aes_decrypt_mysql`
function for a mode that does not need it.

#### RQ.SRS008.AES.MySQL.Decrypt.Function.Mode.KeyAndInitializationVector.Length
version: 1.0

[ClickHouse] SHALL return an error when the `aes_decrypt_mysql` function is called with the following parameter values

* `aes-128-ecb` mode and `key` is less than 16 bytes or `iv` is specified
* `aes-192-ecb` mode and `key` is less than 24 bytes or `iv` is specified
* `aes-256-ecb` mode and `key` is less than 32 bytes or `iv` is specified
* `aes-128-cbc` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes
* `aes-192-cbc` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-cbc` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes
* `aes-128-cfb1` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes
* `aes-192-cfb1` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-cfb1` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes
* `aes-128-cfb8` mode and `key` is less than 16 bytes and if specified `iv` is less than 16 bytes
* `aes-192-cfb8` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-cfb8` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes
* `aes-128-cfb128` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes
* `aes-192-cfb128` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-cfb128` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes
* `aes-128-ofb` mode and `key` is less than 16 bytes or if specified `iv` is less than 16 bytes
* `aes-192-ofb` mode and `key` is less than 24 bytes or if specified `iv` is less than 16 bytes
* `aes-256-ofb` mode and `key` is less than 32 bytes or if specified `iv` is less than 16 bytes

## References

* **GDPR:** https://en.wikipedia.org/wiki/General_Data_Protection_Regulation
* **MySQL:** https://www.mysql.com/
* **AES:** https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
* **ClickHouse:** https://clickhouse.com
* **Git:** https://git-scm.com/

[AEAD]: #aead
[OpenSSL]: https://www.openssl.org/
[LowCardinality]: https://clickhouse.com/docs/en/sql-reference/data-types/lowcardinality/
[MergeTree]: https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/
[MySQL Database Engine]: https://clickhouse.com/docs/en/engines/database-engines/mysql/
[MySQL Table Engine]: https://clickhouse.com/docs/en/engines/table-engines/integrations/mysql/
[MySQL Table Function]: https://clickhouse.com/docs/en/sql-reference/table-functions/mysql/
[MySQL Dictionary]: https://clickhouse.com/docs/en/sql-reference/dictionaries/external-dictionaries/external-dicts-dict-sources/#dicts-external_dicts_dict_sources-mysql
[GCM]: https://en.wikipedia.org/wiki/Galois/Counter_Mode
[CTR]: https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)
[CBC]: https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)
[ECB]: https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)
[CFB]: https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_feedback_(CFB)
[CFB128]: https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_feedback_(CFB)
[OFB]: https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Output_feedback_(OFB)
[GDPR]: https://en.wikipedia.org/wiki/General_Data_Protection_Regulation
[RFC5116]: https://tools.ietf.org/html/rfc5116#section-5.1
[MySQL]: https://www.mysql.com/
[MySQL 5.7]: https://dev.mysql.com/doc/refman/5.7/en/
[MySQL aes_encrypt]: https://dev.mysql.com/doc/refman/5.7/en/encryption-functions.html#function_aes-encrypt
[MySQL aes_decrypt]: https://dev.mysql.com/doc/refman/5.7/en/encryption-functions.html#function_aes-decrypt
[AES]: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
[ClickHouse]: https://clickhouse.com
[GitHub repository]: https://github.com/ClickHouse/ClickHouse/blob/master/tests/testflows/aes_encryption/requirements/requirements.md
[Revision history]: https://github.com/ClickHouse/ClickHouse/commits/master/tests/testflows/aes_encryption/requirements/requirements.md
[Git]: https://git-scm.com/
[NIST test vectors]: https://csrc.nist.gov/Projects/Cryptographic-Algorithm-Validation-Program
""",
)
