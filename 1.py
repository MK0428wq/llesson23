import streamlit as st
import random


st.title("目押しアプリ")
st.write("目押しとは、スロットマシーンなどのゲーム。")

if st.button("始める"):
    数字=random.randint(1,9)
    for i in range(1, 4):
        st.write(数字)




st.button("STOP")



