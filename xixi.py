import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px  
from PIL import Image

# ---------------------- 页面配置 ----------------------
st.set_page_config(
    page_title="甜点店评价",
    page_icon="🍰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 粉色主题（统一所有图表边框样式）
st.markdown("""
    <style>
    /* 页面整体背景：柔和的粉色 */
    .stApp {
        background-color: #FFE6F2;
        color: #D81B60;
    }
    /* 数据卡片设置：边框稍深的粉色，带圆角 */
    .stMetric {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #F06292;
    }
    /* 标题文字颜色加深*/
    h1, h2, h3, h4 {
        color: #C2185B !important;
        font-weight: bold !important;
    }
    /* 按钮/交互组件hover效果 */
    button:hover {
        background-color: #F8BBD0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- 模拟数据 ----------------------
# 1. 地图数据
map_data = pd.DataFrame({
    "lat": [22.830670, 22.813848, 22.850004,22.849213,22.813348],
    "lon": [108.197466, 108.321465, 108.238748,108.270221,108.197466],
    "name": ["都市甜心(相思湖店)", "赵记传承", "李饱饱·新鲜手作甜品(民大店)","喜三德","DEMO黛慕蛋糕(三街两巷店)"]
})

# 2. 餐厅评分数据
rating_data = pd.DataFrame({
    "五大维度": ["口味", "环境", "服务", "性价比", "食材"],
    "具体评分": [4.5, 4.9, 4.2, 4.0, 4.3],
    "满分": [5, 5, 5, 5, 5]
})


# 3. 用餐高峰时段数据
peak_data = pd.DataFrame({
    "时段": ["09:00", "10:00", "12:00", "14:00", "16:00", "19:00", "20:00"],
    "周一至周五": [20, 30, 80, 40, 30, 70, 50],
    "周末": [10, 35, 90, 60, 40, 70, 85]
})

# 4. 不同甜品店价格
data={
    '提拉米苏': [27, 22, 17, 12, 17, 22, 27, 25, 20, 18, 16, 15],
    '甜甜圈': [15, 10, 15, 20, 25, 20, 15, 10, 5, 12, 15, 14],
    '慕斯蛋糕': [22, 16, 10, 5, 12, 18, 22, 29, 35, 22, 15,6],
    '舒芙蕾': [6, 12, 16, 22, 25, 28, 30, 25, 22, 16, 12, 6],
    '榴莲千层': [35, 33, 34, 35, 20, 10, 19, 25, 30, 35, 38, 35]
}


# ---------------------- 页面内容 ----------------------
# 1. 地图展示
st.subheader("📍 今日5家甜品店分布")
st.map(map_data, zoom=12)

# 2. 甜点店评分（柱状图）- 保持原样式
st.subheader("⭐ 赵记传承店甜品评分")
fig_rating = px.bar(
    rating_data,
    x="五大维度",
    y="具体评分",
    title="赵记传承各维度评分（5分）",
    color="五大维度",
    color_discrete_sequence=["#FF80AB", "#F48FB1", "#F06292", "#EC407A", "#FFB6C1"],
    text="具体评分",
    height=400
)
fig_rating.update_layout(
    plot_bgcolor='white',
    font=dict(size=12, color="#C2185B"),
    title=dict(font=dict(size=16, weight="bold")),
    yaxis=dict(range=[0, 5], gridcolor='#f8bbd0'),
    showlegend=False,
    margin=dict(l=10, r=10, t=30, b=10)
)
fig_rating.update_traces(
    textfont=dict(size=12, weight='bold', color="#C2185B"),
    marker=dict(line=dict(color='#C2185B', width=1.5), opacity=0.9),
    hovertemplate='<b>%{x}</b><br>评分：%{y}/5<extra></extra>'
)
st.plotly_chart(fig_rating, use_container_width=True)

# 3. 用餐高峰时段（面积图）- 移除边框容器
st.subheader("⏰ 用餐高峰时段")
st.area_chart(
    peak_data,
    x="时段",
    y=["周一至周五", "周末"],
    use_container_width=True
)

# 4. 价格趋势（折线图）- 移除边框容器
st.subheader("💰 不同甜品价格趋势")
ind=pd.Series(['01月', '02月', '03月', 
     '04月', '05月', '06月', '07月', '08月', '09月','10月', '11月', '12月',],
    name='月份')
df=pd.DataFrame(data,index=ind)
st.line_chart(df)
