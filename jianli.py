import streamlit as st
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="🕴︎个人简历",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义深色样式（调整卡片布局）
st.markdown("""
    <style>
    /* 全局样式 */
    .stApp {background-color: #121212 !important; color: #E0E0E0 !important;}
    
    /* 侧边栏样式 */
    .css-1d391kg {background-color: #E8F4FD !important; padding-top: 20px !important;}
    
    /* 输入框样式 */
    .css-1cpxqw2, .css-1x8cf1d, .css-1v0mbdj, .css-1lcbmhc {
        background-color: #2D2D2D !important; border-radius: 4px !important;
        padding: 8px !important; margin-bottom: 12px !important; color: #E0E0E0 !important;
    }
    /* 简历卡片样式：放大+内边距增加 */
    .resume-card {
        background-color: #1E1E1E !important; border-radius: 8px !important;
        padding: 30px !important; 
        margin-bottom: 20px !important;
        width: 100% !important;
    }
    /* 卡片内容：垂直居中+文字左对齐 */
    .card-content {
        height: 450px !important; /* 适配新增字段的高度 */
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important; /* 垂直居中 */
        text-align: left !important; /* 文字左对齐 */
    }
    /* 按钮样式 */
    .css-1n543e5 {background-color: #3B82F6 !important; color: white !important; border-radius: 4px !important;}
    
    /* 链接样式 */
    a {color: #3B82F6 !important;}
    </style>
""", unsafe_allow_html=True)

# 左侧表单
with st.sidebar:
    st.markdown('<h1>个人信息表单</h1>', unsafe_allow_html=True)
    name = st.text_input("姓名", placeholder="请输入姓名")
    gender = st.selectbox("性别", ["男", "女", "其他"])
    birth_date = st.date_input("出生日期", value=datetime(2013, 1, 1))
    age = datetime.now().year - birth_date.year
    phone = st.text_input("电话", placeholder="请输入手机号")
    email = st.text_input("邮箱", placeholder="请输入邮箱")
    political = st.selectbox("政治面貌", ["中共党员","中共预备党员",  "团员", "群众"])
    edu_bg = st.selectbox("学历", ["本科", "专科", "硕士", "博士"])
    school = st.text_input("毕业学校", placeholder="请输入毕业学校")
    native_place = st.text_input("籍贯", placeholder="请输入籍贯")
    major = st.text_input("专业", placeholder="请输入专业")
    target_job = st.text_input("意向职业", placeholder="请输入意向职业")
    exp_years = st.slider("工作经验（年）", 0, 10, 3)
    salary_exp = st.slider("期望薪资（元）", 3000, 20000, (5000, 8000))
    self_intro = st.text_area("个人简介", placeholder="请输入个人简介内容", height=100)
    self_xixi = st.text_area("在校经历", placeholder="请输入个人在校经历", height=100)
    skills = st.multiselect("专业技能", ["HTML", "CSS", "Python", "Streamlit", "其他"])
    upload_resume = st.file_uploader("上传简历", type=["pdf", "docx", "png", "jpg"])
    st.download_button("下载简历", data=b"", file_name="我的简历.pdf", mime="application/pdf")

# 右侧布局
st.title("我的个人信息")
# 第一行：左侧（头像+信息1）+ 右侧（信息2）
col_left_top, col_right_top = st.columns([1.5, 1.5])

with col_left_top:
 # 左边板块
    st.image("https://preview.qiantucdn.com/58pic/Hj/1b/4V/CG/rly4fas8h70deptgx3mojqk2cunvb5z6_PIC2018.png!w1024_new_0_1", width=150, caption=name if name else "姓名")
    st.markdown(f"""
    <div class="resume-card">
        <p>姓名：{name if name else "未填写"}</p>
        <p>职位：{major if major else "未填写"}</p>
        <p>电话：{phone if phone else "未填写"}</p>
        <p>邮箱：{email if email else "未填写"}</p>
    </div>
    """, unsafe_allow_html=True)

with col_right_top:
    # 右边板块
    st.markdown(f"""
    <div class="resume-card card-content">
        <p>意向职业：{target_job if target_job else "未填写"}</p>
        <p>性别：{gender}</p>
        <p>出生日期：{birth_date.strftime("%Y-%m-%d")}</p>
        <p>年龄：{age}岁</p>
        <p>籍贯：{native_place if native_place else "未填写"}</p>
        <p>政治面貌：{political}</p>
        <p>学历：{edu_bg}</p>
        <p>毕业学校：{school if school else "未填写"}</p>
        <p>工作经验：{exp_years}年</p>
        <p>期望薪资：{salary_exp[0]}-{salary_exp[1]}元</p>
    </div>
    """, unsafe_allow_html=True)

# 第二行
st.subheader("个人简介")
st.markdown(f"""
<div class="resume-card">
    {self_intro if self_intro else "请在左侧填写个人简介内容"}
</div>
""", unsafe_allow_html=True)

st.subheader("在校经历")
st.markdown(f"""
<div class="resume-card">
    {self_xixi if self_xixi else "请在左侧补充在校经历内容"}
</div>
""", unsafe_allow_html=True)

st.subheader("专业技能")
st.markdown(f"""
<div class="resume-card">
    {", ".join(skills) if skills else "请在左侧选择专业技能"}
</div>
""", unsafe_allow_html=True)