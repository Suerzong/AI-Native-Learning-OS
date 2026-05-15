import asyncio, sys, re, os, time, random
from pathlib import Path

sys.path.insert(0, "/tmp/pw_env/lib/python3.12/site-packages")
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
import requests

OUTPUT_DIR = Path("/home/ubuntu/Edge-AI/temp/PPTs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 全部 115 个 PPT URL (去重后)
PPT_LIST = [
    "https://www.1ppt.com/article/143920.html",
    "https://www.1ppt.com/article/143511.html",
    "https://www.1ppt.com/article/136124.html",
    "https://www.1ppt.com/article/136122.html",
    "https://www.1ppt.com/article/134425.html",
    "https://www.1ppt.com/article/132867.html",
    "https://www.1ppt.com/article/143111.html",
    "https://www.1ppt.com/article/136123.html",
    "https://www.1ppt.com/article/136121.html",
    "https://www.1ppt.com/article/136119.html",
    "https://www.1ppt.com/article/134655.html",
    "https://www.1ppt.com/article/132883.html",
    "https://www.1ppt.com/article/132882.html",
    "https://www.1ppt.com/article/132879.html",
    "https://www.1ppt.com/article/132870.html",
    "https://www.1ppt.com/article/132869.html",
    "https://www.1ppt.com/article/132868.html",
    "https://www.1ppt.com/article/131852.html",
    "https://www.1ppt.com/article/144302.html",
    "https://www.1ppt.com/article/143818.html",
    "https://www.1ppt.com/article/143160.html",
    "https://www.1ppt.com/article/142729.html",
    "https://www.1ppt.com/article/141197.html",
    "https://www.1ppt.com/article/141084.html",
    "https://www.1ppt.com/article/138228.html",
    "https://www.1ppt.com/article/137376.html",
    "https://www.1ppt.com/article/136537.html",
    "https://www.1ppt.com/article/135791.html",
    "https://www.1ppt.com/article/135788.html",
    "https://www.1ppt.com/article/140857.html",
    "https://www.1ppt.com/article/139063.html",
    "https://www.1ppt.com/article/138444.html",
    "https://www.1ppt.com/article/137347.html",
    "https://www.1ppt.com/article/136505.html",
    "https://www.1ppt.com/article/135769.html",
    "https://www.1ppt.com/article/140020.html",
    "https://www.1ppt.com/article/136129.html",
    "https://www.1ppt.com/article/136120.html",
    "https://www.1ppt.com/article/134910.html",
    "https://www.1ppt.com/article/132884.html",
    "https://www.1ppt.com/article/132881.html",
    "https://www.1ppt.com/article/132878.html",
    "https://www.1ppt.com/article/132873.html",
    "https://www.1ppt.com/article/132872.html",
    "https://www.1ppt.com/article/132871.html",
    "https://www.1ppt.com/article/132450.html",
    "https://www.1ppt.com/article/142975.html",
    "https://www.1ppt.com/article/141295.html",
    "https://www.1ppt.com/article/141089.html",
    "https://www.1ppt.com/article/139711.html",
    "https://www.1ppt.com/article/136131.html",
    "https://www.1ppt.com/article/134918.html",
    "https://www.1ppt.com/article/134657.html",
    "https://www.1ppt.com/article/134653.html",
    "https://www.1ppt.com/article/134652.html",
    "https://www.1ppt.com/article/134650.html",
    "https://www.1ppt.com/article/134039.html",
    "https://www.1ppt.com/article/134034.html",
    "https://www.1ppt.com/article/133952.html",
    "https://www.1ppt.com/article/133382.html",
    "https://www.1ppt.com/article/133372.html",
    "https://www.1ppt.com/article/131855.html",
    "https://www.1ppt.com/article/131854.html",
    "https://www.1ppt.com/article/144300.html",
    "https://www.1ppt.com/article/143881.html",
    "https://www.1ppt.com/article/142976.html",
    "https://www.1ppt.com/article/142728.html",
    "https://www.1ppt.com/article/140640.html",
    "https://www.1ppt.com/article/139713.html",
    "https://www.1ppt.com/article/139710.html",
    "https://www.1ppt.com/article/137377.html",
    "https://www.1ppt.com/article/135652.html",
    "https://www.1ppt.com/article/134911.html",
    "https://www.1ppt.com/article/134656.html",
    "https://www.1ppt.com/article/134265.html",
    "https://www.1ppt.com/article/133951.html",
    "https://www.1ppt.com/article/133946.html",
    "https://www.1ppt.com/article/133944.html",
    "https://www.1ppt.com/article/132880.html",
    "https://www.1ppt.com/article/132513.html",
    "https://www.1ppt.com/article/131853.html",
    "https://www.1ppt.com/article/144244.html",
    "https://www.1ppt.com/article/144240.html",
    "https://www.1ppt.com/article/142289.html",
    "https://www.1ppt.com/article/139717.html",
    "https://www.1ppt.com/article/139709.html",
    "https://www.1ppt.com/article/139707.html",
    "https://www.1ppt.com/article/139703.html",
    "https://www.1ppt.com/article/136437.html",
    "https://www.1ppt.com/article/136118.html",
    "https://www.1ppt.com/article/135526.html",
    "https://www.1ppt.com/article/134919.html",
    "https://www.1ppt.com/article/134917.html",
    "https://www.1ppt.com/article/134915.html",
    "https://www.1ppt.com/article/134914.html",
    "https://www.1ppt.com/article/134913.html",
    "https://www.1ppt.com/article/134909.html",
    "https://www.1ppt.com/article/134908.html",
    "https://www.1ppt.com/article/134027.html",
    "https://www.1ppt.com/article/133953.html",
    "https://www.1ppt.com/article/133950.html",
    "https://www.1ppt.com/article/133948.html",
    "https://www.1ppt.com/article/133943.html",
    "https://www.1ppt.com/article/132877.html",
    "https://www.1ppt.com/article/132876.html",
    "https://www.1ppt.com/article/132875.html",
    "https://www.1ppt.com/article/132874.html",
    "https://www.1ppt.com/article/132453.html",
    "https://www.1ppt.com/article/108720.html",
    "https://www.1ppt.com/article/104157.html",
    "https://www.1ppt.com/article/144311.html",
    "https://www.1ppt.com/article/142793.html",
    "https://www.1ppt.com/article/138035.html",
    "https://www.1ppt.com/article/138005.html",
    "https://www.1ppt.com/article/137914.html",
    "https://www.1ppt.com/article/137687.html",
    "https://www.1ppt.com/article/137678.html",
    "https://www.1ppt.com/article/137673.html",
    "https://www.1ppt.com/article/137671.html",
    "https://www.1ppt.com/article/137670.html",
    "https://www.1ppt.com/article/137662.html",
    "https://www.1ppt.com/article/137212.html",
    "https://www.1ppt.com/article/134641.html",
]


async def download_one(browser, url, output_dir):
    """用独立 context 下载一个 PPT。返回 (标题, 成功/失败)。"""
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1920, "height": 1080},
        locale="zh-CN",
    )
    page = await context.new_page()
    await Stealth().apply_stealth_async(page)
    label = url

    try:
        # 1. 文章页
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        for _ in range(15):
            html = await page.content()
            if "acw_sc__v2" not in html and "aliyun_waf" not in html:
                break
            await page.wait_for_timeout(1000)
        else:
            await context.close()
            return url, False, "[文章页 WAF]"

        await page.wait_for_timeout(1000)

        title_el = await page.query_selector("h1")
        title = (await title_el.inner_text()).strip() if title_el else url.split("/")[-1].replace(".html", "")
        title = re.sub(r"[PPT模板下载\-_ ]", "", title).strip()
        if len(title) < 2:
            title = url.split("/")[-1]

        dl_el = await page.query_selector('a[href*="download.php"]')
        if not dl_el:
            await context.close()
            return title, False, "[无下载链接]"

        href = await dl_el.get_attribute("href")
        dl_url = href if href.startswith("http") else "https://www.1ppt.com" + href

        # 2. 下载页
        await page.goto(dl_url, wait_until="domcontentloaded", timeout=30000)
        for _ in range(10):
            html = await page.content()
            if "acw_sc__v2" not in html and "aliyun_waf" not in html:
                break
            await page.wait_for_timeout(1000)
        else:
            await context.close()
            return title, False, "[下载页 WAF]"

        await page.wait_for_timeout(1500)
        html = await page.content()

        # 3. 提取文件 URL
        file_url = None
        all_a = await page.query_selector_all("a[href]")
        for a in all_a:
            try:
                h = await a.get_attribute("href")
                if not h: continue
                hl = h.lower()
                if any(ext in hl for ext in [".pptx", ".ppt", ".rar", ".zip", ".7z"]):
                    file_url = h; break
                if "ppt.1ppt.com" in hl:
                    file_url = h; break
            except: pass

        if not file_url:
            m = re.search(r'(https?://ppt\.1ppt\.com[^\s"\'<>]+)', html)
            if m: file_url = m.group(1)
        if not file_url:
            m = re.search(r'(https?://[^\s"\'<>]+\.(?:pptx?|rar|zip|7z))', html, re.I)
            if m: file_url = m.group(1)

        if not file_url:
            await context.close()
            return title, False, "[无文件链接]"

        if file_url.startswith("//"): file_url = "https:" + file_url
        elif file_url.startswith("/"): file_url = "https://www.1ppt.com" + file_url

        # 4. 下载
        cookies = await context.cookies()
        cookie_str = "; ".join(f"{c['name']}={c['value']}" for c in cookies)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                   "Cookie": cookie_str, "Referer": "https://www.1ppt.com/"}

        r = requests.get(file_url, headers=headers, timeout=120, stream=True, allow_redirects=True)
        r.raise_for_status()
        ct = r.headers.get("content-type", "").lower()
        cd = r.headers.get("content-disposition", "")

        if "text/html" in ct and "attachment" not in cd:
            prev = next(r.iter_content(2048), b"").decode("utf-8", errors="ignore")
            if "acw_sc__v2" in prev or "aliyun_waf" in prev:
                await context.close(); return title, False, "[下载 WAF]"
            await context.close(); return title, False, "[非文件响应]"

        filename = None
        if cd:
            m = re.findall(r'filename[*]?=["\']?(?:UTF-8\'\')?([^"\';\s]+)', cd)
            if m: filename = m[0]
        if not filename:
            safe = re.sub(r'[<>:"/\\|?*]', '_', title)[:50]
            ext = ".zip"
            if "rar" in ct or "octet" in ct: ext = ".rar"
            elif "pptx" in ct: ext = ".pptx"
            elif "ppt" in ct: ext = ".ppt"
            else:
                url_ext = re.search(r'\.(pptx?|rar|zip|7z)', file_url, re.I)
                if url_ext: ext = "." + url_ext.group(1)
            filename = safe + ext

        safe_name = re.sub(r'[<>:"/\\|?*]', '_', filename)[:80]
        filepath = output_dir / safe_name
        with open(filepath, "wb") as f:
            for chunk in r.iter_content(8192): f.write(chunk)

        size = filepath.stat().st_size
        if size < 1000:
            filepath.unlink()
            await context.close(); return title, False, f"[太小 {size}B]"

        await context.close()
        return title, True, f"{safe_name} ({size/1024:.0f} KB)"

    except Exception as e:
        await context.close()
        label_text = title if 'title' in dir() and title else url
        return label_text, False, f"[错误 {e}]"


