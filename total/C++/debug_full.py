import urllib.request
import re
import html as html_mod

BASE = "https://www.runoob.com/cplusplus/"

def decode(s):
    return html_mod.unescape(s)

CPP_TEMPLATES = {}

def protect_cpp_templates(s):
    global CPP_TEMPLATES
    CPP_TEMPLATES = {}
    counter = [0]
    def replacer(m):
        placeholder = f"___CPP_INCLUDE_{counter[0]}___"
        CPP_TEMPLATES[placeholder] = m.group(0)
        counter[0] += 1
        return placeholder
    s = re.sub(r'#include\s*<([a-zA-Z_][a-zA-Z0-9_.]*)>', replacer, s)
    s = re.sub(r'#include\s*&lt;([a-zA-Z_][a-zA-Z0-9_.]*)&gt;', replacer, s)
    return s

def restore_cpp_templates(s):
    for placeholder, original in CPP_TEMPLATES.items():
        s = s.replace(placeholder, original)
    return s

def clean_code(text):
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'</?span[^>]*>', '', text)
    text = re.sub(r'<div[^>]*>', '', text)
    text = re.sub(r'</div>', '', text)
    global CPP_TEMPLATES
    counter = [len(CPP_TEMPLATES)]
    def replacer(m):
        placeholder = f"___CPP_INCLUDE_{counter[0]}___"
        CPP_TEMPLATES[placeholder] = m.group(0)
        counter[0] += 1
        return placeholder
    text = re.sub(r'#include\s*&lt;([a-zA-Z_][a-zA-Z0-9_.]*)&gt;', replacer, text)
    text = re.sub(r'<[^>]+>', '', text)
    for placeholder, original in CPP_TEMPLATES.items():
        text = text.replace(placeholder, original)
    text = decode(text)
    text = text.replace('\xa0', ' ')
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# Fetch page
url = BASE + "cpp-tutorial.html"
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

# Simulate html_to_md step by step
s = article

# Remove ads/scripts
s = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.DOTALL)
s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)
s = re.sub(r'<!--.*?-->', '', s, flags=re.DOTALL)

# Protect C++ templates
s = protect_cpp_templates(s)
print(f"After protect: {len(CPP_TEMPLATES)} templates protected")
for k, v in CPP_TEMPLATES.items():
    print(f"  {k} -> {v}")

# Process example_code blocks
def handle_example_code(m):
    code_html = m.group(1)
    print(f"\n=== Processing example_code block ===")
    print(f"Raw HTML (first 200): {repr(code_html[:200])}")
    code = clean_code(code_html)
    print(f"Cleaned code:\n{code}")
    return f'\n\n```cpp\n{code}\n```\n\n'

result = re.sub(
    r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>\s*</div>\s*(?:</div>)?',
    handle_example_code, s, flags=re.DOTALL
)

# Restore templates
result = restore_cpp_templates(result)

# Find the first code block in result
idx = result.find('```cpp')
if idx >= 0:
    print(f"\n=== First code block in final output ===")
    print(result[idx:idx+200])
