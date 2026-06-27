
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from collections import Counter

STOPWORDS = {
    "the", "and", "is", "in", "it", "of", "to", "a", "an", "that", "this", "for", "on", "with",
    "as", "by", "from", "at", "be", "are", "or", "was", "were", "will", "can", "has", "have",
    "not", "but", "if", "so", "they", "their", "its", "which", "about", "into", "than", "also",
}

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._skip = 0
        self._text = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript"}:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript"} and self._skip > 0:
            self._skip -= 1

    def handle_data(self, data):
        if self._skip == 0:
            self._text.append(data)

    def get_text(self):
        return " ".join(self._text).strip()


def fetch_html(url, timeout=15):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        encoding = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(encoding, errors="replace")


def extract_text(html):
    parser = TextExtractor()
    parser.feed(html)
    parser.close()
    text = parser.get_text()
    text = re.sub(r"\s+", " ", text)
    return text


def split_sentences(text):
    text = text.replace("\n", " ")
    sentences = re.split(r"(?<=[。！？!?])\s+", text)
    return [s.strip() for s in sentences if len(s.strip()) >= 20]


def word_tokens(text):
    text = text.lower()
    return re.findall(r"[a-z0-9\u4e00-\u9fff]+", text)


def summarize(text, limit=3):
    sentences = split_sentences(text)
    if not sentences:
        return "无法从文章中提取到足够的可总结内容。"

    words = [w for w in word_tokens(text) if w not in STOPWORDS]
    if not words:
        return "文章内容无法用于摘要。"

    frequencies = Counter(words)
    max_freq = max(frequencies.values(), default=1)
    for word in frequencies:
        frequencies[word] /= max_freq

    sentence_scores = []
    for index, sentence in enumerate(sentences):
        sent_words = [w for w in word_tokens(sentence) if w not in STOPWORDS]
        score = sum(frequencies.get(w, 0) for w in sent_words)
        sentence_scores.append((index, score, sentence))

    sentence_scores.sort(key=lambda item: (item[1], -item[0]), reverse=True)
    top_indices = sorted(idx for idx, _, _ in sentence_scores[:limit])
    summary = "\n".join(sentences[i] for i in top_indices)
    return summary


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("请输入文章链接：").strip()

    if not url:
        print("请输入有效的文章链接。")
        return

    print("\n文章链接：")
    print(url)

    try:
        html = fetch_html(url)
        text = extract_text(html)
        summary = summarize(text)
    except urllib.error.URLError as error:
        summary = f"无法获取文章内容：{error.reason}"
    except Exception as error:
        summary = f"处理文章时发生错误：{error}"

    print("\n文章摘要：")
    print(summary)

    print("\n请将这个链接发送给Claude：")
    print(f"请帮我总结这篇文章的核心观点：{url}")


if __name__ == "__main__":
    main()
