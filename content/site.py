# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://seodaemun-massage1.pages.dev"

BRAND = "바로GO"
BRAND_MARK = "바"          # 헤더·파비콘 원형 마크 글자
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

GU = "서대문구"
TAGLINE = "서대문구 전지역 방문 관리 · 24시간 상담"

# IndexNow 키 — 변경 금지(루트의 {KEY}.txt 파일과 일치해야 함). 빙·네이버 즉시 색인 통보용.
INDEXNOW_KEY = "1ca325a0dc0d5bc2043aa3229d9b443a"

# 푸터 텔레그램 버튼 링크 (제휴 문의 채널이 따로 있으면 TELEGRAM_BIZ만 교체)
TELEGRAM_MAKE = "https://t.me/googleseolab"
TELEGRAM_BIZ = "https://t.me/googleseolab"

# 상단 메뉴 — 하위 메뉴에는 키워드를 과도하게 반복하지 않고 지역명·역명·생활권명만 표시한다.
NAV = [
    ("서대문 홈", "/", []),
    ("지역별 안내", "/seoul/seodaemun/areas/", [
        ("서대문구 전체", "/seoul/seodaemun/areas/"),
        ("충현동", "/seoul/seodaemun/chunghyeon-dong/"),
        ("천연동", "/seoul/seodaemun/cheonyeon-dong/"),
        ("북아현동", "/seoul/seodaemun/bugahyeon-dong/"),
        ("신촌동", "/seoul/seodaemun/sinchon-dong/"),
        ("연희동", "/seoul/seodaemun/yeonhui-dong/"),
        ("홍제동", "/seoul/seodaemun/hongje-dong/"),
        ("홍은동", "/seoul/seodaemun/hongeun-dong/"),
        ("남가좌동", "/seoul/seodaemun/namgajwa-dong/"),
        ("북가좌동", "/seoul/seodaemun/bukgajwa-dong/"),
    ]),
    ("역세권 안내", "/seoul/seodaemun/stations/", [
        ("역 전체", "/seoul/seodaemun/stations/"),
        ("홍제역", "/seoul/seodaemun/hongje-station/"),
        ("무악재역", "/seoul/seodaemun/muakjae-station/"),
        ("독립문역", "/seoul/seodaemun/dongnimmun-station/"),
        ("충정로역", "/seoul/seodaemun/chungjeongno-station/"),
        ("서대문역", "/seoul/seodaemun/seodaemun-station/"),
        ("이대역", "/seoul/seodaemun/ewha-womans-univ-station/"),
        ("신촌역", "/seoul/seodaemun/sinchon-station/"),
        ("가좌역", "/seoul/seodaemun/gajwa-station/"),
        ("아현역 인접", "/seoul/seodaemun/ahyeon-nearby-area/"),
        ("DMC역 인접", "/seoul/seodaemun/dmc-nearby-area/"),
    ]),
    ("생활권 안내", "/seoul/seodaemun/living/", [
        ("생활권 전체", "/seoul/seodaemun/living/"),
        ("신촌·연세대", "/seoul/seodaemun/sinchon-yonsei-area/"),
        ("이대·북아현", "/seoul/seodaemun/ewha-bugahyeon-area/"),
        ("홍제역·무악재", "/seoul/seodaemun/hongje-muakjae-area/"),
        ("독립문·형무소터", "/seoul/seodaemun/dongnimmun-prison-history-area/"),
        ("충정로·업무권", "/seoul/seodaemun/chungjeongno-business-area/"),
        ("연희동 주거지", "/seoul/seodaemun/yeonhui-residential-area/"),
        ("홍은동·홍제천", "/seoul/seodaemun/hongeun-hongjecheon-area/"),
        ("남가좌·명지대", "/seoul/seodaemun/namgajwa-myongji-area/"),
        ("북가좌·가좌역", "/seoul/seodaemun/bukgajwa-gajwa-area/"),
        ("안산자락길·홍제천", "/seoul/seodaemun/ansan-hongjecheon-area/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 가능 지역", "/reservation/#place"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("추가 이동비 안내", "/reservation/#move"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("예약 변경 안내", "/reservation/#change"),
        ("취소 기준 안내", "/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/precautions/", [
        ("방문 가능 주소 확인", "/precautions/#address"),
        ("자택 이용 전 확인", "/precautions/#home"),
        ("숙소 이용 전 확인", "/precautions/#stay"),
        ("사무실 인근 이용 전 확인", "/precautions/#office"),
        ("개인정보 처리 기준", "/precautions/#privacy"),
        ("고객 안전 안내", "/precautions/#safety"),
        ("불법·선정적 서비스 불가", "/precautions/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/hometai-guide/", [
        ("홈타이란?", "/hometai-guide/#what"),
        ("출장마사지와 홈타이 차이", "/hometai-guide/#diff"),
        ("이용 전 기준", "/hometai-guide/#standard"),
        ("지역별 이동 기준", "/hometai-guide/#move"),
        ("추가 비용 확인 기준", "/hometai-guide/#cost"),
        ("처음 이용하는 고객 안내", "/hometai-guide/#first"),
    ]),
    ("고객센터", "/support/", [
        ("문의하기", "/support/#contact"),
        ("자주 묻는 질문", "/support/#faq"),
        ("운영 기준", "/support/#policy"),
        ("사이트 소개", "/about/"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
