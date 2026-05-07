#!/usr/bin/env python3
"""Batch translate Markdown files from English to Chinese."""

import os
import re
import time
from deep_translator import GoogleTranslator

BASE = r"C:\Users\sez18\Desktop\Workspace\Edge-AI\Document\L5-项目实战-部署-MLOps-边缘AI"

ALL_FILES = []

def add_files(directory, pairs):
    for src, dst in pairs:
        ALL_FILES.append((directory, src, dst))

add_files("fast-ai", [
    ("03-lesson3.md", "cn-03-lesson3.md"),
    ("04-lesson4.md", "cn-04-lesson4.md"),
    ("05-lesson5.md", "cn-05-lesson5.md"),
    ("06-lesson6.md", "cn-06-lesson6.md"),
    ("07-lesson7.md", "cn-07-lesson7.md"),
    ("08-lesson8.md", "cn-08-lesson8.md"),
    ("09-lesson9.md", "cn-09-lesson9.md"),
    ("10-lesson10.md", "cn-10-lesson10.md"),
    ("11-lesson11.md", "cn-11-lesson11.md"),
    ("12-lesson12.md", "cn-12-lesson12.md"),
    ("13-lesson13.md", "cn-13-lesson13.md"),
    ("14-lesson14.md", "cn-14-lesson14.md"),
    ("15-lesson15.md", "cn-15-lesson15.md"),
    ("16-lesson16.md", "cn-16-lesson16.md"),
    ("17-lesson17.md", "cn-17-lesson17.md"),
    ("18-lesson18.md", "cn-18-lesson18.md"),
    ("19-lesson19.md", "cn-19-lesson19.md"),
    ("20-lesson20.md", "cn-20-lesson20.md"),
    ("21-lesson21.md", "cn-21-lesson21.md"),
    ("22-lesson22.md", "cn-22-lesson22.md"),
    ("23-lesson23.md", "cn-23-lesson23.md"),
    ("24-lesson24.md", "cn-24-lesson24.md"),
    ("25-lesson25.md", "cn-25-lesson25.md"),
    ("26-fastai-docs.md", "cn-26-fastai-docs.md"),
])

add_files("MLflow", [
    ("00-mlflow-index.md", "cn-00-mlflow-index.md"),
    ("01-getting-started.md", "cn-01-getting-started.md"),
    ("02-tracking.md", "cn-02-tracking.md"),
    ("03-model-registry.md", "cn-03-model-registry.md"),
    ("04-models.md", "cn-04-models.md"),
    ("05-deployment.md", "cn-05-deployment.md"),
    ("06-genai.md", "cn-06-genai.md"),
    ("07-genai-eval-monitor.md", "cn-07-genai-eval-monitor.md"),
])

add_files("LiteRT-TensorFlow-Lite", [
    ("00-litert-home.md", "cn-00-litert-home.md"),
    ("01-models.md", "cn-01-models.md"),
    ("02-inference.md", "cn-02-inference.md"),
    ("03-performance.md", "cn-03-performance.md"),
    ("04-android.md", "cn-04-android.md"),
    ("05-ios.md", "cn-05-ios.md"),
    ("06-microcontrollers.md", "cn-06-microcontrollers.md"),
    ("07-model-convert.md", "cn-07-model-convert.md"),
    ("08-model-optimize.md", "cn-08-model-optimize.md"),
])

add_files("ONNX-ONNX-Runtime", [
    ("00-onnx-home.md", "cn-00-onnx-home.md"),
    ("01-onnxruntime-docs.md", "cn-01-onnxruntime-docs.md"),
    ("02-get-started.md", "cn-02-get-started.md"),
    ("03-tutorials-index.md", "cn-03-tutorials-index.md"),
    ("04-api-basics.md", "cn-04-api-basics.md"),
    ("05-accelerate-pytorch.md", "cn-05-accelerate-pytorch.md"),
    ("06-mobile.md", "cn-06-mobile.md"),
    ("07-web.md", "cn-07-web.md"),
    ("08-iot-edge.md", "cn-08-iot-edge.md"),
    ("09-performance.md", "cn-09-performance.md"),
    ("10-model-optimizations.md", "cn-10-model-optimizations.md"),
    ("11-execution-providers.md", "cn-11-execution-providers.md"),
    ("12-cuda-provider.md", "cn-12-cuda-provider.md"),
    ("13-tensorrt-provider.md", "cn-13-tensorrt-provider.md"),
    ("14-openvino-provider.md", "cn-14-openvino-provider.md"),
])

