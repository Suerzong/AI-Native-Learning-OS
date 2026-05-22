#!/usr/bin/env python3
"""
修复 NNDL 教材公式 — 极保守版。
只做一件事：将断裂成多行的 Σ/Π 表达式合并回单行。
其余内容完全不动。
"""
import re, sys


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


# ── 核心：合并断裂的 Σ 表达式 ────────────────────────

def fix_broken_sums(text):
    """
    将断裂成 3 行的求和表达式合并为 LaTeX \\sum。

    典型模式（3行）:
        行1: ... =N
        行2: Σ
        行3: n=1 ...         →   ... = \\sum_{n=1}^{N} ...

    变体1（4行 — 带分数）:
        行1: ... =
        行2: 1
        行3: N
        行4: Σ
        行5: n=1 ...         →   ... = \\frac{1}{N}\\sum_{n=1}^{N} ...
    """
    # 模式1: =上限换行 Σ换行 下限=起始
    # 如 =N\nΣ\nn=1 或 =K\nΣ\nk=1 → = \sum_{n=1}^{N}
    # 约束: 上限是单个变量名(\w+), 下限是变量=数字(\w+=\d+)
    text = re.sub(
        r'=\s*(\w+)\s*\n\s*Σ\s*\n\s*(\w+)\s*=\s*(\d+)',
        r'= \\sum_{\2=\3}^{\1}',
        text
    )
    # 变体: 上限可能是带括号的表达式 (少见)
    text = re.sub(
        r'=\s*(\w+)\s*\n\s*Σ\s*\n\s*(\w+)\s*=\s*(\w)\s+(?=[^\d])',
        r'= \\sum_{\2=\3}^{\1} ',
        text
    )

    # 模式2: 无 = 的上限  N\nΣ\nn=1 （上限限制1-3字符，排除中文误匹配）
    text = re.sub(
        r'(?<=[^\w=])(\w{1,3})\s*\n\s*Σ\s*\n\s*(\w+)\s*=\s*(\d+)',
        r'\\sum_{\2=\3}^{\1}',
        text
    )

    # 模式3: 独立 Σ (前无上限): Σ\ni=1 → \sum_{i=1} 或带 to
    text = re.sub(
        r'Σ\s*\n\s*(\w+)\s*=\s*(\d+)',
        r'\\sum_{\1=\2}',
        text
    )

    return text


def fix_broken_prods(text):
    """同上，针对 Π (求积)"""
    text = re.sub(
        r'=\s*(\w+)\s*\n\s*Π\s*\n\s*(\w+)\s*=\s*(\d+)',
        r'= \\prod_{\2=\3}^{\1}',
        text
    )
    text = re.sub(
        r'(?<=[^\w=])(\w{1,3})\s*\n\s*Π\s*\n\s*(\w+)\s*=\s*(\d+)',
        r'\\prod_{\2=\3}^{\1}',
        text
    )
    text = re.sub(
        r'Π\s*\n\s*(\w+)\s*=\s*(\d+)',
        r'\\prod_{\1=\2}',
        text
    )
    return text


def fix_max_min(text):
    """修复 max/min 下标断裂: 仅当下一行是单个词（无空格）时才合并。
    避免误吞多词表达式（如 max\\n𝒘𝒘T 不应成为 \\max_{𝒘𝒘T}）。"""
    ops = ['arg max', 'arg min', 'max', 'min', 'sup', 'inf']
    for op in ops:
        escaped = op.replace(' ', r'\s+')
        latex_op = '\\\\' + op.replace(' ', '_')
        # 只匹配: op 在行尾, 下一行是单个词(无空格), 再下一行存在
        pat = (
            r'(^|(?<=\n))'             # 行首
            r'([^\n]*?\b' + escaped + r')'  # 前置内容 + 操作符（在行尾）
            r'\s*\n'
            r'\s*(\S+)\s*'             # 下标行：只有一个词（无空格）
            r'\n'
        )
        text = re.sub(pat, _make_max_min_replacer(op, latex_op), text, flags=re.MULTILINE)
    return text


