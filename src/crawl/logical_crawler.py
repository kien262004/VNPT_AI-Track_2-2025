import json
import os
from ..core import *
from tqdm import tqdm
import requests
import numpy as np
from ddgs import DDGS
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError, Error as PlaywrightError


def web_search(query: str, max_results: int = 5):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
    urls = [r.get("href") for r in results if r.get("href")]
    return urls

def clean_text(soup: BeautifulSoup) -> str:
    # loại bỏ script, style, noscript
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # ưu tiên lấy nội dung text
    text = soup.get_text(separator="\n")

    # làm sạch dòng
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n".join(lines)


def crawl_page(url: str, timeout: int = 10000) -> str:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=["--disable-gpu", "--no-sandbox"]
            )
            page = browser.new_page()
            page.goto(url, timeout=timeout)
            page.wait_for_load_state("networkidle")
            html = page.content()
            browser.close()

        soup = BeautifulSoup(html, "html.parser")
        text = clean_text(soup)
        return text

    except (PlaywrightError, TimeoutError) as e:
        print(f"[WARN] Không thể truy cập {url}: {e}")
        return ""

def query_crawl(query: str, max_results: int = 3, max_pages: int = 3) -> str:
    urls = web_search(query, max_results=max_results)
    all_texts = []
    for url in urls[:max_pages]:
        print(f"[INFO] Crawling {url}")
        page_text = crawl_page(url)
        if page_text:
            all_texts.append(page_text)

    # Nối tất cả text lại với nhau
    combined_text = "\n\n".join(all_texts)
    return combined_text

def crawl(path, outpath):
    with open(path, mode='r') as f:
        data = json.load(f)
    res = []
    llm = get_llm('openai-oss')
    for element in tqdm(data):
        if element['datasource'] not in ['Mandatory_Accuracy_Questions', 'Various_Domain']: continue
        res_web = query_crawl(element['question'])
        res.append({
            'question':element['question'],
            'info': res_web
        })
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
        
    
if __name__ == '__main__':
    crawl('data/val_routed.json', 'data/val_web.json')
    