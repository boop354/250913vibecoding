# streamlit_character_style_recommender.py
# Streamlit app: 캐릭터를 누르면 그에 맞는 옷 스타일을 추천해주는 사이트
# 사용법: streamlit run streamlit_character_style_recommender.py

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Character Style Recommender", layout="wide")

# --- 데이터 정의 ---
CHARACTERS = {
    "🌸 소녀 (Youth)": {
        "description": "발랄하고 루즈한 스트리트 캐주얼을 좋아하는 소녀 스타일",
        "styles": [
            {"occasion": "일상", "season": "봄/가을", "items": ["오버사이즈 후드", "데님 스커트", "하이탑 스니커즈", "미니 백"]},
            {"occasion": "데이트", "season": "여름", "items": ["플로럴 미니 원피스", "웨지 샌들", "라탄 백"]},
        ],
    },
    "🕴️ 어른 (Business Casual)": {
        "description": "단정하고 세련된 비즈니스 캐주얼",
        "styles": [
            {"occasion": "출근", "season": "사계절", "items": ["블레이저", "테이퍼드 슬랙스", "옥스포드 구두", "미니멀 토트백"]},
            {"occasion": "회의/프레젠테이션", "season": "사계절", "items": ["셔츠 + 니트 베스트", "슬림 스커트", "심플 힐"]},
        ],
    },
    "🏃 스포츠형 (Sporty)": {
        "description": "활동적인 라이프스타일을 위한 애슬레저 룩",
        "styles": [
            {"occasion": "운동/산책", "season": "사계절", "items": ["테크 니트 탑", "레깅스", "러닝화", "스냅백"]},
            {"occasion": "캐주얼 외출", "season": "여름", "items": ["트랙 재킷", "쇼츠", "슬라이드 샌들"]},
        ],
    },
    "👗 우아한 (Elegant)": {
        "description": "우아하고 클래식한 분위기의 페미닌 룩",
        "styles": [
            {"occasion": "파티/행사", "season": "가을/겨울", "items": ["실크 드레스", "클래식 펌프스", "클러치 백", "진주 액세서리"]},
            {"occasion": "저녁 데이트", "season": "봄/여름", "items": ["랩 원피스", "스트랩 힐", "미니멀 주얼리"]},
        ],
    },
    "🌿 보헤미안 (Boho)": {
        "description": "자유롭고 내추럴한 보헤미안 무드",
        "styles": [
            {"occasion": "페스티벌", "season": "여름", "items": ["맥시 스커트", "오프숄더 톱", "샌들", "프린지 백"]},
            {"occasion": "카페 데이", "season": "봄/가을", "items": ["니트 가디건", "와이드 팬츠", "레더 샌들"]},
        ],
    },
}

# 색상 팔레트 생성 (간단한 시각화용 이미지)
def make_color_strip(colors, size=(400, 60)):
    img = Image.new('RGB', size)
    draw = ImageDraw.Draw(img)
    w = size[0] // len(colors)
    for i, c in enumerate(colors):
        draw.rectangle([i*w, 0, (i+1)*w, size[1]], fill=c)
    return img

# 추천 결과 렌더링
def render_recommendation(character_key):
    data = CHARACTERS[character_key]
    st.subheader(character_key)
    st.write(data['description'])

    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("**추천 스타일 목록**")
        for s in data['styles']:
            with st.expander(f"{s['occasion']} — {s['season']}"):
                st.write("• " + "  \n• ".join(s['items']))
                # 간단한 스타일 팁
                if s['occasion'] == '출근':
                    st.info("팁: 포인트 액세서리는 단정함을 유지하면서 개인의 취향을 드러냅니다.")
                if s['occasion'] == '데이트':
                    st.success("팁: 부드러운 텍스처(실크, 벨벳)가 로맨틱한 분위기를 살려줍니다.")

    with col2:
        st.markdown("**컬러 팔레트 예시**")
        # 계절에 따라 팔레트 다르게 (예시)
        pal = ['#d6e8ff', '#9fc5ff', '#2b7fff', '#112f6b']
        img = make_color_strip(pal, size=(320,60))
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        st.image(buf)

        st.markdown("**아이템 체크리스트 다운로드**")
        # 간단한 텍스트 파일로 저장
        checklist = "\n".join([f"- {item}" for s in data['styles'] for item in s['items']])
        st.download_button("체크리스트 다운로드 (.txt)", data=checklist, file_name=f"{character_key}_checklist.txt")

# 메인 레이아웃
st.title("캐릭터별 옷 스타일 추천기")
st.write("원하는 캐릭터를 골라서 그에 맞는 옷 스타일과 아이템을 확인하세요.")

# 캐릭터 선택 UI: 컬럼으로 나눠서 버튼을 보여주기
chars = list(CHARACTERS.keys())
cols = st.columns(len(chars))
for i, ch in enumerate(chars):
    with cols[i]:
        # 버튼 대신 이미지를 사용하고 싶다면 여기에 이미지를 넣을 수 있음
        if st.button(ch, key=f"btn_{i}"):
            st.session_state['selected'] = ch

# 선택 초기값
if 'selected' not in st.session_state:
    st.session_state['selected'] = chars[0]

# 선택된 캐릭터 렌더
render_recommendation(st.session_state['selected'])

# 추가 기능: 계절 / 상황 필터
st.sidebar.header("필터")
season = st.sidebar.selectbox("계절", ['모두', '봄/가을', '여름', '가을/겨울', '사계절'])
occasion = st.sidebar.selectbox("상황", ['모두', '일상', '데이트', '출근', '운동/산책', '파티/행사', '캐주얼 외출'])

if st.sidebar.button("필터 적용"):
    # 필터링된 결과를 단순하게 표시
    st.sidebar.markdown("---")
    st.sidebar.markdown("**필터 결과 미리보기**")
    for k, v in CHARACTERS.items():
        matched = []
        for s in v['styles']:
            if (season == '모두' or season in s['season']) and (occasion == '모두' or occasion == s['occasion']):
                matched.append(f"{k}: {s['occasion']} — {s['season']}")
        if matched:
            for m in matched:
                st.sidebar.write(m)

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ — 원하는 캐릭터나 스타일을 추가해 달라고 알려주세요!")
