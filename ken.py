import streamlit as st
import time
# ========== 核心修改：添加自定义CSS设置黑色背景 ==========
st.markdown(
    """
    <style>
    /* 整个页面背景设为黑色 */
    .stApp {
        background-color: #000000;
    }
    /* 标题、文字设为白色（保证可读性） */
    h1, h2, h3, h4, h5, h6, p, span, div, .stCaption, .stButton>button {
        color: #ffffff !important;
    }
    /* 按钮背景设为深灰色，hover时变浅 */
    .stButton>button {
        background-color: #222222 !important;
        border: none !important;
    }
    .stButton>button:hover {
        background-color: #444444 !important;
    }
    /* 滑块样式适配黑色背景 */
    .stSlider [data-baseweb="slider"] {
        color: #ffffff !important;
    }
    .stSlider [data-baseweb="slider"] > div {
        background-color: #444444 !important;
    }
    /* 音频播放器背景适配 */
    audio {
        background-color: #111111 !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1. 设置页面标题和图标
st.set_page_config(
    page_title="我的喜欢列表播放",
    page_icon="🎵",
    layout="centered"
)

# 2. 页面标题与描述
st.title("🎵 我的喜欢列表播放")
st.caption("网易云播放")

# 3. 定义音乐列表（包含封面、歌曲名、歌手、时长、音频链接）
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

# 4. 初始化session_state（保存核心状态）
if "current_music_idx" not in st.session_state:
    st.session_state.current_music_idx = 0
if "is_playing" not in st.session_state:
    st.session_state.is_playing = False
if "current_second" not in st.session_state:
    st.session_state.current_second = 0
if "progress" not in st.session_state:
    st.session_state.progress = 0
if "volume" not in st.session_state:
    st.session_state.volume = 0.7  # 默认音量70%

# 5. 获取当前播放的音乐信息
current_music = music_list[st.session_state.current_music_idx]

# 6. 核心控制逻辑
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

def update_volume():
    # 从session_state获取音量滑块值，转换为0-1范围
    st.session_state.volume = float(st.session_state.volume_slider) / 100

# 7. 布局：左侧封面，右侧歌曲信息
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

# 8. 音频播放 + 进度条 
st.markdown("---")
col_play, col_progress, col_volume = st.columns([2, 5, 0.5])

with col_play:
    # 播放/暂停按钮
    play_btn_text = "⏸ 暂停" if st.session_state.is_playing else "▶ 播放"
    st.button(play_btn_text, on_click=toggle_play, use_container_width=True)

with col_progress:
    # 嵌入HTML5音频播放器（支持代码控制）
    audio_html = f"""
    <audio id="audio-player" controls style="width:100%;" volume="{st.session_state.volume}">
        <source src="{current_music['audio_url']}" type="audio/mp3">
        您的浏览器不支持音频播放
    </audio>
    <script>
        const audio = document.getElementById('audio-player');
        audio.volume = {st.session_state.volume};  // 设置音量
        audio.currentTime = {st.session_state.current_second};  // 设置播放进度
        
        // 同步播放状态
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
            # 播放完毕自动暂停
            st.session_state.is_playing = False
            st.session_state.current_second = 0
            st.session_state.progress = 0
            st.rerun()
    