add_files("PyTorch-Recipes", [
    ("00-recipes-index.md", "cn-00-recipes-index.md"),
    ("01-defining-neural-network.md", "cn-01-defining-neural-network.md"),
    ("02-state-dict.md", "cn-02-state-dict.md"),
    ("03-save-load-inference.md", "cn-03-save-load-inference.md"),
    ("04-save-load-checkpoint.md", "cn-04-save-load-checkpoint.md"),
    ("05-tensorboard.md", "cn-05-tensorboard.md"),
    ("06-profiler.md", "cn-06-profiler.md"),
])


def translate_line(line, translator):
    """Translate a single line, preserving inline code and markdown links."""
    if not line.strip():
        return line

    # Preserve leading whitespace
    indent = len(line) - len(line.lstrip())
    prefix = line[:indent]
    rest = line[indent:]

    # Handle standalone link lines like [ __ Text ](url) or [ Text __ ](url)
    link_match = re.match(r'^(\[\s*__?\s*)([^\]]+?)(\s*__?\s*\]\([^)]+\))(.*)$', rest)
    if link_match:
        try:
            text = translator.translate(link_match.group(2).strip())
        except Exception:
            text = link_match.group(2)
        return prefix + link_match.group(1) + text + link_match.group(3) + link_match.group(4)

    # Handle markdown links [text](url) - translate text portion only
    def replace_link(m):
        link_text = m.group(1)
        url = m.group(2)
        # Don't translate if it's just a URL or code-like
        if link_text.startswith('http') or link_text.startswith('__'):
            return m.group(0)
        try:
            translated = translator.translate(link_text)
        except Exception:
            translated = link_text
        return f'[{translated}]({url})'

    # Process line: split by inline code and links
    # First protect inline code
    parts = re.split(r'(`[^`]+`)', rest)
    processed = []
    for part in parts:
        if part.startswith('`') and part.endswith('`'):
            processed.append(part)
        else:
            # Translate links within this part
            translated = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, part)
            if translated.strip():
                try:
                    translated = translator.translate(translated)
                except Exception:
                    pass
            processed.append(translated)

    return prefix + ''.join(processed)


def translate_markdown(content, translator):
    """Translate markdown content preserving code blocks."""
    lines = content.split('\n')
    result = []
    in_code_block = False

    for line in lines:
        # Toggle code block state
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        # Don't translate code blocks
        if in_code_block:
            result.append(line)
            continue

        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            result.append(line)
            continue

        # Skip horizontal rules
        if re.match(r'^(---+|\*\*\*+|___+)\s*$', stripped):
            result.append(line)
            continue

        # Skip table separator rows
        if re.match(r'^[\|\s\-:]+$', stripped) and '|' in stripped:
            result.append(line)
            continue

        # Skip lines that are pure HTML comments or tags
        if stripped.startswith('<!--') or stripped.startswith('<!') or stripped == '':
            result.append(line)
            continue

        try:
            translated = translate_line(line, translator)
            result.append(translated)
        except Exception as e:
            print(f"    Warning: translation error on line: {line[:50]}... - {e}")
            result.append(line)

    return '\n'.join(result)


def process_file(src_path, dst_path, translator):
    """Read, translate, and write a single file."""
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    translated = translate_markdown(content, translator)

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(translated)


def main():
    translator = GoogleTranslator(source='en', target='zh-CN')

    total = len(ALL_FILES)
    print(f"Starting translation of {total} files...")

    for idx, (directory, src, dst) in enumerate(ALL_FILES):
        src_path = os.path.join(BASE, directory, src)
        dst_path = os.path.join(BASE, directory, dst)

        if not os.path.exists(src_path):
            print(f"  SKIP (not found): {src_path}")
            continue

        # Skip already translated files (cn-00, cn-01, cn-02 from fast-ai already done)
        if os.path.exists(dst_path):
            print(f"  [{idx+1}/{total}] SKIP (exists): {directory}/{dst}")
            continue

        print(f"  [{idx+1}/{total}] Translating: {directory}/{src} -> {dst}")
        try:
            process_file(src_path, dst_path, translator)
            print(f"    Done.")
        except Exception as e:
            print(f"    ERROR: {e}")

        # Small delay to avoid rate limiting
        time.sleep(0.3)

    print(f"\nComplete!")


if __name__ == '__main__':
    main()
