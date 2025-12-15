# 导入streamlit库并简写为st，streamlit是用于快速构建Web应用的Python库
import streamlit as st

# 设置页面配置：页面标题为“番剧世界”，页面图标为星星⭐
st.set_page_config(page_title="番剧世界",page_icon="⭐")

# 定义视频数据数组，包含3个剧集的URL、标题、集数信息
video_arr=[
    {
    'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/91/14/29196421491/29196421491-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&oi=1385955528&deadline=1765774569&og=cos&trid=1677b5a5f63f4835bdac5bd895ebeccO&platform=html5&mid=0&gen=playurlv3&os=estgcos&upsig=f5de7ed516c285940c305b68e41d4efb&uparams=e,uipk,nbs,oi,deadline,og,trid,platform,mid,gen,os&bvc=vod&nettype=1&bw=738164&agrr=0&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',  # 第1集视频地址
    'title':'第1集',  # 第1集标题
    'episode':1  # 第1集集数标识
    },{
    'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/96/96/29196619696/29196619696-1-192.mp4?e=ig8euxZM2rNcNbRV7wdVhwdlhWdMhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&os=zosbv&og=hw&nbs=1&oi=2067284620&uipk=5&platform=html5&gen=playurlv3&trid=4eddd86a48354b19b09902255a29774O&deadline=1765774596&upsig=82ca91d33e273f9925585edf1f797b53&uparams=e,mid,os,og,nbs,oi,uipk,platform,gen,trid,deadline&bvc=vod&nettype=1&bw=838374&agrr=0&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',  # 第2集视频地址
    'title':'第2集',  # 第2集标题
    'episode':2  # 第2集集数标识
    },{
    'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/46/01/29196750146/29196750146-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=87ad3b73791241058fef0591f1e6f36O&mid=0&uipk=5&deadline=1765774616&oi=1385955528&nbs=1&gen=playurlv3&os=estgcos&og=cos&upsig=f453eb05e390b4aa724e4b6d35dbaab1&uparams=e,platform,trid,mid,uipk,deadline,oi,nbs,gen,os,og&bvc=vod&nettype=1&bw=683878&agrr=0&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',  # 第3集视频地址
    'title':'第3集',  # 第3集标题
    'episode':3  # 第3集集数标识
    },{
    'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/96/72/29196747296/29196747296-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1765774641&nbs=1&uipk=5&trid=efbd6773c88245c8b9da4d253a12258O&platform=html5&mid=0&gen=playurlv3&os=estgoss&og=ali&oi=1385955528&upsig=bbef0dbcf843100effba19b1aeb9f0e0&uparams=e,deadline,nbs,uipk,trid,platform,mid,gen,os,og,oi&bvc=vod&nettype=1&bw=766961&f=O_0_0&agrr=0&buvid=&build=7330300&dl=0&orderid=0,3',  # 第3集视频地址
    'title':'第4集',  # 第4集标题
    'episode':4  # 第4集集数标识
    },{
    'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/81/24/29196812481/29196812481-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&oi=144233936&nbs=1&uipk=5&gen=playurlv3&os=08cbv&trid=8cf581b2ecd44b588e5ad975824489aO&deadline=1765774666&og=hw&platform=html5&upsig=e7ea9e91fbaa2f9f3832cf3bbbb7a3d0&uparams=e,mid,oi,nbs,uipk,gen,os,trid,deadline,og,platform&bvc=vod&nettype=1&bw=754812&dl=0&f=O_0_0&agrr=0&buvid=&build=7330300&orderid=0,3',  # 第3集视频地址
    'title':'第5集',  # 第5集标题
    'episode':5 # 第5集集数标识
    }
    ]

# 初始化session_state：如果'ind'键不存在，设置初始值为0（默认选中第1集）
# session_state用于在Streamlit应用中保存跨交互的状态
if 'ind' not in st.session_state:
    st.session_state['ind']=0

# 获取当前选中剧集的集数：根据session_state中的'ind'索引，从video_arr中取对应episode值
current_episode = video_arr[st.session_state['ind']]["episode"]

# 设置页面标题：拼接“开心超人 第X集”，X为当前选中的集数
st.title(f"开心超人 第{current_episode}集")

# 播放当前选中剧集的视频：根据'ind'索引取对应URL，设置自动播放
st.video(video_arr[st.session_state['ind']]['url'],autoplay=True)

# 定义剧集切换函数：接收索引i，更新session_state中的'ind'为选中的索引
def play(i):
        st.session_state['ind']=int(i)

# --- 用columns将按钮排成一排 ---
# 创建与剧集数量相同的列容器（3列），用于横向排列按钮
cols = st.columns(len(video_arr))  
# 遍历剧集索引，为每个剧集创建按钮
for i in range(len(video_arr)):
    with cols[i]:  # 将按钮放入对应的列中，实现横向排列
        # 创建剧集按钮：显示“第X集”，宽度适配列容器，点击时调用play函数并传入当前索引i
        st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))

# 添加分隔线：用于视觉上分隔视频/按钮区域和简介区域
st.markdown('***')

# 添加“简介”小标题（6级标题）
st.markdown('###### 简介')

# 显示番剧简介文本
st.text("五超人在执行任务中，意外发现体内暗藏了能控制他们的程序代码，在调查过程中，超人们发现所有的线索都指向了宇宙开发集团-五金公司。超人们为了解开谜题，踏上了寻找真相之路，五金公司的阴谋也逐渐浮出水面。原来，五金公司曾经拥有过诞生超人们的超能机械石，并试图将超人改造成为自己的武器，从而称霸宇宙。超人们得知真相后，合力摧毁了五金公司，解决了宇宙的危机。")

# 添加“配音”小标题（6级标题）（此处未补充配音内容，仅创建标题）
st.markdown('###### 配音')
st.text("开心超人：刘红韵 甜心超人：邓玉婷 花心超人：严彦子 粗心超人：祖晴")

