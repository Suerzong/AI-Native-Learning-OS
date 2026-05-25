#!/usr/bin/env python3
"""
插入知识点标注到教材 markdown 文件中。

用法:
  python3 annotate_textbook.py <教材.md> <知识点.json> [输出.md]

知识点 JSON 格式:
{
  "sections": {
    "0.1": {
      "core": ["核心知识点1", "核心知识点2", ...],
      "background": ["重要背景1", ...],
      "understand": ["了解项1", ...]
    },
    ...
  }
}

标注格式 (与 NNDL 教材一致):
> **核心知识点：** 知识点1、知识点2、...
> **重要背景：** 背景1、背景2、...
> **了解：** 项1、项2、...
"""

import re
import json
import sys
import os


def load_knowledge_points(json_path):
    """加载知识点JSON文件"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('sections', {})


def format_annotation(kp_data):
    """将知识点数据格式化为标注文本"""
    lines = []

    core = kp_data.get('core', [])
    if core:
        lines.append(f"> **核心知识点：** {'、'.join(core)}")

    background = kp_data.get('background', [])
    if background:
        lines.append(f"> **重要背景：** {'、'.join(background)}")

    understand = kp_data.get('understand', [])
    if understand:
        lines.append(f"> **了解：** {'、'.join(understand)}")

    return '\n'.join(lines) + '\n'


def find_section_boundaries(content, pattern_config):
    """
    找到所有 section 边界。
    返回 [(section_id, start_line, next_section_start_line), ...]

    pattern_config 包含:
    - heading_pattern: 匹配 section 标题的正则
    - section_id_group: 正则中 section_id 在第几组
    - include_subsections: 是否也匹配子节
    """
    heading_pattern = pattern_config['heading_pattern']
    section_id_group = pattern_config.get('section_id_group', 1)

    boundaries = []
    matches = list(re.finditer(heading_pattern, content, re.MULTILINE))

    for i, m in enumerate(matches):
        section_id = m.group(section_id_group).strip()
        start_pos = m.start()
        # Next boundary is either next match or end of file
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)

        boundaries.append({
            'section_id': section_id,
            'start_pos': start_pos,
            'end_pos': end_pos,
            'match_text': m.group(0),
            'match_start': m.start(),
            'match_end': m.end()
        })

    return boundaries


def insert_annotations(content, boundaries, kp_data, skip_existing=True):
    """
    在 section 边界前插入标注。
    从后往前插入，避免位置偏移。
    """
    # Sort boundaries by position descending so insertions don't shift positions
    boundaries_sorted = sorted(boundaries, key=lambda b: b['match_start'], reverse=True)

    for b in boundaries_sorted:
        section_id = b['section_id']

        # Check if annotation already exists just before this section
        if skip_existing:
            # Look back ~200 chars before the section heading
            pre_text = content[max(0, b['match_start'] - 300):b['match_start']]
            if '核心知识点' in pre_text or '**核心知识点：**' in pre_text:
                continue

        if section_id not in kp_data:
            continue

        annotation = format_annotation(kp_data[section_id])
        if not annotation.strip():
            continue

        # Insert annotation before the section heading
        # Add a blank line before annotation for readability
        insert_pos = b['match_start']
        content = content[:insert_pos] + '\n' + annotation + '\n' + content[insert_pos:]

    return content


def process_linux_textbook(content, kp_data):
    """
    处理 Linux 教材 (鸟哥的书)。
    匹配 ## 0.1, ### 0.1.1 格式的标题。
    """
    # Match: ## 0.1 电脑：辅助人脑的好工具
    # Match: ### 0.1.1 计算机硬件的五大单元
    heading_pattern = r'^(#{2,3})\s+(\d+\.\d+(?:\.\d+)?)\s+(.+)$'

    boundaries = find_section_boundaries(content, {
        'heading_pattern': heading_pattern,
        'section_id_group': 2
    })

    print(f"  找到 {len(boundaries)} 个章节边界")

    # Show what was found
    for b in boundaries[:10]:
        print(f"    [{b['section_id']}] {b['match_text'][:80]}")
    if len(boundaries) > 10:
        print(f"    ... 还有 {len(boundaries) - 10} 个")

    return insert_annotations(content, boundaries, kp_data)


def process_rtos_textbook(content, kp_data):
    """
    处理 RTOS 教材 (Mastering FreeRTOS)。
    匹配 ## 1.1, ### 1.1.1 格式的标题。
    """
    # Match markdown headings with section numbers
    heading_pattern = r'^(#{2,4})\s+(\d+\.\d+(?:\.\d+)?)\s+(.+)$'

    boundaries = find_section_boundaries(content, {
        'heading_pattern': heading_pattern,
        'section_id_group': 2
    })

    print(f"  找到 {len(boundaries)} 个章节边界")

    for b in boundaries[:10]:
        print(f"    [{b['section_id']}] {b['match_text'][:80]}")
    if len(boundaries) > 10:
        print(f"    ... 还有 {len(boundaries) - 10} 个")

    return insert_annotations(content, boundaries, kp_data)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    textbook_path = sys.argv[1]
    kp_json_path = sys.argv[2]

    if len(sys.argv) >= 4:
        output_path = sys.argv[3]
    else:
        base, ext = os.path.splitext(textbook_path)
        output_path = f"{base}-annotated{ext}"

    print(f"教材文件: {textbook_path}")
    print(f"知识点文件: {kp_json_path}")
    print(f"输出文件: {output_path}")

    # Load
    with open(textbook_path, 'r', encoding='utf-8') as f:
        content = f.read()

    kp_data = load_knowledge_points(kp_json_path)
    print(f"加载 {len(kp_data)} 个章节的知识点标注")

    # Detect textbook type
    filename = os.path.basename(textbook_path)
    if 'linux' in filename.lower() or '鸟哥' in filename:
        print("检测到 Linux 教材格式")
        content = process_linux_textbook(content, kp_data)
    elif 'free' in filename.lower() or 'rtos' in filename.lower():
        print("检测到 RTOS 教材格式")
        content = process_rtos_textbook(content, kp_data)
    else:
        # Generic: try both patterns
        print("未识别教材类型，尝试通用匹配...")
        content = process_linux_textbook(content, kp_data)

    # Save
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"完成！标注后的文件已保存到: {output_path}")


if __name__ == '__main__':
    main()
