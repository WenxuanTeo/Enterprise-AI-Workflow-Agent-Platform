import openai

def plan_task(query: str):
    prompt = f"""
你是一个任务拆解Agent，请将用户需求拆解为步骤。

输出JSON格式：

{{
  "task": "...",
  "steps": [
    "...",
    "..."
  ]
}}

用户需求：
{query}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
