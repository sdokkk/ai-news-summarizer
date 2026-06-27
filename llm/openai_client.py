import os

from dotenv import load_dotenv
from openai import OpenAI

# 读取 .env 文件
load_dotenv()

# 创建 OpenAI 客户端
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize(text: str) -> str:
    """使用 GPT 对文章进行总结"""

    response = client.responses.create(
        model="gpt-5.5",
        input=f"""
请总结下面文章。

要求：
1. 三句话总结
2. 提炼核心观点
3. 给出普通人的启发

文章：

{text}
""",
    )

    return response.output_text