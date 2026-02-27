import streamlit as st

# ==========================================
# 1. البيانات (الأسئلة والمواد)
# ==========================================

SUBJECTS = [
    {
        "icon": "🤖",
        "name": "Machine Learning",
        "code": "AIE121",
        "desc": "Intro, KNN, Decision Trees...",
        "key": "ml",
        "lectures": [
            {
                "num": "01",
                "title": "Intro to ML",
                "count": "37 سؤال",
                "file": "ml_lec1",
                "available": True,
            },
            {
                "num": "02",
                "title": "KNN Algorithm",
                "count": "50 سؤال",
                "file": "ml_lec2",
                "available": False,
            },
        ]
    },
]

# تم تجميع الأسئلة في قاموس (Dictionary) مفتاحه هو اسم المحاضرة
ALL_QUESTIONS = {
    "ml_lec1": [
        {
            "q": "What does KNN stand for?",
            "type": "mcq",
            "options": ["K-Nearest Neighbors", "K-Neural Network", "K-Norm Node", "K-Net Numeric"],
            "ans": "K-Nearest Neighbors",
            "explain_correct": "✅ صح! KNN = K-Nearest Neighbors، خوارزمية بتصنّف النقطة الجديدة بناءً على أقرب K جيران ليها في البيانات.",
            "explain_wrong":   "❌ غلط! KNN اختصار K-Nearest Neighbors فقط — مش Neural Network ولا أي حاجة تانية."
        },
        {
            "q": "KNN is classified as a ________ learning algorithm.",
            "type": "mcq",
            "options": ["Supervised", "Unsupervised", "Reinforcement", "Semi-supervised"],
            "ans": "Supervised",
            "explain_correct": "✅ صح! KNN خوارزمية Supervised لأنها بتتدرب على بيانات معندها labels (فئات معروفة مسبقاً).",
            "explain_wrong":   "❌ غلط! KNN بتحتاج labels عشان تشتغل، يعني هي Supervised مش Unsupervised."
        },
        {
            "q": "KNN is called a 'lazy learner' because...",
            "type": "mcq",
            "options": [
                "It memorizes training data and delays computation to prediction time",
                "It trains very slowly on large datasets",
                "It uses a very simple mathematical model",
                "It ignores most of the training data"
            ],
            "ans": "It memorizes training data and delays computation to prediction time",
            "explain_correct": "✅ صح! KNN 'كسول' لأنه مش بيبني model أثناء التدريب، بيحفظ البيانات وبيحسب كل حاجة وقت التنبؤ فقط.",
            "explain_wrong":   "❌ غلط! الـ Lazy مش معناها بطيء في التدريب، معناها إنه مش بيعمل تدريب حقيقي — بيؤجل الحساب لوقت التنبؤ."
        },
        {
            "q": "k-NN algorithm does more computation on test time rather than train time.",
            "type": "tf",
            "options": ["True", "False"],
            "ans": "True",
            "explain_correct": "✅ صح! KNN مش بيتعلم وقت التدريب، كل الحساب (المسافات والتصنيف) بيحصل وقت الاختبار (prediction time).",
            "explain_wrong":   "❌ غلط! KNN بالفعل بيعمل معظم الحساب وقت الـ testing مش الـ training — وده اللي بيخليه lazy learner."
        },
        {
            "q": "Which is a STRENGTH of the KNN algorithm?",
            "type": "mcq",
            "options": [
                "Simple and effective with no assumptions about data distribution",
                "Fast classification phase",
                "Handles missing data automatically",
                "Produces an interpretable model"
            ],
            "ans": "Simple and effective with no assumptions about data distribution",
            "explain_correct": "✅ صح! KNN بسيط وفعّال، ومش بيفترض أي شكل معين للبيانات (no assumptions about distribution).",
            "explain_wrong":   "❌ غلط! KNN معروف بإن الـ classification phase بطيئة، ومش بيعمل model قابل للتفسير."
        },
        {
            "q": "Which is a WEAKNESS of the KNN algorithm?",
            "type": "mcq",
            "options": [
                "Slow classification phase",
                "Requires large training time",
                "Makes strong assumptions about data",
                "Cannot handle numeric features"
            ],
            "ans": "Slow classification phase",
            "explain_correct": "✅ صح! KNN بطيء وقت التصنيف لأنه بيحسب المسافة لكل نقطة في البيانات لكل تنبؤ جديد.",
            "explain_wrong":   "❌ غلط! الـ training في KNN سريعة جداً (بيحفظ البيانات بس)، لكن الـ classification هي اللي بطيئة."
        },
        {
            "q": "KNN does NOT produce a model, which limits our ability to...",
            "type": "mcq",
            "options": [
                "Understand how features are related to the class",
                "Classify new data points",
                "Use Euclidean distance",
                "Normalize the data"
            ],
            "ans": "Understand how features are related to the class",
            "explain_correct": "✅ صح! لأن KNN مش بيبني model، مش قادرين نفهم إزاي كل feature بتأثر على التصنيف.",
            "explain_wrong":   "❌ غلط! KNN بيقدر يصنف بيانات جديدة كويس، بس مش بيديك تفسير لعلاقة الـ features بالنتيجة."
        },
        {
            "q": "In KNN, the unlabeled test instance is assigned the class of...",
            "type": "mcq",
            "options": [
                "The majority of the k nearest neighbors",
                "The single closest neighbor only",
                "The farthest neighbor",
                "A randomly selected neighbor"
            ],
            "ans": "The majority of the k nearest neighbors",
            "explain_correct": "✅ صح! KNN بيشوف الـ K جيران الأقرب، وبيختار الفئة اللي عندها أكبر عدد (majority vote).",
            "explain_wrong":   "❌ غلط! KNN مش بيعتمد على جار واحد بس (ده K=1)، بيعتمد على أغلبية الـ K جيران."
        },
        {
            "q": "What is the Euclidean distance formula used in KNN?",
            "type": "mcq",
            "options": [
                "dist(p,q) = sqrt((p1-q1)² + (p2-q2)² + ... + (pn-qn)²)",
                "dist(p,q) = |p1-q1| + |p2-q2|",
                "dist(p,q) = (p1-q1)² + (p2-q2)²",
                "dist(p,q) = (p1+q1) / (p2+q2)"
            ],
            "ans": "dist(p,q) = sqrt((p1-q1)² + (p2-q2)² + ... + (pn-qn)²)",
            "explain_correct": "✅ صح! دي معادلة Euclidean Distance الصح — جذر مجموع مربعات الفروق لكل بُعد.",
            "explain_wrong":   "❌ غلط! الصيغة الأولى (Manhattan) بتجمع القيم المطلقة، والصح هو الجذر التربيعي لمجموع المربعات."
        },
        {
            "q": "What is the Euclidean distance between points A(0,1) and B(2,3)?",
            "type": "mcq",
            "options": ["√8 ≈ 2.83", "1", "2", "4"],
            "ans": "√8 ≈ 2.83",
            "explain_correct": "✅ صح! dist = sqrt((2-0)² + (3-1)²) = sqrt(4+4) = sqrt(8) ≈ 2.83 ✓",
            "explain_wrong":   "❌ غلط! الحساب الصح: sqrt((2-0)² + (3-1)²) = sqrt(4+4) = sqrt(8) ≈ 2.83"
        },
        {
            "q": "Which property of distance metrics states d(x,y) = d(y,x)?",
            "type": "mcq",
            "options": ["Symmetry", "Non-negativity", "Identity", "Triangle inequality"],
            "ans": "Symmetry",
            "explain_correct": "✅ صح! Symmetry تعني إن المسافة من x لـ y = المسافة من y لـ x.",
            "explain_wrong":   "❌ غلط! الخاصية دي اسمها Symmetry (التماثل) — المسافة لازم تكون متساوية في الاتجاهين."
        },
        {
            "q": "Which axiom of distance metrics states that d(x,x) = 0?",
            "type": "mcq",
            "options": ["Identity of indiscernibles", "Non-negativity", "Symmetry", "Triangle inequality"],
            "ans": "Identity of indiscernibles",
            "explain_correct": "✅ صح! d(x,x) = 0 يعني المسافة من نقطة لنفسها = صفر، وده أكسيوم الـ Identity.",
            "explain_wrong":   "❌ غلط! d(x,x)=0 بيعبر عن Identity (المسافة بين شيء ونفسه = صفر)."
        },
        {
            "q": "The triangle inequality in distance metrics states...",
            "type": "mcq",
            "options": [
                "d(x,y) + d(y,z) ≥ d(x,z)",
                "d(x,y) = d(y,x)",
                "d(x,x) = 0",
                "d(x,y) ≥ 0"
            ],
            "ans": "d(x,y) + d(y,z) ≥ d(x,z)",
            "explain_correct": "✅ صح! Triangle inequality: أي ضلع في مثلث أقل من أو يساوي مجموع الضلعين الآخرين.",
            "explain_wrong":   "❌ غلط! Triangle inequality هي d(x,y) + d(y,z) ≥ d(x,z)."
        },
        {
            "q": "What does the axiom d(x,y) ≥ 0 represent?",
            "type": "mcq",
            "options": ["Non-negativity", "Symmetry", "Identity", "Triangle inequality"],
            "ans": "Non-negativity",
            "explain_correct": "✅ صح! Non-negativity تعني إن المسافة دايماً ≥ صفر، مش ممكن تبقى سالبة.",
            "explain_wrong":   "❌ غلط! d(x,y) ≥ 0 هو شرط Non-negativity — المسافة دايماً موجبة أو صفر."
        },
        {
            "q": "Why do we normalize data before applying KNN?",
            "type": "mcq",
            "options": [
                "To prevent features with large ranges from dominating the distance",
                "To speed up the training process",
                "To remove noise from the dataset",
                "To increase the number of features"
            ],
            "ans": "To prevent features with large ranges from dominating the distance",
            "explain_correct": "✅ صح! بدون Normalization، الـ Salary (18000–150000) هتطغى على الـ Age (18–48) في حساب المسافة.",
            "explain_wrong":   "❌ غلط! Normalization مش للسرعة — هي عشان الـ features تبقى متساوية في التأثير على حساب المسافة."
        },
        {
            "q": "The normalization formula used in KNN is...",
            "type": "mcq",
            "options": [
                "x = (x - MIN) / (MAX - MIN)",
                "x = (x - MEAN) / STD",
                "x = x / MAX",
                "x = x - MIN"
            ],
            "ans": "x = (x - MIN) / (MAX - MIN)",
            "explain_correct": "✅ صح! دي صيغة Min-Max Normalization — بتحول القيم لنطاق بين 0 و1.",
            "explain_wrong":   "❌ غلط! الصيغة الصح هي Min-Max: (x - MIN)/(MAX - MIN). الصيغة اللي فيها MEAN وSTD دي Z-score."
        },
        {
            "q": "Min-Max Normalization scales data to the range...",
            "type": "mcq",
            "options": ["[0, 1]", "[-1, 1]", "[0, 100]", "[-∞, +∞]"],
            "ans": "[0, 1]",
            "explain_correct": "✅ صح! Min-Max Normalization بتحول كل القيم لتكون بين 0 و1 بالظبط.",
            "explain_wrong":   "❌ غلط! Min-Max بتعطي نطاق [0,1] — مش [-1,1] دي Z-score."
        },
        {
            "q": "Given values: 7, 4, 25, -5, 10 (MIN=-5, MAX=25). Normalized value of 7 = ?",
            "type": "mcq",
            "options": ["0.4", "0.3", "0.5", "0.6"],
            "ans": "0.4",
            "explain_correct": "✅ صح! (7 - (-5)) / (25 - (-5)) = 12/30 = 0.4 ✓",
            "explain_wrong":   "❌ غلط! الحساب الصح: (7-(-5)) / (25-(-5)) = 12/30 = 0.4"
        },
        {
            "q": "Given values: 7, 4, 25, -5, 10 (MIN=-5, MAX=25). Normalized value of 4 = ?",
            "type": "mcq",
            "options": ["0.3", "0.4", "0.5", "0.1"],
            "ans": "0.3",
            "explain_correct": "✅ صح! (4 - (-5)) / (25 - (-5)) = 9/30 = 0.3 ✓",
            "explain_wrong":   "❌ غلط! الحساب الصح: (4-(-5)) / (25-(-5)) = 9/30 = 0.3"
        },
        {
            "q": "Given values: 7, 4, 25, -5, 10 (MIN=-5, MAX=25). Normalized value of -5 = ?",
            "type": "mcq",
            "options": ["0", "0.1", "-1", "0.5"],
            "ans": "0",
            "explain_correct": "✅ صح! (-5-(-5)) / (25-(-5)) = 0/30 = 0. القيمة الدنيا دايماً = 0 في Min-Max.",
            "explain_wrong":   "❌ غلط! (-5-(-5)) / (25-(-5)) = 0. القيمة الدنيا دايماً = 0 بعد الـ normalization."
        },
        {
            "q": "Given values: 7, 4, 25, -5, 10 (MIN=-5, MAX=25). Normalized value of 25 = ?",
            "type": "mcq",
            "options": ["1", "0.9", "0.8", "25"],
            "ans": "1",
            "explain_correct": "✅ صح! (25-(-5)) / (25-(-5)) = 30/30 = 1. القيمة العليا دايماً = 1 في Min-Max.",
            "explain_wrong":   "❌ غلط! (25-(-5))/(25-(-5)) = 1. القيمة العليا دايماً = 1 بعد الـ normalization."
        },
        {
            "q": "k-NN performs much better if all of the data have the same scale.",
            "type": "tf",
            "options": ["True", "False"],
            "ans": "True",
            "explain_correct": "✅ صح! لما كل الـ features على نفس الـ scale، حساب المسافة بيبقى عادل ومش feature واحدة تطغى.",
            "explain_wrong":   "❌ غلط! ده صح — KNN بيشتغل أحسن بكتير لما البيانات على نفس الـ scale."
        },
        {
            "q": "What are the correct steps of the KNN algorithm in order?",
            "type": "mcq",
            "options": [
                "Select K → Calculate distances → Take K nearest → Count per class → Assign majority",
                "Calculate distances → Select K → Assign class → Count neighbors",
                "Train model → Select K → Calculate distances → Predict",
                "Normalize → Train → Test → Select K"
            ],
            "ans": "Select K → Calculate distances → Take K nearest → Count per class → Assign majority",
            "explain_correct": "✅ صح! الخطوات الصح: اختار K → احسب المسافات → خذ K الأقرب → عد النقاط → اختار الأغلبية.",
            "explain_wrong":   "❌ غلط! الترتيب الصح: اختيار K أولاً ← حساب المسافات ← K الأقرب ← العد ← التصنيف."
        },
        {
            "q": "In case of a very large value of K, we may...",
            "type": "mcq",
            "options": [
                "Include points from other classes into the neighborhood",
                "Get more accurate results always",
                "Reduce computation time significantly",
                "Eliminate the need for normalization"
            ],
            "ans": "Include points from other classes into the neighborhood",
            "explain_correct": "✅ صح! K كبير جداً بيوسّع دائرة الجيران لدرجة إنها تشمل نقاط من فئات تانية.",
            "explain_wrong":   "❌ غلط! K كبير مش أفضل دايماً — بيجيب جيران بعيدين من فئات مختلفة وبيخرب التصنيف."
        },
        {
            "q": "In case of a very small value of K (like K=1), the algorithm is...",
            "type": "mcq",
            "options": [
                "Very sensitive to noise",
                "More accurate always",
                "Faster in prediction",
                "Better at handling outliers"
            ],
            "ans": "Very sensitive to noise",
            "explain_correct": "✅ صح! K=1 بيعتمد على جار واحد بس، لو كان outlier أو noise هيأثر على النتيجة كلها.",
            "explain_wrong":   "❌ غلط! K صغير (خصوصاً K=1) بيخلي الخوارزمية حساسة جداً للـ noise."
        },
        {
            "q": "The main benefit of using k neighbors instead of just 1 neighbor is...",
            "type": "mcq",
            "options": [
                "Voting overcomes noise",
                "Faster computation",
                "No need for distance calculation",
                "Better handling of missing data"
            ],
            "ans": "Voting overcomes noise",
            "explain_correct": "✅ صح! لما بتستخدم K جيران، الـ voting بينهم بيتغلب على الـ noise في البيانات.",
            "explain_wrong":   "❌ غلط! الفايدة الأساسية من K جيران هي إن الـ voting بيقلل تأثير الـ noise."
        },
        {
            "q": "As K increases beyond the optimal point, the error rate...",
            "type": "mcq",
            "options": ["Increases", "Decreases", "Stays the same", "Reaches zero"],
            "ans": "Increases",
            "explain_correct": "✅ صح! بعد النقطة المثلى، زيادة K بيزيد الـ error لأنه بيدخل فئات تانية في الحساب.",
            "explain_wrong":   "❌ غلط! الـ error rate مش بينخفض باستمرار — في نقطة مثلى وبعدها يزيد مع زيادة K."
        },
        {
            "q": "Which value of K is generally preferred to avoid tie voting?",
            "type": "mcq",
            "options": ["Odd K", "Even K", "K=1 always", "K=100 for stability"],
            "ans": "Odd K",
            "explain_correct": "✅ صح! K الفردي بيتجنب الـ tie voting لما يكون عندك فئتين متساويتين.",
            "explain_wrong":   "❌ غلط! K الزوجي ممكن يسبب Tie Voting — فضل K الفردي عشان دايماً في فائز واضح."
        },
        {
            "q": "What problem occurs with an even value of K in binary classification?",
            "type": "mcq",
            "options": ["Tie voting", "Overfitting", "Underfitting", "Slow training"],
            "ans": "Tie voting",
            "explain_correct": "✅ صح! لو K زوجي، ممكن يطلع تعادل بين الفئتين (مثلاً 2-2) ومش هيقدر يقرر.",
            "explain_wrong":   "❌ غلط! المشكلة مع K الزوجي هي Tie Voting مش Overfitting."
        },
        {
            "q": "When you increase K in KNN, the bias...",
            "type": "mcq",
            "options": ["Increases", "Decreases", "Stays the same", "Becomes zero"],
            "ans": "Increases",
            "explain_correct": "✅ صح! زيادة K بيعمل smoothing أكثر للـ decision boundary وبيزيد الـ bias (underfitting).",
            "explain_wrong":   "❌ غلط! زيادة K = زيادة bias لأن الـ model بيبقى أكثر generalization وأقل دقة في التفاصيل."
        },
        {
            "q": "Class-label noise in KNN means...",
            "type": "mcq",
            "options": [
                "The class label provided for an example is incorrect",
                "The feature values are missing",
                "The distance calculation is wrong",
                "The K value is too large"
            ],
            "ans": "The class label provided for an example is incorrect",
            "explain_correct": "✅ صح! Class-label noise = الـ label المعطى للمثال غلط (مثلاً: بيقول pos وهو فعلاً neg).",
            "explain_wrong":   "❌ غلط! Class-label noise = الـ label غلط مش قيمة الـ feature."
        },
        {
            "q": "Attribute noise in KNN causes...",
            "type": "mcq",
            "options": [
                "The nearest neighbor may not be really the nearest one",
                "The class label to be wrong",
                "K to be selected incorrectly",
                "Normalization to fail"
            ],
            "ans": "The nearest neighbor may not be really the nearest one",
            "explain_correct": "✅ صح! لو قيمة الـ attribute غلطة، حساب المسافة هيبقى غلط وهيختار neighbors مش الأقرب فعلاً.",
            "explain_wrong":   "❌ غلط! Attribute noise بتأثر على حساب المسافة — فالـ nearest neighbor اللي بيختاره مش فعلاً الأقرب."
        },
        {
            "q": "Irrelevant attributes in KNN are a problem because...",
            "type": "mcq",
            "options": [
                "They affect distances but not the class, causing wrong neighbors",
                "They slow down the algorithm significantly",
                "They cause K to be selected incorrectly",
                "They prevent the use of Min-Max normalization"
            ],
            "ans": "They affect distances but not the class, causing wrong neighbors",
            "explain_correct": "✅ صح! الـ attributes الغير مهمة بتأثر على المسافة رغم إنها مش مهمة للتصنيف.",
            "explain_wrong":   "❌ غلط! مشكلة الـ irrelevant attributes = بتأثر على حساب المسافة رغم إنها مش مهمة للـ class."
        },
        {
            "q": "The scaling problem in KNN occurs when...",
            "type": "mcq",
            "options": [
                "One attribute with large range overwhelms others in distance calculation",
                "The dataset is too large to process",
                "K is set to a very high value",
                "The model overfits the training data"
            ],
            "ans": "One attribute with large range overwhelms others in distance calculation",
            "explain_correct": "✅ صح! مثلاً x1 ∈ [0,1] و x2 ∈ [0,100] — الـ x2 هتسيطر على حساب المسافة.",
            "explain_wrong":   "❌ غلط! Scaling problem = feature بـ range كبيرة بتطغى على باقي الـ features."
        },
        {
            "q": "k-NN works well with a small number of input variables but struggles when the number of inputs is very large.",
            "type": "tf",
            "options": ["True", "False"],
            "ans": "True",
            "explain_correct": "✅ صح! مع زيادة عدد الـ features (curse of dimensionality)، حساب المسافة بيبقى أقل دقة.",
            "explain_wrong":   "❌ غلط! ده صح — KNN بيعاني مع الـ features الكتيرة بسبب curse of dimensionality."
        },
        {
            "q": "KNN makes no assumptions about the functional form of the problem being solved.",
            "type": "tf",
            "options": ["True", "False"],
            "ans": "True",
            "explain_correct": "✅ صح! ده من أهم مميزات KNN — مش بيفترض إن البيانات linear أو أي شكل معين (non-parametric).",
            "explain_wrong":   "❌ غلط! KNN فعلاً مش بيفترض أي شكل للبيانات، وده ميزة قوية ليه."
        },
        {
            "q": "Which of the following statements about KNN is TRUE?",
            "type": "mcq",
            "options": [
                "All three: same scale + small inputs + no assumptions",
                "KNN performs better with same-scale data only",
                "KNN works well with large number of input variables",
                "KNN makes strong assumptions about data distribution"
            ],
            "ans": "All three: same scale + small inputs + no assumptions",
            "explain_correct": "✅ صح! الثلاث statements صحيحة — KNN أحسن مع نفس الـ scale، وعدد features صغير، وما بيفترض أي شكل للبيانات.",
            "explain_wrong":   "❌ غلط! الإجابة الصح هي إن الثلاث شروط صحيحة عن KNN."
        }
    ]
}

