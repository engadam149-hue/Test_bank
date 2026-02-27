import streamlit as st

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
.question-card.correct-card  { border-color: #22c55e44; }
.question-card.wrong-card    { border-color: #ef444444; }
.question-card.essay-revealed { border-color: #f59e0b55; }
.q-meta { font-size: 11px; font-weight: 700; letter-spacing: 2px; color: #3a3555; text-transform: uppercase; margin-bottom: 6px; }
.q-type-badge { display: inline-block; font-size: 10px; font-weight: 700; letter-spacing: 1px; padding: 2px 10px; border-radius: 20px; margin-bottom: 10px; }
.q-type-tf    { background: #1a2a3a; color: #60a5fa; border: 1px solid #60a5fa44; }
.q-type-mcq   { background: #1a1a2a; color: #a78bfa; border: 1px solid #a78bfa44; }
.q-type-essay { background: #2a1f0a; color: #f59e0b; border: 1px solid #f59e0b44; }
.q-text { font-size: 16px; font-weight: 500; color: #e0ddf5; line-height: 1.6; margin-bottom: 16px; }
.correct-opt  { background: #15291e; border: 1.5px solid #22c55e; border-radius: 10px; padding: 12px 18px; color: #4ade80; font-size: 14px; margin-bottom: 8px; direction: rtl; text-align: right; }
.wrong-opt    { background: #2a1515; border: 1.5px solid #ef4444; border-radius: 10px; padding: 12px 18px; color: #f87171; font-size: 14px; margin-bottom: 8px; direction: rtl; text-align: right; }
.reveal-opt   { background: #15291e88; border: 1.5px solid #22c55e55; border-radius: 10px; padding: 12px 18px; color: #4ade8077; font-size: 14px; margin-bottom: 8px; direction: rtl; text-align: right; }
.neutral-opt  { background: #1a1826; border: 1.5px solid #252235; border-radius: 10px; padding: 12px 18px; color: #5a5570; font-size: 14px; margin-bottom: 8px; direction: rtl; text-align: right; }
.essay-answer-box { background: #1a1508; border: 1.5px solid #f59e0b55; border-radius: 12px; padding: 20px 24px; color: #fcd34d; font-size: 14px; line-height: 2; margin-top: 8px; margin-bottom: 14px; direction: rtl; text-align: right; }
.explain-box     { border-radius: 10px; padding: 14px 18px; font-size: 14px; line-height: 1.7; margin-top: 4px; margin-bottom: 14px; direction: rtl; text-align: right; }
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

# ════════════════════════════════════════════════════════════════════════
# 📦  DATA
# ════════════════════════════════════════════════════════════════════════

ML_LEC1 = [
    {"q":"All learning must begin with...","type":"mcq","options":["Algorithms","Data","Models","Testing"],"ans":"Data","explain_correct":"✅ صح! كل تعلم يبدأ بالبيانات — هي الأساس اللي بنبني عليه أي نموذج.","explain_wrong":"❌ غلط! البيانات هي نقطة البداية في أي عملية تعلم."},
    {"q":"Computers have short- and long-term recall capabilities using...","type":"mcq","options":["Sensors","RAM and Hard drives","Monitors","Keyboards"],"ans":"RAM and Hard drives","explain_correct":"✅ صح! RAM = ذاكرة قصيرة المدى، Hard Drive = ذاكرة طويلة المدى.","explain_wrong":"❌ غلط! الكمبيوتر بيستخدم RAM وHard Drive للتخزين."},
    {"q":"The process of assigning meaning to stored data occurs during...","type":"mcq","options":["Evaluation","Generalization","Abstraction","Storage"],"ans":"Abstraction","explain_correct":"✅ صح! الـ Abstraction هي اللي بتعطي معنى للبيانات المخزنة.","explain_wrong":"❌ غلط! إعطاء معنى للبيانات = Abstraction."},
    {"q":"During knowledge representation, the computer summarizes raw data using a...","type":"mcq","options":["Model","Sensor","CPU","Hard Disk"],"ans":"Model","explain_correct":"✅ صح! الكمبيوتر بيلخص البيانات في شكل Model.","explain_wrong":"❌ غلط! الـ knowledge representation بيستخدم Model."},
    {"q":"The process of fitting a model to a dataset is known as...","type":"mcq","options":["Training","Evaluating","Testing","Generalizing"],"ans":"Training","explain_correct":"✅ صح! ملاءمة الـ Model على البيانات = Training.","explain_wrong":"❌ غلط! تطبيق الـ Model على البيانات = Training."},
    {"q":"Turning abstracted knowledge into a form utilized for future action is called...","type":"mcq","options":["Storage","Training","Generalization","Abstraction"],"ans":"Generalization","explain_correct":"✅ صح! تطبيق المعرفة على مواقف جديدة = Generalization.","explain_wrong":"❌ غلط! تحويل المعرفة لشكل قابل للاستخدام المستقبلي = Generalization."},
    {"q":"If conclusions are systematically erroneous, the algorithm has a...","type":"mcq","options":["High variance","Bias","Perfect fit","Good model"],"ans":"Bias","explain_correct":"✅ صح! الأخطاء المنتظمة = Bias.","explain_wrong":"❌ غلط! الأخطاء المنتظمة = Bias."},
    {"q":"To judge how well a model generalizes, it is evaluated on a...","type":"mcq","options":["New test dataset","Training dataset","Old dataset","Corrupted dataset"],"ans":"New test dataset","explain_correct":"✅ صح! لمعرفة الـ Generalization، نقيّم على بيانات جديدة.","explain_wrong":"❌ غلط! لازم نقيّم على New test dataset."},
    {"q":"Trying to model noise is the basis of a problem called...","type":"mcq","options":["Underfitting","Overfitting","Perfect fitting","Evaluation"],"ans":"Overfitting","explain_correct":"✅ صح! تعلم الـ Noise = Overfitting.","explain_wrong":"❌ غلط! تعلم الـ Noise = Overfitting."},
    {"q":"A model with High Training Error and High Test Error is...","type":"mcq","options":["Overfitting","Underfitting","Just right","Perfect"],"ans":"Underfitting","explain_correct":"✅ صح! High error في الاتنين = Underfitting.","explain_wrong":"❌ غلط! High Training + High Test = Underfitting."},
    {"q":"A model with Low Training Error but High Test Error is...","type":"mcq","options":["Overfitting","Underfitting","Just right","Biased"],"ans":"Overfitting","explain_correct":"✅ صح! Low Training + High Test = Overfitting.","explain_wrong":"❌ غلط! Low training وHigh test = Overfitting."},
    {"q":"Low Bias and High Variance leads to...","type":"mcq","options":["Underfitting","Overfitting","Just right","No fitting"],"ans":"Overfitting","explain_correct":"✅ صح! Low Bias + High Variance = Overfitting.","explain_wrong":"❌ غلط! Low Bias وHigh Variance = Overfitting."},
    {"q":"High Bias and Low Variance leads to...","type":"mcq","options":["Overfitting","Underfitting","Just right","Perfect fitting"],"ans":"Underfitting","explain_correct":"✅ صح! High Bias + Low Variance = Underfitting.","explain_wrong":"❌ غلط! High Bias وLow Variance = Underfitting."},
    {"q":"To fix Underfitting, one remedy is to...","type":"mcq","options":["Complexify model","Get more data","Regularize","Try smaller features"],"ans":"Complexify model","explain_correct":"✅ صح! لحل Underfitting = زيادة تعقيد الـ Model.","explain_wrong":"❌ غلط! لحل Underfitting = زيادة تعقيد الـ Model."},
    {"q":"Which of the following fixes Overfitting?","type":"mcq","options":["Train longer","Add more features","Get more data","Complexify model"],"ans":"Get more data","explain_correct":"✅ صح! زيادة البيانات تساعد في حل Overfitting.","explain_wrong":"❌ غلط! لحل Overfitting = زيادة البيانات."},
    {"q":"If your model has High Bias, you should try to...","type":"mcq","options":["Add more features","Select fewer features","Get more data","Regularize"],"ans":"Add more features","explain_correct":"✅ صح! High Bias = الـ Model بسيط → زيادة features.","explain_wrong":"❌ غلط! High Bias بنحله بإضافة features."},
    {"q":"If your model has High Variance, you should try to...","type":"mcq","options":["Train longer","Add more features","Regularize","Make more complex"],"ans":"Regularize","explain_correct":"✅ صح! High Variance بنحله بالـ Regularization.","explain_wrong":"❌ غلط! High Variance بنحله بالـ Regularization."},
    {"q":"Bias measures the ________ of the model.","type":"mcq","options":["Precision","Speed","Accuracy or quality","Size"],"ans":"Accuracy or quality","explain_correct":"✅ صح! الـ Bias بيقيس الـ Accuracy.","explain_wrong":"❌ غلط! الـ Bias بيقيس الـ Accuracy."},
    {"q":"Variance measures the ________ of the model.","type":"mcq","options":["Accuracy","Precision or specificity","Speed","Memory"],"ans":"Precision or specificity","explain_correct":"✅ صح! الـ Variance بيقيس الـ Precision.","explain_wrong":"❌ غلط! الـ Variance بيقيس الـ Precision."},
    {"q":"When Model Complexity is LOW, the result is...","type":"mcq","options":["Overfitting","Underfitting","Perfect Fit","High Variance"],"ans":"Underfitting","explain_correct":"✅ صح! Low Complexity = Underfitting.","explain_wrong":"❌ غلط! Low Complexity = Underfitting."},
    {"q":"When Model Complexity is HIGH, the result is...","type":"mcq","options":["Overfitting","Underfitting","Perfect Fit","High Bias"],"ans":"Overfitting","explain_correct":"✅ صح! High Complexity = Overfitting.","explain_wrong":"❌ غلط! High Complexity = Overfitting."},
    {"q":"A model with Low Bias and Low Variance is considered...","type":"mcq","options":["Underfitting","Overfitting","Just right (Good Fit)","A failure"],"ans":"Just right (Good Fit)","explain_correct":"✅ صح! Low Bias + Low Variance = Good Fit المثالي.","explain_wrong":"❌ غلط! Low Bias وLow Variance = الـ Good Fit."},
    {"q":"Bias is considered a ________ associated with abstraction and generalization.","type":"mcq","options":["Necessary evil","Perfect feature","Hardware issue","Random noise"],"ans":"Necessary evil","explain_correct":"✅ صح! الـ Bias هو Necessary evil — موجود في كل عملية تعميم.","explain_wrong":"❌ غلط! الـ Bias يُعتبر Necessary evil."},
    {"q":"Which step provides a feedback mechanism to measure utility?","type":"mcq","options":["Abstraction","Storage","Evaluation","Generalization"],"ans":"Evaluation","explain_correct":"✅ صح! الـ Evaluation هي اللي بتوفر feedback عن أداء الـ Model.","explain_wrong":"❌ غلط! الـ Evaluation هي الـ feedback mechanism."},
    {"q":"Noisy data can be caused by...","type":"mcq","options":["Measurement error","Perfect sensors","Clean data","Good subjects"],"ans":"Measurement error","explain_correct":"✅ صح! Measurement error هو أحد أسباب الـ Noisy data.","explain_wrong":"❌ غلط! الـ Noise بيجي من Measurement errors."},
]

ML_LEC2 = [
    {"q":"What does KNN stand for?","type":"mcq","options":["K-Nearest Neighbors","K-Neural Network","K-Norm Node","K-Net Numeric"],"ans":"K-Nearest Neighbors","explain_correct":"✅ صح! KNN = K-Nearest Neighbors.","explain_wrong":"❌ غلط! KNN = K-Nearest Neighbors."},
    {"q":"KNN is classified as a ________ learning algorithm.","type":"mcq","options":["Supervised","Unsupervised","Reinforcement","Semi-supervised"],"ans":"Supervised","explain_correct":"✅ صح! KNN تحتاج labels = Supervised.","explain_wrong":"❌ غلط! KNN = Supervised (تحتاج labels)."},
    {"q":"k-NN algorithm does more computation on test time rather than train time.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! كل الحساب بيحصل وقت الـ testing.","explain_wrong":"❌ غلط! KNN بيعمل معظم الحساب وقت الـ testing."},
    {"q":"Which is a STRENGTH of the KNN algorithm?","type":"mcq","options":["Simple and effective with no assumptions about data","Fast classification","Handles missing data","Produces interpretable model"],"ans":"Simple and effective with no assumptions about data","explain_correct":"✅ صح! KNN بسيط وفعّال ومش بيفترض شكل البيانات.","explain_wrong":"❌ غلط! الـ classification phase في KNN بطيئة."},
    {"q":"Which is a WEAKNESS of the KNN algorithm?","type":"mcq","options":["Slow classification phase","Large training time","Strong assumptions","Cannot handle numeric features"],"ans":"Slow classification phase","explain_correct":"✅ صح! KNN بطيء وقت التصنيف.","explain_wrong":"❌ غلط! الـ training سريعة، لكن الـ classification بطيئة."},
    {"q":"In KNN, the unlabeled instance is assigned the class of...","type":"mcq","options":["Majority of k nearest neighbors","Single closest neighbor","Farthest neighbor","Random neighbor"],"ans":"Majority of k nearest neighbors","explain_correct":"✅ صح! KNN بيختار الفئة الأغلبية من الـ K جيران.","explain_wrong":"❌ غلط! KNN بيعتمد على أغلبية الـ K جيران."},
    {"q":"What is the Euclidean distance between A(0,1) and B(2,3)?","type":"mcq","options":["√8 ≈ 2.83","1","2","4"],"ans":"√8 ≈ 2.83","explain_correct":"✅ صح! sqrt((2-0)²+(3-1)²) = sqrt(8) ≈ 2.83","explain_wrong":"❌ غلط! sqrt((2-0)²+(3-1)²) = sqrt(8) ≈ 2.83"},
    {"q":"The normalization formula in KNN is...","type":"mcq","options":["x = (x-MIN)/(MAX-MIN)","x = (x-MEAN)/STD","x = x/MAX","x = x-MIN"],"ans":"x = (x-MIN)/(MAX-MIN)","explain_correct":"✅ صح! Min-Max Normalization = (x-MIN)/(MAX-MIN).","explain_wrong":"❌ غلط! الصيغة الصح = (x-MIN)/(MAX-MIN)."},
    {"q":"Min-Max Normalization scales data to...","type":"mcq","options":["[0, 1]","[-1, 1]","[0, 100]","[-∞,+∞]"],"ans":"[0, 1]","explain_correct":"✅ صح! Min-Max = [0,1].","explain_wrong":"❌ غلط! Min-Max = [0,1]."},
    {"q":"Given MIN=-5, MAX=25. Normalized value of 7 = ?","type":"mcq","options":["0.4","0.3","0.5","0.6"],"ans":"0.4","explain_correct":"✅ صح! (7-(-5))/(25-(-5)) = 12/30 = 0.4","explain_wrong":"❌ غلط! (7-(-5))/(25-(-5)) = 12/30 = 0.4"},
    {"q":"Very large K may...","type":"mcq","options":["Include points from other classes","Always give accurate results","Reduce computation","Eliminate normalization"],"ans":"Include points from other classes","explain_correct":"✅ صح! K كبير = يدخل نقاط من فئات تانية.","explain_wrong":"❌ غلط! K كبير = يجلب جيران من فئات مختلفة."},
    {"q":"Very small K (like K=1) makes algorithm...","type":"mcq","options":["Very sensitive to noise","More accurate","Faster","Better at outliers"],"ans":"Very sensitive to noise","explain_correct":"✅ صح! K=1 حساس جداً للـ noise.","explain_wrong":"❌ غلط! K صغير = حساسية عالية للـ noise."},
    {"q":"Odd K is preferred to avoid...","type":"mcq","options":["Tie voting","Overfitting","Underfitting","Slow training"],"ans":"Tie voting","explain_correct":"✅ صح! K الفردي يتجنب الـ tie voting.","explain_wrong":"❌ غلط! K الزوجي يسبب Tie Voting."},
    {"q":"Increasing K in KNN increases the...","type":"mcq","options":["Bias","Variance","Accuracy","Speed"],"ans":"Bias","explain_correct":"✅ صح! زيادة K = زيادة bias (underfitting).","explain_wrong":"❌ غلط! زيادة K = زيادة bias."},
    {"q":"k-NN performs better when data have the same scale.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! نفس الـ scale = حساب مسافة عادل.","explain_wrong":"❌ غلط! KNN أحسن مع نفس الـ scale."},
    {"q":"100% training accuracy + poor test accuracy = ...","type":"mcq","options":["Overfitting","Underfitting","Perfect model","Test data problem"],"ans":"Overfitting","explain_correct":"✅ صح! 100% training + ضعيف testing = Overfitting.","explain_wrong":"❌ غلط! ده Overfitting."},
    {"q":"A Tomek Link is a pair [x,y] where both are each other's nearest neighbor but have...","type":"mcq","options":["Different classes","Same class","Same distance","Same weight"],"ans":"Different classes","explain_correct":"✅ صح! Tomek Link = أقرب جار لبعض من فئتين مختلفتين.","explain_wrong":"❌ غلط! Tomek Link = فئتين مختلفتين."},
    {"q":"Weighted k-NN: if Σ(POS) > Σ(NEG), classify as...","type":"mcq","options":["Positive","Negative","Neutral","Undecided"],"ans":"Positive","explain_correct":"✅ صح! ΣPOS > ΣNEG → Positive.","explain_wrong":"❌ غلط! ΣPOS > ΣNEG → Positive."},
    {"q":"KNN makes no assumptions about data distribution.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! KNN non-parametric = مش بيفترض شكل البيانات.","explain_wrong":"❌ غلط! KNN فعلاً مش بيفترض شكل البيانات."},
    {"q":"The scaling problem in KNN occurs when...","type":"mcq","options":["One feature with large range overwhelms others","Dataset too large","K too high","Model overfits"],"ans":"One feature with large range overwhelms others","explain_correct":"✅ صح! Feature بـ range كبيرة تطغى على الباقي.","explain_wrong":"❌ غلط! Scaling problem = feature بـ range كبيرة تطغى."},
    {"q":"k-NN struggles when the number of input variables is very large.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! Curse of dimensionality بيأثر على KNN.","explain_wrong":"❌ غلط! KNN بيعاني مع الـ features الكتيرة."},
    {"q":"The main benefit of using k neighbors vs 1 neighbor is...","type":"mcq","options":["Voting overcomes noise","Faster computation","No distance needed","Better missing data"],"ans":"Voting overcomes noise","explain_correct":"✅ صح! الـ voting بين K جيران بيتغلب على الـ noise.","explain_wrong":"❌ غلط! الفايدة = الـ voting بيقلل الـ noise."},
    {"q":"Nearest neighbor classifiers struggle when...","type":"mcq","options":["Data is noisy with no clear class distinction","Too many examples","All features normalized","K is odd"],"ans":"Data is noisy with no clear class distinction","explain_correct":"✅ صح! Noisy data + مفيش حدود واضحة = KNN بيصعب عليه.","explain_wrong":"❌ غلط! KNN بيصعب عليه مع noisy data."},
    {"q":"Weighted 5-NN (d1=1, d5=8): weight of nearest neighbor w1 = ?","type":"mcq","options":["1","5/7","4/7","0"],"ans":"1","explain_correct":"✅ صح! w1 = (8-1)/(8-1) = 1.","explain_wrong":"❌ غلط! w1 = (8-1)/(8-1) = 1."},
    {"q":"Weighted 5-NN (d1=1, d5=8): weight of farthest neighbor w5 = ?","type":"mcq","options":["0","1","3/7","5/7"],"ans":"0","explain_correct":"✅ صح! w5 = (8-8)/(8-1) = 0.","explain_wrong":"❌ غلط! w5 = (8-8)/(8-1) = 0."},
]

ARC_LEC1 = [
    {"q":"Computer Organization deals with how hardware components are interconnected and operate to execute instructions.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! Computer Organization = كيفية ترابط وتشغيل المكونات المادية.","explain_wrong":"❌ غلط! Computer Organization يتعامل مع كيفية ترابط المكونات المادية."},
    {"q":"Computer Architecture refers to those attributes of a system visible to the...","type":"mcq","options":["Programmer","Hardware engineer","OS only","Network administrator"],"ans":"Programmer","explain_correct":"✅ صح! Computer Architecture = الخصائص المرئية للـ programmer.","explain_wrong":"❌ غلط! Computer Architecture = الخصائص المرئية للـ programmer."},
    {"q":"ISA stands for...","type":"mcq","options":["Instruction Set Architecture","Internal System Array","Input Signal Analyzer","Integrated Storage Area"],"ans":"Instruction Set Architecture","explain_correct":"✅ صح! ISA = Instruction Set Architecture.","explain_wrong":"❌ غلط! ISA = Instruction Set Architecture."},
    {"q":"'Is there a multiply instruction?' — this is an example of...","type":"mcq","options":["Architecture attribute","Organization attribute","Memory technology","Control signal"],"ans":"Architecture attribute","explain_correct":"✅ صح! وجود تعليمة الضرب هو Architecture attribute — مرئية للمبرمج.","explain_wrong":"❌ غلط! هل في multiply instruction = Architecture (يراها المبرمج)."},
    {"q":"'Is multiplication done by repeated addition or hardware unit?' — this is an example of...","type":"mcq","options":["Organization attribute","Architecture attribute","ISA attribute","Memory attribute"],"ans":"Organization attribute","explain_correct":"✅ صح! طريقة تنفيذ الضرب داخلياً = Organization (شفافة للمبرمج).","explain_wrong":"❌ غلط! كيفية تنفيذ الضرب داخلياً = Organization attribute."},
    {"q":"Structure is the way in which components ________ to each other.","type":"mcq","options":["Relate","Compete","Disconnect","Replace"],"ans":"Relate","explain_correct":"✅ صح! Structure = طريقة ارتباط المكونات ببعضها.","explain_wrong":"❌ غلط! Structure = كيفية ارتباط المكونات."},
    {"q":"Function is the operation of individual components as part of the structure.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! Function = عمل كل مكون كجزء من الـ Structure.","explain_wrong":"❌ غلط! Function = عمل المكون كجزء من الـ Structure."},
    {"q":"Which component controls the computer and performs data processing?","type":"mcq","options":["CPU","Main Memory","I/O","Bus"],"ans":"CPU","explain_correct":"✅ صح! الـ CPU بيتحكم وينفذ معالجة البيانات.","explain_wrong":"❌ غلط! الـ CPU هو المتحكم ومعالج البيانات."},
    {"q":"Main memory's primary function is to...","type":"mcq","options":["Store data","Process data","Transfer to external devices","Control operations"],"ans":"Store data","explain_correct":"✅ صح! Main Memory = Store data.","explain_wrong":"❌ غلط! Main Memory = Store data."},
    {"q":"I/O moves data between the computer and its external environment (peripherals).","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! I/O بتنقل البيانات بين الكمبيوتر والـ peripherals.","explain_wrong":"❌ غلط! I/O = نقل البيانات بين الكمبيوتر والبيئة الخارجية."},
    {"q":"Organizational attributes are hardware details ________ to the programmer.","type":"mcq","options":["Transparent (invisible)","Visible","Critical","Essential"],"ans":"Transparent (invisible)","explain_correct":"✅ صح! Organizational attributes شفافة (غير مرئية) للمبرمج.","explain_wrong":"❌ غلط! Organizational attributes = Transparent للمبرمج."},
    {"q":"System interconnection provides communication among CPU, main memory, and I/O.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! System interconnection (Bus) يربط الـ CPU والـ Memory والـ I/O.","explain_wrong":"❌ غلط! System interconnection يربط الـ CPU والـ Memory والـ I/O."},
    # ─── ESSAY ───────────────────────────────────────────────────────────────
    {
        "q": "What is the distinction between Computer Organization and Computer Architecture?",
        "type": "essay",
        "ans": (
            "• Computer Architecture:\n"
            "  الخصائص المرئية للمبرمج اللي ليها تأثير مباشر على تنفيذ البرنامج.\n"
            "  مثال: هل في multiply instruction?\n\n"
            "• Computer Organization:\n"
            "  التفاصيل المادية الشفافة للمبرمج (لا يراها ولا يتأثر بها).\n"
            "  مثال: هل الضرب بـ hardware unit أم بـ repeated addition?\n\n"
            "الفرق: Architecture = ماذا يرى المبرمج | Organization = كيف يتم التنفيذ داخلياً"
        )
    },
    {
        "q": "What is the distinction between Computer Structure and Computer Function?",
        "type": "essay",
        "ans": (
            "• Structure: طريقة ارتباط المكونات ببعضها (How components relate to each other).\n\n"
            "• Function: عمل كل مكون بشكل فردي كجزء من الـ Structure\n"
            "  (Operation of individual components as part of the structure).\n\n"
            "الفرق: Structure = العلاقة بين المكونات | Function = وظيفة كل مكون"
        )
    },
    {
        "q": "List and briefly define the main structural components of a computer.",
        "type": "essay",
        "ans": (
            "1. CPU (Central Processing Unit):\n"
            "   يتحكم في عمليات الكمبيوتر وينفذ معالجة البيانات.\n\n"
            "2. Main Memory:\n"
            "   تخزن البيانات.\n\n"
            "3. I/O (Input/Output):\n"
            "   تنقل البيانات بين الكمبيوتر والبيئة الخارجية (peripherals).\n\n"
            "4. System Interconnection:\n"
            "   توفر التواصل بين CPU والـ Memory والـ I/O (مثل الـ Bus)."
        )
    },
]

ARC_LEC2 = [
    {"q":"Which component of the CPU controls its operation?","type":"mcq","options":["Control Unit (CU)","ALU","Registers","Cache"],"ans":"Control Unit (CU)","explain_correct":"✅ صح! الـ CU هو اللي بيتحكم في عمليات الـ CPU.","explain_wrong":"❌ غلط! الـ CU = يتحكم في الـ CPU."},
    {"q":"The ALU performs arithmetic and logic operations.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! ALU = Arithmetic and Logic Unit.","explain_wrong":"❌ غلط! ALU بيعمل العمليات الحسابية والمنطقية."},
    {"q":"AND, NOT, and shift operations are examples of ________ operations.","type":"mcq","options":["Logic","Arithmetic","Control","Memory"],"ans":"Logic","explain_correct":"✅ صح! AND, NOT, Shift = Logic operations.","explain_wrong":"❌ غلط! AND, NOT, Shift = Logic operations."},
    {"q":"Registers provide ________ storage to the CPU.","type":"mcq","options":["Internal","External","Permanent","Optical"],"ans":"Internal","explain_correct":"✅ صح! Registers = Internal storage للـ CPU.","explain_wrong":"❌ غلط! Registers = Internal storage."},
    {"q":"What are the four main functions of a computer?","type":"mcq","options":["Data processing, storage, movement, Control","Printing, scanning, networking, display","Input, output, memory, CPU","Fetch, decode, execute, store"],"ans":"Data processing, storage, movement, Control","explain_correct":"✅ صح! الأربع وظائف: معالجة، تخزين، تحريك، تحكم.","explain_wrong":"❌ غلط! الوظائف الأربعة: processing, storage, movement, Control."},
    {"q":"Data movement refers to transfer of data between different components.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! Data movement = نقل البيانات بين المكونات.","explain_wrong":"❌ غلط! Data movement = نقل البيانات بين المكونات."},
    {"q":"A processor with multiple cores is called a...","type":"mcq","options":["Multicore processor","Single-core processor","Virtual processor","Parallel processor"],"ans":"Multicore processor","explain_correct":"✅ صح! Multiple cores = Multicore processor.","explain_wrong":"❌ غلط! Multiple cores = Multicore processor."},
    {"q":"In a bus, each line carries...","type":"mcq","options":["One bit","One byte","One word","Multiple bits"],"ans":"One bit","explain_correct":"✅ صح! كل line في الـ bus = 1 bit.","explain_wrong":"❌ غلط! كل line في الـ bus = 1 bit."},
    {"q":"Single Bus structure: all units connected to the same bus.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! Single Bus = كل الوحدات على نفس الـ bus.","explain_wrong":"❌ غلط! Single Bus = كل الوحدات على نفس الـ bus."},
    {"q":"Which bus structure has better performance?","type":"mcq","options":["Multiple Bus","Single Bus","Both equal","Neither"],"ans":"Multiple Bus","explain_correct":"✅ صح! Multiple Bus أحسن في الأداء.","explain_wrong":"❌ غلط! Multiple Bus أحسن أداءً."},
    {"q":"Which bus structure is cheaper?","type":"mcq","options":["Single Bus","Multiple Bus","Both equal","Depends on CPU"],"ans":"Single Bus","explain_correct":"✅ صح! Single Bus أرخص لكن أداؤه أقل.","explain_wrong":"❌ غلط! Single Bus أرخص."},
    {"q":"Data bus lines are...","type":"mcq","options":["Bi-directional","Unidirectional","Input only","Output only"],"ans":"Bi-directional","explain_correct":"✅ صح! Data bus = Bi-directional.","explain_wrong":"❌ غلط! Data bus = Bi-directional (في الاتجاهين)."},
    {"q":"The address bus is...","type":"mcq","options":["Unidirectional","Bi-directional","Wireless","Virtual"],"ans":"Unidirectional","explain_correct":"✅ صح! Address bus = Unidirectional (من CPU لـ Memory).","explain_wrong":"❌ غلط! Address bus = Unidirectional."},
    {"q":"The control bus is...","type":"mcq","options":["Bi-directional","Unidirectional","Input only","Output only"],"ans":"Bi-directional","explain_correct":"✅ صح! Control bus = Bi-directional.","explain_wrong":"❌ غلط! Control bus = Bi-directional."},
    {"q":"Maximum addressable memory = ?","type":"mcq","options":["2^n (n = address lines)","n × 8","2 × n","n^2"],"ans":"2^n (n = address lines)","explain_correct":"✅ صح! Maximum addressable memory = 2^n.","explain_wrong":"❌ غلط! Maximum addressable memory = 2^n."},
    {"q":"A 16-bit address bus can access...","type":"mcq","options":["65,536 locations","256 locations","4 GB","1,024 locations"],"ans":"65,536 locations","explain_correct":"✅ صح! 2^16 = 65,536.","explain_wrong":"❌ غلط! 2^16 = 65,536."},
    {"q":"A 32-bit address bus can access...","type":"mcq","options":["4 GB","2 GB","1 GB","16 GB"],"ans":"4 GB","explain_correct":"✅ صح! 2^32 = 4 GB.","explain_wrong":"❌ غلط! 2^32 = 4 GB."},
    {"q":"A computer system has 16 GB of RAM. Minimum address bus size = ?","type":"mcq","options":["34 bits","32 bits","30 bits","16 bits"],"ans":"34 bits","explain_correct":"✅ صح! 16 GB = 16 × 2^30 = 2^34 → 34 bits.","explain_wrong":"❌ غلط! 16 GB = 2^34 → نحتاج 34 bits."},
    {"q":"A computer system has 512 MB of RAM. Minimum address bus size = ?","type":"mcq","options":["29 bits","32 bits","20 bits","512 bits"],"ans":"29 bits","explain_correct":"✅ صح! 512 MB = 512 × 2^20 = 2^29 → 29 bits.","explain_wrong":"❌ غلط! 512 MB = 2^29 → نحتاج 29 bits."},
    {"q":"Address Bus Size = log₂(Memory Size in Bytes).","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! Address Bus Size = log₂(Memory Size in Bytes).","explain_wrong":"❌ غلط! Address Bus Size = log₂(Memory Size in Bytes)."},
    {"q":"If address bus = 4 bits, number of memory locations = ?","type":"mcq","options":["16","4","8","32"],"ans":"16","explain_correct":"✅ صح! 2^4 = 16 مواقع.","explain_wrong":"❌ غلط! 2^4 = 16."},
    {"q":"If data bus = 3 bits, each memory cell stores...","type":"mcq","options":["3 bits","8 bits","16 bits","1 bit"],"ans":"3 bits","explain_correct":"✅ صح! حجم خلية الذاكرة = حجم data bus = 3 bits.","explain_wrong":"❌ غلط! حجم خلية الذاكرة = حجم data bus = 3 bits."},
    {"q":"The CPU uses the control bus to send read/write signals to memory.","type":"tf","options":["True","False"],"ans":"True","explain_correct":"✅ صح! الـ CPU بيستخدم Control bus لإرسال إشارات القراءة/الكتابة.","explain_wrong":"❌ غلط! الـ CPU بيستخدم Control bus لإرسال إشارات التحكم."},
    # ─── ESSAY ───────────────────────────────────────────────────────────────
    {
        "q": "Distinguish between Single Bus and Multiple Bus structures (with description).",
        "type": "essay",
        "ans": (
            "• Single Bus:\n"
            "  كل الوحدات (CPU, Memory, I/O) متصلة بـ bus واحد مشترك.\n"
            "  ✅ التكلفة أقل (Cheaper)\n"
            "  ❌ الأداء أقل (Lower performance) — الوحدات بتتنافس على نفس الـ bus\n\n"
            "• Multiple Bus:\n"
            "  في أكثر من bus متخصص لنقل البيانات (مثل Memory Bus + I/O Bus).\n"
            "  ✅ الأداء أفضل (Better performance)\n"
            "  ❌ التكلفة أعلى (More expensive)\n\n"
            "مثال Double Bus: Memory Bus (CPU ↔ Memory) | I/O Bus (Input/Output ↔ CPU)"
        )
    },
    {
        "q": "Compare between Data Bus, Address Bus, and Control Bus.",
        "type": "essay",
        "ans": (
            "Data Bus:\n"
            "  - الوظيفة: نقل البيانات والتعليمات بين المكونات\n"
            "  - الاتجاه: Bi-directional (في الاتجاهين)\n"
            "  - الحجم: 8, 16, 32, أو 64 bit\n\n"
            "Address Bus:\n"
            "  - الوظيفة: نقل عناوين الذاكرة من CPU للذاكرة\n"
            "  - الاتجاه: Unidirectional (اتجاه واحد فقط)\n"
            "  - يحدد الـ Maximum Addressable Memory = 2^n\n\n"
            "Control Bus:\n"
            "  - الوظيفة: نقل إشارات التحكم (Read/Write/Interrupt)\n"
            "  - الاتجاه: Bi-directional\n"
            "  - مثال: CPU يطلب من Memory القراءة عبر Control Bus"
        )
    },
]

# ════════════════════════════════════════════════════════════════════════
# ⚙️  Config
# ════════════════════════════════════════════════════════════════════════
SUBJECTS = [
    {
        "icon":"🤖","name":"Machine Learning","code":"AIE121",
        "desc":"Intro, KNN, Decision Trees...","key":"ml",
        "lectures":[
            {"num":"01","title":"Intro to ML",   "count":"25 سؤال","key":"ml_lec1","available":True},
            {"num":"02","title":"KNN Algorithm", "count":"25 سؤال","key":"ml_lec2","available":True},
        ]
    },
    {
        "icon":"💻","name":"Computer Architecture","code":"CSE132",
        "desc":"Organization, CPU, Bus, Memory...","key":"arc",
        "lectures":[
            {"num":"01","title":"Org vs Architecture","count":"12 MCQ + 3 مقالي","key":"arc_lec1","available":True},
            {"num":"02","title":"CPU & Bus Structures", "count":"23 MCQ + 2 مقالي","key":"arc_lec2","available":True},
        ]
    },
]

QUESTIONS_DB = {
    "ml_lec1" : ML_LEC1,
    "ml_lec2" : ML_LEC2,
    "arc_lec1": ARC_LEC1,
    "arc_lec2": ARC_LEC2,
}

# ════════════════════════════════════════════════════════════════════════
# 🔧  Session State
# ════════════════════════════════════════════════════════════════════════
for k, v in [("sel_subj",None),("sel_lec",None),("answers",{}),("essay_revealed",set())]:
    if k not in st.session_state:
        st.session_state[k] = v

# ════════════════════════════════════════════════════════════════════════
# 🎨  UI
# ════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
    <div class="uni-name">🎓 جامعة المنصورة الجديدة · NMU</div>
    <h1>بنك <span>أسئلة</span> الدفعة</h1>
    <p>اختر المادة والمحاضرة وابدأ المذاكرة — مع تصحيح وشرح فوري لكل إجابة</p>
</div>
""", unsafe_allow_html=True)

# ── المادة
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
            st.session_state.sel_subj       = subj["key"]
            st.session_state.sel_lec        = None
            st.session_state.answers        = {}
            st.session_state.essay_revealed = set()
            st.rerun()

# ── المحاضرة
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
                    st.session_state.sel_lec        = lec["key"]
                    st.session_state.answers        = {}
                    st.session_state.essay_revealed = set()
                    st.rerun()
            else:
                st.markdown("<p style='color:#3a3555;font-size:13px;text-align:center;'>قريباً...</p>", unsafe_allow_html=True)

# ── الكويز
if st.session_state.sel_lec:
    questions = QUESTIONS_DB.get(st.session_state.sel_lec, [])
    if questions:
        st.markdown("---")

        mcq_tf = [(i,q) for i,q in enumerate(questions) if q["type"] != "essay"]
        essays  = [(i,q) for i,q in enumerate(questions) if q["type"] == "essay"]
        answered = sum(1 for i,_ in mcq_tf if i in st.session_state.answers)
        score    = sum(1 for i,q in mcq_tf if st.session_state.answers.get(i) == q["ans"])
        total_m  = len(mcq_tf)
        revealed = len(st.session_state.essay_revealed)

        prog_val = (answered + revealed) / len(questions) if questions else 0
        st.progress(prog_val,
            text=f"MCQ/TF: {answered}/{total_m}  ✅ {score} صح  |  مقالي: {revealed}/{len(essays)} شوفتهم")

        if answered == total_m and total_m > 0:
            pct   = int(score/total_m*100)
            emoji = "🏆" if pct==100 else "🎉" if pct>=80 else "👍" if pct>=60 else "📚"
            msg   = "نتيجة مثالية!" if pct==100 else "ممتاز!" if pct>=80 else "جيد، كمّل!" if pct>=60 else "راجع المحاضرة تاني!"
            if pct==100: st.balloons()
            st.markdown(f"""
            <div class="score-banner">
                <div class="score-big">{score}<span style="font-size:32px;color:#4a4560">/{total_m}</span></div>
                <div class="score-label">{emoji} {msg}</div>
                <div class="score-sub">{pct}% إجابات صحيحة</div>
            </div>""", unsafe_allow_html=True)
            if st.button("🔄 إعادة المحاولة", use_container_width=True):
                st.session_state.answers        = {}
                st.session_state.essay_revealed = set()
                st.rerun()
            st.markdown("---")

        for i, q in enumerate(questions):
            qt = q.get("type","mcq")

            # ═══ ESSAY ════════════════════════════════════════════
            if qt == "essay":
                is_rev   = i in st.session_state.essay_revealed
                card_cls = "essay-revealed" if is_rev else ""
                st.markdown(f"""
                <div class="question-card {card_cls}">
                    <div class="q-meta">Question {str(i+1).zfill(2)}</div>
                    <span class="q-type-badge q-type-essay">ESSAY ✍️</span>
                    <div class="q-text">{q['q']}</div>
                </div>""", unsafe_allow_html=True)
                if is_rev:
                    formatted = q["ans"].replace("\n","<br>")
                    st.markdown(f'<div class="essay-answer-box">📝 <b>الإجابة النموذجية:</b><br><br>{formatted}</div>', unsafe_allow_html=True)
                else:
                    c1, c2, c3 = st.columns([1,2,1])
                    with c2:
                        if st.button("👁️ عرض الإجابة النموذجية", key=f"essay_{i}", use_container_width=True):
                            st.session_state.essay_revealed.add(i)
                            st.rerun()

            # ═══ MCQ / TF ═════════════════════════════════════════
            else:
                chosen      = st.session_state.answers.get(i)
                is_answered = chosen is not None
                is_correct  = chosen == q["ans"]
                card_cls    = "correct-card" if is_answered and is_correct else "wrong-card" if is_answered else ""
                badge_lbl   = "TRUE / FALSE" if qt=="tf" else "MCQ"
                badge_cls   = "q-type-tf"   if qt=="tf" else "q-type-mcq"

                st.markdown(f"""
                <div class="question-card {card_cls}">
                    <div class="q-meta">Question {str(i+1).zfill(2)}</div>
                    <span class="q-type-badge {badge_cls}">{badge_lbl}</span>
                    <div class="q-text">{q['q']}</div>
                </div>""", unsafe_allow_html=True)

                if is_answered:
                    for opt in q["options"]:
                        if opt==q["ans"] and opt==chosen:
                            st.markdown(f'<div class="correct-opt">✅ {opt}</div>', unsafe_allow_html=True)
                        elif opt==chosen:
                            st.markdown(f'<div class="wrong-opt">❌ {opt}</div>', unsafe_allow_html=True)
                        elif opt==q["ans"]:
                            st.markdown(f'<div class="reveal-opt">✅ {opt} ← الإجابة الصحيحة</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="neutral-opt">{opt}</div>', unsafe_allow_html=True)
                    exp_key = "explain_correct" if is_correct else "explain_wrong"
                    exp_txt = q.get(exp_key,"")
                    exp_cls = "explain-correct" if is_correct else "explain-wrong"
                    if exp_txt:
                        st.markdown(f'<div class="explain-box {exp_cls}">{exp_txt}</div>', unsafe_allow_html=True)
                else:
                    opt_cols = st.columns(2)
                    for j, opt in enumerate(q["options"]):
                        with opt_cols[j%2]:
                            if st.button(opt, key=f"q{i}_o{j}", use_container_width=True):
                                st.session_state.answers[i] = opt
                                st.rerun()

            st.markdown("<div style='margin-bottom:12px'></div>", unsafe_allow_html=True)
