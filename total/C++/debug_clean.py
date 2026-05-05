import re
import html as html_mod

CPP_TEMPLATES = {}

def protect(s):
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

def restore(s):
    for placeholder, original in CPP_TEMPLATES.items():
        s = s.replace(placeholder, original)
    return s

def clean_code(text):
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'</?span[^>]*>', '', text)
    text = re.sub(r'<div[^>]*>', '', text)
    text = re.sub(r'</div>', '', text)
    # protect BEFORE removing remaining tags
    global CPP_TEMPLATES
    counter = [len(CPP_TEMPLATES)]
    def replacer(m):
        placeholder = f"___CPP_INCLUDE_{counter[0]}___"
        CPP_TEMPLATES[placeholder] = m.group(0)
        counter[0] += 1
        return placeholder
    # Match encoded form: #include &lt;xxx&gt;
    text = re.sub(r'#include\s*&lt;([a-zA-Z_][a-zA-Z0-9_.]*)&gt;', replacer, text)
    text = re.sub(r'<[^>]+>', '', text)
    for placeholder, original in CPP_TEMPLATES.items():
        text = text.replace(placeholder, original)
    # Decode AFTER removing tags
    text = html_mod.unescape(text)
    text = text.replace('\xa0', ' ')
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# Simulate the raw content
raw = '\r\n<div class="hl-main"><span class="hl-prepro">#include</span><span class="hl-prepro"> </span><span class="hl-quotes">&lt;</span><span class="hl-string">iostream</span><span class="hl-quotes">&gt;</span><span class="hl-prepro"></span><span class="hl-code">\n</span><span class="hl-reserved">using</span><span class="hl-code"> </span><span class="hl-types">namespace</span><span class="hl-code"> </span><span class="hl-identifier">std</span><span class="hl-code">;\n</span><span class="hl-types">int</span><span class="hl-code"> </span><span class="hl-identifier">main</span><span class="hl-brackets">()</span><span class="hl-code">\n</span><span class="hl-brackets">{</span><span class="hl-code">\n    </span><span class="hl-identifier">cout</span><span class="hl-code"> &lt;&lt; </span><span class="hl-quotes">&quot;</span><span class="hl-string">Hello, world!</span><span class="hl-quotes">&quot;</span><span class="hl-code"> &lt;&lt; </span><span class="hl-identifier">endl</span><span class="hl-code">;\n    </span><span class="hl-reserved">return</span><span class="hl-code"> </span><span class="hl-number">0</span><span class="hl-code">;\n</span><span class="hl-brackets">}</span></div>\r\n'

result = clean_code(raw)
print("Result:")
print(result)
