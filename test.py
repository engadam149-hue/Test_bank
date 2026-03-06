import streamlit as st
import random
from data import SUBJECTS, QUESTIONS_DB

# ════════════════════════════════════════════════════════════
# ⚙️ Page Config
# ════════════════════════════════════════════════════════════
st.set_page_config(page_title="بنك أسئلة NMU", page_icon="🤖", layout="wide")

# ════════════════════════════════════════════════════════════
# 🔧 State Initialization
# ════════════════════════════════════════════════════════════
if "page" not in st.session_state: st.session_state.page = "subjects"
if "sel_subj" not in st.session_state: st.session_state.sel_subj = None
if "sel_lec" not in st.session_state: st.session_state.sel_lec = None
if "answers" not in st.session_state: st.session_state.answers = {}
if "seed" not in st.session_state: st.session_state.seed = 42
if "q_order" not in st.session_state: st.session_state.q_order = []
if "show_mistakes_only" not in st.session_state: st.session_state.show_mistakes_only = False
if "theme" not in st.session_state: st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def toggle_mistakes():
    st.session_state.show_mistakes_only = not st.session_state.show_mistakes_only

# ════════════════════════════════════════════════════════════
# 🚀 Routing Logic
# ════════════════════════════════════════════════════════════
def go_to_page(page_name, subj=None, lec=None):
    st.session_state.page = page_name
    if page_name == "subjects":
        st.session_state.sel_subj = None
        st.session_state.sel_lec  = None
    elif page_name == "lectures":
        if subj: st.session_state.sel_subj = subj
        st.session_state.sel_lec = None
    elif page_name == "quiz":
        if lec:
            st.session_state.sel_lec  = lec
            st.session_state.answers  = {}
            st.session_state.seed     = random.randint(1, 10000)
            st.session_state.show_mistakes_only = False
            
            questions = QUESTIONS_DB.get(lec, [])
            order = list(range(len(questions)))
            rng = random.Random(st.session_state.seed)
            rng.shuffle(order)
            st.session_state.q_order = order

def record_answer(q_idx, opt):
    st.session_state.answers[q_idx] = opt

def retry_quiz():
    st.session_state.answers = {}
    st.session_state.seed    = random.randint(1, 10000)
    st.session_state.show_mistakes_only = False
    
    questions = QUESTIONS_DB.get(st.session_state.sel_lec, [])
    order = list(range(len(questions)))
    rng = random.Random(st.session_state.seed)
    rng.shuffle(order)
    st.session_state.q_order = order

