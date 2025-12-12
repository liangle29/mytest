import streamlit as st

# 格式标签页的文字和图标
st.set_page_config(page_title="猫和老鼠动画合集", page_icon="🐾")

st.title("动画合集")

# 初始化图片索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

images = [
    {
        'url': "http://puui.qpic.cn/vpic_cover/r0925dw1a8b/r0925dw1a8b_hz.jpg",
        'text': '情敌'
    },
    {
        'url': "https://puui.qpic.cn/vpic_cover/b3353ubb1ho/b3353ubb1ho_hz.jpg",
        'text': '杰瑞'
    },
    {
        'url': "https://pic2.zhimg.com/v2-8a7c81a6869ba579acbfa575d792627f_r.jpg",
        'text': '汤姆杰瑞'
    }
]

# 显示当前图片
st.image(images[st.session_state['ind']]["url"], caption=images[st.session_state['ind']]["text"])

# 定义“上下一张”的函数
def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

# 按钮布局
col1, col2 = st.columns(2)
with col1:
    st.button("上一张", on_click=prevImg, use_container_width=True)
with col2:
    st.button("下一张", on_click=nextImg, use_container_width=True)
