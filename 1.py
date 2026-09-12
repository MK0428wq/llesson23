import streamlit as st
import random
import time

st.title("目押しアプリ")
st.write("目押しとは、スロットマシーンなどのゲーム。")

if st.button("始める"):
        数字=random.randint(1,9)
        st.write(数字)
        time.sleep(0.5)
        字=random.randint(1,9)
        st.write(字)
        time.sleep(0.5)
        数=random.randint(1,9)
        st.write(数)
        time.sleep(0.5)
st.button("STOP")