def section_header(label):
    st.markdown(f"""
    <div class="section-hdr">
        <div class="section-hdr-line"></div>
        <div class="section-hdr-label">{label}</div>
        <div class="section-hdr-line right"></div>
    </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# 🔧 Scroll-lock (JavaScript)
# ════════════════════════════════════════════════════════════
st.markdown("""
<script>
(function () {
    const KEY = 'nmu_scroll_y';
    const saved = sessionStorage.getItem(KEY);
    if (saved !== null) window.scrollTo(0, parseInt(saved, 10));

    window.addEventListener('beforeunload', () => { sessionStorage.setItem(KEY, window.scrollY); });
    document.addEventListener('click', (e) => {
        if (e.target.closest('button')) sessionStorage.setItem(KEY, window.scrollY);
    }, true);

    const observer = new MutationObserver(() => {
        const y = sessionStorage.getItem(KEY);
        if (y !== null) window.scrollTo(0, parseInt(y, 10));
    });
    observer.observe(document.body, { childList: true, subtree: true });
})();
</script>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# 🎨 CSS - CYBERPUNK THEME + NORMAL BUTTONS
# ════════════════════════════════════════════════════════════
if st.session_state.theme == "dark":
    css_vars = """
    :root {
        --bg-main: #06070a; 
        --bg-card: #0c0e14; 
        --bg-hero: transparent;
        --border-card: #1f2233; 
        --border-line: #1f2233;
        --text-main: #e2e8f0; 
        --text-muted: #8b949e; 
        --text-card-title: #ffffff;
        --primary: #00f3ff; 
        --primary-light: #bc13fe; 
        --badge-bg: rgba(0, 243, 255, 0.1); 
        --btn-bg: #0c0e14; 
        --btn-border: #1f2233; 
        --btn-hover: #131722;
        --opt-neutral-bg: #0c0e14; 
        --opt-correct-bg: rgba(0, 243, 255, 0.05); 
        --opt-correct-text: #00f3ff; 
        --opt-correct-border: #00f3ff;
        --opt-wrong-bg: rgba(255, 0, 85, 0.05); 
        --opt-wrong-text: #ff0055; 
        --opt-wrong-border: #ff0055;
        --scrollbar-thumb: #1f2233; 
        --prog-bg: #0c0e14;
        --ring-bg: #06070a; 
        --ring-border: #1f2233;
        --badge-tf-bg: rgba(188, 19, 254, 0.1); 
        --badge-tf-text: #bc13fe; 
        --badge-tf-border: rgba(188, 19, 254, 0.3);
        --special-bg: linear-gradient(135deg, rgba(188, 19, 254, 0.05), #0c0e14);
        --special-border: rgba(188, 19, 254, 0.6);
        --special-shadow: 0 4px 30px rgba(188, 19, 254, 0.2);
        --grid-color: rgba(0, 243, 255, 0.03);
    }
    """
else:
    css_vars = """
    :root {
        --bg-main: #f4f5f8; --bg-card: #ffffff; --bg-hero: transparent;
        --border-card: #e2e4ea; --border-line: #d0d4e0;
        --text-main: #1f1b2e; --text-muted: #6b667a; --text-card-title: #141021;
        --primary: #6d28d9; --primary-light: #8b5cf6;
        --badge-bg: #f3f0ff; --btn-bg: #ffffff; --btn-border: #d0d4e0; --btn-hover: #f9f8fc;
        --opt-neutral-bg: #fdfcff; --opt-correct-bg: #f0fdf4; --opt-correct-text: #15803d; --opt-correct-border: #22c55e;
        --opt-wrong-bg: #fef2f2; --opt-wrong-text: #b91c1c; --opt-wrong-border: #ef4444;
        --scrollbar-thumb: #a78bfa; --prog-bg: #e2e4ea;
        --ring-bg: #ffffff; --ring-border: #d0d4e0;
        --badge-tf-bg: #eff6ff; --badge-tf-text: #1d4ed8; --badge-tf-border: #bfdbfe;
        --special-bg: linear-gradient(135deg, #f3f0ff, #ffffff);
        --special-border: #8b5cf6;
        --special-shadow: 0 8px 30px #8b5cf644;
        --grid-color: rgba(109, 40, 217, 0.03);
    }
    """

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Tajawal:wght@300;400;500;700;800&display=swap');
{css_vars}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
* {{ font-family: 'Tajawal', sans-serif !important; }}
[data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display: none !important; }}

/* Matrix Grid Background */
.stApp {{ background-color: var(--bg-main); background-image: linear-gradient(var(--grid-color) 1px, transparent 1px), linear-gradient(90deg, var(--grid-color) 1px, transparent 1px); background-size: 40px 40px; color: var(--text-main); transition: background-color 0.3s ease; }}
section[data-testid="stMain"] > div {{ padding-top: 0 !important; }}
.block-container {{ padding: 1rem 2rem 4rem !important; max-width: 1200px !important; }}

::-webkit-scrollbar {{ width: 4px; }}
::-webkit-scrollbar-track {{ background: var(--bg-main); }}
::-webkit-scrollbar-thumb {{ background: var(--scrollbar-thumb); border-radius: 4px; }}

