# 바로GO — 서대문구 출장마사지·홈타이 안내 사이트

서울 서대문구 전지역 방문형 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 디자인: 프리미엄 팔레트(미드나잇 사파이어 + 샴페인 골드) + Pretendard 본문 + 세리프 헤딩

```
build.py            # 빌드 스크립트 (레이아웃·목차 자동생성·글자수 검사·sitemap)
content/
  site.py           # 상호(바로GO)·전화·BASE_URL·상단 메뉴(NAV)
  main.py           # 메인 페이지 (+ Organization/WebPage/BreadcrumbList/ImageObject/FAQPage JSON-LD)
  areas.py          # 지역별: 서대문구 허브 + 대표 동 9곳
  stations.py       # 역세권: 허브 + 역 10곳(인접 생활권 포함)
  living.py         # 생활권: 허브 + 생활권 10곳
  info.py           # 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·약관
  about.py          # 사이트 소개 (E-E-A-T)
assets/             # CSS, 모바일 내비 JS, 파비콘, OG 이미지
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 대표 동 9곳만 (충현·천연·북아현·신촌·연희·홍제·홍은·남가좌·북가좌) — 번호 행정동 페이지 없음
  (홍제1~3동→홍제동, 홍은1·2동→홍은동, 남가좌1·2동→남가좌동, 북가좌1·2동→북가좌동 통합)
- 역은 역 1개당 페이지 1개 — 환승역·경계역도 URL 하나, 출구별·노선별 페이지 없음
- 홍대입구·아현·디지털미디어시티역 등 타 구 성격 역은 인접 생활권으로만 설명
- 실제 오프라인 주소가 없는 방문형 사이트이므로 **LocalBusiness Schema는 사용하지 않음**
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console·네이버 서치어드바이저에 `sitemap.xml` 제출
