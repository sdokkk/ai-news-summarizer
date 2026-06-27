
import sys
import urllib.error

from tools.validator import validate_url
from tools.fetcher import fetch_webpage
from tools.parser import extract_text
from tools.markdown import save_markdown
from llm.openai_client import summarize


def main():
    url = input("请输入文章链接：").strip()

    if not validate_url(url):
        print("请输入有效的网址。")
        return

    print("正在下载网页...")

    html = fetch_webpage(url)

    if not html:
        print("网页下载失败。")
        return

    print("正在提取正文...")

    text = extract_text(html)

    if not text:
        print("没有提取到正文。")
        return

    print("正在调用 GPT，总结中，请稍候...")

    summary = summarize(text)

    filepath = save_markdown(url, summary)

    print("\n========== AI 总结 ==========")
    print(summary)

    print("\nMarkdown 已保存：")
    print(filepath)


if __name__ == "__main__":
    main()