/* ═════ HERO SECTION ═════ */
.hero {{ position: relative; overflow: hidden; background: var(--bg-hero); border-bottom: 1px solid var(--border-line); padding: 56px 48px 48px; margin: 0 -2rem 48px; text-align: center; }}
.hero::before {{ content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 80% 60% at 50% -10%, rgba(0, 243, 255, 0.05) 0%, transparent 70%); pointer-events: none; }}
.hero-inner {{ position: relative; z-index: 1; }}
.hero-badge {{ display: inline-flex; align-items: center; gap: 8px; background: var(--badge-bg); border: 1px solid rgba(0, 243, 255, 0.3); border-radius: 100px; padding: 6px 18px; font-size: 11px; font-weight: 700; letter-spacing: 3px; color: var(--primary); text-transform: uppercase; margin-bottom: 20px; box-shadow: 0 0 15px rgba(0, 243, 255, 0.1); }}
.hero-title {{ font-family: 'Playfair Display', serif !important; font-size: clamp(36px, 5vw, 56px); font-weight: 800; color: var(--text-main); line-height: 1.1; margin-bottom: 12px; }}
.hero-title em {{ font-style: normal; color: var(--primary-light); text-shadow: 0 0 20px rgba(188, 19, 254, 0.4); }}
.hero-sub {{ font-size: 15px; color: var(--text-muted); max-width: 480px; margin: 0 auto; line-height: 1.7; }}
.hero-stats {{ display: flex; justify-content: center; gap: 40px; margin-top: 32px; padding-top: 28px; border-top: 1px solid var(--border-line); }}
.stat {{ text-align: center; }}
.stat-num {{ font-size: 24px; font-weight: 800; color: var(--primary-light); line-height: 1; }}
.stat-lbl {{ font-size: 11px; color: var(--text-muted); font-weight: 600; letter-spacing: 1px; margin-top: 4px; }}

.section-hdr {{ display: flex; align-items: center; gap: 14px; margin-bottom: 20px; }}
.section-hdr-line {{ flex: 1; height: 1px; background: linear-gradient(90deg, var(--border-line), transparent); }}
.section-hdr-line.right {{ background: linear-gradient(270deg, var(--border-line), transparent); }}
.section-hdr-label {{ font-size: 10px; font-weight: 700; letter-spacing: 4px; color: var(--text-muted); text-transform: uppercase; white-space: nowrap; }}

/* ═════ CARDS DESIGN (Normal) ═════ */
.subject-card {{ background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 20px; padding: 28px 24px; text-align: right; direction: rtl; transition: all .3s ease; height: 100%; margin-bottom: 15px; backdrop-filter: blur(10px); }}
.subject-card:hover {{ border-color: var(--primary); box-shadow: 0 10px 30px rgba(0, 243, 255, 0.1); transform: translateY(-4px); }}
.subj-icon {{ font-size: 36px; margin-bottom: 14px; display: block; }}
.subj-name {{ font-size: 16px; font-weight: 700; color: var(--text-card-title); margin-bottom: 4px; }}
.subj-code {{ font-size: 10px; font-weight: 700; letter-spacing: 2px; color: var(--primary); text-transform: uppercase; margin-bottom: 10px; }}
.subj-desc {{ font-size: 13px; color: var(--text-muted); line-height: 1.5; }}