def load_questions(file_name):
    """تقوم بإرجاع قائمة الأسئلة من القاموس المحلي بدلاً من استيراد ملف خارجي"""
    return ALL_QUESTIONS.get(file_name, [])

# ==========================================
# 2. إعدادات الصفحة والتصميم (Streamlit & CSS)
# ==========================================

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
}
.uni-name { font-size: 13px; font-weight: 700; letter-spacing: 4px; color: #a78bfa; margin-bottom: 12px; }
.hero h1 { font-size: 42px; font-weight: 800; color: #f0eeff; margin-bottom: 10px; }
.hero h1 span { color: #a78bfa; }
.hero p { color: #6a6480; font-size: 15px; }

.section-title { font-size: 13px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #4a4560; margin-bottom: 16px; text-align: center; }

.subject-card { background: #12101e; border: 1.5px solid #1e1c2e; border-radius: 18px; padding: 28px 24px; text-align: right; direction: rtl; }
.subject-card.active { border-color: #a78bfa; background: #1a1530; }
.subject-icon { font-size: 32px; margin-bottom: 12px; }
.subject-name { font-size: 16px; font-weight: 700; color: #f0eeff; margin-bottom: 4px; }
.subject-code { font-size: 12px; color: #a78bfa; font-weight: 600; letter-spacing: 1px; }
.subject-desc { font-size: 13px; color: #5a5570; margin-top: 8px; }

.lecture-card { background: #12101e; border: 1.5px solid #1e1c2e; border-radius: 14px; padding: 20px; text-align: right; direction: rtl; }
.lecture-card.active { border-color: #a78bfa; background: #1a1530; }
.lecture-card.coming-soon { opacity: 0.4; }
.lec-num { font-size: 11px; color: #a78bfa; font-weight: 700; letter-spacing: 2px; margin-bottom: 6px; }
.lec-title { font-size: 15px; font-weight: 700; color: #e0ddf5; margin-bottom: 4px; }
.lec-count { font-size: 12px; color: #4a4560; }

.question-card { background: #12101e; border: 1px solid #1e1c2e; border-radius: 16px; padding: 28px; margin-bottom: 6px; direction: ltr; }
.question-card.correct-card { border-color: #22c55e44; }
.question-card.wrong-card   { border-color: #ef444444; }
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

div[data-testid="stButton"] button {
    background: #1a1826 !important;
    border: 1.5px solid #252235 !important;
    border-radius: 10px !important;
    color: #c4c0d8 !important;
    font-size: 14px !important;
    padding: 12px 16px !important;
    width: 100% !important;
    text-align: center !important;
    transition: all 0.2s !important;
}
div[data-testid="stButton"] button:hover {
    border-color: #6c63ff !important;
    color: #e0ddf5 !important;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. إدارة الجلسة والمنطق (Session State)
# ==========================================

for key, val in [("selected_subject", None), ("selected_lecture", None),
                 ("selected_file", None), ("answers", {})]:
    if key not in st.session_state:
        st.session_state[key] = val


st.markdown("""
<div class="hero">
    <div class="uni-name">🎓 جامعة المنصورة الجديدة · NMU</div>
    <h1>بنك <span>أسئلة</span> الدفعة</h1>
    <p>اختر المادة والمحاضرة وابدأ المذاكرة — مع تصحيح وشرح فوري لكل إجابة</p>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="section-title">· اختر المادة ·</div>', unsafe_allow_html=True)

cols = st.columns(len(SUBJECTS))
for idx, subj in enumerate(SUBJECTS):
    with cols[idx]:
        is_active = st.session_state.selected_subject == subj["key"]
        st.markdown(f"""
        <div class="subject-card {'active' if is_active else ''}">
            <div class="subject-icon">{subj['icon']}</div>
            <div class="subject-name">{subj['name']}</div>
            <div class="subject-code">{subj['code']}</div>
            <div class="subject-desc">{subj['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"اختر {subj['name']}", key=f"subj_{subj['key']}", use_container_width=True):
            st.session_state.selected_subject = subj["key"]
            st.session_state.selected_lecture = None
            st.session_state.selected_file = None
            st.session_state.answers = {}
            st.rerun()


if st.session_state.selected_subject:
    st.markdown("---")
    st.markdown('<div class="section-title">· اختر المحاضرة ·</div>', unsafe_allow_html=True)

    current_subject = next(s for s in SUBJECTS if s["key"] == st.session_state.selected_subject)
    lecs = current_subject["lectures"]
    lec_cols = st.columns(len(lecs))

    for idx, lec in enumerate(lecs):
        with lec_cols[idx]:
            is_active = st.session_state.selected_lecture == lec["file"]
            st.markdown(f"""
            <div class="lecture-card {'active' if is_active else ''} {'coming-soon' if not lec['available'] else ''}">
                <div class="lec-num">Lecture {lec['num']}</div>
                <div class="lec-title">{lec['title']}</div>
                <div class="lec-count">{lec['count']}</div>
            </div>
            """, unsafe_allow_html=True)
            if lec["available"]:
                if st.button(f"ابدأ {lec['title']}", key=f"lec_{lec['file']}", use_container_width=True):
                    st.session_state.selected_lecture = lec["file"]
                    st.session_state.selected_file = lec["file"]
                    st.session_state.answers = {}
                    st.rerun()
            else:
                st.markdown("<p style='color:#3a3555;font-size:13px;text-align:center;'>قريباً...</p>", unsafe_allow_html=True)


if st.session_state.selected_file:
    questions = load_questions(st.session_state.selected_file)

    if questions:
        st.markdown("---")
        answered = len(st.session_state.answers)
        score    = sum(1 for i, v in st.session_state.answers.items() if v == questions[i]["ans"])
        total    = len(questions)

        st.progress(
            answered / total if total > 0 else 0,
            text=f"تم الإجابة على {answered} من {total}  |  ✅ {score} صح  |  ❌ {answered - score} غلط"
        )

        if answered == total and total > 0:
            pct   = int((score / total) * 100)
            emoji = "🏆" if pct == 100 else "🎉" if pct >= 80 else "👍" if pct >= 60 else "📚"
            msg   = "نتيجة مثالية!" if pct == 100 else "ممتاز!" if pct >= 80 else "جيد، كمّل!" if pct >= 60 else "راجع المحاضرة تاني!"
            if pct == 100:
                st.balloons()
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

        for i, q_data in enumerate(questions):
            chosen      = st.session_state.answers.get(i)
            is_answered = chosen is not None
            is_correct  = chosen == q_data["ans"]
            q_type      = q_data.get("type", "mcq")

            card_class = "correct-card" if is_answered and is_correct else "wrong-card" if is_answered else ""
            type_label = "TRUE / FALSE" if q_type == "tf" else "MCQ"
            type_class = "q-type-tf"   if q_type == "tf" else "q-type-mcq"

            st.markdown(f"""
            <div class="question-card {card_class}">
                <div class="q-meta">Question {str(i+1).zfill(2)}</div>
                <span class="q-type-badge {type_class}">{type_label}</span>
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

                explain_key   = "explain_correct" if is_correct else "explain_wrong"
                explain_class = "explain-correct"  if is_correct else "explain-wrong"
                explain_text  = q_data.get(explain_key, "")
                if explain_text:
                    st.markdown(f'<div class="explain-box {explain_class}">{explain_text}</div>', unsafe_allow_html=True)

            else:
                opt_cols = st.columns(2)
                for j, opt in enumerate(q_data["options"]):
                    with opt_cols[j % 2]:
                        if st.button(opt, key=f"q{i}_o{j}", use_container_width=True):
                            st.session_state.answers[i] = opt
                            st.rerun()

            st.markdown("<div style='margin-bottom:12px'></div>", unsafe_allow_html=True)
