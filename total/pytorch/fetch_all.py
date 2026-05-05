#!/usr/bin/env python3
"""抓取菜鸟教程 PyTorch 所有子页面，整理成 md 文件"""
import re, os, urllib.request, html as htmllib

BASE = "https://www.runoob.com/pytorch"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
OUT_DIR = r"c:\Users\sez18\Desktop\pytorch\pytorch-pages"
os.makedirs(OUT_DIR, exist_ok=True)

PAGES = [
    ("pytorch-tutorial", "PyTorch 教程"),
    ("pytorch-intro", "PyTorch 简介"),
    ("pytorch-install", "PyTorch 安装"),
    ("pytorch-basic", "PyTorch 基础"),
    ("pytorch-tensor", "PyTorch 张量"),
    ("pytorch-neural-network", "PyTorch 神经网络基础"),
    ("pytorch-first-neural-network", "PyTorch 第一个神经网络"),
    ("pytorch-dataset-dataloader", "PyTorch 数据处理与加载"),
    ("pytorch-linear-regression", "PyTorch 线性回归"),
    ("pytorch-cnn", "PyTorch 卷积神经网络"),
    ("pytorch-recurrent-neural-network", "PyTorch 循环神经网络"),
    ("pytorch-datasets", "PyTorch 数据集"),
    ("pytorch-transforms", "PyTorch 数据转换"),
    ("pytorch-torch-ref", "PyTorch torch 参考手册"),
    ("pytorch-torch-nn-ref", "PyTorch torch.nn 参考手册"),
    ("transformer-model", "Transformer 模型"),
    ("pytorch-transformer-model", "PyTorch 构建 Transformer 模型"),
    ("pytorch-torch-optim", "PyTorch torch.optim 优化器"),
    ("pytorch-torchvision", "PyTorch torchvision"),
    ("pytorch-model-deployment", "PyTorch 模型部署"),
    ("pytorch-model-save", "PyTorch 模型保存和加载"),
    ("pytorch-image-classification", "PyTorch 图像分类实例"),
    ("pytorch-text-classification", "PyTorch 文本情感分析实例"),
    ("pytorch-autograd", "PyTorch Autograd 自动微分"),
    ("pytorch-gpu-cuda", "PyTorch GPU / CUDA 加速"),
    ("pytorch-loss-function", "PyTorch 损失函数"),
    ("pytorch-lr-scheduler", "PyTorch 学习率调度器"),
    ("pytorch-transfer-learning", "PyTorch 迁移学习"),
    ("pytorch-batchnorm-dropout", "PyTorch 批归一化与 Dropout"),
    ("pytorch-lstm-gru", "PyTorch LSTM / GRU"),
    ("pytorch-embedding", "PyTorch 词嵌入"),
    ("pytorch-gan", "PyTorch 生成对抗网络"),
    ("pytorch-autoencoder", "PyTorch 自编码器"),
    ("pytorch-evaluation-debugging", "PyTorch 模型评估与调试"),
    ("pytorch-torchtext", "PyTorch torchtext"),
    ("pytorch-amp", "PyTorch 混合精度训练"),
    ("pytorch-torchscript-onnx-export", "PyTorch TorchScript/ONNX 导出"),
    ("pytorch-distributed", "PyTorch 分布式训练"),
    ("pytorch-attention", "PyTorch 注意力机制"),
]

def fetch(slug):
    url = f"{BASE}/{slug}.html"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [ERROR] {e}")
        return ""

