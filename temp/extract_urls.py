#!/usr/bin/env python3
"""从 1ppt.com 文章页提取下载链接。"""
import sys, re, json
sys.path.insert(0, "/tmp/pw_env/lib/python3.12/site-packages")
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": "acw_sc__v2=5d28f9cf9488b842094f6a6bfc41376161c0b6451bcbde0ab1",  # 固定值试试
}

# 测试页面
url = "https://www.1ppt.com/article/143511.html"
r = requests.get(url, headers=HEADERS, timeout=30)
print(f"Status: {r.status_code}")
print(f"Content length: {len(r.text)}")
print(f"WAF: {'acw_sc__v2' in r.text or 'aliyun_waf' in r.text}")

soup = BeautifulSoup(r.text, "html.parser")

# 找 downurllist
downlist = soup.find("ul", class_="downurllist")
if downlist:
    print("\n=== downurllist ===")
    links = downlist.find_all("a")
    for a in links:
        href = a.get("href", "")
        text = a.get_text(strip=True)
        print(f"  {href} - {text}")
else:
    print("\nNo downurllist found")
    # 查看页面中所有 download 相关
    for el in soup.find_all(["a", "div", "ul"], string=re.compile(r"down", re.I)):
        print(f"  Found: {el.name} - {el.get_text(strip=True)[:100]}")

    # 查找下载区域
    for el in soup.find_all("ul"):
        if "down" in str(el.get("class", "")).lower():
            print(f"\n  ul class={el.get('class')}:")
            print(el.prettify()[:500])

    # 保存预览
    body = soup.find("body")
    if body:
        text = body.get_text()
        idx = text.lower().find("下载")
        if idx >= 0:
            print(f"\n=== 页面中 '下载' 附近内容 ===")
            print(text[max(0,idx-200):idx+500])
