import streamlit as st
import random
import time

st.title("スロットゲーム")

# レベル
if "レベル" not in st.session_state:
    st.session_state.レベル = 1

st.write("レベル", st.session_state.レベル)

if st.button("始める"):

    # レベルによって数字の数を決める
    個数 = st.session_state.レベル * 3

    表示 = []

    # 数字を表示する場所を作る
    for i in range(個数):
        表示.append(st.empty())

    # 数字を動かす
    for i in range(20):

        数字 = []

        for j in range(個数):
            数字.append(random.randint(1, 9))

        # 数字を表示
        for j in range(個数):
            表示[j].write(数字[j])

        time.sleep(0.05)

    # 全部同じか確認
    if len(set(数字)) == 1:

        st.balloons()
        st.success("🎉 そろいました！")

        # レベルアップ
        st.session_state.レベル += 1

        st.write("レベルアップ！")
        st.write("次は", st.session_state.レベル * 3, "個です！")

    else:
        st.write("そろいませんでした")



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
