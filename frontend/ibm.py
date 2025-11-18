import streamlit as st

# 页面配置
st.set_page_config(
    page_title="EPLC Assistant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    /* 侧边栏样式 */
    .sidebar-header {
        font-size: 1.8rem;
        font-weight: bold;
        text-align: left;
        margin-bottom: 0.5rem;
        color: #1f1f1f;
    }
    .sidebar-subheader {
        font-size: 1rem;
        text-align: left;
        margin-bottom: 2rem;
        color: #666;
        line-height: 1.4;
    }

    /* Create a Document 页面样式 */
    .create-main-title {
        font-size: 24px;
        font-weight: bold;
        color: #1f1f1f;
        margin-bottom: 20px;
        text-align: center;
    }
    .nav-section {
        margin-bottom: 20px;
        text-align: center;
    }
    .nav-item {
        display: inline-block;
        margin: 0 15px;
        font-size: 16px;
        font-weight: normal;
    }
    .nav-item.active {
        font-weight: bold;
        color: #007bff;
    }
    .phase-section {
        text-align: center;
        margin: 25px 0;
    }
    .section-title {
        font-size: 18px;
        font-weight: bold;
        color: #1f1f1f;
        margin-bottom: 20px;
        text-align: center;
    }
    .option-grid {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
        flex-wrap: wrap;
    }
    .option-button {
        padding: 12px 20px;
        border: 2px solid #007bff;
        background-color: white;
        color: #007bff;
        border-radius: 8px;
        font-size: 14px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        min-width: 120px;
        text-align: center;
    }
    .option-button:hover {
        background-color: #f8f9fa;
        transform: translateY(-1px);
    }
    .option-button.selected {
        background-color: rgb(40,100,245);
        color: white;
        border-color: rgb(40,100,245);
    }
    .document-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
        margin: 20px 0;
        justify-content: center;
    }
    .document-button {
        padding: 10px 15px;
        border: 2px solid #007bff;
        background-color: white;
        color: #007bff;
        border-radius: 6px;
        font-size: 13px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
    }
    .document-button:hover {
        background-color: #f8f9fa;
    }
    .document-button.selected {
        background-color: rgb(40,100,245);
        color: white;
        border-color: rgb(40,100,245);
    }
    .ready-section {
        text-align: center;
        margin: 20px 0;
        padding: 15px;
        background-color: #f8f9fa;
        border-radius: 10px;
        border-left: 4px solid #007bff;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }
    .ready-title {
        font-size: 18px;
        font-weight: bold;
        color: #1f1f1f;
        margin-bottom: 0;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #666;
        font-size: 14px;
    }
    .centered-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    /* Streamlit primary按钮样式 */
    .stButton > button[kind="primary"] {
        background-color: rgb(40,100,245) !important;
        border-color: rgb(40,100,245) !important;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: rgb(32,80,220) !important;
        border-color: rgb(32,80,220) !important;
    }

    /* 侧边栏选中按钮样式 */
    .stButton > button[kind="primary"] {
        background-color: rgb(40,100,245) !important;
        border-color: rgb(40,100,245) !important;
    }
</style>
""", unsafe_allow_html=True)
# 初始化session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "learn_how"

if 'current_question' not in st.session_state:
    st.session_state.current_question = ""

if 'create_doc_step' not in st.session_state:
    st.session_state.create_doc_step = 1

if 'selected_phase' not in st.session_state:
    st.session_state.selected_phase = None

if 'selected_document' not in st.session_state:
    st.session_state.selected_document = None

# 阶段选项
PHASES = ["Design", "Development", "Implementation", "Requirement"]

# 文档类型选项
DOCUMENTS = ["Product Design", "Test Plan", "Capacity Planning", "Implementation Plan", "Contingency Planning"]


# 侧边栏
def show_sidebar():
    with st.sidebar:
        # 标题和子标题放在侧边栏
        st.markdown('<div class="sidebar-header">EPLC Assistant</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="sidebar-subheader">Empowering IT Project Managers with<br>smarter, faster documentation.</div>',
            unsafe_allow_html=True)

        st.markdown("---")

        # 导航选项
        st.markdown("### Navigation")

        if st.button("📚 Learn How to Use",
                     use_container_width=True,
                     type="primary" if st.session_state.current_page == "learn_how" else "secondary"):
            st.session_state.current_page = "learn_how"
            st.rerun()

        if st.button("💬 Ask a Question",
                     use_container_width=True,
                     type="primary" if st.session_state.current_page == "ask_question" else "secondary"):
            st.session_state.current_page = "ask_question"
            st.rerun()

        if st.button("📄 Create a Document",
                     use_container_width=True,
                     type="primary" if st.session_state.current_page == "create_document" else "secondary"):
            st.session_state.current_page = "create_document"
            st.session_state.create_doc_step = 1
            st.rerun()

        st.markdown("---")
        st.markdown("### Help & Support")


        st.markdown("""
        <div style="font-size: 15px; color: #666;">
            <p><a href="https://github.com/XinleiCheng/QMSS_IBM_Practicum_2025Fall" target="_blank"><img src="https://cdnjs.cloudflare.com/ajax/libs/octicons/8.5.0/svg/mark-github.svg" width="16" height="16" style="vertical-align: middle; margin-right: 5px;">GitHub</a></p>
        </div>
        """, unsafe_allow_html=True)


# Learn How to Use 页面
def show_learn_page():
    st.markdown("<h1 style='text-align: center;'>How to Use EPLC Assistant</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color: #e6f2ff; padding: 30px; border-radius: 10px; margin: 20px 0; border: 1px solid #b3d9ff;">
            <div style="font-size: 24px; font-weight: bold; color: rgb(40,100,245); margin: 0 0 20px 0;">Ask a Question</div>
            <div style="text-align: center;font-size: 18px; font-weight: bold; color: #1f1f1f; margin: 15px 0 8px 0;">Step 1 – Ask Your Question</div>
            <div style="text-align: center;font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 12px;">Type your EPLC-related question about an executive order in the input box.</div>
            <div style="text-align: center;font-size: 18px; font-weight: bold; color: #1f1f1f; margin: 15px 0 8px 0;">Step 2 – Get Responses</div>
            <div style="text-align: center;font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 12px;">The chatbot searches policy libraries and provides accurate, summarized answers.</div>
            <div style="text-align: center;font-size: 18px; font-weight: bold; color: #1f1f1f; margin: 15px 0 8px 0;">Step 3 – Review and Save</div>
            <div style="text-align: center;font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 12px;">Edit or export the response for your project.</div>
            <div style="border-top: 2px solid #99ccff; margin: 25px 0;"></div>
            <div style="font-size: 18px; font-weight: bold; color: rgb(40,100,245); margin: 20px 0 12px 0;">🔔 Tips for Best Results</div>
            <div style="font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 8px;">• Be specific – mention the EPLC phase or document type you're referring to.</div>
            <div style="font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 8px;">• Try rephrasing your question if the chatbot doesn't understand.</div>
            <div style="font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 8px;">• You can always find official templates and policies linked below.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #e6f2ff; padding: 30px; border-radius: 10px; margin: 20px 0; border: 1px solid #b3d9ff;">
            <div style="font-size: 24px; font-weight: bold; color: rgb(40,100,245); margin: 0 0 20px 0;">Create a Document</div>
            <div style="text-align: center;font-size: 18px; font-weight: bold; color: #1f1f1f; margin: 15px 0 8px 0;">Step 1 – Choose your phase</div>
            <div style="text-align: center;font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 12px;">Choose which EPLC phase your project is in (e.g., Design, Development, Implementation, Requirement).</div>
            <div style="text-align: center;font-size: 18px; font-weight: bold; color: #1f1f1f; margin: 15px 0 8px 0;">Step 2 – Choose a Document Template</div>
            <div style="text-align: center;font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 12px;">Pick the specific template you want to generate – such as Product Design, Test Plan, or Implementation Plan.</div>
            <div style="text-align: center;font-size: 18px; font-weight: bold; color: #1f1f1f; margin: 15px 0 8px 0;">Step 3 – Edit and Build Your Document</div>
            <div style="text-align: center;font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 12px;">Review the provided sections and add project-specific content.</div>
            <div style="border-top: 2px solid #99ccff; margin: 25px 0;"></div>
            <div style="font-size: 18px; font-weight: bold; color: rgb(40,100,245); margin: 20px 0 12px 0;">🔔 Tips for Best Results</div>
            <div style="font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 8px;">• Specify your EPLC phase before selecting a document type.</div>
            <div style="font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 8px;">• You can edit or customize any generated template.</div>
            <div style="font-size: 16px; color: #333333; line-height: 1.5; margin-bottom: 8px;">• All templates follow CDC UP and EPLC guidelines.</div>
        </div>
        """, unsafe_allow_html=True)


