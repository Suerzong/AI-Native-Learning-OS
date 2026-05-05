#!/usr/bin/env python3
"""
Scrape runoob.com tutorials and convert to Markdown.
Usage: python scrape_runoob.py
"""

import os
import re
import sys
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOPICS = {
    "Python3": "https://www.runoob.com/python3/",
    "TensorFlow": "https://www.runoob.com/tensorflow/",
    "ML": "https://www.runoob.com/ml/",
    "NLP": "https://www.runoob.com/nlp/",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

def get_session():
    s = requests.Session()
    s.headers.update(HEADERS)
    return s

def fetch_page(session, url, retries=3):
    for i in range(retries):
        try:
            resp = session.get(url, timeout=20)
            resp.encoding = 'utf-8'
            return resp.text
        except Exception as e:
            print(f"  Retry {i+1}/{retries} for {url}: {e}")
            time.sleep(2)
    return None

def extract_subpage_links(html, base_url, topic_prefix):
    """Extract all tutorial sub-page links from the index page."""
    soup = BeautifulSoup(html, 'lxml')
    links = []
    seen = set()

    # Find sidebar or content links matching the topic
    for a in soup.find_all('a', href=True):
        href = a['href'].strip()
        title = a.get_text(strip=True)

        # Skip empty, javascript, external links
        if not href or href.startswith('javascript') or href.startswith('mailto'):
            continue

        # Build full URL
        full_url = urljoin(base_url, href)

        # Only include links within the same topic path
        if topic_prefix in full_url and full_url.endswith('.html'):
            if full_url not in seen:
                seen.add(full_url)
                links.append((full_url, title))

    return links

def html_to_markdown(html, title=""):
    """Convert HTML content to clean Markdown."""
    soup = BeautifulSoup(html, 'lxml')

    # Find main content area
    content = soup.find('div', class_='article-intro') or \
              soup.find('div', class_='entry-content') or \
              soup.find('div', id='content') or \
              soup.find('article') or \
              soup.find('div', class_='col-group')

    if not content:
        # Fallback: use body
        content = soup.find('body')

    if not content:
        return ""

    # Remove unwanted elements
    for tag in content.find_all(['script', 'style', 'nav', 'footer', 'header',
                                  'ins', 'iframe', 'noscript']):
        tag.decompose()

    # Remove ads and navigation
    for tag in content.find_all(class_=re.compile(r'(ad-|adsbygoogle|nav|menu|sidebar|footer|header|comment)', re.I)):
        tag.decompose()
    for tag in content.find_all(id=re.compile(r'(ad-|nav|menu|sidebar|footer|header|comment)', re.I)):
        tag.decompose()

    # Remove runoob-specific elements
    for tag in content.find_all(class_=re.compile(r'(runoob|cnzz|share|social|prev-next|breadcrumb|crumb)', re.I)):
        tag.decompose()

    md_lines = []

    def process_element(element, depth=0):
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            text = element.get_text(strip=True)
            # Skip site slogan h1
            if text and '学的不仅是技术' in text:
                return
            if text:
                md_lines.append('\n' + '#' * level + ' ' + text + '\n')

        elif element.name == 'p':
            text = extract_inline(element)
            if text.strip():
                md_lines.append(text)

        elif element.name == 'pre':
            code = element.get_text()
            lang = ''
            # Try to detect language from class
            cls = element.get('class', [])
            for c in cls:
                if 'python' in c.lower():
                    lang = 'python'
                elif 'html' in c.lower():
                    lang = 'html'
                elif 'css' in c.lower():
                    lang = 'css'
                elif 'js' in c.lower() or 'javascript' in c.lower():
                    lang = 'javascript'
                elif 'java' in c.lower():
                    lang = 'java'
                elif 'bash' in c.lower() or 'shell' in c.lower():
                    lang = 'bash'
            # Also check parent for language hints
            if not lang:
                parent_cls = ' '.join(element.parent.get('class', []))
                if 'python' in parent_cls.lower():
                    lang = 'python'

            md_lines.append('\n```' + lang)
            md_lines.append(code.rstrip())
            md_lines.append('```\n')

        elif element.name == 'code':
            # Inline code - handled by extract_inline
            pass

        elif element.name in ['ul', 'ol']:
            for i, li in enumerate(element.find_all('li', recursive=False)):
                prefix = f"{i+1}. " if element.name == 'ol' else "- "
                text = extract_inline(li)
                if text.strip():
                    md_lines.append(prefix + text)
            md_lines.append('')

        elif element.name == 'table':
            rows = element.find_all('tr')
            if rows:
                # Header
                headers = [th.get_text(strip=True) for th in rows[0].find_all(['th', 'td'])]
                if headers:
                    md_lines.append('| ' + ' | '.join(headers) + ' |')
                    md_lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
                    for row in rows[1:]:
                        cells = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])]
                        # Pad if needed
                        while len(cells) < len(headers):
                            cells.append('')
                        md_lines.append('| ' + ' | '.join(cells) + ' |')
                md_lines.append('')

        elif element.name == 'blockquote':
            text = element.get_text(strip=True)
            if text:
                for line in text.split('\n'):
                    md_lines.append('> ' + line)
                md_lines.append('')

        elif element.name == 'hr':
            md_lines.append('\n---\n')

        elif element.name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '')
            if src and not src.startswith('data:'):
                md_lines.append(f'\n![{alt}]({src})\n')

        elif element.name == 'br':
            md_lines.append('')

        elif element.name == 'div':
            # Check if it's a code block wrapper
            classes = ' '.join(element.get('class', []))
            if 'code' in classes.lower() or 'example' in classes.lower():
                code_text = element.get_text()
                if code_text.strip():
                    md_lines.append('\n```')
                    md_lines.append(code_text.rstrip())
                    md_lines.append('```\n')
            # Check for "尝试一下" button - skip
            elif 'tryit' in classes.lower():
                pass
            else:
                for child in element.children:
                    if hasattr(child, 'name') and child.name:
                        process_element(child, depth + 1)
        else:
            # For other block elements, recurse
            if element.name and element.name not in ['span', 'a', 'strong', 'em', 'b', 'i', 'u', 'small', 'font', 'sub', 'sup', 'label', 'input', 'button', 'select', 'option']:
                for child in element.children:
                    if hasattr(child, 'name') and child.name:
                        process_element(child, depth + 1)

    def extract_inline(element):
        """Extract text with inline formatting."""
        parts = []
        for child in element.children:
            if isinstance(child, str):
                t = child
                if t.strip():
                    parts.append(t)
            elif child.name == 'code':
                parts.append('`' + child.get_text() + '`')
            elif child.name == 'strong' or child.name == 'b':
                parts.append('**' + child.get_text() + '**')
            elif child.name == 'em' or child.name == 'i':
                parts.append('*' + child.get_text() + '*')
            elif child.name == 'a':
                href = child.get('href', '')
                text = child.get_text(strip=True)
                if href and text:
                    parts.append(f'[{text}]({href})')
                elif text:
                    parts.append(text)
            elif child.name == 'img':
                src = child.get('src', '')
                alt = child.get('alt', '')
                if src:
                    parts.append(f'![{alt}]({src})')
            elif child.name == 'br':
                parts.append('\n')
            elif child.name == 'span':
                parts.append(extract_inline(child))
            elif child.name in ['sub', 'sup']:
                parts.append(child.get_text())
            else:
                t = child.get_text()
                if t.strip():
                    parts.append(t)
        return ''.join(parts)

    # Process all content
    if content.name:
        process_element(content)
    else:
        for child in content:
            if hasattr(child, 'name') and child.name:
                process_element(child)

    # Clean up
    result = '\n'.join(md_lines)
    # Remove excessive blank lines
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    return result.strip()


