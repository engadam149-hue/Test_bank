import streamlit as st

st.set_page_config(page_title="بنك أسئلة الدفعة", page_icon="📚", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;700&display=swap');
* { font-family: 'Tajawal', sans-serif !important; }

.stApp { background-color: #0a0a0f; color: #e8e6f0; }

.question-card {
    background: #12101e;
    border: 1px solid #1e1c2e;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
}

div[data-testid="stRadio"] label {
    color: #c4c0d8 !important;
    font-size: 15px !important;
}
</style>
""", unsafe_allow_html=True)

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

# ============================================================
st.sidebar.title("📚 اختر المادة")
subject = st.sidebar.selectbox("المواد المتاحة:", ["اختر مادة...", "Machine Learning (AIE121)"])

if subject == "Machine Learning (AIE121)":
    st.title("🤖 أسئلة Machine Learning - AIE121")

    lecture = st.sidebar.selectbox("اختر المحاضرة:", ["اختر...", "Lecture 1: Intro (50 Questions)", "Lecture 2: KNN Algorithm"])

    if lecture == "Lecture 1: Intro (50 Questions)":
        st.subheader("📝 أسئلة المحاضرة الأولى")

        # Progress tracking
        if "answers" not in st.session_state:
            st.session_state.answers = {}

        answered = len(st.session_state.answers)
        score = sum(1 for i, v in st.session_state.answers.items() if v == lec1_questions[i]["ans"])

        # Progress bar
        st.progress(answered / len(lec1_questions), text=f"تم الإجابة على {answered} من {len(lec1_questions)} سؤال")

        if answered == len(lec1_questions):
            pct = int((score / len(lec1_questions)) * 100)
            if pct == 100:
                st.balloons()
                st.success(f"🏆 نتيجة مثالية! {score} / {len(lec1_questions)} ({pct}%)")
            elif pct >= 80:
                st.success(f"🎉 ممتاز! {score} / {len(lec1_questions)} ({pct}%)")
            elif pct >= 60:
                st.warning(f"👍 جيد! {score} / {len(lec1_questions)} ({pct}%)")
            else:
                st.error(f"📚 تحتاج مراجعة! {score} / {len(lec1_questions)} ({pct}%)")

            if st.button("🔄 إعادة المحاولة"):
                st.session_state.answers = {}
                st.rerun()

        st.divider()

        # عرض الأسئلة مع instant feedback
        for i, q_data in enumerate(lec1_questions):
            with st.container():
                st.markdown(f"**Q{i+1}. {q_data['q']}**")

                if i in st.session_state.answers:
                    chosen = st.session_state.answers[i]
                    is_correct = chosen == q_data["ans"]

                    # عرض الخيارات ملونة بعد الإجابة
                    for opt in q_data["options"]:
                        if opt == q_data["ans"] and opt == chosen:
                            st.success(f"✅ {opt}")
                        elif opt == chosen and opt != q_data["ans"]:
                            st.error(f"❌ {opt}")
                        elif opt == q_data["ans"]:
                            st.success(f"✅ {opt} ← الإجابة الصحيحة")
                        else:
                            st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;◦ {opt}")

                    if is_correct:
                        st.caption("✔️ إجابة صحيحة!")
                    else:
                        st.caption(f"✖️ إجابتك: {chosen} | الصح: {q_data['ans']}")
                else:
                    # عرض الأزرار للإجابة
                    cols = st.columns(2)
                    for j, opt in enumerate(q_data["options"]):
                        col = cols[j % 2]
                        if col.button(opt, key=f"q{i}_opt{j}"):
                            st.session_state.answers[i] = opt
                            st.rerun()

                st.divider()

    elif lecture == "Lecture 2: KNN Algorithm":
        st.info("سيتم إضافة أسئلة هذه المحاضرة قريباً... استعد! 🚀")

else:
    st.write("👈 أهلاً بك! يرجى اختيار مادة من القائمة الجانبية للبدء.")
