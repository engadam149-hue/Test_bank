import streamlit as st
import random
from data import SUBJECTS, QUESTIONS_DB

# ════════════════════════════════════════════════════════════
# ⚙️ Page Config
# ════════════════════════════════════════════════════════════
st.set_page_config(page_title="بنك أسئلة NMU", page_icon="📚", layout="wide")

# ════════════════════════════════════════════════════════════
# 🎨 CSS — Luxury Dark Academy
# ════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Tajawal:wght@300;400;500;700;800&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
* { font-family: 'Tajawal', sans-serif !important; }
[data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }
.stApp { background: #08070f; color: #e8e4f0; }
section[data-testid="stMain"] > div { padding-top: 0 !important; }
.block-container { padding: 0 2rem 4rem !important; max-width: 1200px !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #08070f; }
::-webkit-scrollbar-thumb { background: #3d2d6e; border-radius: 4px; }

/* ════ HERO ════ */
.hero {
    position: relative; overflow: hidden;
    background: #0c0a18;
    border-bottom: 1px solid #1e1633;
    padding: 56px 48px 48px;
    margin: 0 -2rem 48px;
    text-align: center;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 50% -10%, #2d1b6933 0%, transparent 70%),
        radial-gradient(ellipse 40% 40% at 20% 100%, #0a1f4422 0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 80% 100%, #1a0d3322 0%, transparent 60%);
}
.hero::after {
    content: '';
    position: absolute; bottom: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, #7c3aed55, #c4b5fd44, #7c3aed55, transparent);
}
.hero-inner { position: relative; z-index: 1; }
.hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: #1a1333; border: 1px solid #3d2d6e;
    border-radius: 100px; padding: 6px 18px;
    font-size: 11px; font-weight: 700; letter-spacing: 3px;
    color: #a78bfa; text-transform: uppercase; margin-bottom: 20px;
}
.hero-badge::before { content: '◆'; font-size: 8px; color: #7c3aed; }
.hero-title {
    font-family: 'Playfair Display', serif !important;
    font-size: clamp(36px, 5vw, 56px); font-weight: 800;
    color: #f0eeff; line-height: 1.1; margin-bottom: 12px;
    letter-spacing: -1px;
}
.hero-title em { font-style: normal; color: #a78bfa; }
.hero-sub {
    font-size: 15px; color: #5a5078; max-width: 480px;
    margin: 0 auto; line-height: 1.7;
}
.hero-stats {
    display: flex; justify-content: center; gap: 40px;
    margin-top: 32px; padding-top: 28px;
    border-top: 1px solid #1e1633;
}
.stat { text-align: center; }
.stat-num { font-size: 24px; font-weight: 800; color: #a78bfa; line-height: 1; }
.stat-lbl { font-size: 11px; color: #3d3558; font-weight: 600; letter-spacing: 1px; margin-top: 4px; }

/* ════ SECTION HEADER ════ */
.section-hdr {
    display: flex; align-items: center; gap: 14px;
    margin-bottom: 20px;
}
.section-hdr-line {
    flex: 1; height: 1px;
    background: linear-gradient(90deg, #1e1633, transparent);
}
.section-hdr-line.right {
    background: linear-gradient(270deg, #1e1633, transparent);
}
.section-hdr-label {
    font-size: 10px; font-weight: 700; letter-spacing: 4px;
    color: #3d2d6e; text-transform: uppercase; white-space: nowrap;
}

/* ════ SUBJECT CARDS ════ */
.subject-card {
    background: #0e0c1a;
    border: 1px solid #1a1530;
    border-radius: 20px;
    padding: 28px 24px;
    text-align: right; direction: rtl;
    transition: border-color 0.25s, transform 0.25s, box-shadow 0.25s;
    cursor: pointer; height: 100%;
    position: relative; overflow: hidden;
}
.subject-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, transparent, #3d2d6e, transparent);
    opacity: 0; transition: opacity 0.3s;
}
.subject-card.active {
    border-color: #7c3aed;
    background: #110e20;
    box-shadow: 0 0 0 1px #7c3aed33, 0 20px 60px #7c3aed1a;
}
.subject-card.active::before { opacity: 1; }
.subj-icon { font-size: 36px; margin-bottom: 14px; display: block; }
.subj-name { font-size: 16px; font-weight: 700; color: #e8e4f0; margin-bottom: 4px; }
.subj-code {
    font-size: 10px; font-weight: 700; letter-spacing: 2px;
    color: #7c3aed; text-transform: uppercase; margin-bottom: 10px;
}
.subj-desc { font-size: 13px; color: #3d3558; line-height: 1.5; }
.subj-arrow {
    position: absolute; bottom: 20px; left: 20px;
    width: 28px; height: 28px; border-radius: 50%;
    background: #1a1530; border: 1px solid #2a2045;
    display: flex; align-items: center; justify-content: center;
    font-size: 12px; color: #4a3d78;
    transition: all 0.25s;
}
.subject-card.active .subj-arrow {
    background: #7c3aed22; border-color: #7c3aed55; color: #a78bfa;
}

/* ════ LECTURE CARDS ════ */
.lec-card {
    background: #0e0c1a; border: 1px solid #1a1530;
    border-radius: 14px; padding: 18px 20px;
    text-align: right; direction: rtl;
    transition: all 0.2s; cursor: pointer;
    position: relative;
    height: 100%;
}
.lec-card:hover { border-color: #3d2d6e; transform: translateY(-2px); }
.lec-card.locked { opacity: 0.35; cursor: not-allowed; }
.lec-num {
    font-size: 9px; font-weight: 700; letter-spacing: 3px;
    color: #3d2d6e; text-transform: uppercase; margin-bottom: 8px;
}
.lec-title { font-size: 14px; font-weight: 700; color: #c8c0e0; margin-bottom: 6px; }
.lec-count-badge {
    display: inline-block; background: #1a1530;
    border: 1px solid #2a2045; border-radius: 100px;
    padding: 2px 10px; font-size: 11px; color: #4a3d78;
}
.soon-tag {
    font-size: 10px; color: #2a2045; font-weight: 600;
    letter-spacing: 1px; margin-top: 6px;
}

/* ════ PROGRESS BAR ════ */
.prog-wrap {
    background: #0e0c1a; border: 1px solid #1a1530;
    border-radius: 16px; padding: 20px 24px;
    margin-bottom: 28px; direction: rtl;
}
.prog-top {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 12px;
}
.prog-label { font-size: 13px; color: #5a5078; font-weight: 600; }
.prog-stats { display: flex; gap: 16px; }
.prog-stat { font-size: 13px; font-weight: 700; }
.prog-stat.correct { color: #4ade80; }
.prog-stat.wrong { color: #f87171; }
.prog-bar-bg { background: #1a1530; border-radius: 100px; height: 6px; overflow: hidden; }
.prog-bar-fill {
    height: 100%; border-radius: 100px;
    background: linear-gradient(90deg, #7c3aed, #a78bfa);
    transition: width 0.4s ease;
}

/* ════ SCORE BANNER ════ */
.score-banner {
    background: #0e0c1a; border: 1px solid #1e1633;
    border-radius: 24px; padding: 48px 40px;
    text-align: center; margin-bottom: 32px;
    position: relative; overflow: hidden;
    direction: rtl;
}
.score-banner::before {
    content: '';
    position: absolute; top: -50%; left: 50%; transform: translateX(-50%);
    width: 300px; height: 300px; border-radius: 50%;
    background: radial-gradient(circle, #7c3aed0d 0%, transparent 70%);
}
.score-ring {
    width: 120px; height: 120px; border-radius: 50%;
    border: 3px solid #1e1633; margin: 0 auto 20px;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    position: relative; background: #0c0a18;
    box-shadow: 0 0 0 1px #7c3aed22, inset 0 0 30px #7c3aed08;
}
.score-ring-num { font-size: 36px; font-weight: 800; color: #a78bfa; line-height: 1; }
.score-ring-den { font-size: 14px; color: #3d2d6e; }
.score-title { font-size: 22px; font-weight: 800; color: #e8e4f0; margin-bottom: 6px; }
.score-pct { font-size: 14px; color: #5a5078; }

/* ════ QUESTION CARD ════ */
.q-card {
    background: #0e0c1a;
    border: 1px solid #1a1530;
    border-radius: 18px; padding: 28px 32px;
    margin-bottom: 8px; direction: ltr;
    transition: border-color 0.3s;
}
.q-card.state-correct { border-color: #166534; }
.q-card.state-wrong   { border-color: #7f1d1d; }
.q-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
.q-num { font-size: 10px; font-weight: 700; letter-spacing: 3px; color: #3d2d6e; text-transform: uppercase; }
.q-badge { font-size: 9px; font-weight: 700; letter-spacing: 1.5px; padding: 3px 10px; border-radius: 100px; text-transform: uppercase; }
.badge-mcq { background: #1a1530; color: #7c3aed; border: 1px solid #3d2d6e; }
.badge-tf  { background: #0d1f30; color: #3b82f6; border: 1px solid #1e3a5f; }
.q-text { font-size: 17px; font-weight: 500; color: #d8d4ec; line-height: 1.65; margin-bottom: 0; text-align: left; }

/* ════ OPTIONS ════ */
.opt {
    border-radius: 12px; padding: 14px 20px;
    font-size: 14px; font-weight: 500;
    margin-bottom: 8px; direction: rtl; text-align: right;
    line-height: 1.5; transition: all 0.2s;
}
.opt-correct { background: #0a1f12; border: 1.5px solid #16a34a; color: #4ade80; text-align: left; direction: ltr; }
.opt-wrong { background: #1c0a0a; border: 1.5px solid #dc2626; color: #f87171; text-decoration: line-through; text-align: left; direction: ltr;}
.opt-reveal { background: #0a1f1288; border: 1.5px solid #16a34a66; color: #4ade8066; text-align: left; direction: ltr;}
.opt-neutral { background: #0e0c1a; border: 1.5px solid #1a1530; color: #e0ddf5; text-align: left; direction: ltr;}

/* ════ EXPLAIN BOX ════ */
.explain-box {
    border-radius: 12px; padding: 16px 20px;
    font-size: 14px; line-height: 1.75;
    margin-top: 6px; margin-bottom: 4px;
    direction: rtl; text-align: right;
}
.explain-correct { background: #091510; border: 1px solid #14532d55; color: #86efac; }
.explain-wrong   { background: #180a0a; border: 1px solid #7f1d1d55; color: #fca5a5; }

/* ════ DIVIDER ════ */
.q-sep { height: 1px; background: #12101e; margin: 20px 0; }

/* ════ STREAMLIT BUTTON OVERRIDE ════ */
div[data-testid="stButton"] button {
    background: #0e0c1a !important; border: 1px solid #1e1a30 !important;
    border-radius: 10px !important; color: #8b80a8 !important;
    font-size: 14px !important; font-weight: 500 !important;
    padding: 12px 16px !important; transition: all 0.2s !important;
    width: 100% !important; height: 100% !important; /* Added height 100% for alignment */
}
div[data-testid="stButton"] button:hover {
    border-color: #5b21b6 !important; color: #c4b5fd !important;
    background: #110e20 !important;
}
/* Back button special style */
div[data-testid="stButton"][aria-label*="back"] button {
    border-color: #1e1a30 !important;
    font-size: 12px !important;
}

/* ════ HIDE STREAMLIT CHROME ════ */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ════ TRANSITION HACK ════ */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.q-card, .subject-card, .lec-card { animation: fadeUp 0.3s ease both; }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# 🔧 Session State & Routing (تم تطبيق تحسيناتك هنا ✅)
# ════════════════════════════════════════════════════════════
for k, v in [("page", "subjects"), ("sel_subj", None), ("sel_lec", None), ("answers", {}), ("seed", 42)]:
    if k not in st.session_state:
        st.session_state[k] = v

def go_to_page(page_name, subj=None, lec=None):
    st.session_state.page = page_name
    
    # 👈 إصلاح الـ State عند الرجوع للصفحة الرئيسية
    if page_name == "subjects":
        st.session_state.sel_subj = None
        st.session_state.sel_lec = None
        
    # 👈 إصلاح الـ State عند اختيار مادة أو الرجوع للمحاضرات
    elif page_name == "lectures":
        if subj: 
            st.session_state.sel_subj = subj
        st.session_state.sel_lec = None
        
    # فتح الاختبار
    elif page_name == "quiz":
        if lec:  
            st.session_state.sel_lec = lec
            st.session_state.answers = {}
            st.session_state.seed = random.randint(1, 10000)

def record_answer(q_idx, opt):
    st.session_state.answers[q_idx] = opt

def retry_quiz():
    st.session_state.answers = {}
    st.session_state.seed = random.randint(1, 10000)

# Helper for Headers
def section_header(label):
    st.markdown(f"""
    <div class="section-hdr">
        <div class="section-hdr-line"></div>
        <div class="section-hdr-label">{label}</div>
        <div class="section-hdr-line right"></div>
    </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# 1️⃣ PAGE: SUBJECTS
# ════════════════════════════════════════════════════════════
if st.session_state.page == "subjects":
    total_q = sum(len(v) for v in QUESTIONS_DB.values())
    total_lec = sum(len(s["lectures"]) for s in SUBJECTS)

    st.markdown(f"""
    <div class="hero">
        <div class="hero-inner">
            <div class="hero-badge">🎓 جامعة المنصورة الجديدة · NMU</div>
            <div class="hero-title">بنك <em>أسئلة</em> الدفعة</div>
            <div class="hero-sub">اختر المادة والمحاضرة وابدأ المذاكرة — مع تصحيح وشرح فوري لكل إجابة</div>
            <div class="hero-stats">
                <div class="stat"><div class="stat-num">{len(SUBJECTS)}</div><div class="stat-lbl">مادة</div></div>
                <div class="stat"><div class="stat-num">{total_lec}</div><div class="stat-lbl">محاضرة</div></div>
                <div class="stat"><div class="stat-num">{total_q}+</div><div class="stat-lbl">سؤال</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    section_header("اختر المادة")
    
    # أعمدة المواد (Dynamic)
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
            st.button("اختر المادة", key=f"btn_{subj['key']}", on_click=go_to_page, args=("lectures", subj["key"]), use_container_width=True)

# ════════════════════════════════════════════════════════════
# 2️⃣ PAGE: LECTURES
# ════════════════════════════════════════════════════════════
elif st.session_state.page == "lectures":
    cur_subj = next(s for s in SUBJECTS if s["key"] == st.session_state.sel_subj)
    
    col1, col2 = st.columns([10, 2])
    with col2: 
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        st.button("🔙 رجوع للمواد", on_click=go_to_page, args=("subjects",), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col1: section_header(f"محاضرات · {cur_subj['name']}")

    # 👈 جعل الأعمدة ديناميكية بناءً على عدد المحاضرات الفعلي (بحد أقصى 3)
    num_lecs = len(cur_subj["lectures"])
    col_count = max(1, min(num_lecs, 3)) 
    lec_cols = st.columns(col_count)
    
    for idx, lec in enumerate(cur_subj["lectures"]):
        with lec_cols[idx % col_count]:
            st.markdown(f"""
            <div class="lec-card {'locked' if not lec['available'] else ''}">
                <div class="lec-num">Lecture {lec['num']}</div>
                <div class="lec-title">{lec['title']}</div>
                <span class="lec-count-badge">{lec['count']}</span>
                {'' if lec['available'] else '<div class="soon-tag">قريباً ⏳</div>'}
            </div>""", unsafe_allow_html=True)
            
            if lec["available"]:
                st.button("ابدأ الاختبار", key=f"btn_{lec['key']}", on_click=go_to_page, args=("quiz", None, lec["key"]), use_container_width=True)
            else:
                st.button("مغلق", key=f"locked_{lec['key']}", disabled=True, use_container_width=True)

# ════════════════════════════════════════════════════════════
# 3️⃣ PAGE: QUIZ
# ════════════════════════════════════════════════════════════
elif st.session_state.page == "quiz":
    questions = QUESTIONS_DB.get(st.session_state.sel_lec, [])
    
    col1, col2 = st.columns([10, 2])
    with col2: 
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        st.button("🔙 رجوع للمحاضرات", on_click=go_to_page, args=("lectures",), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col1: section_header("الاختبار")

    if not questions:
        st.markdown("<p style='color:#3d2d6e;text-align:center;padding:40px'>لا توجد أسئلة بعد.</p>", unsafe_allow_html=True)
    else:
        answered = len(st.session_state.answers)
        score    = sum(1 for i, v in st.session_state.answers.items() if v == questions[i]["ans"])
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
            <div class="prog-bar-bg"><div class="prog-bar-fill" style="width:{pct_done*100:.1f}%"></div></div>
        </div>""", unsafe_allow_html=True)

        if answered == total:
            pct = int((score / total) * 100)
            if pct == 100: emoji, msg = "🏆", "نتيجة مثالية!"
            elif pct >= 80: emoji, msg = "🎉", "ممتاز جداً!"
            elif pct >= 60: emoji, msg = "👍", "جيد، كمّل!"
            else: emoji, msg = "📚", "راجع المحاضرة تاني!"
            
            if pct == 100: st.balloons()
            st.markdown(f"""
            <div class="score-banner">
                <div class="score-ring"><div class="score-ring-num">{score}</div><div class="score-ring-den">/ {total}</div></div>
                <div class="score-title">{emoji} {msg}</div>
                <div class="score-pct">{pct}% إجابات صحيحة</div>
            </div>""", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([2, 3, 2])
            with c2: st.button("🔄 إعادة المحاولة", on_click=retry_quiz, use_container_width=True)
            st.markdown("<div style='margin-bottom:32px'></div>", unsafe_allow_html=True)

        for i, q in enumerate(questions):
            chosen      = st.session_state.answers.get(i)
            is_answered = chosen is not None
            is_correct  = chosen == q["ans"]
            q_type      = q.get("type", "mcq")

            card_cls  = "state-correct" if is_answered and is_correct else ("state-wrong" if is_answered else "")
            badge_lbl = "True / False" if q_type == "tf" else "MCQ"
            badge_cls = "badge-tf" if q_type == "tf" else "badge-mcq"

            st.markdown(f"""
            <div class="q-card {card_cls}">
                <div class="q-header">
                    <span class="q-num">Q{str(i+1).zfill(2)}</span>
                    <span class="q-badge {badge_cls}">{badge_lbl}</span>
                </div>
                <div class="q-text">{q['q']}</div>
            </div>""", unsafe_allow_html=True)

            if is_answered:
                for opt in q["options"]:
                    if opt == q["ans"] and opt == chosen:
                        st.markdown(f'<div class="opt opt-correct">✅ &nbsp;{opt}</div>', unsafe_allow_html=True)
                    elif opt == chosen:
                        st.markdown(f'<div class="opt opt-wrong">❌ &nbsp;{opt}</div>', unsafe_allow_html=True)
                    elif opt == q["ans"]:
                        st.markdown(f'<div class="opt opt-reveal">✅ &nbsp;{opt} &nbsp;<span style="font-size:12px;opacity:.6">← الإجابة الصحيحة</span></div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="opt opt-neutral">{opt}</div>', unsafe_allow_html=True)

                exp_key = "explain_correct" if is_correct else "explain_wrong"
                exp_cls = "explain-correct"  if is_correct else "explain-wrong"
                exp_txt = q.get(exp_key, "")
                if exp_txt: st.markdown(f'<div class="explain-box {exp_cls}">{exp_txt}</div>', unsafe_allow_html=True)
            else:
                shuffled = q["options"].copy()
                random.Random(st.session_state.seed + i).shuffle(shuffled)
                opt_cols = st.columns(2)
                for j, opt in enumerate(shuffled):
                    with opt_cols[j % 2]:
                        st.button(opt, key=f"q{i}_{opt}", on_click=record_answer, args=(i, opt), use_container_width=True)

            st.markdown("<div class='q-sep'></div>", unsafe_allow_html=True)