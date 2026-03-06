import streamlit as st
import random
from data import SUBJECTS, QUESTIONS_DB

# ════════════════════════════════════════════════════════════
# ⚙️ Page Config
# ════════════════════════════════════════════════════════════
st.set_page_config(page_title="بنك أسئلة NMU", page_icon="📚", layout="wide")

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
# 🚀 Routing Logic (With Random Seed Fix)
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
# 🎨 CSS — Dynamic Theme (Dark/Light)
# ════════════════════════════════════════════════════════════
if st.session_state.theme == "dark":
    css_vars = """
    :root {
        --bg-main: #08070f; --bg-card: #0e0c1a; --bg-hero: #0c0a18;
        --border-card: #1a1530; --border-line: #1e1633;
        --text-main: #e8e4f0; --text-muted: #5a5078; --text-card-title: #e8e4f0;
        --primary: #7c3aed; --primary-light: #a78bfa;
        --badge-bg: #1a1333; --btn-bg: #0e0c1a; --btn-border: #1e1a30; --btn-hover: #110e20;
        --opt-neutral-bg: #0e0c1a; --opt-correct-bg: #0a1f12; --opt-correct-text: #4ade80; --opt-correct-border: #16a34a;
        --opt-wrong-bg: #1c0a0a; --opt-wrong-text: #f87171; --opt-wrong-border: #dc2626;
        --scrollbar-thumb: #3d2d6e; --prog-bg: #1a1530;
        --ring-bg: #0c0a18; --ring-border: #1e1633;
        --badge-tf-bg: #0d1f30; --badge-tf-text: #3b82f6; --badge-tf-border: #1e3a5f;
        --special-bg: linear-gradient(135deg, #1e133c, #0e0c1a);
        --special-border: #a78bfa;
        --special-shadow: 0 4px 30px #7c3aed33;
    }
    """
else:
    css_vars = """
    :root {
        --bg-main: #f4f5f8; --bg-card: #ffffff; --bg-hero: #ffffff;
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
    }
    """

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Tajawal:wght@300;400;500;700;800&display=swap');
{css_vars}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
* {{ font-family: 'Tajawal', sans-serif !important; }}
[data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display: none !important; }}
.stApp {{ background: var(--bg-main); color: var(--text-main); transition: background 0.3s ease; }}
section[data-testid="stMain"] > div {{ padding-top: 0 !important; }}
.block-container {{ padding: 1rem 2rem 4rem !important; max-width: 1200px !important; }}

::-webkit-scrollbar {{ width: 4px; }}
::-webkit-scrollbar-track {{ background: var(--bg-main); }}
::-webkit-scrollbar-thumb {{ background: var(--scrollbar-thumb); border-radius: 4px; }}