.lec-card {{ background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 14px; padding: 18px 20px; text-align: right; direction: rtl; transition: all .3s ease; height: 100%; margin-bottom: 15px; backdrop-filter: blur(10px); }}
.lec-card:not(.locked):hover {{ border-color: var(--primary); box-shadow: 0 10px 30px rgba(0, 243, 255, 0.1); transform: translateY(-4px); }}
.lec-card.locked {{ opacity: .5; filter: grayscale(1); }}
.lec-card.special-card {{ background: var(--special-bg); border: 2px solid var(--special-border); box-shadow: var(--special-shadow); }}
.lec-card.special-card:not(.locked):hover {{ border-color: #d85bff; box-shadow: 0 10px 40px rgba(188, 19, 254, 0.3); transform: scale(1.02) translateY(-2px); }}

.special-card .lec-num {{ font-size: 12px; color: var(--primary-light); font-weight: 800; }}
.special-card .lec-title {{ color: var(--text-main); font-size: 16px; }}
.lec-num {{ font-size: 9px; font-weight: 700; letter-spacing: 3px; color: var(--text-muted); text-transform: uppercase; margin-bottom: 8px; }}
.lec-title {{ font-size: 14px; font-weight: 700; color: var(--text-card-title); margin-bottom: 6px; }}
.lec-count-badge {{ display: inline-block; background: var(--border-card); border: 1px solid var(--border-line); border-radius: 100px; padding: 2px 10px; font-size: 11px; color: var(--text-muted); }}

/* ═════ QUIZ UI ═════ */
.prog-wrap {{ background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 16px; padding: 20px 24px; margin-bottom: 28px; direction: rtl; }}
.prog-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
.prog-label {{ font-size: 13px; color: var(--text-muted); font-weight: 600; }}
.prog-stats {{ display: flex; gap: 16px; }}
.prog-stat {{ font-size: 13px; font-weight: 700; }}
.prog-stat.correct {{ color: var(--opt-correct-text); }}
.prog-stat.wrong   {{ color: var(--opt-wrong-text); }}
.prog-bar-bg {{ background: var(--prog-bg); border-radius: 100px; height: 6px; overflow: hidden; border: 1px solid var(--border-line); }}
.prog-bar-fill {{ height: 100%; border-radius: 100px; background: linear-gradient(90deg, var(--primary), var(--primary-light)); transition: width .4s ease; box-shadow: 0 0 10px var(--primary); }}

.q-card {{ background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 18px; padding: 28px 32px; margin-bottom: 8px; direction: ltr; transition: border-color .3s; }}
.q-card.state-correct {{ border-color: var(--opt-correct-border); box-shadow: 0 0 15px rgba(0,243,255,0.05); }}
.q-card.state-wrong   {{ border-color: var(--opt-wrong-border); box-shadow: 0 0 15px rgba(255,0,85,0.05); }}
.q-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }}
.q-num  {{ font-size: 10px; font-weight: 700; letter-spacing: 3px; color: var(--text-muted); text-transform: uppercase; }}
.q-badge {{ font-size: 9px; font-weight: 700; letter-spacing: 1.5px; padding: 3px 10px; border-radius: 100px; text-transform: uppercase; }}
.badge-mcq {{ background: var(--badge-bg); color: var(--primary); border: 1px solid rgba(0,243,255,0.2); }}
.badge-tf  {{ background: var(--badge-tf-bg); color: var(--badge-tf-text); border: 1px solid var(--badge-tf-border); }}
.q-text {{ font-size: 17px; font-weight: 500; color: var(--text-card-title); line-height: 1.65; margin-bottom: 0; text-align: left; }}

.opt {{ border-radius: 12px; padding: 14px 20px; font-size: 14px; font-weight: 500; margin-bottom: 8px; line-height: 1.5; transition: all .2s; display: flex; align-items: center; height: 100%; cursor: pointer; }}
.opt-correct {{ background: var(--opt-correct-bg); border: 1.5px solid var(--opt-correct-border); color: var(--opt-correct-text); text-align: left; direction: ltr; box-shadow: inset 0 0 10px rgba(0,243,255,0.1); }}
.opt-wrong   {{ background: var(--opt-wrong-bg); border: 1.5px solid var(--opt-wrong-border); color: var(--opt-wrong-text); text-decoration: line-through; text-align: left; direction: ltr; }}
.opt-reveal  {{ background: var(--opt-correct-bg); border: 1.5px solid var(--opt-correct-border); color: var(--opt-correct-text); opacity: 0.8; text-align: left; direction: ltr; }}
.opt-neutral {{ background: var(--opt-neutral-bg); border: 1.5px solid var(--border-card); color: var(--text-main); text-align: left; direction: ltr; }}

.explain-box {{ border-radius: 12px; padding: 16px 20px; font-size: 14px; line-height: 1.75; margin-top: 6px; margin-bottom: 4px; direction: rtl; text-align: right; }}
.explain-correct {{ background: var(--opt-correct-bg); border: 1px solid var(--opt-correct-border); color: var(--opt-correct-text); }}
.explain-wrong   {{ background: var(--opt-wrong-bg); border: 1px solid var(--opt-wrong-border); color: var(--opt-wrong-text); }}
.q-sep {{ height: 1px; background: var(--border-line); margin: 20px 0; }}

