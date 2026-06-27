from pathlib import Path
from datetime import datetime


def save_markdown(url: str, summary: str) -> str:
    """保存摘要为 Markdown 文件"""

    # 创建 output 文件夹
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # 用时间作为文件名
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.md")

    filepath = output_dir / filename

    content = f"""# AI News Summary

## 原文链接

{url}

## AI 总结

{summary}
"""

    filepath.write_text(content, encoding="utf-8")

    return str(filepath)