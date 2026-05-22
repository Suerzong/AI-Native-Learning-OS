#!/usr/bin/env python3
"""Merge all chapter KP files and apply to textbook."""
import json, glob, sys

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Merge all KP files
all_sections = []
files = sorted(glob.glob('tools/kp_ch*.json')) + ['tools/kp_appendix.json']
total_core = total_bg = total_und = 0
for fname in files:
    data = json.loads(read_file(fname))
    all_sections.extend(data['sections'])
    c = sum(len(s.get('core',[])) for s in data['sections'])
    b = sum(len(s.get('background',[])) for s in data['sections'])
    u = sum(len(s.get('understand',[])) for s in data['sections'])
    total_core += c; total_bg += b; total_und += u
    print(f"  + {fname}: {len(data['sections'])} sections, core={c} bg={b} und={u}")

merged = {"sections": all_sections}
write_file('tools/kp_merged.json', json.dumps(merged, ensure_ascii=False, indent=2))
print(f"Merged {len(all_sections)} sections total (core={total_core} bg={total_bg} und={total_und})")

# Apply to textbook
from insert_knowledge_points import insert_kps

textbook = 'courses/neural-networks/materials/《神经网络与深度学习》.md'
text = read_file(textbook)
text = insert_kps(text, merged)
write_file(textbook, text)
print(f"Applied to: {textbook}")
