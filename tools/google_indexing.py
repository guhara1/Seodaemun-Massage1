#!/usr/bin/env python3
"""Google Indexing API 즉시 색인 통보 (구글은 IndexNow 미참여).

설정(최초 1회):
  1) Google Cloud 콘솔에서 프로젝트 생성 → "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드 (service_account.json)
  3) Search Console > 설정 > 사용자 및 권한 에서 그 서비스 계정 이메일을
     "소유자(Owner)"로 추가
  4) pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/경로/service_account.json
  python3 tools/google_indexing.py                # sitemap.xml 전체
  python3 tools/google_indexing.py URL [URL ...]   # 특정 URL만

주의: 구글 Indexing API는 공식적으로 JobPosting/BroadcastEvent 용도이며,
일반 페이지에 대한 색인 보장은 없습니다. 일반 페이지는 Search Console의
sitemap 제출 + URL 검사가 정석이고, 본 스크립트는 보조 수단입니다.
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main():
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("먼저 설치하세요:  pip install google-auth requests")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.isfile(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 service_account.json 경로를 지정하세요.")

    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    session = AuthorizedSession(creds)

    urls = sys.argv[1:] or sitemap_urls()
    print(f"Google Indexing API 통보: {len(urls)}개 URL")
    for url in urls:
        r = session.post(ENDPOINT, json={"url": url, "type": "URL_UPDATED"}, timeout=30)
        flag = "OK" if r.status_code == 200 else f"{r.status_code}"
        print(f"  {flag}  {url}")


if __name__ == "__main__":
    main()
