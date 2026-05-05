import urllib.request
import re
import html as html_mod

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

# Show the raw HTML around example_code
idx = article.find('example_code')
print("=== Around first example_code ===")
print(repr(article[idx-50:idx+500]))
print()

# Test the triple-div pattern
matches = list(re.finditer(
    r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>\s*</div>\s*(?:</div>)?',
    article, re.DOTALL
))
print(f"Found {len(matches)} matches with triple pattern")

for i, m in enumerate(matches):
    raw = m.group(1)
    print(f"\n--- Match {i+1} ---")
    print(f"Position: {m.start()}-{m.end()}")
    # Simulate clean_code
    text = re.sub(r'<br\s*/?>', '\n', raw)
    text = re.sub(r'</?span[^>]*>', '', text)
    text = re.sub(r'<div[^>]*>', '', text)
    text = re.sub(r'</div>', '', text)
    # protect
    CPP_TEMPLATES = {}
    counter = [0]
    def replacer(m2):
        placeholder = f"___CPP_INCLUDE_{counter[0]}___"
        CPP_TEMPLATES[placeholder] = m2.group(0)
        counter[0] += 1
        return placeholder
    text = re.sub(r'#include\s*&lt;([a-zA-Z_][a-zA-Z0-9_.]*)&gt;', replacer, text)
    text = re.sub(r'<[^>]+>', '', text)
    for ph, orig in CPP_TEMPLATES.items():
        text = text.replace(ph, orig)
    text = html_mod.unescape(text)
    print(text[:200])
