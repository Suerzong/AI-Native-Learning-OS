#!/usr/bin/env python3
"""
知识点插入工具。读取教材文件，在每个小节标题前插入三层知识点标注。
知识点 JSON 格式：
{
  "chapter": "第1章 绪论",
  "sections": [
    {
      "heading": "### 1.1 人工智能",
      "core": ["核心概念1", "核心概念2"],
      "background": ["背景说明1"],
      "understand": ["了解信息1", "了解信息2"]
    }
  ]
}
至少需要一个非空列表（core / background / understand），否则跳过该节。
"""
import json, re, sys


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def escape_kp(kp_text):
    """确保知识点文本中不包含破坏 markdown 的字符"""
    return kp_text.replace('\n', ' ').strip()


def build_annotation(sec):
    """构建三层知识点标注。至少有一层非空才返回，否则返回 None。"""
    parts = []
    if core := sec.get('core', []):
        parts.append('> **核心知识点：** ' + '、'.join(escape_kp(k) for k in core))
    if bg := sec.get('background', []):
        parts.append('> **重要背景：** ' + '、'.join(escape_kp(b) for b in bg))
    if und := sec.get('understand', []):
        parts.append('> **了解：** ' + '、'.join(escape_kp(u) for u in und))
    return '\n'.join(parts) + '\n\n' if parts else None


def insert_kps(text, kp_data):
    """在每小节标题前插入三层知识点标注"""
    sections = kp_data.get('sections', [])
    if not sections:
        print("  警告: 知识点数据为空")
        return text

    inserted = 0
    for sec in sections:
        heading = sec.get('heading', '')
        annotation = build_annotation(sec)
        if not heading or not annotation:
            continue

        # 匹配标题行（支持有无 markdown 前缀和空格差异）
        base = heading.strip()
        base_no_prefix = re.sub(r'^#{2,4}\s+', '', base)
        matched = False

        # Pattern 1: exact heading (with optional markdown prefix)
        pat = r'^(#{2,4}\s+)?' + re.escape(base) + r'[^\n]*\n'
        new_text = re.sub(pat, annotation + r'\g<0>', text, count=1, flags=re.MULTILINE)
        if new_text != text:
            inserted += 1
            text = new_text
            matched = True

        if not matched:
            # Pattern 2: heading text without markdown prefix
            pat = r'^(#{2,4}\s+)?' + re.escape(base_no_prefix) + r'[^\n]*\n'
            new_text = re.sub(pat, annotation + r'\g<0>', text, count=1, flags=re.MULTILINE)
            if new_text != text:
                inserted += 1
                text = new_text
                matched = True

        if not matched:
            # Pattern 3: space-insensitive match
            base_stripped = re.sub(r'\s+', '', base_no_prefix)
            if base_stripped:
                flexible = r'(#{2,4}\s+)?' + r'\s*'.join(re.escape(c) for c in base_stripped)
                pat = r'^' + flexible + r'[^\n]*\n'
                new_text = re.sub(pat, annotation + r'\g<0>', text, count=1, flags=re.MULTILINE)
                if new_text != text:
                    inserted += 1
                    text = new_text
                    matched = True
        if not matched:
            # Fallback 1: inline text
            inline_pat = re.escape(base_no_prefix)
            m = re.search(inline_pat, text)
            if m:
                pos = m.start()
                before = text[max(0,pos-80):pos]
                if '> **核心' not in before and '> **重要' not in before \
                   and '> **了解' not in before and '> **知识点' not in before:
                    text = text[:pos] + '\n\n' + annotation + text[pos:]
                    inserted += 1
                    matched = True
        if not matched:
            # Fallback 2: space-insensitive inline
            base_stripped = re.sub(r'\s+', '', base_no_prefix)
            if base_stripped:
                flexible_pat = r'\s*'.join(re.escape(c) for c in base_stripped)
                m = re.search(flexible_pat, text)
                if m:
                    pos = m.start()
                    before = text[max(0,pos-80):pos]
                    if '> **核心' not in before and '> **重要' not in before \
                       and '> **了解' not in before and '> **知识点' not in before:
                        text = text[:pos] + '\n\n' + annotation + text[pos:]
                        inserted += 1
                        matched = True
        if not matched:
            print(f"  未找到标题: {heading[:60]}")

    print(f"  已插入 {inserted}/{len(sections)} 个小节的知识点")
    return text


def list_sections(text):
    """列出文件中所有小节标题，用于生成知识点 JSON 模板"""
    headings = []
    for m in re.finditer(r'^(#{2,4}\s+.+)$', text, flags=re.MULTILINE):
        line = m.group(1).strip()
        level = len(re.match(r'^#+', line).group())
        headings.append({
            'line': m.start(),
            'level': level,
            'heading': line,
        })

    chapters = []
    current_chapter = None
    current_sections = []

    for h in headings:
        if h['level'] == 2:
            if current_chapter:
                chapters.append({
                    'chapter': current_chapter,
                    'sections': current_sections,
                })
            current_chapter = h['heading']
            current_sections = []
        elif h['level'] in (3, 4):
            current_sections.append({
                'heading': h['heading'],
                'core': [],
                'background': [],
                'understand': [],
            })

    if current_chapter:
        chapters.append({
            'chapter': current_chapter,
            'sections': current_sections,
        })

    return chapters


# ── 主流程 ──────────────────────────────────────────

def main():
    textbook = '/home/ubuntu/Edge-AI/courses/neural-networks/materials/《神经网络与深度学习》.md'

    if len(sys.argv) < 2:
        print("用法:")
        print("  python3 insert_knowledge_points.py list       # 列出所有小节，生成模板")
        print("  python3 insert_knowledge_points.py apply <kp.json>  # 应用知识点 JSON")
        return

    cmd = sys.argv[1]

    if cmd == 'list':
        text = read_file(textbook)
        chapters = list_sections(text)
        output = 'tools/nndl_sections_template.json'
        write_file(output, json.dumps(chapters, ensure_ascii=False, indent=2))
        total = sum(len(ch['sections']) for ch in chapters)
        print(f"共 {len(chapters)} 章, {total} 个小节")
        print(f"模板已写入: {output}")

    elif cmd == 'apply':
        if len(sys.argv) < 3:
            print("请指定知识点 JSON 文件")
            return
        kp_file = sys.argv[2]
        text = read_file(textbook)
        kp_data = json.loads(read_file(kp_file))
        text = insert_kps(text, kp_data)
        write_file(textbook, text)
        print(f"已写回: {textbook}")

    else:
        print(f"未知命令: {cmd}")


if __name__ == '__main__':
    main()