def html2md(html_str):
    """正则提取 article-body 内容并转 markdown"""
    # 提取 article-body 到 archive-list 之间的内容
    m = re.search(
        r'<div[^>]*class="[^"]*article-body[^"]*"[^>]*>(.*?)'
        r'(?=<div[^>]*class="[^"]*(?:archive-list|previous-next-links))',
        html_str, re.DOTALL
    )
    if not m:
        return ""
    body = m.group(1)

    # 1) 先把代码块提取出来，避免后续处理破坏代码
    codes = []
    def pull_code(mm):
        raw = mm.group(1)
        raw = re.sub(r'<br\s*/?>', '\n', raw)
        raw = re.sub(r'<[^>]+>', '', raw)
        raw = htmllib.unescape(raw).strip()
        # 去掉每行开头的 &nbsp; 序列
        lines = [re.sub(r'^(\xc2\xa0| )+', '', l) for l in raw.split('\n')]
        raw = '\n'.join(lines).strip()
        codes.append(raw)
        return f'\n\n§CODE{len(codes)-1}§\n\n'
    body = re.sub(r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>', pull_code, body, flags=re.DOTALL)
    body = re.sub(r'<pre[^>]*>(.*?)</pre>', pull_code, body, flags=re.DOTALL)

    # 2) 标题
    for lv in range(1, 5):
        body = re.sub(
            rf'<h{lv}[^>]*>(.*?)</h{lv}>',
            lambda m, n=lv: f'\n\n{"#"*n} {htmllib.unescape(re.sub("<[^>]*>","",m.group(1))).strip()}\n\n',
            body, flags=re.DOTALL
        )

    # 3) 表格 — 简化为 | 分隔
    def fix_table(m):
        tbl = m.group(1)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', tbl, re.DOTALL)
        lines = []
        for ri, row in enumerate(rows):
            cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.DOTALL)
            cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
            cells = [c for c in cells if c]  # 去掉空单元格
            if cells:
                lines.append('| ' + ' | '.join(cells) + ' |')
            if ri == 0 and cells:
                lines.append('|' + '|'.join([' --- '] * len(cells)) + '|')
        return '\n\n' + '\n'.join(lines) + '\n\n'
    body = re.sub(r'<table[^>]*>(.*?)</table>', fix_table, body, flags=re.DOTALL)

    # 4) 列表
    body = re.sub(r'<li[^>]*>', '\n- ', body)

    # 5) 内联格式
    body = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', body, flags=re.DOTALL)
    body = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', body, flags=re.DOTALL)
    body = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', body, flags=re.DOTALL)
    body = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', body, flags=re.DOTALL)
    body = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', body, flags=re.DOTALL)

    # 6) 换行相关
    body = re.sub(r'<br\s*/?>', '\n', body)
    body = re.sub(r'</?p[^>]*>', '\n', body)
    body = re.sub(r'</?(?:div|ul|ol|dl|blockquote|section)[^>]*>', '\n', body)

    # 7) 去掉广告/脚本等无用块
    body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<ins[^>]*>.*?</ins>', '', body, flags=re.DOTALL)
    body = re.sub(r'<iframe[^>]*>.*?</iframe>', '', body, flags=re.DOTALL)

    # 8) 去掉剩余 HTML 标签
    body = re.sub(r'<[^>]+>', '', body)

    # 9) 解码 HTML 实体，清理空格
    body = htmllib.unescape(body)
    body = body.replace('\xa0', ' ')

    # 10) 恢复代码块
    for i, code in enumerate(codes):
        body = body.replace(f'§CODE{i}§', f'\n```python\n{code}\n```\n')

    # 11) 清理连续空行（最多保留2个）
    body = re.sub(r'\n{3,}', '\n\n', body)
    body = body.strip()

    return body


def clean(md):
    """最终清理"""
    lines = md.split('\n')
    out = []
    in_code = False
    prev_empty = False
    for line in lines:
        if line.startswith('```'):
            in_code = not in_code
            out.append(line)
            prev_empty = False
            continue
        if not in_code:
            line = line.rstrip()
            is_empty = (line.strip() == '')
            if is_empty and prev_empty:
                continue  # 跳过连续空行
            prev_empty = is_empty
        out.append(line)
    return '\n'.join(out).strip('\n')


def main():
    print(f"共 {len(PAGES)} 个页面\n")
    all_contents = []

    for i, (slug, title) in enumerate(PAGES, 1):
        print(f"[{i:02d}/{len(PAGES)}] {slug} ... ", end="", flush=True)
        raw = fetch(slug)
        if not raw:
            print("跳过")
            continue
        md = html2md(raw)
        md = clean(md)
        if not md or len(md) < 30:
            print(f"内容过少({len(md)}字)")
            continue
        # 单页文件
        fname = os.path.join(OUT_DIR, f"{i:02d}-{slug}.md")
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n{md}\n")
        all_contents.append((title, md))
        print(f"OK ({len(md)}字)")

    # 合并大文件
    print(f"\n合并 {len(all_contents)} 章...")
    parts = ["# PyTorch 完整教程\n\n"]
    parts.append("> 来源：[菜鸟教程 PyTorch](https://www.runoob.com/pytorch/pytorch-tutorial.html)\n\n")
    parts.append("## 目录\n\n")
    for i, (t, _) in enumerate(all_contents, 1):
        parts.append(f"{i}. {t}\n")
    parts.append("\n---\n")
    for title, content in all_contents:
        parts.append(f"\n\n---\n\n{content}\n")
    big = clean(''.join(parts))

    big_path = os.path.join(OUT_DIR, "PyTorch完整教程.md")
    with open(big_path, 'w', encoding='utf-8') as f:
        f.write(big + '\n')

    print(f"\n完成！")
    print(f"  单页: {OUT_DIR}/")
    print(f"  合并: {big_path}")
    print(f"  总字数: {len(big)}")


if __name__ == "__main__":
    main()
