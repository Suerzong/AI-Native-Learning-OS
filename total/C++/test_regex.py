import re

test = '<div class="example"><h2 class="example">test</h2> <div class="example_code">\ncode line 1\ncode line 2\n</div></div>'
m = re.search(r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>\s*(?:</div>)?', test, re.DOTALL)
if m:
    print('Match found, length:', len(m.group(1)))
    print(repr(m.group(1)[:200]))
else:
    print('No match')
