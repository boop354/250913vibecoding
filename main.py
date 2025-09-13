import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("🌍 MBTI 유형별 비율이 가장 높은 국가 Top 10")

# 기본 CSV 경로
default_path = "countriesMBTI_16types.csv"

# CSV 불러오기 함수
def load_data():
    if os.path.exists(default_path):
        return pd.read_csv(default_path)
    else:
        uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
        if uploaded_file is not None:
            return pd.read_csv(uploaded_file)
        else:
            return None

# 데이터 불러오기
df = load_data()

if df is not None:
    # MBTI 유형 리스트 (Country 제외)
    mbti_types = df.columns[1:].tolist()

    # MBTI 유형 선택
    selected_type = st.selectbox("MBTI 유형을 선택하세요", mbti_types)

    # 선택된 유형 기준으로 Top 10 국가 추출
    top10 = df.nlargest(10, selected_type)[["Country", selected_type]]

    # Altair 차트 생성
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_type, title="비율", scale=alt.Scale(domain=[0, top10[selected_type].max()*1.1])),
            y=alt.Y("Country", sort="-x"),
            tooltip=["Country", selected_type],
            color=alt.Color("Country", legend=None)
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.info("기본 CSV 파일이 없으면, 파일을 업로드하세요.")
