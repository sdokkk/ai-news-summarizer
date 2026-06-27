import re
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    """从HTML中提取文本"""
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


def extract_text(html):
    """从HTML提取纯文本"""
    parser = TextExtractor()
    parser.feed(html)
    parser.close()
    text = parser.get_text()
    text = re.sub(r"\s+", " ", text)
    return text


def split_sentences(text):
    """将文本分割成句子"""
    text = text.replace("\n", " ")
    sentences = re.split(r"(?<=[。！？!?])\s+", text)
    return [s.strip() for s in sentences if len(s.strip()) >= 20]


def word_tokens(text):
    """将文本分词"""
    text = text.lower()
    return re.findall(r"[a-z0-9\u4e00-\u9fff]+", text)
