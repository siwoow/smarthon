
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="흡연자 탐지 시스템",
    page_icon="🚭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 스타일 설정
st.markdown("""
    <style>
    .main {
        background-color: #2B2D42;
        color: white;
    }
    .stButton>button {
        background-color: #EF233C;
        color: white;
    }
    .stTextInput>div>input {
        background-color: #EDF2F4;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align: center; color: white;'>흡연자 탐지 시스템</h1>", unsafe_allow_html=True)

# 컬럼 설정
col1, col2 = st.columns([1, 2])

# 탐지 결과 영역
with col1:
    st.markdown("<h2 style='text-align: center; color: white;'>탐지 결과</h2>", unsafe_allow_html=True)
    st.write("탐지된 결과가 여기에 표시됩니다.")

# 탐지된 이미지 영역
with col2:
    st.markdown("<h2 style='text-align: center; color: white;'>탐지된 이미지</h2>", unsafe_allow_html=True)
    st.write("탐지된 이미지가 여기에 표시됩니다.")
