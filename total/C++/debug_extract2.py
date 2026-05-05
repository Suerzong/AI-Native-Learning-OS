import urllib.request
import re

url = "https://www.runoob.com/cplusplus/cpp-tutorial.html"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
})
with urllib.request.urlopen(req, timeout=20) as resp:
    html_content = resp.read().decode("utf-8", errors="replace")

m = re.search(
    r'class="article-body"[^>]*>(.*?)(?:<div\s+class="previous-next-links"|<div\s+class="article-footer")',
    html_content, re.DOTALL
)

article = m.group(1)

# Find example_code with triple </div> pattern
codes = re.findall(
    r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>\s*</div>\s*(?:</div>)?',
    article, re.DOTALL
)
print(f"Found {len(codes)} blocks with triple pattern")

for i, code in enumerate(codes):
    print(f"\n--- Raw captured block {i+1} ({len(code)} chars) ---")
    print(repr(code[:500]))