/* Score Banner */
.score-banner {{ background: var(--bg-card); border: 1px solid var(--border-line); border-radius: 24px; padding: 48px 40px; text-align: center; margin-bottom: 32px; position: relative; overflow: hidden; direction: rtl; box-shadow: inset 0 0 50px rgba(0,243,255,0.02); }}
.score-ring {{ width: 120px; height: 120px; border-radius: 50%; border: 3px solid var(--ring-border); margin: 0 auto 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--ring-bg); box-shadow: 0 0 20px rgba(188,19,254,0.1); }}
.score-ring-num {{ font-size: 36px; font-weight: 800; color: var(--primary-light); line-height: 1; text-shadow: 0 0 10px rgba(188,19,254,0.3); }}
.score-ring-den {{ font-size: 14px; color: var(--text-muted); }}
.score-title    {{ font-size: 22px; font-weight: 800; color: var(--text-card-title); margin-bottom: 6px; }}
.score-pct      {{ font-size: 14px; color: var(--text-muted); }}

/* ═════ REGULAR BUTTONS (quiz options, nav, explicitly visible) ═════ */
div[data-testid="stButton"] button {{ background: var(--btn-bg) !important; border: 1px solid var(--btn-border) !important; border-radius: 10px !important; color: var(--text-main) !important; font-size: 14px !important; font-weight: 700 !important; padding: 12px 16px !important; transition: all .3s ease !important; width: 100% !important; height: 100% !important; margin-bottom: 10px; }}
div[data-testid="stButton"] button:hover {{ border-color: var(--primary) !important; color: var(--primary) !important; background: var(--btn-hover) !important; box-shadow: 0 0 15px rgba(0,243,255,0.1); }}

/* Theme toggle pill */
div[data-testid="stButton"][aria-label*="Mode"] button {{ border-radius: 50px !important; border: 1px solid var(--border-card) !important; color: var(--text-muted) !important; background: var(--bg-card) !important; font-weight: 700 !important; margin-bottom: 10px; font-family: sans-serif !important; box-shadow: none !important; }}
div[data-testid="stButton"][aria-label*="Mode"] button:hover {{ background: var(--primary) !important; color: #000 !important; border-color: var(--primary) !important; }}

#MainMenu, footer, header {{ visibility: hidden; }}
.stDeployButton {{ display: none; }}
@keyframes fadeUp {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: translateY(0); }} }}
.q-card, .subject-card, .lec-card {{ animation: fadeUp .4s ease both; }}
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# 🌙 THEME TOGGLE BUTTON
# ════════════════════════════════════════════════════════════
t_col_space, t_col_btn = st.columns([8, 2])
with t_col_btn:
    btn_text = "☀️ Light Mode" if st.session_state.theme == "dark" else "🌙 Dark Mode"
    st.button(btn_text, on_click=toggle_theme, use_container_width=True)

# ════════════════════════════════════════════════════════════
# 1️⃣  PAGE: SUBJECTS
# ════════════════════════════════════════════════════════════
if st.session_state.page == "subjects":
    total_q   = sum(len(v) for v in QUESTIONS_DB.values())
    total_lec = sum(len(s["lectures"]) for s in SUBJECTS)

    st.markdown(f"""
    <div class="hero">
        <div class="hero-inner">
            <div class="hero-badge">🎓 جامعة المنصورة الجديدة · NMU</div>
            <div class="hero-title" style="color:var(--text-main);">Question Bank</div>
            <div class="hero-sub">اختر المادة والمحاضرة وابدأ المذاكرة — مع تصحيح وشرح فوري لكل إجابة</div>
            <div class="hero-stats">
                <div class="stat"><div class="stat-num">{len(SUBJECTS)}</div><div class="stat-lbl">مادة</div></div>
                <div class="stat"><div class="stat-num">{total_lec}</div><div class="stat-lbl">محاضرة</div></div>
                <div class="stat"><div class="stat-num">{total_q}+</div><div class="stat-lbl">سؤال</div></div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    section_header("اختر المادة")
    
    subj_count = 3
    for i in range(0, len(SUBJECTS), subj_count):
        cols = st.columns(subj_count)
        for j in range(subj_count):
            if i + j < len(SUBJECTS):
                subj = SUBJECTS[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="subject-card">
                        <span class="subj-icon">{subj['icon']}</span>
                        <div class="subj-name">{subj['name']}</div>
                        <div class="subj-code">{subj['code']}</div>
                        <div class="subj-desc">{subj['desc']}</div>
                    </div>""", unsafe_allow_html=True)
                    st.button("اختر المادة", key=f"btn_{subj['key']}", on_click=go_to_page, args=("lectures", subj["key"]), use_container_width=True)

