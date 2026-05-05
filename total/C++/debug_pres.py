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

# Find <pre> blocks
pres = re.findall(r'<pre[^>]*>(.*?)</pre>', article, re.DOTALL)
print(f"Found {len(pres)} <pre> blocks")
for i, p in enumerate(pres):
    print(f"\n--- <pre> {i+1} ---")
    print(repr(p[:200]))

# Also check if there are any <pre> BEFORE the first example_code
idx = article.find('example_code')
before = article[:idx]
pres_before = re.findall(r'<pre[^>]*>(.*?)</pre>', before, re.DOTALL)
print(f"\n\nFound {len(pres_before)} <pre> blocks before first example_code")

# Check the exact text around line 98 area
# Let's simulate what the html_to_md does for the ENTIRE article
# (not just code blocks)
print("\n\n=== Checking what html_to_md produces ===")

import html as html_mod

def decode(s):
    return html_mod.unescape(s)

s = article
# Remove ads
s = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.DOTALL)
s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)
s = re.sub(r'<!--.*?-->', '', s, flags=re.DOTALL)

# Remove example_code blocks first
def handle_example_code(m):
    code_html = m.group(1)
    code = re.sub(r'<br\s*/?>', '\n', code_html)
    code = re.sub(r'</?span[^>]*>', '', code)
    code = re.sub(r'<div[^>]*>', '', code)
    code = re.sub(r'</div>', '', code)
    import html as _html
    CPP = {}
    ctr = [0]
    def rep(m2):
        ph = f"___CPP_INC_{ctr[0]}___"
        CPP[ph] = m2.group(0)
        ctr[0] += 1
        return ph
    code = re.sub(r'#include\s*&lt;([a-zA-Z_][a-zA-Z0-9_.]*)&gt;', rep, code)
    code = re.sub(r'<[^>]+>', '', code)
    for ph, orig in CPP.items():
        code = code.replace(ph, orig)
    code = _html.unescape(code)
    code = code.strip()
    return f'\n\n```cpp\n{code}\n```\n\n'

s = re.sub(
    r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>\s*</div>\s*(?:</div>)?',
    handle_example_code, s, flags=re.DOTALL
)

# Handle <pre> blocks
def handle_pre(m):
    code = m.group(1)
    code = re.sub(r'<br\s*/?>', '\n', code)
    import html as _html
    CPP = {}
    ctr = [0]
    def rep(m2):
        ph = f"___CPP_INC_{ctr[0]}___"
        CPP[ph] = m2.group(0)
        ctr[0] += 1
        return ph
    code = re.sub(r'#include\s*&lt;([a-zA-Z_][a-zA-Z0-9_.]*)&gt;', rep, code)
    code = re.sub(r'<[^>]+>', '', code)
    for ph, orig in CPP.items():
        code = code.replace(ph, orig)
    code = _html.unescape(code)
    code = code.strip()
    return f'\n\n```cpp\n{code}\n```\n\n'

s = re.sub(r'<pre[^>]*>(.*?)</pre>', handle_pre, s, flags=re.DOTALL)

# Find first ```cpp
idx = s.find('```cpp')
if idx >= 0:
    print(f"First code block:")
    print(s[idx:idx+300])
