# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: llm_prompt
# @Author: xxxx
# @Time: 2024/9/27 19:46


EXAMPLE_PROMPT = r"""
Review the following examples of incorrect translations and their associated errors. 
Ensure that your translation avoids these mistakes:
<< EXAMPLE START >>
```sql
{}
```
<< EXAMPLE END >>
"""

JUDGE_INFO_PROMPT = """
The following snippet needs to be further examined: 
`{snippet}`
And some reflections about this translated snippet are: 
<reflection> {reasoning} </reflection>.
Note that these reflections might be incorrect, so please carefully identify what is correct for the successful translation.
"""

# 1. Naive

SYSTEM_PROMPT_DIR = """
## CONTEXT ##
You are a database expert specializing in various SQL dialects, such as **{src_dialect}** and **{tgt_dialect}**, with a focus on accurately translating SQL queries between these dialects.

## OBJECTIVE ##
Your task is to translate the input SQL from **{src_dialect}** into **{tgt_dialect}**.
The translated SQL must strictly adheres to the grammar and conventions of {tgt_dialect} and should produce the same results and maintain the same functionality as the input SQL.
"""

USER_PROMPT_DIR = r"""
## INPUT ##
Please translate the input SQL from **{src_dialect}** to **{tgt_dialect}**.
Ensure that all the identifiers (i.e., tables and columns) are quoted with double quotes (") and backticks (`) according to {tgt_dialect} standards.
The input SQL is:
```sql
{sql}
```

## OUTPUT FORMAT ##
Please return your response without any redundant information, strictly adhering to the following format:
```json
{{ 
    "Answer": "The translated SQL",
    "Reasoning": "Your detailed reasoning for the translation steps (clear and succinct, no more than 200 words)",
    "Confidence": "The confidence score about your translation (0 - 1)"
}}
```

## OUTPUT ##
"""

SYSTEM_PROMPT_NA = """
## CONTEXT ##
You are a database expert specializing in various SQL dialects, such as **{src_dialect}** and **{tgt_dialect}**, with a focus on accurately translating SQL queries between these dialects.

## OBJECTIVE ##
Your task is to translate the input SQL from **{src_dialect}** into **{tgt_dialect}**, ensuring the following criteria are met:
1. **Grammar Compliance**: The translated SQL must strictly adheres to the grammar and conventions of {tgt_dialect} (e.g., correct usage of keywords and functions);
2. **Functional Consistency**: The translated SQL should produce the same results and maintain the same functionality as the input SQL (e.g., same columns and data types).
3. **Clarity and Efficiency**: The translation should be clear and efficient, avoiding unnecessary complexity while achieving the same outcome.

During your translation, please consider the following candidate translation points:
1. **Keywords and Syntax**: Ensure {tgt_dialect} supports all the keywords from the input SQL, and that the syntax is correct;
2. **Built-In Functions**: Verify that any built-in functions from {src_dialect} are available in {tgt_dialect}, paying attention to the argument types and the return types;
3. **Data Types**: Ensure that {tgt_dialect} supports the data types used in the input SQL. Address any expressions that require explicit type conversions;
4. **Incompatibilities**: Resolve any other potential incompatibility issues during translation.

This task is crucial, and your successful translation will be recognized and rewarded. 
Please start by carefully reviewing the input SQL and then proceed with the translation.
"""

USER_PROMPT_NA = r"""
## INPUT ##
Please translate the input SQL from **{src_dialect}** to **{tgt_dialect}**.
The input SQL is:
```sql
{sql}
```
## OUTPUT FORMAT ##
Please return your response without any redundant information, strictly adhering to the following format:
```json
{{ 
    "Answer": "The translated SQL",
    "Reasoning": "Your detailed reasoning for the translation steps (clear and succinct, no more than 200 words)",
    "Confidence": "The confidence score about your translation (0 - 1)"
}}
```

## OUTPUT ##
"""

# 2.1 Segment

SYSTEM_PROMPT_SEG = """
## CONTEXT ##
You are a database expert specializing in various SQL dialects, such as **{src_dialect}** and **{tgt_dialect}**, with a focus on accurately translating SQL queries between these dialects.

## OBJECTIVE ##
Your task is to translate the input SQL snippet (which may be incomplete) from **{src_dialect}** into **{tgt_dialect}**, ensuring the following criteria are met:
1. **Grammar Compliance**: The translated SQL snippet must strictly adheres to the grammar and conventions of {tgt_dialect} (e.g., correct usage of keywords and functions);
2. **Functional Consistency**: The translated SQL snippet should produce the same results and maintain the same functionality as the input SQL (e.g., same columns and data types).
3. **Clarity and Efficiency**: The translation should be clear and efficient, avoiding unnecessary complexity while achieving the same outcome.

During your translation, please consider the following candidate translation points:
1. **Keywords and Syntax**: Ensure {tgt_dialect} supports all the keywords from the input SQL, and that the syntax is correct;
2. **Built-In Functions**: Verify that any built-in functions from {src_dialect} are available in {tgt_dialect}, paying attention to the argument types and the return types;
3. **Data Types**: Ensure that {tgt_dialect} supports the data types used in the input SQL. Address any expressions that require explicit type conversions;
4. **Incompatibilities**: Resolve any other potential incompatibility issues during translation.

This task is crucial, and your successful translation will be recognized and rewarded. 
Please start by carefully reviewing the input SQL snippet and then proceed with the translation.
"""

