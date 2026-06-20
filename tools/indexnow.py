#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버 등 참여 검색엔진에 URL 변경을 알린다.

사용법:
    python3 tools/indexnow.py                  # sitemap.xml 의 모든 URL 통보
    python3 tools/indexnow.py URL [URL ...]    # 특정 URL만 통보 (글 올린 직후)

전제: 배포된 사이트 루트에서 https://<도메인>/<KEY>.txt 가 키 문자열을 반환해야
검증됩니다. (build.py 가 키 파일을 자동 생성하므로 배포만 되어 있으면 됩니다.)
외부 의존성 없음 — 표준 라이브러리만 사용합니다.
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE)

# 한 곳에 보내면 참여 엔진끼리 공유되지만, 네이버·빙에 직접도 보내 확실히 한다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }).encode("utf-8")
    for endpoint in ENDPOINTS:
        req = urllib.request.Request(
            endpoint, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                print(f"  {resp.status} {resp.reason}  ←  {endpoint}")
        except urllib.error.HTTPError as e:
            print(f"  {e.code} {e.reason}  ←  {endpoint}  (200/202 가 정상)")
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR  ←  {endpoint}: {e}")


def main():
    urls = sys.argv[1:] or sitemap_urls()
    if not urls:
        print("통보할 URL이 없습니다. (sitemap.xml 비어 있음)")
        return
    print(f"IndexNow 통보: {len(urls)}개 URL  (host={HOST})")
    submit(urls)
    print("완료. 빙/네이버는 보통 200 또는 202를 반환합니다.")


if __name__ == "__main__":
    main()
