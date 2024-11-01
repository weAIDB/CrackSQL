# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: judge_prompt
# @Author: xxxx
# @Time: 2024/10/5 14:44


# Judge

SYSTEM_PROMPT_JUDGE = """
## CONTEXT ##
You are a database expert specializing in various SQL dialects, such as **{src_dialect}** and **{tgt_dialect}**.
Your primary focus is on accurately translating SQL queries between these dialects.

## OBJECTIVE ##
Your task is to analyze two SQL queries, one written in {src_dialect} and the other in {tgt_dialect}, to determine if they are functionally equivalent:
1. **Maintain Semantic Consistency**: Perform the same operations on the dataset with the same meaning and intent;
2. **Produce Identical Output**: Return the same results for most practical purposes, ensuring that matched values have consistent data types and are presented in identical formats.
"""

USER_PROMPT_JUDGE = r"""
## INPUT ##
Please analyze whether the following {tgt_dialect} SQL is functionally equivalent to the {src_dialect} SQL for most practical purposes (i.e., they return the same results with consistent data types and formats).
Examine and compare each snippet of the two queries (e.g., the {snippet} in {tgt_dialect} SQL).
The **{src_dialect}** SQL is:
```sql
{src_sql}
```
The **{tgt_dialect}** SQL is:
```sql
{tgt_sql}
```

## OUTPUT FORMAT ##
Identify the first SQL snippet in {tgt_dialect} SQL that needs to be translated while conforming to {tgt_dialect} standards. 
Return your response without any redundant information in the following format:
```json
{{ 
    "SQL Snippet": "The first SQL snippet in {tgt_dialect} SQL that needs to be translated or `NONE`",
    "Reasoning": "Your detailed reasoning for the SQL snippet that needs to be translated (clear and succinct, no more than 200 words)",
    "Confidence": "The confidence score about your judgement (0 - 1)"
}}
```
Return `NONE` if the {tgt_dialect} SQL is already functionally equivalent to the {src_dialect} SQL for most practical purposes (i.e., slightly different over regardless of some edge cases).

## OUTPUT ##
"""

USER_PROMPT_REFLECT = r"""
Using the previously translated snippet (i.e., `{snippet}`), please analyze whether the following translated {tgt_dialect} SQL is equivalent to the reference {src_dialect} SQL for practical purposes. 
This means they should return the same results with consistent data types and formats.
Your task is to carefully examine the {tgt_dialect} SQL and identify the first SQL snippet that needs further translation while following {tgt_dialect} standards.

## INPUT ##
The translated **{tgt_dialect}** SQL is:
```sql
{tgt_sql}
```
The reference **{src_dialect}** SQL is:
```sql
{src_sql}
```

## OUTPUT FORMAT ##
Please provide your response without any unnecessary information, adhering to the following format:
```json
{{ 
    "SQL Snippet": "'NONE' or the first SQL snippet in {tgt_dialect} SQL that needs to be translated",
    "Reasoning": "Your detailed reasoning for identifying the SQL snippet that needs translation (clear and succinct, no more than 200 words)",
    "Confidence": "Your confidence score regarding this judgment (0 - 1)"
}}
```
If the translated {tgt_dialect} SQL is already equivalent, fill the "SQL Snippet" with 'NONE', even if there are minor differences in edge cases.

## OUTPUT ##
"""