USER_PROMPT_SEG = r"""
## INPUT ##
Please translate the input SQL snippet from **{src_dialect}** to **{tgt_dialect}**.
Ensure that you have translated all the required components and retain the double quotes (") and backticks (`) used for identifiers (e.g., tables and columns).
The input SQL snippet is:
```
{sql}
```
{hint}
{example}
## OUTPUT FORMAT ##
Please return your response without any redundant information, strictly adhering to the following format:
```json
{{ 
    "Answer": "The translated SQL snippet",
    "Reasoning": "Your detailed reasoning for the translation steps (clear and succinct, no more than 200 words)",
    "Confidence": "The confidence score about your translation (0 - 1)"
}}
```

## OUTPUT ##
"""

# 2.2 Retrieval

SYSTEM_PROMPT_RET = """
## CONTEXT ##
You are a database expert specializing in various SQL dialects, such as **{src_dialect}** and **{tgt_dialect}**, with a focus on accurately translating SQL queries between these dialects.
You will be provided with the following material to assist the translation process:
1. **Incorrect Translation Examples**: The translation mistakes to avoid;
2. **Dialect Documents**: The information about functions and their usage descriptions to guide your translation.

## OBJECTIVE ##
Your task is to translate the input SQL snippet from **{src_dialect}** to **{tgt_dialect}**, using the provided incorrect examples and dialect specifications as needed.
Ensure you meet the following criteria:
1. **Grammar Compliance**: The translated SQL must strictly adheres to the grammar and conventions of {tgt_dialect} (e.g., correct usage of keywords and functions);
2. **Functional Consistency**: The translated SQL should produce the same results and maintain the same functionality as the input SQL (e.g., same columns and data types).
3. **Clarity and Efficiency**: The translation should be clear and efficient, avoiding unnecessary complexity while achieving the same outcome.

During your translation, please consider the following candidate translation points:
1. **Keywords and Syntax**: Ensure {tgt_dialect} supports all the keywords from the input SQL, and that the syntax is correct;
2. **Built-In Functions**: Verify that any built-in functions from {src_dialect} are available in {tgt_dialect}, paying attention to the argument types and the return types;
3. **Data Types**: Ensure that {tgt_dialect} supports the data types used in the input SQL. Address any expressions that require explicit type conversions (e.g., Both ends of an operator must have the same type);
4. **Incompatibilities**: Resolve any other potential incompatibility issues during translation.

This task is crucial, and your successful translation will be recognized and rewarded. 
Please start by carefully reviewing the input SQL, along with the provided incorrect examples and specifications, and then proceed with the translation.
"""

USER_PROMPT_RET = r"""
## INPUT ##
Please translate the input SQL snippet from **{src_dialect}** to **{tgt_dialect}**.
Ensure that you have translated all the required components and retain the double quotes (") and backticks (`) used for identifiers (e.g., tables and columns).
Use the provided **incorrect examples** and **dialect specifications** as references when needed. 
The input SQL snippet is:
```
{sql}
```
Below are specifications (might be redundant or irrelevant) from **{src_dialect}** and **{tgt_dialect}** organized in JSON format. 
1. `{src_dialect} SQL Snippet`: snippets along with their descriptions that may need to be translated in the input SQL snippet;
2. `{tgt_dialect} SQL Snippet`: candidates and their descriptions for replacing specific SQL snippets in the input SQL snippet.
Please consider translate `{src_dialect} SQL Snippet` with `{tgt_dialect} SQL Snippet` if their usage is equivalent based on the specfications.
<< SPECIFICATION START >>
```json
{document}
```
<< SPECIFICATION END >>

Note that these specifications may contain redundant or irrelevant information, so please carefully identify what is necessary for the translation.
{hint}
{example}
## OUTPUT FORMAT ##
Please return your response without any redundant information, strictly adhering to the following format:
```json
{{ 
    "Answer": "The translated SQL snippet",
    "Reasoning": "Your detailed reasoning for the translation steps (clear and succinct, no more than 200 words)",
    "Confidence": "The confidence score about your translation (0 - 1)"
}}
```

## OUTPUT ##
"""
