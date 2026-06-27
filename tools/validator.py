import re


def validate_url(url):
    """验证URL格式是否有效 - 暂时允许所有 http/https 网站"""
    return url.lower().startswith(("http://", "https://"))
