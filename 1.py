import streamlit as st
import random
import time

st.title("目押しアプリ")
st.write("目押しとは、スロットマシーンなどのゲーム。")

表示 = st.empty()

if st.button("始める"):
    for i in range(10):
        数字=random.randint(1,9)
        time.sleep(0.05)
        表示.write(数字)
        # st.write(数字)
        time.sleep(0.05)
    for i in range(10):
        字=random.randint(1,9)
        time.sleep(0.05)
        表示.write(字)
        # st.write(数字)
    for i in range(10):
        time.sleep(0.05)
        数=random.randint(1,9)
        time.sleep(0.05)
        表示.write(数)
        # st.write(数字)

    time.sleep(0.05)
        # 表示.empty()
        # # 字=random.randint(1,9)
        # 表示.write(数字)

        # # st.write(字)

        # time.sleep(0.05)
        # 表示.empty()
        # # 数=random.randint(1,9)
        # 表示.write(数字)

        # # st.write(数)
        # time.sleep(0.05)
        # 表示.empty()
st.button("STOP")