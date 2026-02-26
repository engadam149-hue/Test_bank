import streamlit as st

st.set_page_config(page_title="بنك أسئلة NMU", page_icon="📚", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;700;800&display=swap');

* { font-family: 'Tajawal', sans-serif !important; }

[data-testid="stSidebar"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }

.stApp { background: #0d0b1a; }

.hero {
    background: linear-gradient(135deg, #1a0533 0%, #0d0b1a 50%, #001a33 100%);
    border: 1px solid #2a1f4a;
    border-radius: 24px;
    padding: 48px 40px;
    text-align: center;
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 50%, #6c63ff11 0%, transparent 50%),
                radial-gradient(circle at 70% 50%, #a855f711 0%, transparent 50%);
    pointer-events: none;
}

.uni-name {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 12px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    color: #f0eeff;
    margin-bottom: 10px;
    line-height: 1.2;
}

.hero h1 span { color: #a78bfa; }

.hero p {
    color: #6a6480;
    font-size: 15px;
    font-weight: 300;
}

.section-title {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #4a4560;
    margin-bottom: 16px;
    text-align: center;
}

.subject-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin-bottom: 40px;
}

.subject-card {
    background: #12101e;
    border: 1.5px solid #1e1c2e;
    border-radius: 18px;
    padding: 28px 24px;
    cursor: pointer;
    transition: all 0.25s ease;
    text-align: right;
    direction: rtl;
}

.subject-card:hover {
    border-color: #6c63ff;
    transform: translateY(-4px);
    box-shadow: 0 12px 40px #6c63ff22;
}

.subject-card.active {
    border-color: #a78bfa;
    background: #1a1530;
    box-shadow: 0 0 0 1px #a78bfa44, 0 12px 40px #6c63ff22;
}

.subject-icon { font-size: 32px; margin-bottom: 12px; }

.subject-name {
    font-size: 16px;
    font-weight: 700;
    color: #f0eeff;
    margin-bottom: 4px;
}

.subject-code {
    font-size: 12px;
    color: #a78bfa;
    font-weight: 600;
    letter-spacing: 1px;
}

.subject-desc {
    font-size: 13px;
    color: #5a5570;
    margin-top: 8px;
}

.lecture-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 12px;
    margin-bottom: 40px;
}

.lecture-card {
    background: #12101e;
    border: 1.5px solid #1e1c2e;
    border-radius: 14px;
    padding: 20px;
    cursor: pointer;
    transition: all 0.2s;
    text-align: right;
    direction: rtl;
}

.lecture-card:hover {
    border-color: #6c63ff;
    transform: translateY(-2px);
}

.lecture-card.active {
    border-color: #a78bfa;
    background: #1a1530;
}

.lecture-card.coming-soon {
    opacity: 0.4;
    cursor: not-allowed;
}

.lec-num {
    font-size: 11px;
    color: #a78bfa;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.lec-title {
    font-size: 15px;
    font-weight: 700;
    color: #e0ddf5;
    margin-bottom: 4px;
}

.lec-count {
    font-size: 12px;
    color: #4a4560;
}

.question-card {
    background: #12101e;
    border: 1px solid #1e1c2e;
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 14px;
    transition: border-color 0.3s;
    direction: ltr;
}

.question-card.correct-card { border-color: #22c55e44; }
.question-card.wrong-card { border-color: #ef444444; }

.q-meta {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #3a3555;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.q-text {
    font-size: 16px;
    font-weight: 500;
    color: #e0ddf5;
    line-height: 1.6;
    margin-bottom: 18px;
}

div[data-testid="stButton"] button {
    background: #1a1826 !important;
    border: 1.5px solid #252235 !important;
    border-radius: 10px !important;
    color: #c4c0d8 !important;
    font-size: 14px !important;
    padding: 10px 16px !important;
    width: 100% !important;
    text-align: right !important;
    transition: all 0.2s !important;
    direction: rtl !important;
}

div[data-testid="stButton"] button:hover {
    border-color: #6c63ff !important;
    color: #e0ddf5 !important;
}

.correct-opt {
    background: #15291e;
    border: 1.5px solid #22c55e;
    border-radius: 10px;
    padding: 10px 16px;
    color: #4ade80;
    font-size: 14px;
    margin-bottom: 8px;
    direction: rtl;
    text-align: right;
}

.wrong-opt {
    background: #2a1515;
    border: 1.5px solid #ef4444;
    border-radius: 10px;
    padding: 10px 16px;
    color: #f87171;
    font-size: 14px;
    margin-bottom: 8px;
    direction: rtl;
    text-align: right;
}

.reveal-opt {
    background: #15291e88;
    border: 1.5px solid #22c55e55;
    border-radius: 10px;
    padding: 10px 16px;
    color: #4ade8077;
    font-size: 14px;
    margin-bottom: 8px;
    direction: rtl;
    text-align: right;
}

.neutral-opt {
    background: #1a1826;
    border: 1.5px solid #252235;
    border-radius: 10px;
    padding: 10px 16px;
    color: #5a5570;
    font-size: 14px;
    margin-bottom: 8px;
    direction: rtl;
    text-align: right;
}

.score-banner {
    background: linear-gradient(135deg, #1a1530, #12101e);
    border: 1px solid #6c63ff44;
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    margin-bottom: 24px;
    direction: rtl;
}

.score-big {
    font-size: 64px;
    font-weight: 800;
    color: #a78bfa;
    line-height: 1;
    margin-bottom: 8px;
}

.score-label {
    font-size: 18px;
    font-weight: 700;
    color: #f0eeff;
    margin-bottom: 4px;
}

.score-sub { font-size: 14px; color: #5a5570; }

div[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #6c63ff, #a855f7) !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA
# ============================================================

lec1_questions = [
    {"q": "All learning must begin with...", "options": ["Algorithms", "Data", "Models", "Testing"], "ans": "Data"},
    {"q": "Computers have short- and long-term recall capabilities using...", "options": ["Sensors", "RAM and Hard drives", "Monitors", "Keyboards"], "ans": "RAM and Hard drives"},
    {"q": "Data storage utilizes observation, memory, and recall to provide a...", "options": ["Abstract representation", "Factual basis", "Generalization", "Bias"], "ans": "Factual basis"},
    {"q": "The human brain uses what kind of signals to store and process observations?", "options": ["Electrochemical", "Mechanical", "Radioactive", "Magnetic"], "ans": "Electrochemical"},
    {"q": "Data storage is used as a foundation for more advanced...", "options": ["Reasoning", "Printing", "Ignoring", "Deleting"], "ans": "Reasoning"},
    {"q": "The process of assigning meaning to stored data occurs during...", "options": ["Evaluation", "Generalization", "Abstraction", "Storage"], "ans": "Abstraction"},
    {"q": "During knowledge representation, the computer summarizes raw data using a...", "options": ["Model", "Sensor", "CPU", "Hard Disk"], "ans": "Model"},
    {"q": "A model is an explicit description of the ________ within the data.", "options": ["Noise", "Errors", "Patterns", "Missing values"], "ans": "Patterns"},
    {"q": "Mathematical equations and relational diagrams are examples of...", "options": ["Noise", "Models", "Hardware", "Sensors"], "ans": "Models"},
    {"q": "The process of fitting a model to a dataset is known as...", "options": ["Training", "Evaluating", "Testing", "Generalizing"], "ans": "Training"},
    {"q": "Why is it called 'training' rather than 'learning'?", "options": ["Because learning ends with abstraction", "Because the process of learning does not end with data abstraction", "Because machines cannot learn", "Because it is faster"], "ans": "Because the process of learning does not end with data abstraction"},
    {"q": "Abstraction involves the translation of stored data into broader...", "options": ["Representations and concepts", "Noise and errors", "Hardware and software", "Zeros and ones"], "ans": "Representations and concepts"},
    {"q": "When a model has been trained, data is transformed into an abstract form that...", "options": ["Deletes original info", "Summarizes original info", "Increases noise", "Creates errors"], "ans": "Summarizes original info"},
    {"q": "Turning abstracted knowledge into a form utilized for future action is called...", "options": ["Storage", "Training", "Generalization", "Abstraction"], "ans": "Generalization"},
    {"q": "Generalization operates on tasks that are similar, but not identical, to...", "options": ["Those it has seen before", "Random tasks", "Impossible tasks", "Tasks from other domains"], "ans": "Those it has seen before"},
    {"q": "In generalization, the learner limits discovered patterns to those most...", "options": ["Irrelevant", "Complex", "Relevant to future tasks", "Noisy"], "ans": "Relevant to future tasks"},
    {"q": "If conclusions are systematically erroneous, the algorithm has a...", "options": ["High variance", "Bias", "Perfect fit", "Good model"], "ans": "Bias"},
    {"q": "Bias is considered a ________ associated with abstraction and generalization.", "options": ["Necessary evil", "Perfect feature", "Hardware issue", "Random noise"], "ans": "Necessary evil"},
    {"q": "Generalization uses abstracted data to create...", "options": ["Hardware errors", "Knowledge and inferences", "Raw data", "Storage memory"], "ans": "Knowledge and inferences"},
    {"q": "Which step drives action in new contexts?", "options": ["Data Storage", "Abstraction", "Generalization", "Evaluation"], "ans": "Generalization"},
    {"q": "Bias means the model is wrong in a ________ manner.", "options": ["Unpredictable", "Random", "Predictable", "Correct"], "ans": "Predictable"},
    {"q": "A model discovering a 'face' by ignoring skin color and focusing on eyes/mouth is an example of...", "options": ["Storage", "Limiting patterns (Generalization)", "Evaluation", "Adding noise"], "ans": "Limiting patterns (Generalization)"},
    {"q": "Which step provides a feedback mechanism to measure utility?", "options": ["Abstraction", "Storage", "Evaluation", "Generalization"], "ans": "Evaluation"},
    {"q": "Evaluation occurs after a model has been trained on an...", "options": ["Test dataset", "Initial training dataset", "Validation dataset", "Random dataset"], "ans": "Initial training dataset"},
    {"q": "To judge how well a model generalizes, it is evaluated on a...", "options": ["New test dataset", "Training dataset", "Old dataset", "Corrupted dataset"], "ans": "New test dataset"},
    {"q": "It is exceedingly rare for a model to generalize perfectly due to...", "options": ["Good hardware", "Noise", "Low bias", "Perfect data"], "ans": "Noise"},
    {"q": "Noisy data can be caused by...", "options": ["Measurement error", "Perfect sensors", "Clean data", "Good human subjects"], "ans": "Measurement error"},
    {"q": "Survey respondents reporting random answers is an example of...", "options": ["Perfect data", "Data quality improvement", "Noise (Issues with human subjects)", "Low variance"], "ans": "Noise (Issues with human subjects)"},
    {"q": "Missing, null, or corrupted values are considered...", "options": ["Data quality problems (Noise)", "Perfect abstraction", "High bias", "Good fitting"], "ans": "Data quality problems (Noise)"},
    {"q": "Trying to model noise is the basis of a problem called...", "options": ["Underfitting", "Overfitting", "Perfect fitting", "Evaluation"], "ans": "Overfitting"},
    {"q": "A model with a High Training Error and High Test Error is...", "options": ["Overfitting", "Underfitting", "Just right", "Perfect"], "ans": "Underfitting"},
    {"q": "A model with a Low Training Error but High Test Error is...", "options": ["Overfitting", "Underfitting", "Just right", "Biased"], "ans": "Overfitting"},
    {"q": "The formula E[(θ_bar - θ)^2] represents...", "options": ["Variance", "Bias", "Noise", "Accuracy"], "ans": "Bias"},
    {"q": "The formula E[(θ_hat - θ_bar)^2] represents...", "options": ["Variance", "Bias", "Noise", "Accuracy"], "ans": "Variance"},
    {"q": "Bias measures the ________ of the model.", "options": ["Precision", "Speed", "Accuracy or quality", "Size"], "ans": "Accuracy or quality"},
    {"q": "Variance measures the ________ of the model.", "options": ["Accuracy", "Precision or specificity", "Speed", "Memory"], "ans": "Precision or specificity"},
    {"q": "Low variance implies the model does not change much as the...", "options": ["Training set varies", "Hardware varies", "Test set is deleted", "Noise increases"], "ans": "Training set varies"},
    {"q": "Models with too few parameters are inaccurate because of...", "options": ["Large variance", "Large bias (not enough flexibility)", "Low bias", "Too much flexibility"], "ans": "Large bias (not enough flexibility)"},
    {"q": "Models with too many parameters are inaccurate because of...", "options": ["Large variance (too sensitive to randomness)", "Large bias", "Low variance", "Not enough flexibility"], "ans": "Large variance (too sensitive to randomness)"},
    {"q": "Low Bias and High Variance leads to...", "options": ["Underfitting", "Overfitting", "Just right fitting", "No fitting"], "ans": "Overfitting"},
    {"q": "High Bias and Low Variance leads to...", "options": ["Overfitting", "Underfitting", "Just right fitting", "Perfect fitting"], "ans": "Underfitting"},
    {"q": "A model with Low Bias and Low Variance is considered...", "options": ["Underfitting", "Overfitting", "Just right (Good Fit)", "A failure"], "ans": "Just right (Good Fit)"},
    {"q": "To fix Underfitting, one remedy is to...", "options": ["Complexify model", "Get more data", "Regularize", "Try a smaller set of features"], "ans": "Complexify model"},
    {"q": "Which of the following fixes Overfitting?", "options": ["Train longer", "Add more features", "Get more data (training examples)", "Complexify model"], "ans": "Get more data (training examples)"},
    {"q": "If your model has High Bias, you should try to...", "options": ["Add more features", "Select fewer features", "Get more data", "Regularize"], "ans": "Add more features"},
    {"q": "If your model has High Variance, you should try to...", "options": ["Train longer", "Add more features", "Regularize", "Make the model more complex"], "ans": "Regularize"},
    {"q": "Trying a smaller set of features is a remedy for...", "options": ["Underfitting", "Overfitting (High Variance)", "Low Bias", "Good Fitting"], "ans": "Overfitting (High Variance)"},
    {"q": "Training the model longer is a suggested fix for...", "options": ["Overfitting", "Underfitting (High Bias)", "High Variance", "Perfect Fit"], "ans": "Underfitting (High Bias)"},
    {"q": "When Model Complexity is LOW, the result is...", "options": ["Overfitting", "Underfitting", "Perfect Fit", "High Variance"], "ans": "Underfitting"},
    {"q": "When Model Complexity is HIGH, the result is...", "options": ["Overfitting", "Underfitting", "Perfect Fit", "High Bias"], "ans": "Overfitting"},
]

subjects = [
    {"icon": "🤖", "name": "Machine Learning", "code": "AIE121", "desc": "Intro, KNN, Decision Trees...", "key": "ml"},
]

lectures = {
    "ml": [
        {"num": "01", "title": "Intro to ML", "count": "50 سؤال", "key": "lec1", "available": True},
        {"num": "02", "title": "KNN Algorithm", "count": "قريباً", "key": "lec2", "available": False},
    ]
}

questions_db = {
    "ml_lec1": lec1_questions,
}

# ============================================================
# SESSION STATE
# ============================================================
if "selected_subject" not in st.session_state:
    st.session_state.selected_subject = None
if "selected_lecture" not in st.session_state:
    st.session_state.selected_lecture = None
if "answers" not in st.session_state:
    st.session_state.answers = {}

# ============================================================
# HERO
# ============================================================
st.markdown("""
<div class="hero">
    <div class="uni-name">🎓 جامعة المنصورة الجديدة · NMU</div>
    <h1>بنك <span>أسئلة</span> الدفعة</h1>
    <p>اختر المادة والمحاضرة وابدأ المذاكرة — مع تصحيح فوري لكل إجابة</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SUBJECT SELECTION
# ============================================================
st.markdown('<div class="section-title">· اختر المادة ·</div>', unsafe_allow_html=True)

cols = st.columns(len(subjects))
for idx, subj in enumerate(subjects):
    with cols[idx]:
        is_active = st.session_state.selected_subject == subj["key"]
        card_class = "subject-card active" if is_active else "subject-card"
        st.markdown(f"""
        <div class="{card_class}">
            <div class="subject-icon">{subj['icon']}</div>
            <div class="subject-name">{subj['name']}</div>
            <div class="subject-code">{subj['code']}</div>
            <div class="subject-desc">{subj['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"اختر {subj['name']}", key=f"subj_{subj['key']}"):
            st.session_state.selected_subject = subj["key"]
            st.session_state.selected_lecture = None
            st.session_state.answers = {}
            st.rerun()

# ============================================================
# LECTURE SELECTION
# ============================================================
if st.session_state.selected_subject:
    st.markdown("---")
    st.markdown('<div class="section-title">· اختر المحاضرة ·</div>', unsafe_allow_html=True)

    lecs = lectures[st.session_state.selected_subject]
    lec_cols = st.columns(len(lecs))

    for idx, lec in enumerate(lecs):
        with lec_cols[idx]:
            is_active = st.session_state.selected_lecture == lec["key"]
            card_class = "lecture-card active" if is_active else ("lecture-card coming-soon" if not lec["available"] else "lecture-card")
            st.markdown(f"""
            <div class="{card_class}">
                <div class="lec-num">Lecture {lec['num']}</div>
                <div class="lec-title">{lec['title']}</div>
                <div class="lec-count">{lec['count']}</div>
            </div>
            """, unsafe_allow_html=True)
            if lec["available"]:
                if st.button(f"ابدأ {lec['title']}", key=f"lec_{lec['key']}"):
                    st.session_state.selected_lecture = lec["key"]
                    st.session_state.answers = {}
                    st.rerun()
            else:
                st.markdown("<p style='color:#3a3555; font-size:13px; text-align:center;'>قريباً...</p>", unsafe_allow_html=True)

# ============================================================
# QUIZ
# ============================================================
if st.session_state.selected_subject and st.session_state.selected_lecture:
    db_key = f"{st.session_state.selected_subject}_{st.session_state.selected_lecture}"
    questions = questions_db.get(db_key, [])

    if questions:
        st.markdown("---")

        answered = len(st.session_state.answers)
        score = sum(1 for i, v in st.session_state.answers.items() if v == questions[i]["ans"])
        total = len(questions)

        # Progress
        st.progress(answered / total, text=f"تم الإجابة على {answered} من {total} سؤال  |  ✅ صح: {score}  |  ❌ غلط: {answered - score}")

        # Score banner
        if answered == total:
            pct = int((score / total) * 100)
            if pct == 100:
                st.balloons()
                emoji = "🏆"
                msg = "نتيجة مثالية!"
            elif pct >= 80:
                emoji = "🎉"
                msg = "ممتاز!"
            elif pct >= 60:
                emoji = "👍"
                msg = "جيد، كمّل!"
            else:
                emoji = "📚"
                msg = "راجع المحاضرة تاني!"

            st.markdown(f"""
            <div class="score-banner">
                <div class="score-big">{score}<span style="font-size:32px;color:#4a4560">/{total}</span></div>
                <div class="score-label">{emoji} {msg}</div>
                <div class="score-sub">{pct}% إجابات صحيحة</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🔄 إعادة المحاولة", use_container_width=True):
                st.session_state.answers = {}
                st.rerun()

            st.markdown("---")

        # Questions
        for i, q_data in enumerate(questions):
            chosen = st.session_state.answers.get(i)
            is_answered = chosen is not None
            is_correct = chosen == q_data["ans"]

            card_class = ""
            if is_answered:
                card_class = "correct-card" if is_correct else "wrong-card"

            st.markdown(f"""
            <div class="question-card {card_class}">
                <div class="q-meta">Question {str(i+1).zfill(2)}</div>
                <div class="q-text">{q_data['q']}</div>
            </div>
            """, unsafe_allow_html=True)

            if is_answered:
                for opt in q_data["options"]:
                    if opt == q_data["ans"] and opt == chosen:
                        st.markdown(f'<div class="correct-opt">✅ {opt}</div>', unsafe_allow_html=True)
                    elif opt == chosen:
                        st.markdown(f'<div class="wrong-opt">❌ {opt}</div>', unsafe_allow_html=True)
                    elif opt == q_data["ans"]:
                        st.markdown(f'<div class="reveal-opt">✅ {opt} &nbsp;←&nbsp; الإجابة الصحيحة</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="neutral-opt">{opt}</div>', unsafe_allow_html=True)
            else:
                opt_cols = st.columns(2)
                for j, opt in enumerate(q_data["options"]):
                    with opt_cols[j % 2]:
                        if st.button(opt, key=f"q{i}_o{j}"):
                            st.session_state.answers[i] = opt
                            st.rerun()

            st.markdown("<div style='margin-bottom:8px'></div>", unsafe_allow_html=True)
