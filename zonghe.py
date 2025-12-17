import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import time
from datetime import datetime

st.set_page_config(
    page_title="综合应用平台",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.title("首页")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📚学生阅读档案", 
    "🍰甜点推荐", 
    "🐾相册", 
    "🎵 音乐播放", 
    "⭐视频播放", 
    "🕴个人简历"
])


with tab1:
    st.header("学生阅读档案")
    st.title("学生图书阅读档案🗎")
    st.subheader("📌 基础信息")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"学生姓名: **张三**")
        st.write(f"学生学号: **22053060152**")
    with col2:
        st.write(f"注册时间: **2025-09-01 08:11**")
        st.write(f"登录状态: 正常")
    with col3:
        st.write(f"阅读情况: **良好** (安全班: 全勤)")
    st.subheader("📚阅读书库")
    skill_data = {
        "书库": ["文学类", "科普类", "生活类"],
        "图书占比": [50, 30, 20],
        "推荐阅读指数": ["↑3%", "↓2%", "↓10%"]
    }
    skill_cols = st.columns(3)
    for i in range(3):
        with skill_cols[i]:
            st.write(f"**{skill_data['书库'][i]}**")
            st.write(f"图书占比：{skill_data['图书占比'][i]}%")
            st.progress(skill_data['图书占比'][i] / 100)
            st.write(f"推荐阅读指数: {skill_data['推荐阅读指数'][i]}")

    # ---------------------- 书籍阅读模块 ----------------------
    st.subheader("📚阅读日志")
    task_data = pd.DataFrame({
        "阅读时长": ["10.1~10.22", "10.23~11.4", "11.5~1.20"],
        "书籍": ["马原", "python", "大数据"],
        "状态": ["✅ 已完成", "❌ 未完成", "🔄 进行中"],
        "深度": ["★★★★☆", "★★★★☆", "★★★☆"]
    })
    st.dataframe(
        task_data,
        hide_index=True,
        column_config={
            "状态": st.column_config.Column(
                "状态",
                help="阅读当前进度",
                width="small"
            )
        }
    )

    # ---------------------- 文章美句摘要模块 ----------------------
    st.subheader("🖆文章美句摘要")
    st.caption('摘要')
    code_content = '''
当代青年沐浴着新时代的阳光雨露，有了更好的生活条件
但肯吃苦能吃苦的优良传统不能丢!
    '''
    st.code(code_content, language="python")

    # ---------------------- 底部信息 ----------------------
    st.markdown("***")
    st.markdown(':red[温馨提示: 还书时间准备截至]')
    st.write("温馨提示: 请尽快阅读")
    st.write("还书时间: 2025.11.24")
    st.write("阅读状态: 休息ing")

with tab2:
    st.header("美食")
    
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

    # 2. 甜点店评分（柱状图）
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

    # 3. 用餐高峰时段（面积图）
    st.subheader("⏰ 用餐高峰时段")
    st.area_chart(
        peak_data,
        x="时段",
        y=["周一至周五", "周末"],
        use_container_width=True
    )

    # 4. 价格趋势（折线图）
    st.subheader("💰 不同甜品价格趋势")
    ind = pd.Series([
        '01月', '02月', '03月', '04月', '05月', '06月', 
        '07月', '08月', '09月','10月', '11月', '12月'
    ], name='月份')
    df = pd.DataFrame(data, index=ind)
    st.line_chart(df)

with tab3:
    st.header("相册")
    # 初始化图片索引
    if 'img_ind' not in st.session_state:
        st.session_state['img_ind'] = 0

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
    st.image(images[st.session_state['img_ind']]["url"], caption=images[st.session_state['img_ind']]["text"])

    # 定义切换函数
    def prevImg():
        st.session_state['img_ind'] = (st.session_state['img_ind'] - 1) % len(images)

    def nextImg():
        st.session_state['img_ind'] = (st.session_state['img_ind'] + 1) % len(images)

    # 按钮布局
    col1, col2 = st.columns(2)
    with col1:
        st.button("上一张", on_click=prevImg, use_container_width=True)
    with col2:
        st.button("下一张", on_click=nextImg, use_container_width=True)