.hero {{ position: relative; overflow: hidden; background: var(--bg-hero); border-bottom: 1px solid var(--border-line); padding: 56px 48px 48px; margin: 0 -2rem 48px; text-align: center; transition: background 0.3s; }}
.hero::before {{ content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 80% 60% at 50% -10%, #7c3aed11 0%, transparent 70%); }}
.hero::after {{ content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, var(--primary-light), transparent); opacity: 0.3; }}
.hero-inner {{ position: relative; z-index: 1; }}
.hero-badge {{ display: inline-flex; align-items: center; gap: 8px; background: var(--badge-bg); border: 1px solid var(--scrollbar-thumb); border-radius: 100px; padding: 6px 18px; font-size: 11px; font-weight: 700; letter-spacing: 3px; color: var(--primary-light); text-transform: uppercase; margin-bottom: 20px; }}
.hero-badge::before {{ content: '◆'; font-size: 8px; color: var(--primary); }}
.hero-title {{ font-family: 'Playfair Display', serif !important; font-size: clamp(36px, 5vw, 56px); font-weight: 800; color: var(--text-main); line-height: 1.1; margin-bottom: 12px; }}
.hero-title em {{ font-style: normal; color: var(--primary-light); }}
.hero-sub {{ font-size: 15px; color: var(--text-muted); max-width: 480px; margin: 0 auto; line-height: 1.7; }}
.hero-stats {{ display: flex; justify-content: center; gap: 40px; margin-top: 32px; padding-top: 28px; border-top: 1px solid var(--border-line); }}
.stat {{ text-align: center; }}
.stat-num {{ font-size: 24px; font-weight: 800; color: var(--primary-light); line-height: 1; }}
.stat-lbl {{ font-size: 11px; color: var(--text-muted); font-weight: 600; letter-spacing: 1px; margin-top: 4px; }}

.section-hdr {{ display: flex; align-items: center; gap: 14px; margin-bottom: 20px; }}
.section-hdr-line {{ flex: 1; height: 1px; background: linear-gradient(90deg, var(--border-line), transparent); }}
.section-hdr-line.right {{ background: linear-gradient(270deg, var(--border-line), transparent); }}
.section-hdr-label {{ font-size: 10px; font-weight: 700; letter-spacing: 4px; color: var(--scrollbar-thumb); text-transform: uppercase; white-space: nowrap; }}

.subject-card {{ background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 20px; padding: 28px 24px; text-align: right; direction: rtl; transition: all .25s; cursor: pointer; height: 100%; position: relative; overflow: hidden; }}
.subject-card::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, var(--scrollbar-thumb), transparent); opacity: 0; transition: opacity .3s; }}
.subject-card:hover {{ border-color: var(--primary); background: var(--btn-hover); box-shadow: 0 10px 30px #7c3aed11; }}
.subject-card:hover::before {{ opacity: 1; }}
.subj-icon {{ font-size: 36px; margin-bottom: 14px; display: block; }}
.subj-name {{ font-size: 16px; font-weight: 700; color: var(--text-card-title); margin-bottom: 4px; }}
.subj-code {{ font-size: 10px; font-weight: 700; letter-spacing: 2px; color: var(--primary); text-transform: uppercase; margin-bottom: 10px; }}
.subj-desc {{ font-size: 13px; color: var(--text-muted); line-height: 1.5; }}

.lec-card {{ background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 14px; padding: 18px 20px; text-align: right; direction: rtl; transition: all .2s; cursor: pointer; position: relative; height: 100%; }}
.lec-card:hover {{ border-color: var(--scrollbar-thumb); transform: translateY(-2px); }}
.lec-card.locked {{ opacity: .5; cursor: not-allowed; filter: grayscale(1); }}

/* 🌟 الكارت المميز بتاع الاسايمنتات */
.lec-card.special-card {{
    background: var(--special-bg);
    border: 2px solid var(--special-border);
    box-shadow: var(--special-shadow);
    transform: scale(1.02);
}}
.lec-card.special-card:hover {{
    transform: scale(1.04);
    box-shadow: 0 8px 40px var(--special-shadow);
}}
.special-card .lec-num {{ font-size: 12px; color: var(--primary-light); font-weight: 800; }}
.special-card .lec-title {{ color: var(--text-main); font-size: 16px; }}

.lec-num {{ font-size: 9px; font-weight: 700; letter-spacing: 3px; color: var(--scrollbar-thumb); text-transform: uppercase; margin-bottom: 8px; }}
.lec-title {{ font-size: 14px; font-weight: 700; color: var(--text-card-title); margin-bottom: 6px; }}
.lec-count-badge {{ display: inline-block; background: var(--border-card); border: 1px solid var(--border-line); border-radius: 100px; padding: 2px 10px; font-size: 11px; color: var(--text-muted); }}

.prog-wrap {{ background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 16px; padding: 20px 24px; margin-bottom: 28px; direction: rtl; }}
.prog-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
.prog-label {{ font-size: 13px; color: var(--text-muted); font-weight: 600; }}
.prog-stats {{ display: flex; gap: 16px; }}
.prog-stat {{ font-size: 13px; font-weight: 700; }}
.prog-stat.correct {{ color: var(--opt-correct-text); }}
.prog-stat.wrong   {{ color: var(--opt-wrong-text); }}
.prog-bar-bg {{ background: var(--prog-bg); border-radius: 100px; height: 6px; overflow: hidden; }}
.prog-bar-fill {{ height: 100%; border-radius: 100px; background: linear-gradient(90deg, var(--primary), var(--primary-light)); transition: width .4s ease; }}

.score-banner {{ background: var(--bg-card); border: 1px solid var(--border-line); border-radius: 24px; padding: 48px 40px; text-align: center; margin-bottom: 32px; position: relative; overflow: hidden; direction: rtl; }}
.score-ring {{ width: 120px; height: 120px; border-radius: 50%; border: 3px solid var(--ring-border); margin: 0 auto 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--ring-bg); }}
.score-ring-num {{ font-size: 36px; font-weight: 800; color: var(--primary-light); line-height: 1; }}
.score-ring-den {{ font-size: 14px; color: var(--scrollbar-thumb); }}
.score-title    {{ font-size: 22px; font-weight: 800; color: var(--text-card-title); margin-bottom: 6px; }}
.score-pct      {{ font-size: 14px; color: var(--text-muted); }}

.q-card {{ background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 18px; padding: 28px 32px; margin-bottom: 8px; direction: ltr; transition: border-color .3s; }}
.q-card.state-correct {{ border-color: var(--opt-correct-border); }}
.q-card.state-wrong   {{ border-color: var(--opt-wrong-border); }}
.q-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }}
.q-num  {{ font-size: 10px; font-weight: 700; letter-spacing: 3px; color: var(--scrollbar-thumb); text-transform: uppercase; }}
.q-badge {{ font-size: 9px; font-weight: 700; letter-spacing: 1.5px; padding: 3px 10px; border-radius: 100px; text-transform: uppercase; }}
.badge-mcq {{ background: var(--border-card); color: var(--primary); border: 1px solid var(--scrollbar-thumb); }}
.badge-tf  {{ background: var(--badge-tf-bg); color: var(--badge-tf-text); border: 1px solid var(--badge-tf-border); }}
.q-text {{ font-size: 17px; font-weight: 500; color: var(--text-card-title); line-height: 1.65; margin-bottom: 0; text-align: left; }}

