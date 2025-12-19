import streamlit as st
from PIL import Image
from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go  
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# ===================== 基础配置=====================
st.set_page_config(
    page_title="学生成绩分析与预测系统",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== 数据加载=====================
@st.cache_data
def load_data():
    df = pd.read_csv("student_data_adjusted_rounded.csv")
    # 确保数据格式正确
    for col in ["上课出勤率", "作业完成率"]:
        if df[col].max() > 1:
            df[col] = df[col] / 100
    return df

df = load_data()

# ===================== 工具函数 =====================
def load_screenshot():
    try:
        return Image.open("images/jietu.png")
    except:
        return Image.open(urlopen("https://via.placeholder.com/600x300?text=系统界面示例"))

screenshot = load_screenshot()

# ===================== 侧边栏导航 =====================
st.sidebar.title("导航菜单")
page = st.sidebar.radio(
    "选择页面",
    ["项目介绍", "专业数据分析", "成绩预测"]
)

# ===================== 项目介绍页面=====================
if page == "项目介绍":
    st.title("🎓学生成绩分析与预测系统")
    st.divider()  # 原生分割线替代<hr>

    # 核心布局
    col_left, col_right = st.columns([2, 1])

    with col_left:
        # 项目概述
        st.subheader("📋项目概述")
        st.write("""
        本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化展示学习数据，帮助教育工作者和学生深入了解学习表现，并预测期末考试成绩。
        """)
        
        # 主要特点
        st.subheader("主要特点")
        st.markdown("""
        - **📊数据可视化**：多维度展示学生学业数据
        - **📌专业分析**：各专业分维度的详细统计分析
        - **🤖智能预测**：基于机器学习模型的成绩预测
        - **💡学习建议**：根据预测结果提供个性化反馈
        """)

    # 右侧列：图片
    with col_right:
        st.image(screenshot, caption="系统界面示例", width=600) 
    
    st.divider()

    # 项目目标
    st.subheader("🚀 项目目标")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🎯 目标一：分析影响因素")
        st.markdown("""
        - 识别关键学习指标
        - 探索成绩相关因素
        - 提供数据支持决策
        """)
    with col2:
        st.markdown("### ✅ 目标二：可视化展示")
        st.markdown("""
        - 专业对比分析
        - 性别差异研究
        - 学习模式识别
        """)
    with col3:
        st.markdown("### 🔮 目标三：成绩预测")
        st.markdown("""
        - 机器学习模型
        - 个性化预测
        - 及时干预预警
        """)
    
    st.divider()

    # 技术架构
    st.subheader("🔧技术架构")
    col_tech1, col_tech2, col_tech3, col_tech4 = st.columns(4)
    with col_tech1:
        st.markdown("#### 前端框架")
        with st.info(""): 
            st.write("Streamlit")
    with col_tech2:
        st.markdown("#### 数据处理")
        with st.info(""):
            st.text('''
Pandas
NumPy''') 
    with col_tech3:
        st.markdown("#### 可视化")
        with st.info(""):
            st.text('''
Matplotlib
Plotly''')
    with col_tech4:
        st.markdown("#### 机器学习")
        with st.info(""):
            st.write("Scikit-Learn")

# ---------------------- 页面2：专业数据分析 ----------------------
elif page == "专业数据分析":
    st.title("专业数据分析")
    st.markdown("""
    基于学生数据的多维度专业对比，包含核心指标、性别比例、成绩趋势、出勤率及专项分析。
    """)
    st.markdown('***')

    # 1. 各专业核心指标表格（不变）
    st.subheader("1. 各专业核心数据统计")
    core_data = df.groupby("专业").agg({
        "每周学习时长（小时）": lambda x: round(x.mean(), 2),
        "期中考试分数": lambda x: round(x.mean(), 2),
        "期末考试分数": lambda x: round(x.mean(), 2),
        "上课出勤率": lambda x: round(x.mean() * 100, 2)
    }).reset_index()
    core_data.columns = ["专业", "每周平均学时（小时）", "期中考试平均分", "期末考试平均分", "平均上课出勤率（%）"]
    st.dataframe(core_data, use_container_width=True, hide_index=True)

    st.markdown('***')

    # 2. 各专业男女性别比例（改为Plotly交互式）
    st.subheader("2. 各专业男女性别比例")
    col_chart, col_table = st.columns([6, 4], gap="medium")
    
    with col_chart:
        gender_count = df.groupby(["专业", "性别"]).size().unstack(fill_value=0)
        if "男" not in gender_count.columns:
            gender_count["男"] = 0
        if "女" not in gender_count.columns:
            gender_count["女"] = 0
        gender_count["总人数"] = gender_count["男"] + gender_count["女"]
        gender_count["女性占比(%)"] = (gender_count["女"] / gender_count["总人数"] * 100).round(1)
        gender_count["男性占比(%)"] = (gender_count["男"] / gender_count["总人数"] * 100).round(1)
        gender_ratio_table = gender_count[["女性占比(%)", "男性占比(%)"]].reset_index()
        gender_ratio_table.columns = ["专业", "女性占比(%)", "男性占比(%)"]
        
        # Plotly交互式堆叠柱状图
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=gender_ratio_table["专业"],
            y=gender_ratio_table["女性占比(%)"],
            name="女性占比(%)",
            marker_color="#ff9999",
            hovertemplate="专业：%{x}<br>女性占比：%{y}%<extra></extra>"
        ))
        fig.add_trace(go.Bar(
            x=gender_ratio_table["专业"],
            y=gender_ratio_table["男性占比(%)"],
            name="男性占比(%)",
            marker_color="#66b3ff",
            hovertemplate="专业：%{x}<br>男性占比：%{y}%<extra></extra>"
        ))
        
        # 布局设置（支持拖拽/缩放/悬停）
        fig.update_layout(
            title="各专业男女性别占比分布",
            xaxis_title="专业",
            yaxis_title="占比(%)",
            yaxis_range=[0, 100],
            barmode="stack",
            hovermode="x unified",
            dragmode="pan",  # 默认拖拽模式
            modebar_add=["zoom", "pan", "reset", "lasso2d"],  # 显示交互工具栏
            height=400
        )
        # 显示图表
        st.plotly_chart(fig, use_container_width=True)
    
    with col_table:
        st.subheader("详细数据")
        st.dataframe(gender_ratio_table, use_container_width=True, hide_index=True)

    st.markdown('***')

    # 3. 各专业学习指标对比（核心：Plotly双Y轴交互式折线图）
    st.subheader("3. 各专业学习指标对比")
    col_chart, col_table = st.columns([6, 4], gap="medium")
    
    with col_chart:
        # 计算学习指标（保留4位小数）
        study_indicator = df.groupby("专业").agg({
            "每周学习时长（小时）": lambda x: round(x.mean(), 4),
            "期中考试分数": lambda x: round(x.mean(), 4),
            "期末考试分数": lambda x: round(x.mean(), 4)
        }).reset_index()
        study_indicator.columns = ["专业", "每周学习时长（小时）", "期中考试分数", "期末考试分数"]
        # 按指定顺序排序
        major_order = ["人工智能", "大数据管理", "工商管理", "电子商务", "财务管理"]
        study_indicator["专业"] = pd.Categorical(study_indicator["专业"], categories=major_order, ordered=True)
        study_indicator = study_indicator.sort_values("专业").reset_index(drop=True)
        
        # 创建Plotly双Y轴交互式图表（现在make_subplots已提前导入）
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # 添加期中/期末成绩折线（左侧Y轴）
        fig.add_trace(
            go.Scatter(
                x=study_indicator["专业"],
                y=study_indicator["期中考试分数"],
                name="期中考试分数",
                line=dict(color="#00008B", width=2),
                hovertemplate="专业：%{x}<br>期中分数：%{y}<extra></extra>"
            ),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(
                x=study_indicator["专业"],
                y=study_indicator["期末考试分数"],
                name="期末考试分数",
                line=dict(color="#1E90FF", width=2),
                hovertemplate="专业：%{x}<br>期末分数：%{y}<extra></extra>"
            ),
            secondary_y=False,
        )
        
        # 添加每周学习时长折线（右侧Y轴）
        fig.add_trace(
            go.Scatter(
                x=study_indicator["专业"],
                y=study_indicator["每周学习时长（小时）"],
                name="每周学习时长（小时）",
                line=dict(color="#FF0000", width=2, dash="solid"),
                marker=dict(size=8, color="#FF0000"),
                hovertemplate="专业：%{x}<br>学习时长：%{y}小时<extra></extra>"
            ),
            secondary_y=True,
        )
        
        # 布局配置（关键：开启拖拽/缩放交互）
        fig.update_layout(
            title="各专业期中期末成绩趋势",
            xaxis_title="专业",
            hovermode="x unified",
            dragmode="pan",  # 拖拽平移
            modebar_add=["zoom", "pan", "reset", "boxzoom", "lasso2d"],  # 交互工具：缩放、平移、重置、框选缩放、套索选择
            height=400,
            legend=dict(
                title="指标类型",
                orientation="v",
                yanchor="top",
                y=1,
                xanchor="right",
                x=1.2
            )
        )
        
        # 设置Y轴范围（匹配参考图）
        fig.update_yaxes(title_text="分数", range=[72, 74.5], dtick=0.5, secondary_y=False)
        fig.update_yaxes(title_text="每周学习时长（小时）", range=[20.05, 20.15], dtick=0.05, secondary_y=True)
        
        # 显示交互式图表
        st.plotly_chart(fig, use_container_width=True)
    
    with col_table:
        st.subheader("详细数据")
        table_data = study_indicator[["专业", "期中考试分数", "期末考试分数", "每周学习时长（小时）"]]
        st.dataframe(table_data, use_container_width=True, hide_index=True)

    st.markdown('***')

    # 4. 各专业平均上课出勤率（改为Plotly交互式）
    st.subheader("4. 各专业平均上课出勤率")
    col_chart, col_table = st.columns([6, 4], gap="medium")
    
    with col_chart:
        attendance_data = df.groupby("专业")["上课出勤率"].agg(lambda x: round(x.mean() * 100, 2)).reset_index()
        attendance_data = attendance_data.sort_values("上课出勤率", ascending=False).reset_index(drop=True)
        attendance_data["排名"] = attendance_data.index + 1
        attendance_data = attendance_data[["排名", "专业", "上课出勤率"]]
        attendance_data.columns = ["排名", "专业", "平均上课出勤率（%）"]
        
        # Plotly交互式柱状图
        fig = go.Figure(go.Bar(
            x=attendance_data["专业"],
            y=attendance_data["平均上课出勤率（%）"],
            marker_color="#66b3ff",
            marker_line_color="black",
            marker_line_width=1,
            hovertemplate="专业：%{x}<br>出勤率：%{y}%<br>排名：第%{customdata}名<extra></extra>",
            customdata=attendance_data["排名"]
        ))
        
        fig.update_layout(
            title="各专业平均上课出勤率排名",
            xaxis_title="专业",
            yaxis_title="平均出勤率（%）",
            yaxis_range=[0, 100],
            dragmode="pan",
            modebar_add=["zoom", "pan", "reset"],
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col_table:
        st.subheader("详细数据")
        st.dataframe(attendance_data, use_container_width=True, hide_index=True)

    st.markdown('***')

    # 5. 大数据管理专业专项分析（改为Plotly交互式）
    st.subheader("5. 大数据管理专业专项分析")
    bigdata_df = df[df["专业"] == "大数据管理"].copy()
    if not bigdata_df.empty:
        avg_attendance = round(bigdata_df["上课出勤率"].mean() * 100, 1)
        avg_final_score = round(bigdata_df["期末考试分数"].mean(), 1)
        avg_study_time = round(bigdata_df["每周学习时长（小时）"].mean(), 1)
        max_attendance = round(bigdata_df["上课出勤率"].max() * 100, 1)
        student_count = len(bigdata_df)
        
        # 核心指标卡片（原生组件+轻量化分组，无自定义CSS）
        st.subheader("大数据管理专业核心学习指标")
        col1, col2, col3, col4 = st.columns(4, gap="small")

        # 核心指标卡片（纯Streamlit原生组件，无自定义CSS）
        col1, col2, col3, col4 = st.columns(4, gap="small")

        with col1:
            st.subheader("平均上课出勤率")
            st.metric(
                label="",
                value=f"{avg_attendance}%",
                help="大数据管理专业所有学生的平均上课出勤率"
            )

        with col2:
            st.subheader("平均期末成绩")
            st.metric(
                label="",
                value=f"{avg_final_score}分",
                help="大数据管理专业所有学生的期末考试平均分"
            )

        with col3:
            st.subheader("最高出勤率")
            st.metric(
                label="",
                value=f"{max_attendance}%",
                help="大数据管理专业学生中的最高上课出勤率"
            )

        with col4:
            st.subheader("平均学习时长")
            st.metric(
                label="",
                value=f"{avg_study_time}小时",
                help="大数据管理专业所有学生每周平均学习时长"
            )        
        # 双交互式图表
        col_chart1, col_chart2 = st.columns(2, gap="medium")
        
        with col_chart1:
            # 出勤率分布交互式柱状图
            attendance_bins = [0, 70, 75, 80, 85, 90, 95, 100]
            attendance_counts = pd.cut(bigdata_df["上课出勤率"] * 100, bins=attendance_bins, include_lowest=True).value_counts().sort_index()
            
            fig = go.Figure(go.Bar(
                x=[str(interval) for interval in attendance_counts.index],
                y=attendance_counts.values,
                marker_color=["#004d26", "#006633", "#008040", "#00994d", "#00b359", "#00cc66", "#00e673"],
                hovertemplate="出勤率区间：%{x}<br>学生数量：%{y}人<extra></extra>"
            ))
            
            fig.update_layout(
                title="大数据管理专业出勤率分布",
                xaxis_title="出勤率区间(%)",
                yaxis_title="学生数量",
                dragmode="pan",
                modebar_add=["zoom", "pan", "reset"],
                height=300
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col_chart2:
            # 学习时长分布交互式折线+柱状图
            study_time_bins = [0, 5, 10, 15, 20, 25, 30, 35]
            study_time_counts = pd.cut(bigdata_df["每周学习时长（小时）"], bins=study_time_bins, include_lowest=True).value_counts().sort_index()
            
            fig = make_subplots(specs=[[{"secondary_y": False}]])
            # 柱状图
            fig.add_trace(go.Bar(
                x=[str(interval) for interval in study_time_counts.index],
                y=study_time_counts.values,
                name="学生数量",
                marker_color="#00cc66",
                opacity=0.7,
                hovertemplate="时长区间：%{x}<br>学生数量：%{y}人<extra></extra>"
            ))
            # 折线图
            fig.add_trace(go.Scatter(
                x=[str(interval) for interval in study_time_counts.index],
                y=study_time_counts.values,
                name="趋势",
                line=dict(color="#00ff99", width=2),
                marker=dict(size=6, color="#00ff99"),
                hovertemplate="时长区间：%{x}<br>学生数量：%{y}人<extra></extra>"
            ))
            
            fig.update_layout(
                title="大数据管理专业学习时长分布",
                xaxis_title="学习时长区间(小时)",
                yaxis_title="学生数量",
                dragmode="pan",
                modebar_add=["zoom", "pan", "reset"],
                height=300,
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # 折叠详情
        with st.expander("查看详细指标数据", expanded=False):
            bigdata_detail = pd.DataFrame({
                "指标名称": [
                    "学生总数", "每周平均学习时长", "期中考试平均分", 
                    "作业完成率（平均）", "出勤率中位数", "成绩中位数"
                ],
                "数值": [
                    f"{student_count}人",
                    f"{avg_study_time}小时",
                    f"{round(bigdata_df['期中考试分数'].mean(), 1)}分",
                    f"{round(bigdata_df['作业完成率'].mean() * 100, 1)}%",
                    f"{round(bigdata_df['上课出勤率'].median() * 100, 1)}%",
                    f"{round(bigdata_df['期末考试分数'].median(), 1)}分"
                ]
            })
            st.dataframe(bigdata_detail, use_container_width=True, hide_index=True)
    else:
        st.warning("当前数据中未找到「大数据管理」专业的学生数据！")

# ===================== 成绩预测页面=====================
elif page == "成绩预测":
    st.title("学生期末成绩预测")
    
    # 构建机器学习模型
    @st.cache_resource
    def train_model():
        X = df[["每周学习时长（小时）", "上课出勤率", "期中考试分数", "作业完成率"]]
        y = df["期末考试分数"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    
    model = train_model()
    
    # 用户输入
    st.markdown('###### 请输入学生的学习信息，系统将预测其期末成绩并提供学习建议')
    col1, col2, col3 = st.columns(3)
    with col1:
        student_id = st.text_input("学号")
        gender = st.selectbox("性别", ["男", "女"])
        major = st.selectbox("专业", df["专业"].unique())
    with col2:
        study_time = st.number_input(
            "每周学习时长（小时）", 
            min_value=0.0,
            max_value=40.0,
            value=10.0,
            step=0.1
        )
        attendance = st.number_input(
            "上课出勤率（%）", 
            min_value=0.0, 
            max_value=100.0, 
            value=80.0, 
            step=0.1
        ) / 100
        mid_score = st.number_input(
            "期中考试分数", 
            min_value=0.0, 
            max_value=100.0, 
            value=60.0, 
            step=0.1
        )
    with col3:
        homework_rate = st.number_input(
            "作业完成率（%）", 
            min_value=0.0, 
            max_value=100.0, 
            value=80.0, 
            step=0.1
        ) / 100
    
    # 预测按钮
    if st.button("预测期末成绩", type="primary"):
        # 输入数据处理
        input_data = pd.DataFrame({
            "每周学习时长（小时）": [study_time],
            "上课出勤率": [attendance],
            "期中考试分数": [mid_score],
            "作业完成率": [homework_rate]
        })
        pred_score = model.predict(input_data)[0].round(2)
        pred_score = max(0.0, min(pred_score, 100.0))
        
        # 展示结果
        st.subheader(f"预测期末成绩：{pred_score}分")
        col_empty, col_content, col_empty2 = st.columns([1.25, 1.5, 1.25])
        with col_content:
            if pred_score >= 60:
                st.success("恭喜！预测成绩及格~") 
                st.image("https://bpic.588ku.com/element_pic/20/10/25/52ccb88eafebfa67dd305b814663ba95.jpg", width=600)
            else:
                st.warning("需要加油哦！预测成绩暂未及格~")  
                st.image("https://k.sinaimg.cn/n/sinacn20112/489/w671h618/20190517/f745-hwzkfpu8276416.jpg/w700d1q75cms.jpg", width=600)
        
        # 个性化学习建议
        st.divider()
        st.subheader("📝 个性化学习建议")
        
        suggestions = []
        # 分数分段建议
        if pred_score >= 90:
            suggestions.append("✅ 你的学习表现非常优秀！建议保持当前学习节奏，可尝试拓展专业相关的进阶知识。")
        elif 80 <= pred_score < 90:
            suggestions.append("👍 你的成绩良好，建议针对薄弱知识点进行专项突破，进一步提升成绩上限。")
        elif 70 <= pred_score < 80:
            suggestions.append("💪 你的成绩中等偏上，建议增加每周学习时长，重点巩固课堂重点内容。")
        elif 60 <= pred_score < 70:
            suggestions.append("⚠️ 你的成绩刚过及格线，建议提高上课出勤率，按时完成所有作业，避免成绩下滑。")
        else:
            suggestions.append("🚨 你的成绩暂未及格，需要紧急调整学习计划！以下是针对性建议：")
        
        # 个性化建议
        if study_time < 8.0:
            suggestions.append(f"⏰ 当前每周学习时长仅{study_time}小时，建议至少增加到10小时以上，保证足够的学习投入。")
        if attendance < 0.8:
            suggestions.append(f"📚 上课出勤率仅{attendance*100:.1f}%，建议尽量满勤，课堂听讲是掌握知识的核心环节。")
        if mid_score < 70.0:
            suggestions.append(f"📖 期中考试分数{mid_score}分偏低，建议复盘期中错题，梳理知识漏洞并及时弥补。")
        if homework_rate < 0.9:
            suggestions.append(f"✍️ 作业完成率仅{homework_rate*100:.1f}%，建议按时完成所有作业，通过练习巩固知识点。")
        
        # 展示建议
        for idx, suggestion in enumerate(suggestions, 1):
            st.markdown(f"{idx}. {suggestion}")