# ════════════════════════════════════════════════════════════
# 2️⃣  PAGE: LECTURES
# ════════════════════════════════════════════════════════════
elif st.session_state.page == "lectures":
    cur_subj = next(s for s in SUBJECTS if s["key"] == st.session_state.sel_subj)

    col1, col2 = st.columns([10, 2])
    with col2:
        st.button("🔙 رجوع", on_click=go_to_page, args=("subjects",), use_container_width=True)
    with col1:
        section_header(f"محاضرات · {cur_subj['name']}")

    num_lecs  = len(cur_subj["lectures"])
    col_count = 3
    
    for i in range(0, num_lecs, col_count):
        cols = st.columns(col_count)
        for j in range(col_count):
            if i + j < num_lecs:
                lec = cur_subj["lectures"][i + j]
                with cols[j]:
                    is_special = lec.get("special", False)
                    sp_class = "special-card" if is_special else ""
                    locked_cls = "locked" if not lec['available'] else ""
                    
                    st.markdown(f"""
                    <div class="lec-card {sp_class} {locked_cls}">
                        <div class="lec-num">{'✨' if is_special else 'Lecture'} {lec['num']}</div>
                        <div class="lec-title">{lec['title']}</div>
                        <span class="lec-count-badge">{lec['count']}</span>
                        {'' if lec['available'] else '<div class="soon-tag">قريباً ⏳</div>'}
                    </div>""", unsafe_allow_html=True)

                    if lec["available"]:
                        btn_lbl = "🔥 ابدأ التحدي" if is_special else "ابدأ الاختبار"
                        st.button(btn_lbl, key=f"btn_{lec['key']}", on_click=go_to_page, args=("quiz", None, lec["key"]), use_container_width=True)
                    else:
                        st.button("مغلق", key=f"locked_{lec['key']}", disabled=True, use_container_width=True)

