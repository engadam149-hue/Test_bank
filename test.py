import streamlit as st
import random  # 👈 ضفنا مكتبة العشوائية هنا

# 📦 استدعاء البيانات من ملف data.py
from data import SUBJECTS, QUESTIONS_DB

st.set_page_config(page_title="بنك أسئلة NMU", page_icon="📚", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;700;800&display=swap');
* { font-family: 'Tajawal', sans-serif !important; }
[data-testid="stSidebar"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
.stApp { background: #0d0b1a; }
.hero { background: linear-gradient(135deg, #1a0533 0%, #0d0b1a 50%, #001a33 100%); border: 1px solid #2a1f4a; border-radius: 24px; padding: 48px 40px; text-align: center; margin-bottom: 40px; }
.uni-name { font-size: 13px; font-weight: 700; letter-spacing: 4px; color: #a78bfa; margin-bottom: 12px; }
.hero h1 { font-size: 42px; font-weight: 800; color: #f0eeff; margin-bottom: 10px; }
.hero h1 span { color: #a78bfa; }
.hero p { color: #6a6480; font-size: 15px; }
.section-title { font-size: 13px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #4a4560; margin-bottom: 16px; text-align: center; }
.subject-card { background: #12101e; border: 1.5px solid #1e1c2e; border-radius: 18px; padding: 28px 24px; text-align: right; direction: rtl; cursor: pointer; transition: all 0.25s ease; }
.subject-card:hover { border-color: #6c63ff; transform: translateY(-4px); box-shadow: 0 12px 40px #6c63ff22; }
.subject-card.active { border-color: #a78bfa; background: #1a1530; box-shadow: 0 0 0 1px #a78bfa44, 0 12px 40px #6c63ff22; }
.subject-icon { font-size: 32px; margin-bottom: 12px; }
.subject-name { font-size: 16px; font-weight: 700; color: #f0eeff; margin-bottom: 4px; }
.subject-code { font-size: 12px; color: #a78bfa; font-weight: 600; letter-spacing: 1px; }
.subject-desc { font-size: 13px; color: #5a5570; margin-top: 8px; }
.lecture-card { background: #12101e; border: 1.5px solid #1e1c2e; border-radius: 14px; padding: 20px; text-align: right; direction: rtl; cursor: pointer; transition: all 0.2s; }
.lecture-card:hover { border-color: #6c63ff; transform: translateY(-2px); }
.lecture-card.active { border-color: #a78bfa; background: #1a1530; }
.lecture-card.coming-soon { opacity: 0.4; cursor: not-allowed; }
.lec-num { font-size: 11px; color: #a78bfa; font-weight: 700; letter-spacing: 2px; margin-bottom: 6px; }
.lec-title { font-size: 15px; font-weight: 700; color: #e0ddf5; margin-bottom: 4px; }
.lec-count { font-size: 12px; color: #4a4560; }
.question-card { background: #12101e; border: 1px solid #1e1c2e; border-radius: 16px; padding: 28px; margin-bottom: 6px; direction: ltr; }
.question-card.correct-card { border-color: #22c55e44; }
.question-card.wrong-card { border-color: #ef444444; }
.q-meta { font-size: 11px; font-weight: 700; letter-spacing: 2px; color: #3a3555; text-transform: uppercase; margin-bottom: 6px; }
.q-type-badge { display: inline-block; font-size: 10px; font-weight: 700; letter-spacing: 1px; padding: 2px 10px; border-radius: 20px; margin-bottom: 10px; }
.q-type-tf  { background: #1a2a3a; color: #60a5fa; border: 1px solid #60a5fa44; }
.q-type-mcq { background: #1a1a2a; color: #a78bfa; border: 1px solid #a78bfa44; }
.q-text { font-size: 16px; font-weight: 500; color: #e0ddf5; line-height: 1.6; margin-bottom: 16px; }
.correct-opt { background: #15291e; border: 1.5px solid #22c55e; border-radius: 10px; padding: 12px 18px; color: #4ade80; font-size: 14px; margin-bottom: 8px; direction: rtl; text-align: right; }
.wrong-opt   { background: #2a1515; border: 1.5px solid #ef4444; border-radius: 10px; padding: 12px 18px; color: #f87171; font-size: 14px; margin-bottom: 8px; direction: rtl; text-align: right; }
.reveal-opt  { background: #15291e88; border: 1.5px solid #22c55e55; border-radius: 10px; padding: 12px 18px; color: #4ade8077; font-size: 14px; margin-bottom: 8px; direction: rtl; text-align: right; }
.neutral-opt { background: #1a1826; border: 1.5px solid #252235; border-radius: 10px; padding: 12px 18px; color: #5a5570; font-size: 14px; margin-bottom: 8px; direction: rtl; text-align: right; }
.explain-box { border-radius: 10px; padding: 14px 18px; font-size: 14px; line-height: 1.7; margin-top: 4px; margin-bottom: 14px; direction: rtl; text-align: right; }
.explain-correct { background: #0f2318; border: 1px solid #22c55e33; color: #86efac; }
.explain-wrong   { background: #2a1515; border: 1px solid #ef444433; color: #fca5a5; }
.score-banner { background: linear-gradient(135deg, #1a1530, #12101e); border: 1px solid #6c63ff44; border-radius: 20px; padding: 40px; text-align: center; margin-bottom: 24px; direction: rtl; }
.score-big   { font-size: 64px; font-weight: 800; color: #a78bfa; line-height: 1; margin-bottom: 8px; }
.score-label { font-size: 18px; font-weight: 700; color: #f0eeff; margin-bottom: 4px; }
.score-sub   { font-size: 14px; color: #5a5570; }
div[data-testid="stProgress"] > div > div { background: linear-gradient(90deg, #6c63ff, #a855f7) !important; }
div[data-testid="stButton"] button { background: #1a1826 !important; border: 1.5px solid #252235 !important; border-radius: 10px !important; color: #c4c0d8 !important; font-size: 14px !important; padding: 12px 16px !important; width: 100% !important; text-align: center !important; transition: all 0.2s !important; }
div[data-testid="stButton"] button:hover { border-color: #6c63ff !important; color: #e0ddf5 !important; }
</style>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# 🔧 Session State (تم إضافة seed للعشوائية)
# ════════════════════════════════════════════════════════════

for k, v in [("sel_subj", None), ("sel_lec", None), ("answers", {}), ("seed", 42)]:
    if k not in st.session_state:
        st.session_state[k] = v

# ════════════════════════════════════════════════════════════
# 🎨 UI
# ════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero">
    <div class="uni-name">🎓 جامعة المنصورة الجديدة · NMU</div>
    <h1>بنك <span>أسئلة</span> الدفعة</h1>
    <p>اختر المادة والمحاضرة وابدأ المذاكرة — مع تصحيح وشرح فوري لكل إجابة</p>
</div>
""", unsafe_allow_html=True)

# ── اختيار المادة
st.markdown('<div class="section-title">· اختر المادة ·</div>', unsafe_allow_html=True)
cols = st.columns(len(SUBJECTS))
for idx, subj in enumerate(SUBJECTS):
    with cols[idx]:
        active = st.session_state.sel_subj == subj["key"]
        st.markdown(f"""
        <div class="subject-card {'active' if active else ''}">
            <div class="subject-icon">{subj['icon']}</div>
            <div class="subject-name">{subj['name']}</div>
            <div class="subject-code">{subj['code']}</div>
            <div class="subject-desc">{subj['desc']}</div>
        </div>""", unsafe_allow_html=True)
        if st.button(f"اختر {subj['name']}", key=f"s_{subj['key']}", use_container_width=True):
            st.session_state.sel_subj = subj["key"]
            st.session_state.sel_lec  = None
            st.session_state.answers  = {}
            st.rerun()

# ── اختيار المحاضرة
if st.session_state.sel_subj:
    st.markdown("---")
    st.markdown('<div class="section-title">· اختر المحاضرة ·</div>', unsafe_allow_html=True)
    cur = next(s for s in SUBJECTS if s["key"] == st.session_state.sel_subj)
    lec_cols = st.columns(len(cur["lectures"]))
    for idx, lec in enumerate(cur["lectures"]):
        with lec_cols[idx]:
            active = st.session_state.sel_lec == lec["key"]
            st.markdown(f"""
            <div class="lecture-card {'active' if active else ''} {'coming-soon' if not lec['available'] else ''}">
                <div class="lec-num">Lecture {lec['num']}</div>
                <div class="lec-title">{lec['title']}</div>
                <div class="lec-count">{lec['count']}</div>
            </div>""", unsafe_allow_html=True)
            if lec["available"]:
                if st.button(f"ابدأ {lec['title']}", key=f"l_{lec['key']}", use_container_width=True):
                    st.session_state.sel_lec = lec["key"]
                    st.session_state.answers = {}
                    st.session_state.seed = random.randint(1, 10000) # 👈 تحديث العشوائية
                    st.rerun()
            else:
                st.markdown("<p style='color:#3a3555;font-size:13px;text-align:center;'>قريباً...</p>", unsafe_allow_html=True)

# ── الكويز
if st.session_state.sel_lec:
    questions = QUESTIONS_DB.get(st.session_state.sel_lec, [])
    if questions:
        st.markdown("---")
        answered = len(st.session_state.answers)
        score    = sum(1 for i, v in st.session_state.answers.items() if v == questions[i]["ans"])
        total    = len(questions)

        st.progress(answered / total,
            text=f"تم الإجابة على {answered} من {total}  |  ✅ {score} صح  |  ❌ {answered - score} غلط")

        if answered == total:
            pct   = int((score / total) * 100)
            emoji = "🏆" if pct==100 else "🎉" if pct>=80 else "👍" if pct>=60 else "📚"
            msg   = "نتيجة مثالية!" if pct==100 else "ممتاز!" if pct>=80 else "جيد، كمّل!" if pct>=60 else "راجع المحاضرة تاني!"
            if pct == 100: st.balloons()
            st.markdown(f"""
            <div class="score-banner">
                <div class="score-big">{score}<span style="font-size:32px;color:#4a4560">/{total}</span></div>
                <div class="score-label">{emoji} {msg}</div>
                <div class="score-sub">{pct}% إجابات صحيحة</div>
            </div>""", unsafe_allow_html=True)
            if st.button("🔄 إعادة المحاولة", use_container_width=True):
                st.session_state.answers = {}
                st.session_state.seed = random.randint(1, 10000) # 👈 تحديث العشوائية
                st.rerun()
            st.markdown("---")

        for i, q in enumerate(questions):
            chosen      = st.session_state.answers.get(i)
            is_answered = chosen is not None
            is_correct  = chosen == q["ans"]
            q_type      = q.get("type", "mcq")
            card_cls    = "correct-card" if is_answered and is_correct else "wrong-card" if is_answered else ""
            badge_lbl   = "TRUE / FALSE" if q_type == "tf" else "MCQ"
            badge_cls   = "q-type-tf"   if q_type == "tf" else "q-type-mcq"

            st.markdown(f"""
            <div class="question-card {card_cls}">
                <div class="q-meta">Question {str(i+1).zfill(2)}</div>
                <span class="q-type-badge {badge_cls}">{badge_lbl}</span>
                <div class="q-text">{q['q']}</div>
            </div>""", unsafe_allow_html=True)

            if is_answered:
                for opt in q["options"]:
                    if opt == q["ans"] and opt == chosen:
                        st.markdown(f'<div class="correct-opt">✅ {opt}</div>', unsafe_allow_html=True)
                    elif opt == chosen:
                        st.markdown(f'<div class="wrong-opt">❌ {opt}</div>', unsafe_allow_html=True)
                    elif opt == q["ans"]:
                        st.markdown(f'<div class="reveal-opt">✅ {opt} ← الإجابة الصحيحة</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="neutral-opt">{opt}</div>', unsafe_allow_html=True)

                exp_key = "explain_correct" if is_correct else "explain_wrong"
                exp_cls = "explain-correct"  if is_correct else "explain-wrong"
                exp_txt = q.get(exp_key, "")
                if exp_txt:
                    st.markdown(f'<div class="explain-box {exp_cls}">{exp_txt}</div>', unsafe_allow_html=True)
            else:
                opt_cols = st.columns(2)
                
                # 👈 هنا بنلخبط الاختيارات بذكاء
                shuffled_opts = q["options"].copy()
                random.Random(st.session_state.seed + i).shuffle(shuffled_opts)
                
                for j, opt in enumerate(shuffled_opts):
                    with opt_cols[j % 2]:
                        # ربطنا الزرار بالإجابة نفسها عشان Streamlit ميتلخبطش
                        if st.button(opt, key=f"q{i}_{opt}", use_container_width=True):
                            st.session_state.answers[i] = opt
                            st.rerun()

            st.markdown("<div style='margin-bottom:12px'></div>", unsafe_allow_html=True)