async def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    # 已下载 (所有 zip/rar/pptx)
    existing = set()
    for f in OUTPUT_DIR.iterdir():
        if f.suffix in (".zip", ".rar", ".pptx", ".ppt", ".7z"):
            existing.add(f.stem[:10])

    print(f"总计 {len(PPT_LIST)} 个, 已有 {len(existing)} 个\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )

        success, fail, skip = 0, 0, 0
        failed_list = []

        for i, url in enumerate(PPT_LIST):
            aid = url.split("/")[-1].replace(".html", "")

            # 检查是否已下载
            already = False
            for f in existing:
                if aid[:4] in f: already = True; break
            if already:
                skip += 1
                continue

            print(f"[{i+1}/{len(PPT_LIST)}] {aid}", end=" ", flush=True)

            title, ok, msg = await download_one(browser, url, OUTPUT_DIR)
            print(f"\r[{i+1}/{len(PPT_LIST)}] {msg}" if ok else f"\r[{i+1}/{len(PPT_LIST)}] {msg}")

            if ok:
                success += 1
            else:
                fail += 1
                failed_list.append((url, msg))

            # 3-5 秒间隔
            wait = random.uniform(3.0, 5.0)
            if i < len(PPT_LIST) - 1:
                time.sleep(wait)

        await browser.close()

    print(f"\n{'='*40}")
    print(f"成功: {success}  失败: {fail}  跳过: {skip}  总计: {len(PPT_LIST)}")
    print(f"文件: {OUTPUT_DIR}")
    if failed_list:
        print(f"\n失败:")
        for url, reason in failed_list[:10]:
            print(f"  {url.split('/')[-1]}: {reason}")
        if len(failed_list) > 10:
            print(f"  ... 共 {len(failed_list)} 个")


if __name__ == "__main__":
    asyncio.run(main())