with tab4:
    st.header("音乐播放器")
    
    # 1. 页面标题与描述
    st.title("🎵 我的喜欢列表播放")
    st.caption("网易云播放")

    # 2. 定义音乐列表
    music_list = [
        {
            "cover_url": "https://img.alicdn.com/bao/uploaded/i3/2373566687/O1CN01WH1bnz1zGhBHxrMBT_!!0-item_pic.jpg",
            "audio_url": "https://music.163.com/song/media/outer/url?id=5257138.mp3",
            "title": "Angel Baby",
            "artist": "Troye Sivan",
            "duration": "5:19",
            "total_seconds": 319
        },
        {
            "cover_url": "http://n.sinaimg.cn/sinakd20240916ac/160/w1280h1280/20240916/57ce-fb8d71c691575a5845d5053dc80e7acf.jpg",
            "audio_url": "https://music.163.com/song/media/outer/url?id=5257138.mp3",
            "title": "我成为我的同时",
            "artist": "十个勤天",
            "duration": "5:19",
            "total_seconds": 319
        },
        {
            "cover_url": "https://www.huaiyinjie.com/wp-content/uploads/2024/06/2f023fb9afbd828cbcc0684661e0fe73.jpg",
            "audio_url": "https://music.163.com/song/media/outer/url?id=5257138.mp3",
            "title": "暖一片星光",
            "artist": "卓沅",
            "duration": "5:19",
            "total_seconds": 319
        }
    ]

    # 3. 初始化session_state
    if "current_music_idx" not in st.session_state:
        st.session_state.current_music_idx = 0
    if "is_playing" not in st.session_state:
        st.session_state.is_playing = False
    if "current_second" not in st.session_state:
        st.session_state.current_second = 0
    if "progress" not in st.session_state:
        st.session_state.progress = 0
    if "volume" not in st.session_state:
        st.session_state.volume = 0.7

    # 4. 获取当前播放的音乐信息
    current_music = music_list[st.session_state.current_music_idx]

    # 5. 核心控制逻辑
    def toggle_play():
        st.session_state.is_playing = not st.session_state.is_playing

    def prev_song():
        st.session_state.current_music_idx = (st.session_state.current_music_idx - 1) % len(music_list)
        st.session_state.current_second = 0
        st.session_state.progress = 0
        st.session_state.is_playing = False

    def next_song():
        st.session_state.current_music_idx = (st.session_state.current_music_idx + 1) % len(music_list)
        st.session_state.current_second = 0
        st.session_state.progress = 0
        st.session_state.is_playing = False

    # 6. 布局：左侧封面，右侧歌曲信息
    col_cover, col_info = st.columns([1, 2])
    with col_cover:
        st.image(
            current_music["cover_url"],
            caption="专辑封面",
            use_container_width=True
        )

    with col_info:
        st.subheader(current_music["title"])
        st.write(f"歌手: {current_music['artist']}")
        st.write(f"时长: {current_music['duration']}")

        # 切歌按钮
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.button("◀◀ 上一首", on_click=prev_song, use_container_width=True)
        with btn_col2:
            st.button("▶▶ 下一首", on_click=next_song, use_container_width=True)

    # 7. 音频播放 + 进度条
    st.markdown("---")
    col_play, col_progress = st.columns([2, 5])

    with col_play:
        # 播放/暂停按钮
        play_btn_text = "⏸ 暂停" if st.session_state.is_playing else "▶ 播放"
        st.button(play_btn_text, on_click=toggle_play, use_container_width=True)

    with col_progress:
        # 嵌入HTML5音频播放器
        audio_html = f"""
        <audio id="audio-player" controls style="width:100%;" volume="{st.session_state.volume}">
            <source src="{current_music['audio_url']}" type="audio/mp3">
            您的浏览器不支持音频播放
        </audio>
        <script>
            const audio = document.getElementById('audio-player');
            audio.volume = {st.session_state.volume};
            audio.currentTime = {st.session_state.current_second};
            {'audio.play();' if st.session_state.is_playing else 'audio.pause();'}
        </script>
        """
        st.components.v1.html(audio_html, height=60)
        
        # 进度条自动更新逻辑
        if st.session_state.is_playing:
            if st.session_state.current_second < current_music["total_seconds"]:
                st.session_state.current_second += 1
                st.session_state.progress = (st.session_state.current_second / current_music["total_seconds"]) * 100
                time.sleep(1)
                st.rerun()
            else:
                st.session_state.is_playing = False
                st.session_state.current_second = 0
                st.session_state.progress = 0
                st.rerun()

