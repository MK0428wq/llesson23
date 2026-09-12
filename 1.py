import streamlit as st
import random
import time

st.title("目押しアプリ")

表示3= st.empty()
表示2 = st.empty()
表示1 = st.empty()
if st.button("1ボタン"):
    表示1= st.empty()
    表示2 = st.empty()
    表示3 = st.empty()
    for i in range(10):

        数字1 = random.randint(1, 9)
        数字2 = random.randint(1, 9)
        数字3 = random.randint(1, 9)

        表示1= st.write()
        表示2 = st.write()
        表示3 = st.write()

        time.sleep(0.05)

        表示1= st.empty()
        表示2 = st.empty()
        表示3 = st.empty()


#         数字=random.randint(1,9)
#         表示3.write(数字)
#         # st.write(数字)
#         time.sleep(0.05)
#         表示3.empty()
#         # st.write(数字)
#         time.sleep(0.05)

#     for i in range(10):
#         字=random.randint(1,9)
#         表示2.write(字)
#         time.sleep(0.05)
#         # st.write(数字)
#         表示2.empty()
#         time.sleep(0.05) 

#     for i in range(10):
#         数=random.randint(1,9)
#         表示1.write(数)
#       # st.write(数字)
#         time.sleep(0.05)
#         表示1.empty()
#         time.sleep(0.05)
#         # 表示.empty()
#         # # 字=random.randint(1,9)
#         # 表示.write(数字)

#         # # st.write(字)

#         # time.sleep(0.05)
#         # 表示.empty()
#         # # 数=random.randint(1,9)
#         # 表示.write(数字)

#         # # st.write(数)
#         # time.sleep(0.05)
#         # 表示.empty()
st.button("STOP")