.opt {{ border-radius: 12px; padding: 14px 20px; font-size: 14px; font-weight: 500; margin-bottom: 8px; line-height: 1.5; transition: all .2s; display: flex; align-items: center; height: 100%; }}
.opt-correct {{ background: var(--opt-correct-bg); border: 1.5px solid var(--opt-correct-border); color: var(--opt-correct-text); text-align: left; direction: ltr; }}
.opt-wrong   {{ background: var(--opt-wrong-bg); border: 1.5px solid var(--opt-wrong-border); color: var(--opt-wrong-text); text-decoration: line-through; text-align: left; direction: ltr; }}
.opt-reveal  {{ background: var(--opt-correct-bg); border: 1.5px solid var(--opt-correct-border); color: var(--opt-correct-text); opacity: 0.8; text-align: left; direction: ltr; }}
.opt-neutral {{ background: var(--opt-neutral-bg); border: 1.5px solid var(--border-card); color: var(--text-main); text-align: left; direction: ltr; }}

.explain-box {{ border-radius: 12px; padding: 16px 20px; font-size: 14px; line-height: 1.75; margin-top: 6px; margin-bottom: 4px; direction: rtl; text-align: right; }}
.explain-correct {{ background: var(--opt-correct-bg); border: 1px solid var(--opt-correct-border); color: var(--opt-correct-text); }}
.explain-wrong   {{ background: var(--opt-wrong-bg); border: 1px solid var(--opt-wrong-border); color: var(--opt-wrong-text); }}
.q-sep {{ height: 1px; background: var(--border-line); margin: 20px 0; }}

/* Base Button CSS */
div[data-testid="stButton"] button {{ background: var(--btn-bg) !important; border: 1px solid var(--btn-border) !important; border-radius: 10px !important; color: var(--text-muted) !important; font-size: 14px !important; font-weight: 500 !important; padding: 12px 16px !important; transition: all .2s !important; width: 100% !important; height: 100% !important; }}
div[data-testid="stButton"] button:hover {{ border-color: var(--primary) !important; color: var(--primary) !important; background: var(--btn-hover) !important; }}

/* 🚀 Special Styling for Theme Toggle Button */
div[data-testid="stButton"][aria-label*="Mode"] button {{
    border-radius: 50px !important;
    border: 1px solid var(--primary) !important;
    color: var(--primary) !important;
    background: var(--badge-bg) !important;
    font-weight: 700 !important;
    margin-bottom: 10px;
    font-family: sans-serif !important;
}}
div[data-testid="stButton"][aria-label*="Mode"] button:hover {{
    background: var(--primary) !important;
    color: #fff !important;
}}