def strip_zero_width(text):
    """Remove zero-width and other invisible Unicode characters."""
    return re.sub(r'[​‌‍⁠﻿]', '', text)

def clean_markdown(md_text):
    """Clean up markdown: remove excessive blank lines, trailing spaces, etc."""
    # Normalize line endings
    md_text = md_text.replace('\r\n', '\n').replace('\r', '\n')
    # Strip zero-width chars
    md_text = strip_zero_width(md_text)

    # Remove lines that are only whitespace
    lines = [line.rstrip() for line in md_text.split('\n')]

    # Remove excessive consecutive blank lines (max 2)
    cleaned = []
    blank_count = 0
    for line in lines:
        if line == '':
            blank_count += 1
            if blank_count <= 2:
                cleaned.append(line)
        else:
            blank_count = 0
            cleaned.append(line)

    # Remove leading blank lines
    while cleaned and cleaned[0] == '':
        cleaned.pop(0)
    # Remove trailing blank lines
    while cleaned and cleaned[-1] == '':
        cleaned.pop()

    return '\n'.join(cleaned)


def scrape_topic(topic_name, base_url):
    """Scrape all pages for a topic and save as MD files."""
    print(f"\n{'='*60}")
    print(f"Scraping: {topic_name} ({base_url})")
    print(f"{'='*60}")

    topic_dir = os.path.join(BASE_DIR, topic_name)
    os.makedirs(topic_dir, exist_ok=True)

    session = get_session()

    # 1. Get index page
    print("Fetching index page...")
    index_html = fetch_page(session, base_url)
    if not index_html:
        print(f"ERROR: Could not fetch index page for {topic_name}")
        return []

    # 2. Extract sub-page links
    topic_prefix = base_url.rstrip('/')
    links = extract_subpage_links(index_html, base_url, topic_prefix)
    print(f"Found {len(links)} sub-pages")

    if not links:
        print("WARNING: No sub-pages found, trying alternative extraction...")
        # Try extracting from the full page
        soup = BeautifulSoup(index_html, 'lxml')
        for a in soup.find_all('a', href=True):
            href = a['href'].strip()
            title = a.get_text(strip=True)
            full_url = urljoin(base_url, href)
            if topic_prefix in full_url and full_url.endswith('.html'):
                if full_url not in [l[0] for l in links]:
                    links.append((full_url, title))
        print(f"After retry: found {len(links)} sub-pages")

    # 3. Download each page and convert to MD
    page_contents = []  # (filename, title, markdown_content)

    for i, (url, title) in enumerate(links):
        # Generate filename from URL
        slug = url.rstrip('/').split('/')[-1].replace('.html', '')
        filename = f"{i+1:03d}_{slug}.md"

        print(f"  [{i+1}/{len(links)}] {strip_zero_width(title) or slug}")

        html = fetch_page(session, url)
        if not html:
            print(f"    FAILED to fetch")
            continue

        # Get title from <title> tag
        page_soup = BeautifulSoup(html, 'lxml')
        title_tag = page_soup.find('title')
        if title_tag:
            raw_title = title_tag.get_text(strip=True)
            # Strip site suffix like " | 菜鸟教程"
            raw_title = re.sub(r'\s*[|｜]\s*菜鸟教程\s*$', '', raw_title)
            if raw_title:
                title = raw_title

        md_content = html_to_markdown(html, title)
        if not md_content.strip():
            print(f"    WARNING: Empty content extracted")
            continue

        md_content = clean_markdown(md_content)

        # Save individual file
        filepath = os.path.join(topic_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(md_content)

        page_contents.append((filename, title, md_content))
        time.sleep(0.5)  # Be polite

    print(f"  Saved {len(page_contents)} MD files to {topic_dir}/")
    return page_contents


def combine_topic_md(topic_name, page_contents):
    """Combine all MD files in a topic folder into one big MD with TOC."""
    if not page_contents:
        return

    print(f"\nCombining {topic_name} into single MD...")

    combined_lines = []
    toc_lines = []

    combined_lines.append(f"# {topic_name} 教程\n")
    combined_lines.append(f"*来源: 菜鸟教程 (runoob.com)*\n")
    combined_lines.append("---\n")

    toc_lines.append("## 目录\n")

    for i, (filename, title, content) in enumerate(page_contents):
        # Create anchor from title
        anchor = re.sub(r'[^\w一-鿿-]', '', title.replace(' ', '-')).lower()
        if not anchor:
            anchor = f"section-{i+1}"

        toc_lines.append(f"{i+1}. [{title}](#{anchor})")

        combined_lines.append(f"\n\n{'#'*50}")
        combined_lines.append(f"# {title}\n")
        combined_lines.append(content)

    # Insert TOC after header
    final_lines = []
    # Header
    final_lines.append(f"# {topic_name} 教程\n")
    final_lines.append(f"*来源: 菜鸟教程 (runoob.com)*\n")
    final_lines.append("---\n")
    # TOC
    final_lines.extend(toc_lines)
    final_lines.append("\n---\n")

    # Content
    for i, (filename, title, content) in enumerate(page_contents):
        anchor = re.sub(r'[^\w一-鿿-]', '', title.replace(' ', '-')).lower()
        if not anchor:
            anchor = f"section-{i+1}"
        final_lines.append(f"\n\n<a id=\"{anchor}\"></a>")
        final_lines.append(f"\n## {i+1}. {title}\n")
        final_lines.append(content)

    # Final cleanup
    combined = '\n'.join(final_lines)
    combined = clean_markdown(combined)

    output_path = os.path.join(BASE_DIR, topic_name, f"{topic_name}_完整教程.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(combined)

    print(f"  Combined MD saved: {output_path}")
    print(f"  Total size: {len(combined):,} bytes, {len(page_contents)} sections")


def main():
    print("Runoob Tutorial Scraper")
    print("=" * 60)

    all_results = {}

    # Skip topics already done (TensorFlow needs re-scrape)
    SKIP_TOPICS = set()  # Add topic names here to skip

    for topic_name, base_url in TOPICS.items():
        if topic_name in SKIP_TOPICS:
            print(f"\nSkipping {topic_name} (already done)")
            # Load existing files
            topic_dir = os.path.join(BASE_DIR, topic_name)
            page_contents = []
            if os.path.isdir(topic_dir):
                for fname in sorted(os.listdir(topic_dir)):
                    if fname.endswith('.md') and not fname.endswith('_完整教程.md'):
                        fpath = os.path.join(topic_dir, fname)
                        with open(fpath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        title = content.split('\n')[0].lstrip('# ').strip()
                        page_contents.append((fname, title, content))
            all_results[topic_name] = page_contents
            continue
        page_contents = scrape_topic(topic_name, base_url)
        all_results[topic_name] = page_contents

    # Combine each topic into one big MD
    print("\n" + "=" * 60)
    print("Combining into single MDs per topic...")
    print("=" * 60)

    for topic_name, page_contents in all_results.items():
        combine_topic_md(topic_name, page_contents)

    print("\n" + "=" * 60)
    print("Done! Summary:")
    print("=" * 60)
    for topic_name, page_contents in all_results.items():
        print(f"  {topic_name}: {len(page_contents)} pages scraped")


if __name__ == '__main__':
    main()
