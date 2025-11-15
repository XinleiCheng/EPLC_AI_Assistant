import streamlit as st

def set_page(page):
    st.session_state['page'] = page

if 'page' not in st.session_state:
    st.session_state['page'] = 'welcome'

# --- GLOBAL STYLES ---
st.markdown("""
    <style>
    /* Hide main menu (hamburger), footer, and top black header */
    [data-testid="stHeader"] {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #fff !important;
    }
    .sidebar-title {
        color: #2356C5 !important;
        font-weight: 700;
        margin-bottom: 2.5rem;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #F8F9FA !important;
    }
    /* 隐藏所有streamlit按钮的默认样式 */
    .stButton > button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 根据页面决定是否隐藏侧边栏
if st.session_state['page'] == 'welcome':
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
        </style>
        """, unsafe_allow_html=True)

# --- BUTTON COLOR DEFINITIONS ---
nav_active_bg = "#2356C5"
nav_active_text = "#E3ECFD"
nav_inactive_bg = "#E3ECFD"
nav_inactive_text = "#2356C5"

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 class='sidebar-title'>EPLC Assistant</h2>", unsafe_allow_html=True)
    page_now = st.session_state['page']
    ask_active = page_now == 'question'
    doc_active = page_now == 'document'

    # "Ask a Question" navigation button
    if st.button("Ask a Question", key="sidebar_ask"):
        set_page('question')
    st.markdown(f"""
        <style>
          button[data-testid="baseButton-sidebar_ask"] {{
            width: 100% !important;
            background-color: {nav_active_bg if ask_active else nav_inactive_bg};
            color: {nav_active_text if ask_active else nav_inactive_text};
            font-weight:600;
            border-radius:8px;
            height:44px;
            margin-bottom:14px;
            border:none;
            transition: background 0.2s, color 0.2s;
          }}
        </style>
    """, unsafe_allow_html=True)

    # "Create a Document" navigation button
    if st.button("Create a Document", key="sidebar_doc"):
        set_page('document')
    st.markdown(f"""
        <style>
          button[data-testid="baseButton-sidebar_doc"] {{
            width: 100% !important;
            background-color: {nav_active_bg if doc_active else nav_inactive_bg};
            color: {nav_active_text if doc_active else nav_inactive_text};
            font-weight:600;
            border-radius:8px;
            height:44px;
            margin-bottom:24px;
            border:none;
            transition: background 0.2s, color 0.2s;
          }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("---", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("Help", "https://your-help-link.com")
    with col2:
        st.markdown(
            """
            <a href="https://github.com/XinleiCheng/QMSS_IBM_Practicum_2025Fall" target="_blank">
                <button style="
                    width:100%;height:36px;border:none;border-radius:8px;
                    background-color:#E3ECFD;color:#2356C5;
                    font-weight:600;font-size:15px;cursor:pointer;">
                    GitHub
                </button>
            </a>
            """, unsafe_allow_html=True
        )

# --- MAIN PAGE LOGIC ---
if st.session_state['page'] == 'welcome':

    # 欢迎页面 - 完全按照设计图
    
    # ONLY welcome page removes side padding
    st.markdown("""
        <style>
        .block-container {
            padding-left: 0 !important;
            padding-right: 0 !important;
            max-width: 100% !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align:center; margin-top: 180px;'>
            <h1 style='font-size: 48px; font-weight: 700; color: #000; margin-top: -80px;   margin-bottom: 0 px;'>
                  EPLC Assistant
            </h1>
            <p style='font-size: 25px; font-weight: 600; color: #000; margin-top: 0px; margin-bottom: 60px;'>
                Empowering IT Project Managers with<br>smarter, faster documentation.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    
    # 两个主按钮
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        btn_col1, btn_col2 = st.columns([1.5, 1.5])  # 让“Create a Document →”更宽
        with btn_col1:
            if st.button("Ask a Question →", key="welcome_ask"):
                set_page('question')
        with btn_col2:
            if st.button("Create a Document →", key="welcome_doc"):
                set_page('document')
    
    # 按钮样式
    st.markdown("""
    <style>
    /* welcome 页按钮统一样式 */
    .stButton > button {
        background-color: #0D6EFD;
        color: #FFFFFF;
        font-size: 20px;
        font-weight: 700;
        border-radius: 999px;
        height: 52px;
        padding: 0 32px;
        border: none;
        box-shadow: 0 6px 14px rgba(37, 99, 235, 0.35);
        transition: all 0.15s ease;
        white-space: nowrap;     /* 不允许文字换行 */
        min-width: 200px;        /* 给按钮一个最小宽度，保证内容放得下 */
    }

    .stButton > button:hover {
        background-color: #1D4DB3;
        box-shadow: 0 8px 18px rgba(37, 99, 235, 0.45);
    }
    </style>
    """, unsafe_allow_html=True)



    
    # 底部链接
    st.markdown("""
        <div style='text-align: center; margin-top: 80px;'>
            <a href='#' style='color: #000; text-decoration: none; margin: 0 20px; font-size: 18px;'>
                <svg width="25" height="25" style="margin-right: 8px;" viewBox="0 0 400 400" fill="#000">
                    <path d="M199.996,0C89.719,0,0,89.72,0,200c0,110.279,89.719,200,199.996,200C310.281,400,400,310.279,400,200 C400,89.72,310.281,0,199.996,0z M199.996,373.77C104.187,373.77,26.23,295.816,26.23,200 c0-95.817,77.957-173.769,173.766-173.769c95.816,0,173.772,77.953,173.772,173.769 C373.769,295.816,295.812,373.77,199.996,373.77z"></path>
                    <path d="M199.996,91.382c-35.176,0-63.789,28.616-63.789,63.793c0,7.243,5.871,13.115,13.113,13.115 c7.246,0,13.117-5.873,13.117-13.115c0-20.71,16.848-37.562,37.559-37.562c20.719,0,37.566,16.852,37.566,37.562 c0,20.714-16.849,37.566-37.566,37.566c-7.242,0-13.113,5.873-13.113,13.114v45.684c0,7.243,5.871,13.115,13.113,13.115 s13.117-5.872,13.117-13.115v-33.938c28.905-6.064,50.68-31.746,50.68-62.427C263.793,119.998,235.176,91.382,199.996,91.382z"></path>
                    <path d="M200.004,273.738c-9.086,0-16.465,7.371-16.465,16.462s7.379,16.465,16.465,16.465c9.094,0,16.457-7.374,16.457-16.465 S209.098,273.738,200.004,273.738z"></path>
                    </svg>
                </span> Help
            </a>
            <a href='https://github.com/XinleiCheng/QMSS_IBM_Practicum_2025Fall' target='_blank' 
               style='color: #000; text-decoration: none; margin: 0 20px; font-size: 18px;'>
                <svg width="30" height="30" style="margin-right: 8px;" viewBox="0 0 30 30">
                        <path d="M15,3C8.373,3,3,8.373,3,15c0,5.623,3.872,10.328,9.092,11.63C12.036,26.468,12,26.28,12,26.047v-2.051 c-0.487,0-1.303,0-1.508,0c-0.821,0-1.551-0.353-1.905-1.009c-0.393-0.729-0.461-1.844-1.435-2.526 c-0.289-0.227-0.069-0.486,0.264-0.451c0.615,0.174,1.125,0.596,1.605,1.222c0.478,0.627,0.703,0.769,1.596,0.769 c0.433,0,1.081-0.025,1.691-0.121c0.328-0.833,0.895-1.6,1.588-1.962c-3.996-0.411-5.903-2.399-5.903-5.098 c0-1.162,0.495-2.286,1.336-3.233C9.053,10.647,8.706,8.73,9.435,8c1.798,0,2.885,1.166,3.146,1.481C13.477,9.174,14.461,9,15.495,9 c1.036,0,2.024,0.174,2.922,0.483C18.675,9.17,19.763,8,21.565,8c0.732,0.731,0.381,2.656,0.102,3.594 c0.836,0.945,1.328,2.066,1.328,3.226c0,2.697-1.904,4.684-5.894,5.097C18.199,20.49,19,22.1,19,23.313v2.734 c0,0.104-0.023,0.179-0.035,0.268C23.641,24.676,27,20.236,27,15C27,8.373,21.627,3,15,3z"></path>
                    </svg>
                </span> GitHub
            </a>
        </div>
        """, unsafe_allow_html=True
    )

elif st.session_state['page'] == 'question':
    st.markdown("""
        <div style='text-align:center;margin-top:100px;'>
            <h2 style='font-weight:700;margin-bottom:32px;color:#2356C5;'>Try Asking...</h2>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown("""
        <div style='text-align:center; margin-bottom:20px;'>
            <button style='background-color:#EEF1F8; color:#2356C5; border:none; border-radius:18px; padding:7px 19px; margin-right:10px; font-size:15px;'>What is the EPLC Initial Phase?</button>
            <button style='background-color:#EEF1F8; color:#2356C5; border:none; border-radius:18px; padding:7px 19px; margin-right:10px; font-size:15px;'>Show me a CDC UP template for planning.</button>
            <button style='background-color:#EEF1F8; color:#2356C5; border:none; border-radius:18px; padding:7px 19px; font-size:15px;'>Explain the difference between initiation and planning phases.</button>
        </div>
        <div style='text-align:center;'>
            <input type='text' style='width:380px;height:38px;border-radius:8px;border:1px solid #dee2e6;font-size:16px;padding-left:12px;color:#2356C5;background:#fff;' placeholder='Type your question here...'>
            <button style='background-color:#2356C5; color:#E3ECFD;border:none;border-radius:7px;height:38px;width:34px;font-size:18px;font-weight:600;margin-left:12px;'>&uarr;</button>
        </div>
        """, unsafe_allow_html=True
    )

elif st.session_state['page'] == 'document':
    st.markdown("""
        <div style='text-align:center;margin-top:80px;'>
            <h3 style='font-weight:700; margin-bottom:34px;color:#2356C5;'>Which Phase are you in?</h3>
            <div style='display:flex;justify-content:center;flex-wrap:wrap;gap:18px;'>
                <button style='background-color:#FFF; color:#2356C5; border:none; border-radius:18px; padding:10px 34px; font-size:15px;margin-right:15px; box-shadow:0px 2px 6px rgba(0,0,0,0.08);'>Design</button>
                <button style='background-color:#FFF; color:#2356C5; border:none; border-radius:18px; padding:10px 34px; font-size:15px;margin-right:15px; box-shadow:0px 2px 6px rgba(0,0,0,0.08);'>Development</button>
                <button style='background-color:#FFF; color:#2356C5; border:none; border-radius:18px; padding:10px 34px; font-size:15px;margin-right:15px; box-shadow:0px 2px 6px rgba(0,0,0,0.08);'>Implementation</button>
                <button style='background-color:#FFF; color:#2356C5; border:none; border-radius:18px; padding:10px 34px; font-size:15px; box-shadow:0px 2px 6px rgba(0,0,0,0.08);'>Requirement</button>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