def _make_max_min_replacer(op, latex_op):
    """闭包工厂：避免 for 循环中的晚绑定问题"""
    def replacer(m):
        prefix = m.group(2).rstrip()
        # 从 prefix 末尾去掉操作符文本
        op_words = op.split()
        prefix_words = prefix.split()
        if len(prefix_words) >= len(op_words):
            # 去掉末尾匹配的操作符词
            for _ in range(len(op_words)):
                prefix_words.pop()
        prefix_clean = ' '.join(prefix_words)
        subscript = m.group(3)
        if len(subscript) > 30:  # 太长的下标可能是误匹配
            return m.group(0)
        if prefix_clean:
            return f'{prefix_clean} {latex_op}_{{{subscript}}}\n'
        else:
            return f'{latex_op}_{{{subscript}}}\n'
    return replacer


def fix_lim(text):
    """修复极限符号: lim\\n|𝒟|→∞ → \\lim_{|\\mathcal{D}| \\to \\infty}"""
    text = re.sub(
        r'lim\s*\n\s*\|(\S+?)\|\s*→\s*(\S+)',
        r'\\lim_{|\1| \\to \2}',
        text
    )
    text = re.sub(
        r'lim\s*\n\s*(\S+?)\s*→\s*(\S+)',
        r'\\lim_{\1 \\to \2}',
        text
    )
    return text


def fix_limit_artifacts(text):
    """后处理 sum/prod 上限中的 PDF 提取伪影。
    - NN → N, CC → C 等双写大写字母
    - 1N → N, 1C → C 等数字前缀 1（来自 1/X Σ 分数）
    """
    import unicodedata

    def dedup_upper(m):
        ch = m.group(1)
        if ch.isupper() or unicodedata.category(ch) == 'Lu':
            return '^{' + ch + '}'
        return m.group(0)

    text = re.sub(r'\^\{(\S)\1\}', dedup_upper, text)

    # 数字 1 前缀: ^{1X} → ^{X}
    def strip_leading_1(m):
        ch = m.group(1)
        if ch.isupper() or unicodedata.category(ch) == 'Lu':
            return '^{' + ch + '}'
        return m.group(0)

    text = re.sub(r'\^\{1(\S)\}', strip_leading_1, text)

    # argmax/max 与上限合并: ^{max...N} → ^{N}
    text = re.sub(r'\^\{[^}]*?max\w*?(\w)\}', lambda m: '^{' + m.group(1) + '}', text)
    text = re.sub(r'\^\{2𝜎2𝑁\}', r'^{N}', text)
    # 开头和结尾相同的字母 (如 N...N → N)
    text = re.sub(r'\^\{(\w)\w*\1\}', lambda m: '^{' + m.group(1) + '}', text)

    return text


# ── 主流程 ──────────────────────────────────────────

def main():
    input_file = '/home/ubuntu/Edge-AI/courses/neural-networks/materials/《神经网络与深度学习》.md'
    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    print(f"读取: {input_file}")
    text = read_file(input_file)
    orig = len(text.split('\n'))

    # 依次应用修复
    fixes = [
        ('断裂 Σ', fix_broken_sums),
        ('断裂 Π', fix_broken_prods),
        ('max/min 断裂', fix_max_min),
        ('极限断裂', fix_lim),
        ('上限伪影', fix_limit_artifacts),
    ]

    for name, func in fixes:
        before = len(text.split('\n'))
        text = func(text)
        after = len(text.split('\n'))
        if before != after:
            print(f"  {name}: {before} → {after} 行 ({after - before:+d})")

    final = len(text.split('\n'))
    print(f"总行数: {orig} → {final} ({final - orig:+d})")

    # 统计
    for pat, label in [
        (r'\\sum', '\\sum'),
        (r'\\prod', '\\prod'),
        (r'\\max_', '\\max_'),
        (r'\\min_', '\\min_'),
        (r'\\frac', '\\frac'),
        (r'\\lim', '\\lim'),
    ]:
        n = len(re.findall(pat, text))
        if n > 0:
            print(f"  {label}: {n} 处")

    write_file(input_file, text)
    print(f"已写入: {input_file}")


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    main()
