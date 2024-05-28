import streamlit as st
import time


# 日期：2024年3月29日
# 用于限制恶意刷新，当10秒内访问次数超过3次，禁止IP

def prevent_malicious_refresh(limit_seconds=10, limit_count=3):
    if 'last_visit_time' not in st.session_state:
        st.session_state.last_visit_time = time.time()
    if 'visit_count' not in st.session_state:
        st.session_state.visit_count = 0

    if time.time() - st.session_state.last_visit_time < limit_seconds and st.session_state.visit_count >= limit_count:
        st.error("您的访问频率过高，请稍后再试。")
        st.stop()

    st.session_state.last_visit_time = time.time()
    st.session_state.visit_count += 1
