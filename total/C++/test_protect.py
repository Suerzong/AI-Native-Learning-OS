import re

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
    return s

def restore(s):
    for placeholder, original in CPP_TEMPLATES.items():
        s = s.replace(placeholder, original)
    return s

# Simulate what clean_code does
code = '#include <iostream>\nusing namespace std;\nint main()\n{\n    cout << "Hello, world!" << endl;\n    return 0;\n}'
print("Original:")
print(repr(code[:80]))

protected = protect(code)
print("\nProtected:")
print(repr(protected[:80]))

# Simulate removing HTML tags
cleaned = re.sub(r'<[^>]+>', '', protected)
print("\nAfter HTML strip:")
print(repr(cleaned[:80]))

restored = restore(cleaned)
print("\nRestored:")
print(restored[:200])
