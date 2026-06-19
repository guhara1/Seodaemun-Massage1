# 메인 페이지 — 서대문구 출장마사지·홈타이 허브. 키워드를 몰아넣지 않고 하위 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY

_OG = f"{BASE_URL.rstrip('/')}/assets/og-image.png"

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "image": "{_OG}",
  "logo": "{BASE_URL.rstrip('/')}/assets/icon-512.png",
  "description": "서울 서대문구 전지역 방문형 출장마사지·홈타이 예약 안내",
  "areaServed": {{ "@type": "AdministrativeArea", "name": "서울특별시 서대문구" }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "서대문구 출장마사지·홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "description": "서대문구 출장마사지·홈타이 예약 전 신촌, 홍제, 연희, 북아현 생활권을 확인하세요.",
  "inLanguage": "ko-KR",
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{_OG}",
    "width": 1200,
    "height": 630
  }},
  "breadcrumb": {{ "@id": "{BASE_URL}/#breadcrumb" }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "{BASE_URL}/#breadcrumb",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "서대문구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "예약 시간과 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 충현동, 천연동, 북아현동, 신촌동, 연희동, 홍제동, 홍은동, 남가좌동, 북가좌동 대표 동 안내에서 확인하실 수 있습니다." }}
    }},
    {{
      "@type": "Question",
      "name": "홍제1동·홍은2동처럼 번호가 붙은 동은 왜 따로 없나요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "홍제1~3동은 홍제동, 홍은1·2동은 홍은동, 남가좌1·2동은 남가좌동, 북가좌1·2동은 북가좌동 대표 페이지에서 통합 안내해 중복 페이지 위험을 줄입니다." }}
    }},
    {{
      "@type": "Question",
      "name": "신촌역이나 이대역 인근도 가능한가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "주요 역세권은 역 안내 페이지에서 인근 생활권과 함께 설명합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다." }}
    }},
    {{
      "@type": "Question",
      "name": "출장마사지와 홈타이는 무엇이 다른가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "출장마사지는 관리사가 계신 곳으로 방문하는 방문형 관리 서비스 전체를 가리키고, 홈타이는 그중 자택 등에서 받는 형태를 부르는 말입니다. 홈타이 이용 가이드에서 차이를 정리했습니다." }}
    }},
    {{
      "@type": "Question",
      "name": "추가 이동비가 있나요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "지역과 예약 시간대, 이동 거리에 따라 달라질 수 있어 예약 시 총비용으로 먼저 안내해 드립니다. 안내된 금액 외 추가 요구는 없습니다." }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Care · 서대문구 전지역</p>
    <h1>서대문구 출장마사지 · 서대문구 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">신촌·홍제·연희·북아현까지, 계신 곳에서 받는 방문형 관리.<br>대표동·역세권·생활권을 먼저 확인하고 전화로 예약하세요.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/seoul/seodaemun/areas/">지역별 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>9개</strong><span>대표 동</span></li>
      <li><strong>10개</strong><span>역세권 안내</span></li>
      <li><strong>10개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section>
<h2>서대문구에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>서대문구에서 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 서대문구는 서울 서북권과 도심을 잇는 지역으로, 신촌·이대 주변의 대학가 생활권, 홍제·무악재 중심의 주거지 생활권, 연희·남가좌의 조용한 주거권, 충정로·서대문역 중심의 도심 인접 업무권이 함께 있습니다. 그래서 이 사이트는 “전지역 가능”만 적기보다 대표동·역세권·생활권을 나누어 안내합니다.</p>
</section>

<section>
<h2>신촌·연희·홍제·북아현 생활권 차이</h2>
<p>같은 서대문구라도 생활권마다 분위기가 다릅니다. 신촌·연세대 일대는 대학가와 상권, 주거지가 섞여 유동 인구가 많고, 북아현동은 이대역과 북아현뉴타운을 낀 주거권입니다. 홍제동과 홍은동은 홍제천과 인왕산·안산 자락을 따라 이어지는 주거 밀집 생활권이고, 연희동은 단독·빌라 위주의 차분한 주거지입니다. 남가좌동과 북가좌동은 명지대·가좌역을 낀 서쪽 주거권이며, 충현동과 천연동은 충정로·서대문역을 낀 도심 인접권입니다. 자세한 차이는 <a href="/seoul/seodaemun/living/">생활권 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>대표동별 방문 가능 지역 안내</h2>
<p>대표 동은 충현동, 천연동, 북아현동, 신촌동, 연희동, 홍제동, 홍은동, 남가좌동, 북가좌동 아홉 곳으로 구성합니다. 홍제1~3동은 홍제동, 홍은1·2동은 홍은동, 남가좌1·2동은 남가좌동, 북가좌1·2동은 북가좌동 대표 페이지에서 통합해 안내합니다. 거주하시거나 머무시는 동을 선택해 생활권 특징과 방문 조건을 확인해 주세요.</p>
<ul class="card-grid">
<li><a href="/seoul/seodaemun/chunghyeon-dong-chuljangmassage/">충현동</a></li>
<li><a href="/seoul/seodaemun/cheonyeon-dong-chuljangmassage/">천연동</a></li>
<li><a href="/seoul/seodaemun/bugahyeon-dong-chuljangmassage/">북아현동</a></li>
<li><a href="/seoul/seodaemun/sinchon-dong-chuljangmassage/">신촌동</a></li>
<li><a href="/seoul/seodaemun/yeonhui-dong-chuljangmassage/">연희동</a></li>
<li><a href="/seoul/seodaemun/hongje-dong-chuljangmassage/">홍제동</a></li>
<li><a href="/seoul/seodaemun/hongeun-dong-chuljangmassage/">홍은동</a></li>
<li><a href="/seoul/seodaemun/namgajwa-dong-chuljangmassage/">남가좌동</a></li>
<li><a href="/seoul/seodaemun/bukgajwa-dong-chuljangmassage/">북가좌동</a></li>
</ul>
<p>서대문구 전체 구성은 <a href="/seoul/seodaemun/areas/">지역별 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section>
<h2>홍제역·신촌역·이대역·충정로역 역세권 안내</h2>
<p>역을 기준으로 위치를 설명하는 것이 편하시다면 역세권 안내를 참고하세요. 홍제역부터 가좌역, 아현역·디지털미디어시티역 인접 생활권까지 역마다 한 페이지로 정리했습니다. 신촌역·충정로역·가좌역처럼 노선이 여러 개거나 경계 성격이 있는 역도 노선별로 쪼개지 않고 한 페이지로 운영하며, 홍대입구역처럼 마포구 성격이 강한 역은 인접 생활권으로만 설명합니다.</p>
<ul class="card-grid">
<li><a href="/seoul/seodaemun/hongje-station-chuljangmassage/">홍제역</a></li>
<li><a href="/seoul/seodaemun/muakjae-station-chuljangmassage/">무악재역</a></li>
<li><a href="/seoul/seodaemun/dongnimmun-station-chuljangmassage/">독립문역</a></li>
<li><a href="/seoul/seodaemun/chungjeongno-station-chuljangmassage/">충정로역</a></li>
<li><a href="/seoul/seodaemun/seodaemun-station-chuljangmassage/">서대문역</a></li>
<li><a href="/seoul/seodaemun/ewha-womans-univ-station-chuljangmassage/">이대역</a></li>
<li><a href="/seoul/seodaemun/sinchon-station-chuljangmassage/">신촌역</a></li>
<li><a href="/seoul/seodaemun/gajwa-station-chuljangmassage/">가좌역</a></li>
<li><a href="/seoul/seodaemun/ahyeon-nearby-area-chuljangmassage/">아현역 인접</a></li>
<li><a href="/seoul/seodaemun/dmc-nearby-area-chuljangmassage/">DMC역 인접</a></li>
</ul>
</section>

<section>
<h2>서대문구 홈타이 예약 전 확인사항</h2>
<p>서대문구 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 신촌역과 이대역처럼 접근성이 좋은 지역도 있지만, 홍은동·북가좌동·연희동 일부 주거지는 시간대에 따라 이동 기준이 달라질 수 있습니다. 그래서 예약 전에는 정확한 방문 주소와 추가 이동비 여부, 결제 방식과 취소 기준, 개인정보 처리 기준을 함께 확인해 두시는 것이 좋습니다. 진행 방식은 <a href="/reservation/">예약 안내</a>와 <a href="/precautions/">이용 전 확인사항</a>, <a href="/hometai-guide/">홈타이 이용 가이드</a>에 정리되어 있습니다.</p>
</section>

<section>
<h2>서대문구 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 페이지 수를 늘리는 대신 중복을 줄이는 방향으로 운영합니다. 번호가 붙은 행정동은 대표 동으로 통합하고, 환승역·경계역은 역 이름 기준 한 개 URL만 두며, 지역·역·테마를 조합한 페이지는 만들지 않습니다. 충정로, 냉천동, 영천동, 현저동, 창천동, 대현동 같은 법정동·생활권명은 단독 페이지로 늘리지 않고 관련 대표동 본문에서 보조로 설명합니다. 모든 페이지는 지역명만 바꾼 복사 없이 실제 특징을 따로 작성합니다.</p>
</section>

<section>
<h2>서대문구 출장마사지 사이트 이용 방법</h2>
<p>이용 순서는 간단합니다. 먼저 거주지나 머무는 곳을 기준으로 대표동·역세권·생활권 중 익숙한 안내를 고르고, 방문 조건과 예약 전 확인사항을 읽은 뒤 전화로 위치와 희망 시간을 알려주시면 됩니다. 안내를 확인하신 다음 궁금한 점은 예약 전화에서 정리하시면 됩니다. 운영 기준과 콘텐츠 원칙은 <a href="/about/">사이트 소개</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>서대문구 전지역 방문이 가능한가요?</h3>
<p>예약 시간과 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 충현동·천연동·북아현동·신촌동·연희동·홍제동·홍은동·남가좌동·북가좌동 대표 동 안내에서 확인하실 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>홍제1동·홍은2동처럼 번호가 붙은 동은 왜 따로 없나요?</h3>
<p>홍제1~3동은 홍제동, 홍은1·2동은 홍은동, 남가좌1·2동은 남가좌동, 북가좌1·2동은 북가좌동 대표 페이지에서 통합 안내해 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>신촌역이나 이대역 인근도 가능한가요?</h3>
<p>주요 역세권은 역 안내 페이지에서 인근 생활권과 함께 설명합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>출장마사지와 홈타이는 무엇이 다른가요?</h3>
<p>출장마사지는 관리사가 계신 곳으로 방문하는 방문형 관리 서비스 전체를 가리키고, 홈타이는 그중 자택 등에서 받는 형태를 부르는 말입니다. <a href="/hometai-guide/">홈타이 이용 가이드</a>에서 차이를 정리했습니다.</p>
</div>
<div class="faq-item">
<h3>추가 이동비가 있나요?</h3>
<p>지역과 예약 시간대, 이동 거리에 따라 달라질 수 있어 예약 시 총비용으로 먼저 안내해 드립니다. 안내된 금액 외 추가 요구는 없습니다.</p>
</div>
</section>

<section class="cta">
<h2>예약 문의</h2>
<p>서대문구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "서대문구 출장마사지｜신촌·홍제·연희·북아현 홈타이 지역 안내",
    "desc": "서대문구 출장마사지·홈타이 예약 전 신촌, 홍제, 연희, 북아현 생활권을 확인하세요.",
    "h1": "서대문구 출장마사지 · 서대문구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