# ════════════════════════════════════════════════════════════
# 3️⃣  PAGE: QUIZ
# ════════════════════════════════════════════════════════════
elif st.session_state.page == "quiz":
    questions = QUESTIONS_DB.get(st.session_state.sel_lec, [])

    col1, col2 = st.columns([10, 2])
    with col2:
        st.button("🔙 رجوع", on_click=go_to_page, args=("lectures",), use_container_width=True)
    with col1:
        section_header("الاختبار")

    if not questions:
        st.markdown("<p style='color:var(--text-muted);text-align:center;padding:40px'>لا توجد أسئلة بعد.</p>", unsafe_allow_html=True)
    else:
        answered = len(st.session_state.answers)
        score    = sum(1 for idx, v in st.session_state.answers.items() if v == questions[idx]["ans"])
        total    = len(questions)
        pct_done = answered / total if total else 0

        # ── Progress Bar ──
        st.markdown(f"""
        <div class="prog-wrap">
            <div class="prog-top">
                <span class="prog-label">تم الإجابة على {answered} من {total} سؤال</span>
                <div class="prog-stats">
                    <span class="prog-stat correct">✅ {score} صح</span>
                    <span class="prog-stat wrong">❌ {answered - score} غلط</span>
                </div>
            </div>
            <div class="prog-bar-bg">
                <div class="prog-bar-fill" style="width:{pct_done*100:.1f}%"></div>
            </div>
        </div>""", unsafe_allow_html=True)

        # ── Questions Display ──
        display_num = 1
        for orig_idx in st.session_state.q_order:
            q = questions[orig_idx]
            chosen      = st.session_state.answers.get(orig_idx)
            is_answered = chosen is not None
            is_correct  = chosen == q["ans"]
            q_type      = q.get("type", "mcq")

            if st.session_state.show_mistakes_only and is_correct:
                continue

            card_cls  = "state-correct" if is_answered and is_correct else ("state-wrong"  if is_answered else "")
            badge_lbl = "True / False" if q_type == "tf" else "MCQ"
            badge_cls = "badge-tf"     if q_type == "tf" else "badge-mcq"

            st.markdown(f"""
            <div class="q-card {card_cls}">
                <div class="q-header">
                    <span class="q-num">Q{str(display_num).zfill(2)}</span>
                    <span class="q-badge {badge_cls}">{badge_lbl}</span>
                </div>
                <div class="q-text">{q['q']}</div>
            </div>""", unsafe_allow_html=True)
            display_num += 1

            shuffled_opts = q["options"].copy()
            rng_opts = random.Random(st.session_state.seed + orig_idx)
            rng_opts.shuffle(shuffled_opts)
            opt_cols = st.columns(2)

            if is_answered:
                for j, opt in enumerate(shuffled_opts):
                    with opt_cols[j % 2]:
                        if opt == q["ans"] and opt == chosen:
                            st.markdown(f'<div class="opt opt-correct">✅ &nbsp;{opt}</div>', unsafe_allow_html=True)
                        elif opt == chosen:
                            st.markdown(f'<div class="opt opt-wrong">❌ &nbsp;{opt}</div>', unsafe_allow_html=True)
                        elif opt == q["ans"]:
                            st.markdown(f'<div class="opt opt-reveal">✅ &nbsp;{opt} &nbsp;<span style="font-size:11px;opacity:.6">← الإجابة الصحيحة</span></div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="opt opt-neutral">{opt}</div>', unsafe_allow_html=True)

                exp_key = "explain_correct" if is_correct else "explain_wrong"
                exp_cls = "explain-correct" if is_correct else "explain-wrong"
                exp_txt = q.get(exp_key, "")
                if exp_txt:
                    st.markdown(f'<div class="explain-box {exp_cls}">{exp_txt}</div>', unsafe_allow_html=True)
            else:
                for j, opt in enumerate(shuffled_opts):
                    with opt_cols[j % 2]:
                        st.button(opt, key=f"q{orig_idx}_{opt}", on_click=record_answer, args=(orig_idx, opt), use_container_width=True)

            st.markdown("<div class='q-sep'></div>", unsafe_allow_html=True)

        # ── Score Display ──
        if answered == total:
            pct = int((score / total) * 100)
            if   pct == 100: emoji, msg = "🏆", "نتيجة مثالية!"
            elif pct >= 80:  emoji, msg = "🎉", "ممتاز جداً!"
            elif pct >= 60:  emoji, msg = "👍", "جيد، كمّل!"
            else:            emoji, msg = "📚", "راجع المحاضرة تاني!"

            if pct == 100 and not st.session_state.show_mistakes_only: st.balloons()

            st.markdown(f"""
            <div class="score-banner">
                <div class="score-ring">
                    <div class="score-ring-num">{score}</div>
                    <div class="score-ring-den">/ {total}</div>
                </div>
                <div class="score-title">{emoji} {msg}</div>
                <div class="score-pct">{pct}% إجابات صحيحة</div>
            </div>""", unsafe_allow_html=True)

            c_btn1, c_btn2 = st.columns(2)
            with c_btn1:
                st.button("🔄 إعادة المحاولة", on_click=retry_quiz, use_container_width=True)
            with c_btn2:
                if score < total:
                    lbl = "📖 عرض كل الأسئلة" if st.session_state.show_mistakes_only else "🔍 مراجعة أخطائي فقط"
                    st.button(lbl, on_click=toggle_mistakes, use_container_width=True)
                
            st.markdown("<div style='margin-bottom:32px'></div>", unsafe_allow_html=True)