# Ask a Question 页面
def show_ask_question_page():
    if st.session_state.current_question:
        st.markdown(f"**You:** {st.session_state.current_question}")
        # st.markdown("---")
        st.markdown("**EPLC Assistant:** This is a sample response.")
        if st.button("Ask New Question", key="new_question"):
            st.session_state.current_question = ""
            st.rerun()
    else:
        st.markdown("""
        <div style="height: 100px; display: flex; align-items: center; justify-content: center; color: #666; font-size: 16px;">
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Try Asking...</h4>", unsafe_allow_html=True)
    suggestions = [
        "What is the EPLC Initial Phase?",
        "Show me a CDC UP template for planning.",
        "Explain the difference between initiation and planning phases."
    ]

    for suggestion in suggestions:
        if st.button(suggestion, key=f"suggestion_{suggestions.index(suggestion)}", use_container_width=True):
            st.session_state.current_question = suggestion
            st.rerun()
    user_question = st.chat_input(
        "Type your question here...",
    )

    if user_question:
        st.session_state.current_question = user_question
        st.rerun()


# Create a Document 页面 - 步骤1: 选择阶段
def show_create_doc_step1():

    # 阶段选择部分
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Which Phase are you in?</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 使用Streamlit按钮代替HTML按钮
    cols = st.columns(4)
    for i, phase in enumerate(PHASES):
        with cols[i]:
            if st.button(phase, use_container_width=True,
                         type="primary" if st.session_state.selected_phase == phase else "secondary"):
                st.session_state.selected_phase = phase
                st.session_state.create_doc_step = 2
                st.rerun()


# Create a Document 页面 - 步骤2: 选择文档类型
def show_create_doc_step2():

    # 阶段显示
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Which Phase are you in?</div>', unsafe_allow_html=True)
    phase_display = " | ".join([
        f"{phase}" if phase == st.session_state.selected_phase else phase
        for phase in PHASES
    ])
    # st.markdown(phase_display)
    st.markdown(f"<div style='text-align: center;'>{phase_display}</div>",
                unsafe_allow_html=True)

    # 文档选择
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Which Document do you want to create?</div>', unsafe_allow_html=True)

    # 文档选择按钮
    cols = st.columns(5)
    for i, doc in enumerate(DOCUMENTS):
        with cols[i]:
            if st.button(doc, use_container_width=True,
                         type="primary" if st.session_state.selected_document == doc else "secondary"):
                st.session_state.selected_document = doc
                st.session_state.create_doc_step = 3
                st.rerun()

    # 返回按钮
    if st.button("← Back to Phase Selection", use_container_width=False):
        st.session_state.create_doc_step = 1
        st.rerun()


# Create a Document 页面 - 步骤3: 确认选择
def show_create_doc_step3():

    # 阶段显示
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Which Phase are you in?</div>', unsafe_allow_html=True)
    # st.markdown("Design | Development | Implementation | Requirement")
    st.markdown("<div style='text-align: center;'>Design | Development | Implementation | Requirement</div>",
                unsafe_allow_html=True)

    # 文档显示
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Which Document do you want to create?</div>', unsafe_allow_html=True)
    # st.markdown("Product Design | Test Plan | Capacity Planning | Implementation Plan | Contingency Planning")
    st.markdown("<div style='text-align: center;'>Product Design | Test Plan | Capacity Planning | Implementation Plan | Contingency Planning</div>",
                unsafe_allow_html=True)
    # 准备开始部分

    st.markdown('<div class="phase-section">', unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Ready? Let's do it session by session! 👇</h5>", unsafe_allow_html=True)



    # 操作按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Generate Document", use_container_width=True, type="primary"):
            st.success(
                f"Generating {st.session_state.selected_document} for {st.session_state.selected_phase} phase...")
            # 这里可以添加文档生成的逻辑

        if st.button("← Back to Document Selection", use_container_width=True):
            st.session_state.create_doc_step = 2
            st.rerun()

    # 显示当前选择
    st.info(f"**Selected:** {st.session_state.selected_phase} Phase → {st.session_state.selected_document}")


# Create a Document 主页面
def show_create_document_page():
    if st.session_state.create_doc_step == 1:
        show_create_doc_step1()
    elif st.session_state.create_doc_step == 2:
        show_create_doc_step2()
    elif st.session_state.create_doc_step == 3:
        show_create_doc_step3()


# 主应用逻辑
def main():
    show_sidebar()

    if st.session_state.current_page == "learn_how":
        show_learn_page()
    elif st.session_state.current_page == "ask_question":
        show_ask_question_page()
    elif st.session_state.current_page == "create_document":
        show_create_document_page()


if __name__ == "__main__":
    main()