with tab5:
    st.header("动画片")

    # 定义视频数据数组
    video_arr = [
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/91/14/29196421491/29196421491-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&oi=1385955528&deadline=1765774569&og=cos&trid=1677b5a5f63f4835bdac5bd895ebeccO&platform=html5&mid=0&gen=playurlv3&os=estgcos&upsig=f5de7ed516c285940c305b68e41d4efb&uparams=e,uipk,nbs,oi,deadline,og,trid,platform,mid,gen,os&bvc=vod&nettype=1&bw=738164&agrr=0&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
            'title': '第1集',
            'episode': 1
        },
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/96/96/29196619696/29196619696-1-192.mp4?e=ig8euxZM2rNcNbRV7wdVhwdlhWdMhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&os=zosbv&og=hw&nbs=1&oi=2067284620&uipk=5&platform=html5&gen=playurlv3&trid=4eddd86a48354b19b09902255a29774O&deadline=1765774596&upsig=82ca91d33e273f9925585edf1f797b53&uparams=e,mid,os,og,nbs,oi,uipk,platform,gen,trid,deadline&bvc=vod&nettype=1&bw=838374&agrr=0&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
            'title': '第2集',
            'episode': 2
        },
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/46/01/29196750146/29196750146-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=87ad3b73791241058fef0591f1e6f36O&mid=0&uipk=5&deadline=1765774616&oi=1385955528&nbs=1&gen=playurlv3&os=estgcos&og=cos&upsig=f453eb05e390b4aa724e4b6d35dbaab1&uparams=e,platform,trid,mid,uipk,deadline,oi,nbs,gen,os,og&bvc=vod&nettype=1&bw=683878&agrr=0&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
            'title': '第3集',
            'episode': 3
        },
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/96/72/29196747296/29196747296-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1765774641&nbs=1&uipk=5&trid=efbd6773c88245c8b9da4d253a12258O&platform=html5&mid=0&gen=playurlv3&os=estgoss&og=ali&oi=1385955528&upsig=bbef0dbcf843100effba19b1aeb9f0e0&uparams=e,deadline,nbs,uipk,trid,platform,mid,gen,os,og,oi&bvc=vod&nettype=1&bw=766961&f=O_0_0&agrr=0&buvid=&build=7330300&dl=0&orderid=0,3',
            'title': '第4集',
            'episode': 4
        },
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/81/24/29196812481/29196812481-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&oi=144233936&nbs=1&uipk=5&gen=playurlv3&os=08cbv&trid=8cf581b2ecd44b588e5ad975824489aO&deadline=1765774666&og=hw&platform=html5&upsig=e7ea9e91fbaa2f9f3832cf3bbbb7a3d0&uparams=e,mid,oi,nbs,uipk,gen,os,trid,deadline,og,platform&bvc=vod&nettype=1&bw=754812&dl=0&f=O_0_0&agrr=0&buvid=&build=7330300&orderid=0,3',
            'title': '第5集',
            'episode': 5
        }
    ]

    # 初始化session_state
    if 'video_ind' not in st.session_state:
        st.session_state['video_ind'] = 0

    # 获取当前选中剧集
    current_episode = video_arr[st.session_state['video_ind']]["episode"]
    st.title(f"开心超人 第{current_episode}集")

    # 播放视频
    st.video(video_arr[st.session_state['video_ind']]['url'], autoplay=True)

    # 定义切换函数
    def play(i):
        st.session_state['video_ind'] = int(i)

    # 横向排列剧集按钮
    cols = st.columns(len(video_arr))
    for i in range(len(video_arr)):
        with cols[i]:
            st.button('第' + str(i+1) + '集', use_container_width=True, on_click=play, args=([i]))

    # 简介区域
    st.markdown('***')
    st.markdown('###### 简介')
    st.text("五超人在执行任务中，意外发现体内暗藏了能控制他们的程序代码，在调查过程中，超人们发现所有的线索都指向了宇宙开发集团-五金公司。超人们为了解开谜题，踏上了寻找真相之路，五金公司的阴谋也逐渐浮出水面。原来，五金公司曾经拥有过诞生超人们的超能机械石，并试图将超人改造成为自己的武器，从而称霸宇宙。超人们得知真相后，合力摧毁了五金公司，解决了宇宙的危机。")

    st.markdown('###### 配音')
    st.text("开心超人：刘红韵 甜心超人：邓玉婷 花心超人：严彦子 粗心超人：祖晴")

with tab6:
    st.header("个人简历")
    
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
        st.image(
            "https://preview.qiantucdn.com/58pic/Hj/1b/4V/CG/rly4fas8h70deptgx3mojqk2cunvb5z6_PIC2018.png!w1024_new_0_1", 
            width=150, 
            caption=name if name else "姓名"
        )
        st.write(f"姓名：{name if name else '未填写'}")
        st.write(f"职位：{major if major else '未填写'}")
        st.write(f"电话：{phone if phone else '未填写'}")
        st.write(f"邮箱：{email if email else '未填写'}")

    with col_right_top:
        # 右边板块
        st.write(f"意向职业：{target_job if target_job else '未填写'}")
        st.write(f"性别：{gender}")
        st.write(f"出生日期：{birth_date.strftime('%Y-%m-%d')}")
        st.write(f"年龄：{age}岁")
        st.write(f"籍贯：{native_place if native_place else '未填写'}")
        st.write(f"政治面貌：{political}")
        st.write(f"学历：{edu_bg}")
        st.write(f"毕业学校：{school if school else '未填写'}")
        st.write(f"工作经验：{exp_years}年")
        st.write(f"期望薪资：{salary_exp[0]}-{salary_exp[1]}元")

    # 第二行
    st.subheader("个人简介")
    st.write(self_intro if self_intro else "请在左侧填写个人简介内容")

    st.subheader("在校经历")
    st.write(self_xixi if self_xixi else "请在左侧补充在校经历内容")

    st.subheader("专业技能")
    st.write(", ".join(skills) if skills else "请在左侧选择专业技能")
