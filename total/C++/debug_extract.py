import urllib.request
import re
import html as html_mod

url = "https://www.runoob.com/cplusplus/cpp-tutorial.html"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
})
with urllib.request.urlopen(req, timeout=20) as resp:
    html_content = resp.read().decode("utf-8", errors="replace")

# Extract article body
m = re.search(
    r'class="article-body"[^>]*>(.*?)(?:<div\s+class="previous-next-links"|<div\s+class="article-footer")',
    html_content, re.DOTALL
)

if m:
    article = m.group(1)
    # Find example_code divs
    codes = re.findall(r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>\s*</div>', article, re.DOTALL)
    print(f"Found {len(codes)} example_code blocks")
    for i, code in enumerate(codes):
        # Strip span tags
        clean = re.sub(r'</?span[^>]*>', '', code)
        clean = re.sub(r'<br\s*/?>', '\n', clean)
        clean = html_mod.unescape(clean)
        clean = re.sub(r'<[^>]+>', '', clean)
        print(f"\n--- Code block {i+1} ({len(clean)} chars) ---")
        print(clean[:300])
else:
    print("No article-body found")