#MainMenu, footer, header {{ visibility: hidden; }}
.stDeployButton {{ display: none; }}
@keyframes fadeUp {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: translateY(0); }} }}
.q-card, .subject-card, .lec-card {{ animation: fadeUp .3s ease both; }}
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
    subj_count = max(1, min(len(SUBJECTS), 3))
    cols = st.columns(subj_count)
    for idx, subj in enumerate(SUBJECTS):
        with cols[idx % subj_count]:
            st.markdown(f"""
            <div class="subject-card">
                <span class="subj-icon">{subj['icon']}</span>
                <div class="subj-name">{subj['name']}</div>
                <div class="subj-code">{subj['code']}</div>
                <div class="subj-desc">{subj['desc']}</div>
            </div>""", unsafe_allow_html=True)
            st.button("اختر المادة", key=f"btn_{subj['key']}",
                      on_click=go_to_page, args=("lectures", subj["key"]),
                      use_container_width=True)

# ════════════════════════════════════════════════════════════
# 2️⃣  PAGE: LECTURES
# ════════════════════════════════════════════════════════════
elif st.session_state.page == "lectures":
    cur_subj = next(s for s in SUBJECTS if s["key"] == st.session_state.sel_subj)

    col1, col2 = st.columns([10, 2])
    with col2:
        st.button("🔙 رجوع للمواد", on_click=go_to_page, args=("subjects",), use_container_width=True)
    with col1:
        section_header(f"محاضرات · {cur_subj['name']}")

    num_lecs  = len(cur_subj["lectures"])
    col_count = max(1, min(num_lecs, 3))
    lec_cols  = st.columns(col_count)

    for idx, lec in enumerate(cur_subj["lectures"]):
        with lec_cols[idx % col_count]:
            is_special = lec.get("special", False)
            sp_class = "special-card" if is_special else ""
            locked_cls = "locked" if not lec['available'] else ""
            
            # عرض الكارت، لو سبيشال هيظهر بشكل وكلمة مختلفة
            st.markdown(f"""
            <div class="lec-card {sp_class} {locked_cls}">
                <div class="lec-num">{'✨' if is_special else 'Lecture'} {lec['num']}</div>
                <div class="lec-title">{lec['title']}</div>
                <span class="lec-count-badge">{lec['count']}</span>
                {'' if lec['available'] else '<div class="soon-tag">قريباً ⏳</div>'}
            </div>""", unsafe_allow_html=True)

            if lec["available"]:
                btn_label = "🔥 ابدأ التحدي" if is_special else "ابدأ الاختبار"
                st.button(btn_label, key=f"btn_{lec['key']}", on_click=go_to_page, args=("quiz", None, lec["key"]), use_container_width=True)
            else:
                st.button("مغلق", key=f"locked_{lec['key']}", disabled=True, use_container_width=True)

# ════════════════════════════════════════════════════════════
# 3️⃣  PAGE: QUIZ
# ════════════════════════════════════════════════════════════
elif st.session_state.page == "quiz":
    questions = QUESTIONS_DB.get(st.session_state.sel_lec, [])

    col1, col2 = st.columns([10, 2])
    with col2:
        st.button("🔙 للمحاضرات", on_click=go_to_page, args=("lectures",), use_container_width=True)
    with col1:
        section_header("الاختبار")

    if not questions:
        st.markdown("<p style='color:var(--text-muted);text-align:center;padding:40px'>لا توجد أسئلة بعد.</p>", unsafe_allow_html=True)
    else:
        answered = len(st.session_state.answers)
        score    = sum(1 for idx, v in st.session_state.answers.items() if v == questions[idx]["ans"])
        total    = len(questions)
        pct_done = answered / total if total else 0

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
                st.button("🔄 إعادة المحاولة (بترتيب جديد)", on_click=retry_quiz, use_container_width=True)
            with c_btn2:
                if score < total:
                    lbl = "📖 عرض كل الأسئلة" if st.session_state.show_mistakes_only else "🔍 مراجعة أخطائي فقط"
                    st.button(lbl, on_click=toggle_mistakes, use_container_width=True)
                
            st.markdown("<div style='margin-bottom:32px'></div>", unsafe_allow_html=True)