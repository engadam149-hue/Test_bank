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
# 📦 البيانات — كل الأسئلة هنا
# ════════════════════════════════════════════════════════════

ML_LEC1 = [
    {"q": "All learning must begin with...", "type": "mcq", "options": ["Algorithms", "Data", "Models", "Testing"], "ans": "Data", "explain_correct": "✅ صح! كل تعلم لازم يبدأ بالبيانات — هي الأساس اللي بنبني عليه أي نموذج.", "explain_wrong": "❌ غلط! البيانات هي نقطة البداية في أي عملية تعلم — مش الخوارزميات أو الموديلز."},
    {"q": "Computers have short- and long-term recall capabilities using...", "type": "mcq", "options": ["Sensors", "RAM and Hard drives", "Monitors", "Keyboards"], "ans": "RAM and Hard drives", "explain_correct": "✅ صح! الـ RAM = ذاكرة قصيرة المدى، الـ Hard Drive = ذاكرة طويلة المدى.", "explain_wrong": "❌ غلط! الكمبيوتر بيستخدم RAM (قصير المدى) و Hard Drive (طويل المدى) للتخزين."},
    {"q": "Data storage utilizes observation, memory, and recall to provide a...", "type": "mcq", "options": ["Abstract representation", "Factual basis", "Generalization", "Bias"], "ans": "Factual basis", "explain_correct": "✅ صح! تخزين البيانات بيوفر Factual basis (أساس واقعي) للتعلم.", "explain_wrong": "❌ غلط! الـ data storage بيوفر Factual basis — يعني حقائق حقيقية نبني عليها."},
    {"q": "The human brain uses what kind of signals to store and process observations?", "type": "mcq", "options": ["Electrochemical", "Mechanical", "Radioactive", "Magnetic"], "ans": "Electrochemical", "explain_correct": "✅ صح! المخ البشري بيستخدم إشارات Electrochemical (كيميائية كهربائية) لتخزين البيانات.", "explain_wrong": "❌ غلط! المخ بيستخدم إشارات Electrochemical — مش ميكانيكية أو مغناطيسية."},
    {"q": "Data storage is used as a foundation for more advanced...", "type": "mcq", "options": ["Reasoning", "Printing", "Ignoring", "Deleting"], "ans": "Reasoning", "explain_correct": "✅ صح! تخزين البيانات هو الأساس للـ Reasoning (الاستدلال) الأكثر تعقيداً.", "explain_wrong": "❌ غلط! الـ data storage بيمهد الطريق للـ Reasoning — التفكير والاستنتاج."},
    {"q": "The process of assigning meaning to stored data occurs during...", "type": "mcq", "options": ["Evaluation", "Generalization", "Abstraction", "Storage"], "ans": "Abstraction", "explain_correct": "✅ صح! الـ Abstraction هي المرحلة اللي بنعطي فيها معنى للبيانات المخزنة.", "explain_wrong": "❌ غلط! إعطاء معنى للبيانات بيحصل في مرحلة الـ Abstraction مش الـ Storage."},
    {"q": "During knowledge representation, the computer summarizes raw data using a...", "type": "mcq", "options": ["Model", "Sensor", "CPU", "Hard Disk"], "ans": "Model", "explain_correct": "✅ صح! الكمبيوتر بيلخص البيانات الخام في شكل Model (نموذج).", "explain_wrong": "❌ غلط! الـ knowledge representation بيستخدم Model لتلخيص البيانات الخام."},
    {"q": "A model is an explicit description of the ________ within the data.", "type": "mcq", "options": ["Noise", "Errors", "Patterns", "Missing values"], "ans": "Patterns", "explain_correct": "✅ صح! الـ Model هو وصف صريح للـ Patterns (الأنماط) الموجودة في البيانات.", "explain_wrong": "❌ غلط! الـ Model بيصف الـ Patterns في البيانات — مش الـ Noise أو الأخطاء."},
    {"q": "Mathematical equations and relational diagrams are examples of...", "type": "mcq", "options": ["Noise", "Models", "Hardware", "Sensors"], "ans": "Models", "explain_correct": "✅ صح! المعادلات الرياضية والمخططات العلائقية كلها أمثلة على الـ Models.", "explain_wrong": "❌ غلط! المعادلات والمخططات هي أمثلة على الـ Models — طرق لتمثيل المعرفة."},
    {"q": "The process of fitting a model to a dataset is known as...", "type": "mcq", "options": ["Training", "Evaluating", "Testing", "Generalizing"], "ans": "Training", "explain_correct": "✅ صح! ملاءمة الـ Model على البيانات هي عملية الـ Training (التدريب).", "explain_wrong": "❌ غلط! تطبيق الـ Model على البيانات يُسمى Training — مش Testing أو Evaluating."},
    {"q": "Why is it called 'training' rather than 'learning'?", "type": "mcq", "options": ["Because learning ends with abstraction", "Because the process of learning does not end with data abstraction", "Because machines cannot learn", "Because it is faster"], "ans": "Because the process of learning does not end with data abstraction", "explain_correct": "✅ صح! التعلم مش بيوقف عند الـ Abstraction — بيكمل للـ Generalization، فالعملية كلها هي اللي تعلم.", "explain_wrong": "❌ غلط! بيتسمى Training لأن التعلم الحقيقي مش بيوقف عند الـ Abstraction بس."},
    {"q": "Abstraction involves the translation of stored data into broader...", "type": "mcq", "options": ["Representations and concepts", "Noise and errors", "Hardware and software", "Zeros and ones"], "ans": "Representations and concepts", "explain_correct": "✅ صح! الـ Abstraction بتحول البيانات لـ Representations and concepts أشمل وأعمق.", "explain_wrong": "❌ غلط! الـ Abstraction بتحول البيانات لـ Representations and concepts — مش Noise أو أخطاء."},
    {"q": "When a model has been trained, data is transformed into an abstract form that...", "type": "mcq", "options": ["Deletes original info", "Summarizes original info", "Increases noise", "Creates errors"], "ans": "Summarizes original info", "explain_correct": "✅ صح! بعد التدريب، البيانات بتتحول لشكل مجرد بيلخص المعلومات الأصلية.", "explain_wrong": "❌ غلط! الشكل المجرد بيلخص المعلومات الأصلية — مش بيحذفها أو بيزيد الـ Noise."},
    {"q": "Turning abstracted knowledge into a form utilized for future action is called...", "type": "mcq", "options": ["Storage", "Training", "Generalization", "Abstraction"], "ans": "Generalization", "explain_correct": "✅ صح! تحويل المعرفة المجردة لشكل قابل للاستخدام في المستقبل هو الـ Generalization.", "explain_wrong": "❌ غلط! تطبيق المعرفة على مواقف جديدة هو الـ Generalization — مش الـ Training أو الـ Storage."},
    {"q": "Generalization operates on tasks that are similar, but not identical, to...", "type": "mcq", "options": ["Those it has seen before", "Random tasks", "Impossible tasks", "Tasks from other domains"], "ans": "Those it has seen before", "explain_correct": "✅ صح! الـ Generalization بتشتغل على مهام مشابهة لكن مش متطابقة مع اللي شافها قبل.", "explain_wrong": "❌ غلط! الـ Generalization بتتعامل مع مهام مشابهة لما شافه الـ Model في التدريب."},
    {"q": "In generalization, the learner limits discovered patterns to those most...", "type": "mcq", "options": ["Irrelevant", "Complex", "Relevant to future tasks", "Noisy"], "ans": "Relevant to future tasks", "explain_correct": "✅ صح! في الـ Generalization، المتعلم بيقصر الأنماط على اللي مهم للمهام المستقبلية.", "explain_wrong": "❌ غلط! الـ Generalization بتركز على الأنماط الـ Relevant to future tasks — مش المعقدة أو الـ Noisy."},
    {"q": "If conclusions are systematically erroneous, the algorithm has a...", "type": "mcq", "options": ["High variance", "Bias", "Perfect fit", "Good model"], "ans": "Bias", "explain_correct": "✅ صح! الاستنتاجات الخاطئة بشكل منتظم = Bias (تحيز) في الخوارزمية.", "explain_wrong": "❌ غلط! الأخطاء المنتظمة والمتوقعة = Bias — مش High Variance."},
    {"q": "Bias is considered a ________ associated with abstraction and generalization.", "type": "mcq", "options": ["Necessary evil", "Perfect feature", "Hardware issue", "Random noise"], "ans": "Necessary evil", "explain_correct": "✅ صح! الـ Bias هو Necessary evil — شر لازم، لأنه موجود في كل عملية تعميم.", "explain_wrong": "❌ غلط! الـ Bias يُعتبر Necessary evil — موجود دايماً ومش ممكن نتجنبه كلياً."},
    {"q": "Generalization uses abstracted data to create...", "type": "mcq", "options": ["Hardware errors", "Knowledge and inferences", "Raw data", "Storage memory"], "ans": "Knowledge and inferences", "explain_correct": "✅ صح! الـ Generalization بتستخدم البيانات المجردة لإنشاء Knowledge and inferences.", "explain_wrong": "❌ غلط! الـ Generalization بتنتج Knowledge and inferences — مش Raw data أو أخطاء."},
    {"q": "Which step drives action in new contexts?", "type": "mcq", "options": ["Data Storage", "Abstraction", "Generalization", "Evaluation"], "ans": "Generalization", "explain_correct": "✅ صح! الـ Generalization هي اللي بتدفع العمل في سياقات جديدة لم يشهدها الـ Model من قبل.", "explain_wrong": "❌ غلط! الـ Generalization هي المرحلة اللي بتطبق المعرفة على مواقف جديدة."},
    {"q": "Bias means the model is wrong in a ________ manner.", "type": "mcq", "options": ["Unpredictable", "Random", "Predictable", "Correct"], "ans": "Predictable", "explain_correct": "✅ صح! الـ Bias = الخطأ بطريقة Predictable (متوقعة ومنتظمة).", "explain_wrong": "❌ غلط! الـ Bias يعني إن الـ Model غلط بشكل Predictable — مش Random."},
    {"q": "A model discovering a 'face' by ignoring skin color and focusing on eyes/mouth is an example of...", "type": "mcq", "options": ["Storage", "Limiting patterns (Generalization)", "Evaluation", "Adding noise"], "ans": "Limiting patterns (Generalization)", "explain_correct": "✅ صح! ده مثال على الـ Generalization — تحديد الأنماط المهمة (عيون وفم) وتجاهل الغير مهمة (لون البشرة).", "explain_wrong": "❌ غلط! ده مثال على الـ Generalization — تقليل الأنماط للأكثر أهمية."},
    {"q": "Which step provides a feedback mechanism to measure utility?", "type": "mcq", "options": ["Abstraction", "Storage", "Evaluation", "Generalization"], "ans": "Evaluation", "explain_correct": "✅ صح! الـ Evaluation هي المرحلة اللي بتقيس مدى كفاءة الـ Model كـ feedback mechanism.", "explain_wrong": "❌ غلط! الـ Evaluation هي اللي بتوفر feedback عن أداء الـ Model — مش الـ Abstraction."},
    {"q": "Evaluation occurs after a model has been trained on an...", "type": "mcq", "options": ["Test dataset", "Initial training dataset", "Validation dataset", "Random dataset"], "ans": "Initial training dataset", "explain_correct": "✅ صح! الـ Evaluation بتحصل بعد التدريب على الـ Initial training dataset.", "explain_wrong": "❌ غلط! الـ Model بيتدرب على الـ Training dataset الأول، وبعدين يتقيّم."},
    {"q": "To judge how well a model generalizes, it is evaluated on a...", "type": "mcq", "options": ["New test dataset", "Training dataset", "Old dataset", "Corrupted dataset"], "ans": "New test dataset", "explain_correct": "✅ صح! لمعرفة مدى الـ Generalization، بنقيّم الـ Model على بيانات جديدة لم يشوفها.", "explain_wrong": "❌ غلط! لازم نقيّم الـ Model على New test dataset — مش نفس بيانات التدريب."},
    {"q": "It is exceedingly rare for a model to generalize perfectly due to...", "type": "mcq", "options": ["Good hardware", "Noise", "Low bias", "Perfect data"], "ans": "Noise", "explain_correct": "✅ صح! الـ Noise في البيانات هو السبب الرئيسي اللي بيمنع الـ Model من الـ Generalization الكامل.", "explain_wrong": "❌ غلط! الـ Noise هو اللي بيمنع الـ Perfect Generalization — مش الـ Hardware."},
    {"q": "Noisy data can be caused by...", "type": "mcq", "options": ["Measurement error", "Perfect sensors", "Clean data", "Good human subjects"], "ans": "Measurement error", "explain_correct": "✅ صح! أخطاء القياس (Measurement error) هي أحد أسباب الـ Noisy data.", "explain_wrong": "❌ غلط! الـ Noise بيجي من Measurement errors — مش من الأجهزة المثالية."},
    {"q": "Survey respondents reporting random answers is an example of...", "type": "mcq", "options": ["Perfect data", "Data quality improvement", "Noise (Issues with human subjects)", "Low variance"], "ans": "Noise (Issues with human subjects)", "explain_correct": "✅ صح! الإجابات العشوائية في الاستطلاعات = Noise ناتجة عن مشاكل مع المستجيبين البشر.", "explain_wrong": "❌ غلط! الإجابات العشوائية مثال على الـ Noise الناتجة عن Human subjects."},
    {"q": "Missing, null, or corrupted values are considered...", "type": "mcq", "options": ["Data quality problems (Noise)", "Perfect abstraction", "High bias", "Good fitting"], "ans": "Data quality problems (Noise)", "explain_correct": "✅ صح! القيم المفقودة أو التالفة = Data quality problems = نوع من الـ Noise.", "explain_wrong": "❌ غلط! القيم المفقودة والتالفة هي Data quality problems (Noise) — مش High bias."},
    {"q": "Trying to model noise is the basis of a problem called...", "type": "mcq", "options": ["Underfitting", "Overfitting", "Perfect fitting", "Evaluation"], "ans": "Overfitting", "explain_correct": "✅ صح! لما الـ Model يحاول يتعلم الـ Noise نفسه، ده بيأدي للـ Overfitting.", "explain_wrong": "❌ غلط! تعلم الـ Noise = Overfitting — الـ Model بيحفظ بدل ما يتعلم."},
    {"q": "A model with a High Training Error and High Test Error is...", "type": "mcq", "options": ["Overfitting", "Underfitting", "Just right", "Perfect"], "ans": "Underfitting", "explain_correct": "✅ صح! High Training + High Test Error = Underfitting — الـ Model مش قادر يتعلم.", "explain_wrong": "❌ غلط! High error في الاتنين = Underfitting — الـ Model بسيط جداً."},
    {"q": "A model with a Low Training Error but High Test Error is...", "type": "mcq", "options": ["Overfitting", "Underfitting", "Just right", "Biased"], "ans": "Overfitting", "explain_correct": "✅ صح! Low Training + High Test = Overfitting — حفظ البيانات بدل التعلم.", "explain_wrong": "❌ غلط! Low training error وHigh test error = Overfitting — الـ Model حافظ مش فاهم."},
    {"q": "The formula E[(θ_bar - θ)^2] represents...", "type": "mcq", "options": ["Variance", "Bias", "Noise", "Accuracy"], "ans": "Bias", "explain_correct": "✅ صح! E[(θ_bar - θ)^2] هي معادلة الـ Bias — الفرق بين متوسط التنبؤات والقيمة الحقيقية.", "explain_wrong": "❌ غلط! E[(θ_bar - θ)^2] = Bias — بتقيس مدى دقة الـ Model بشكل عام."},
    {"q": "The formula E[(θ_hat - θ_bar)^2] represents...", "type": "mcq", "options": ["Variance", "Bias", "Noise", "Accuracy"], "ans": "Variance", "explain_correct": "✅ صح! E[(θ_hat - θ_bar)^2] هي معادلة الـ Variance — تشتت التنبؤات حول متوسطها.", "explain_wrong": "❌ غلط! E[(θ_hat - θ_bar)^2] = Variance — بتقيس مدى تشتت التنبؤات."},
    {"q": "Bias measures the ________ of the model.", "type": "mcq", "options": ["Precision", "Speed", "Accuracy or quality", "Size"], "ans": "Accuracy or quality", "explain_correct": "✅ صح! الـ Bias بيقيس الـ Accuracy or quality — مدى صحة الـ Model بشكل عام.", "explain_wrong": "❌ غلط! الـ Bias بيقيس الـ Accuracy — مش السرعة أو الـ Precision."},
    {"q": "Variance measures the ________ of the model.", "type": "mcq", "options": ["Accuracy", "Precision or specificity", "Speed", "Memory"], "ans": "Precision or specificity", "explain_correct": "✅ صح! الـ Variance بيقيس الـ Precision — مدى تقارب التنبؤات من بعضها.", "explain_wrong": "❌ غلط! الـ Variance بيقيس الـ Precision أو الـ Specificity — مش الـ Accuracy."},
    {"q": "Low variance implies the model does not change much as the...", "type": "mcq", "options": ["Training set varies", "Hardware varies", "Test set is deleted", "Noise increases"], "ans": "Training set varies", "explain_correct": "✅ صح! Low Variance = الـ Model مش بيتغير كتير لو غيرنا الـ Training set.", "explain_wrong": "❌ غلط! Low Variance يعني الـ Model ثابت نسبياً مع تغيير الـ Training set."},
    {"q": "Models with too few parameters are inaccurate because of...", "type": "mcq", "options": ["Large variance", "Large bias (not enough flexibility)", "Low bias", "Too much flexibility"], "ans": "Large bias (not enough flexibility)", "explain_correct": "✅ صح! الـ Model البسيط جداً (parameters قليلة) = Large Bias لأنه مش مرن كفاية.", "explain_wrong": "❌ غلط! Parameters قليلة = Large Bias — الـ Model مش عنده مرونة كافية للتعلم."},
    {"q": "Models with too many parameters are inaccurate because of...", "type": "mcq", "options": ["Large variance (too sensitive to randomness)", "Large bias", "Low variance", "Not enough flexibility"], "ans": "Large variance (too sensitive to randomness)", "explain_correct": "✅ صح! Parameters كتير = Large Variance — الـ Model حساس جداً للـ randomness والـ noise.", "explain_wrong": "❌ غلط! Parameters كتير = Large Variance — الـ Model بيتأثر بكل noise في البيانات."},
    {"q": "Low Bias and High Variance leads to...", "type": "mcq", "options": ["Underfitting", "Overfitting", "Just right fitting", "No fitting"], "ans": "Overfitting", "explain_correct": "✅ صح! Low Bias + High Variance = Overfitting — الـ Model دقيق على التدريب بس مش بيعمّم.", "explain_wrong": "❌ غلط! Low Bias وHigh Variance = Overfitting — حفظ التفاصيل بدل التعميم."},
    {"q": "High Bias and Low Variance leads to...", "type": "mcq", "options": ["Overfitting", "Underfitting", "Just right fitting", "Perfect fitting"], "ans": "Underfitting", "explain_correct": "✅ صح! High Bias + Low Variance = Underfitting — الـ Model بسيط جداً ومش قادر يتعلم.", "explain_wrong": "❌ غلط! High Bias وLow Variance = Underfitting — الـ Model مش معقد كفاية."},
    {"q": "A model with Low Bias and Low Variance is considered...", "type": "mcq", "options": ["Underfitting", "Overfitting", "Just right (Good Fit)", "A failure"], "ans": "Just right (Good Fit)", "explain_correct": "✅ صح! Low Bias + Low Variance = الـ Model المثالي (Good Fit).", "explain_wrong": "❌ غلط! Low Bias وLow Variance هو الهدف — الـ Good Fit المثالي."},
    {"q": "To fix Underfitting, one remedy is to...", "type": "mcq", "options": ["Complexify model", "Get more data", "Regularize", "Try a smaller set of features"], "ans": "Complexify model", "explain_correct": "✅ صح! لحل الـ Underfitting، نزيد تعقيد الـ Model (Complexify) عشان يقدر يتعلم أكثر.", "explain_wrong": "❌ غلط! لحل الـ Underfitting، لازم نزيد تعقيد الـ Model — مش نعمل Regularization."},
    {"q": "Which of the following fixes Overfitting?", "type": "mcq", "options": ["Train longer", "Add more features", "Get more data (training examples)", "Complexify model"], "ans": "Get more data (training examples)", "explain_correct": "✅ صح! زيادة البيانات بتساعد الـ Model يتعلم بشكل أفضل ويتجنب الـ Overfitting.", "explain_wrong": "❌ غلط! لحل الـ Overfitting، بنزيد البيانات — مش نزيد الـ features أو نعقّد الـ Model."},
    {"q": "If your model has High Bias, you should try to...", "type": "mcq", "options": ["Add more features", "Select fewer features", "Get more data", "Regularize"], "ans": "Add more features", "explain_correct": "✅ صح! High Bias = الـ Model بسيط جداً، الحل هو إضافة features أكثر.", "explain_wrong": "❌ غلط! High Bias بنحله بإضافة features — مش بتقليلها أو الـ Regularization."},
    {"q": "If your model has High Variance, you should try to...", "type": "mcq", "options": ["Train longer", "Add more features", "Regularize", "Make the model more complex"], "ans": "Regularize", "explain_correct": "✅ صح! High Variance بنحله بالـ Regularization اللي بتقلل تعقيد الـ Model.", "explain_wrong": "❌ غلط! High Variance بنحله بالـ Regularization — مش بزيادة الـ features أو التعقيد."},
    {"q": "Trying a smaller set of features is a remedy for...", "type": "mcq", "options": ["Underfitting", "Overfitting (High Variance)", "Low Bias", "Good Fitting"], "ans": "Overfitting (High Variance)", "explain_correct": "✅ صح! تقليل الـ features بيساعد في حل الـ Overfitting (High Variance).", "explain_wrong": "❌ غلط! تقليل الـ features = علاج الـ Overfitting (High Variance) — مش الـ Underfitting."},
    {"q": "Training the model longer is a suggested fix for...", "type": "mcq", "options": ["Overfitting", "Underfitting (High Bias)", "High Variance", "Perfect Fit"], "ans": "Underfitting (High Bias)", "explain_correct": "✅ صح! التدريب لفترة أطول بيساعد الـ Model يتعلم أكثر ويحل الـ Underfitting.", "explain_wrong": "❌ غلط! التدريب الأطول علاج للـ Underfitting (High Bias) — مش الـ Overfitting."},
    {"q": "When Model Complexity is LOW, the result is...", "type": "mcq", "options": ["Overfitting", "Underfitting", "Perfect Fit", "High Variance"], "ans": "Underfitting", "explain_correct": "✅ صح! تعقيد منخفض = Underfitting — الـ Model بسيط جداً ومش قادر يتعلم.", "explain_wrong": "❌ غلط! Low Complexity = Underfitting — الـ Model مش عنده complexity كافية."},
    {"q": "When Model Complexity is HIGH, the result is...", "type": "mcq", "options": ["Overfitting", "Underfitting", "Perfect Fit", "High Bias"], "ans": "Overfitting", "explain_correct": "✅ صح! تعقيد عالي = Overfitting — الـ Model معقد جداً وبيحفظ بدل ما يتعلم.", "explain_wrong": "❌ غلط! High Complexity = Overfitting — الـ Model بيحفظ حتى الـ Noise."},
]

ML_LEC2 = [
    {"q": "What does KNN stand for?", "type": "mcq", "options": ["K-Nearest Neighbors", "K-Neural Network", "K-Norm Node", "K-Net Numeric"], "ans": "K-Nearest Neighbors", "explain_correct": "✅ صح! KNN = K-Nearest Neighbors، خوارزمية بتصنّف النقطة الجديدة بناءً على أقرب K جيران.", "explain_wrong": "❌ غلط! KNN اختصار K-Nearest Neighbors فقط — مش Neural Network."},
    {"q": "KNN is classified as a ________ learning algorithm.", "type": "mcq", "options": ["Supervised", "Unsupervised", "Reinforcement", "Semi-supervised"], "ans": "Supervised", "explain_correct": "✅ صح! KNN خوارزمية Supervised لأنها بتتدرب على بيانات معندها labels.", "explain_wrong": "❌ غلط! KNN بتحتاج labels عشان تشتغل، يعني Supervised مش Unsupervised."},
    {"q": "KNN is called a 'lazy learner' because...", "type": "mcq", "options": ["It memorizes training data and delays computation to prediction time", "It trains very slowly on large datasets", "It uses a very simple mathematical model", "It ignores most of the training data"], "ans": "It memorizes training data and delays computation to prediction time", "explain_correct": "✅ صح! KNN 'كسول' لأنه مش بيبني model أثناء التدريب، بيحفظ البيانات وبيحسب وقت التنبؤ.", "explain_wrong": "❌ غلط! الـ Lazy مش معناها بطيء — معناها بيؤجل الحساب لوقت التنبؤ."},
    {"q": "k-NN algorithm does more computation on test time rather than train time.", "type": "tf", "options": ["True", "False"], "ans": "True", "explain_correct": "✅ صح! KNN مش بيتعلم وقت التدريب، كل الحساب بيحصل وقت الاختبار.", "explain_wrong": "❌ غلط! KNN بالفعل بيعمل معظم الحساب وقت الـ testing — وده اللي بيخليه lazy learner."},
    {"q": "Which is a STRENGTH of the KNN algorithm?", "type": "mcq", "options": ["Simple and effective with no assumptions about data distribution", "Fast classification phase", "Handles missing data automatically", "Produces an interpretable model"], "ans": "Simple and effective with no assumptions about data distribution", "explain_correct": "✅ صح! KNN بسيط وفعّال، ومش بيفترض أي شكل معين للبيانات.", "explain_wrong": "❌ غلط! KNN معروف بإن الـ classification phase بطيئة، ومش بيعمل model قابل للتفسير."},
    {"q": "Which is a WEAKNESS of the KNN algorithm?", "type": "mcq", "options": ["Slow classification phase", "Requires large training time", "Makes strong assumptions about data", "Cannot handle numeric features"], "ans": "Slow classification phase", "explain_correct": "✅ صح! KNN بطيء وقت التصنيف لأنه بيحسب المسافة لكل نقطة لكل تنبؤ جديد.", "explain_wrong": "❌ غلط! الـ training في KNN سريعة جداً، لكن الـ classification هي اللي بطيئة."},
    {"q": "KNN does NOT produce a model, which limits our ability to...", "type": "mcq", "options": ["Understand how features are related to the class", "Classify new data points", "Use Euclidean distance", "Normalize the data"], "ans": "Understand how features are related to the class", "explain_correct": "✅ صح! لأن KNN مش بيبني model، مش قادرين نفهم إزاي كل feature بتأثر على التصنيف.", "explain_wrong": "❌ غلط! KNN بيقدر يصنف بيانات جديدة، بس مش بيديك تفسير لعلاقة الـ features بالنتيجة."},
    {"q": "In KNN, the unlabeled test instance is assigned the class of...", "type": "mcq", "options": ["The majority of the k nearest neighbors", "The single closest neighbor only", "The farthest neighbor", "A randomly selected neighbor"], "ans": "The majority of the k nearest neighbors", "explain_correct": "✅ صح! KNN بيشوف الـ K جيران الأقرب، وبيختار الفئة اللي عندها أكبر عدد (majority vote).", "explain_wrong": "❌ غلط! KNN مش بيعتمد على جار واحد بس — بيعتمد على أغلبية الـ K جيران."},
    {"q": "What is the Euclidean distance formula used in KNN?", "type": "mcq", "options": ["dist(p,q) = sqrt((p1-q1)² + (p2-q2)² + ... + (pn-qn)²)", "dist(p,q) = |p1-q1| + |p2-q2|", "dist(p,q) = (p1-q1)² + (p2-q2)²", "dist(p,q) = (p1+q1) / (p2+q2)"], "ans": "dist(p,q) = sqrt((p1-q1)² + (p2-q2)² + ... + (pn-qn)²)", "explain_correct": "✅ صح! دي معادلة Euclidean Distance الصح — جذر مجموع مربعات الفروق.", "explain_wrong": "❌ غلط! الصح هو الجذر التربيعي لمجموع المربعات، مش مجموع القيم المطلقة."},
    {"q": "What is the Euclidean distance between points A(0,1) and B(2,3)?", "type": "mcq", "options": ["√8 ≈ 2.83", "1", "2", "4"], "ans": "√8 ≈ 2.83", "explain_correct": "✅ صح! dist = sqrt((2-0)² + (3-1)²) = sqrt(4+4) = sqrt(8) ≈ 2.83 ✓", "explain_wrong": "❌ غلط! الحساب الصح: sqrt((2-0)² + (3-1)²) = sqrt(8) ≈ 2.83"},
    {"q": "Which property of distance metrics states d(x,y) = d(y,x)?", "type": "mcq", "options": ["Symmetry", "Non-negativity", "Identity", "Triangle inequality"], "ans": "Symmetry", "explain_correct": "✅ صح! Symmetry = المسافة من x لـ y = المسافة من y لـ x.", "explain_wrong": "❌ غلط! الخاصية دي اسمها Symmetry — المسافة متساوية في الاتجاهين."},
    {"q": "Which axiom of distance metrics states that d(x,x) = 0?", "type": "mcq", "options": ["Identity of indiscernibles", "Non-negativity", "Symmetry", "Triangle inequality"], "ans": "Identity of indiscernibles", "explain_correct": "✅ صح! d(x,x) = 0 = المسافة من نقطة لنفسها = صفر — أكسيوم Identity.", "explain_wrong": "❌ غلط! d(x,x)=0 بيعبر عن Identity."},
    {"q": "The triangle inequality in distance metrics states...", "type": "mcq", "options": ["d(x,y) + d(y,z) ≥ d(x,z)", "d(x,y) = d(y,x)", "d(x,x) = 0", "d(x,y) ≥ 0"], "ans": "d(x,y) + d(y,z) ≥ d(x,z)", "explain_correct": "✅ صح! Triangle inequality: أي ضلع ≤ مجموع الضلعين الآخرين.", "explain_wrong": "❌ غلط! Triangle inequality هي d(x,y) + d(y,z) ≥ d(x,z)."},
    {"q": "What does the axiom d(x,y) ≥ 0 represent?", "type": "mcq", "options": ["Non-negativity", "Symmetry", "Identity", "Triangle inequality"], "ans": "Non-negativity", "explain_correct": "✅ صح! Non-negativity = المسافة دايماً ≥ صفر.", "explain_wrong": "❌ غلط! d(x,y) ≥ 0 = Non-negativity — المسافة دايماً موجبة أو صفر."},
    {"q": "Why do we normalize data before applying KNN?", "type": "mcq", "options": ["To prevent features with large ranges from dominating the distance", "To speed up the training process", "To remove noise from the dataset", "To increase the number of features"], "ans": "To prevent features with large ranges from dominating the distance", "explain_correct": "✅ صح! بدون Normalization، الـ Salary هتطغى على الـ Age في حساب المسافة.", "explain_wrong": "❌ غلط! Normalization مش للسرعة — هي عشان الـ features تبقى متساوية في التأثير."},
    {"q": "The normalization formula used in KNN is...", "type": "mcq", "options": ["x = (x - MIN) / (MAX - MIN)", "x = (x - MEAN) / STD", "x = x / MAX", "x = x - MIN"], "ans": "x = (x - MIN) / (MAX - MIN)", "explain_correct": "✅ صح! دي صيغة Min-Max Normalization — بتحول القيم لنطاق [0,1].", "explain_wrong": "❌ غلط! الصيغة الصح هي Min-Max: (x - MIN)/(MAX - MIN)."},
    {"q": "Min-Max Normalization scales data to the range...", "type": "mcq", "options": ["[0, 1]", "[-1, 1]", "[0, 100]", "[-∞, +∞]"], "ans": "[0, 1]", "explain_correct": "✅ صح! Min-Max بتحول كل القيم لتكون بين 0 و1.", "explain_wrong": "❌ غلط! Min-Max بتعطي [0,1] — مش [-1,1]."},
    {"q": "Given values: 7, 4, 25, -5, 10 (MIN=-5, MAX=25). Normalized value of 7 = ?", "type": "mcq", "options": ["0.4", "0.3", "0.5", "0.6"], "ans": "0.4", "explain_correct": "✅ صح! (7-(-5)) / (25-(-5)) = 12/30 = 0.4 ✓", "explain_wrong": "❌ غلط! الحساب: (7-(-5)) / (25-(-5)) = 12/30 = 0.4"},
    {"q": "Given values: 7, 4, 25, -5, 10 (MIN=-5, MAX=25). Normalized value of 4 = ?", "type": "mcq", "options": ["0.3", "0.4", "0.5", "0.1"], "ans": "0.3", "explain_correct": "✅ صح! (4-(-5)) / (25-(-5)) = 9/30 = 0.3 ✓", "explain_wrong": "❌ غلط! الحساب: (4-(-5)) / (25-(-5)) = 9/30 = 0.3"},
    {"q": "Given values: 7, 4, 25, -5, 10 (MIN=-5, MAX=25). Normalized value of -5 = ?", "type": "mcq", "options": ["0", "0.1", "-1", "0.5"], "ans": "0", "explain_correct": "✅ صح! (-5-(-5))/(25-(-5)) = 0/30 = 0. القيمة الدنيا دايماً = 0.", "explain_wrong": "❌ غلط! (-5-(-5))/(25-(-5)) = 0. القيمة الدنيا دايماً = 0 بعد الـ normalization."},
    {"q": "Given values: 7, 4, 25, -5, 10 (MIN=-5, MAX=25). Normalized value of 25 = ?", "type": "mcq", "options": ["1", "0.9", "0.8", "25"], "ans": "1", "explain_correct": "✅ صح! (25-(-5))/(25-(-5)) = 30/30 = 1. القيمة العليا دايماً = 1.", "explain_wrong": "❌ غلط! (25-(-5))/(25-(-5)) = 1. القيمة العليا دايماً = 1 بعد الـ normalization."},
    {"q": "k-NN performs much better if all of the data have the same scale.", "type": "tf", "options": ["True", "False"], "ans": "True", "explain_correct": "✅ صح! نفس الـ scale = حساب مسافة عادل لكل الـ features.", "explain_wrong": "❌ غلط! ده صح — KNN أحسن بكتير مع البيانات على نفس الـ scale."},
    {"q": "What are the correct steps of the KNN algorithm in order?", "type": "mcq", "options": ["Select K → Calculate distances → Take K nearest → Count per class → Assign majority", "Calculate distances → Select K → Assign class → Count neighbors", "Train model → Select K → Calculate distances → Predict", "Normalize → Train → Test → Select K"], "ans": "Select K → Calculate distances → Take K nearest → Count per class → Assign majority", "explain_correct": "✅ صح! الخطوات: اختار K → احسب المسافات → خذ K الأقرب → عد النقاط → اختار الأغلبية.", "explain_wrong": "❌ غلط! الترتيب الصح: اختيار K أولاً ← حساب المسافات ← K الأقرب ← العد ← التصنيف."},
    {"q": "In case of a very large value of K, we may...", "type": "mcq", "options": ["Include points from other classes into the neighborhood", "Get more accurate results always", "Reduce computation time significantly", "Eliminate the need for normalization"], "ans": "Include points from other classes into the neighborhood", "explain_correct": "✅ صح! K كبير جداً بيوسّع دائرة الجيران لدرجة إنها تشمل نقاط من فئات تانية.", "explain_wrong": "❌ غلط! K كبير بيجيب جيران بعيدين من فئات مختلفة وبيخرب التصنيف."},
    {"q": "In case of a very small value of K (like K=1), the algorithm is...", "type": "mcq", "options": ["Very sensitive to noise", "More accurate always", "Faster in prediction", "Better at handling outliers"], "ans": "Very sensitive to noise", "explain_correct": "✅ صح! K=1 بيعتمد على جار واحد بس، لو كان noise هيأثر على النتيجة كلها.", "explain_wrong": "❌ غلط! K صغير بيخلي الخوارزمية حساسة جداً للـ noise."},
    {"q": "The main benefit of using k neighbors instead of just 1 neighbor is...", "type": "mcq", "options": ["Voting overcomes noise", "Faster computation", "No need for distance calculation", "Better handling of missing data"], "ans": "Voting overcomes noise", "explain_correct": "✅ صح! الـ voting بين K جيران بيتغلب على الـ noise في البيانات.", "explain_wrong": "❌ غلط! الفايدة الأساسية من K جيران هي إن الـ voting بيقلل تأثير الـ noise."},
    {"q": "As K increases beyond the optimal point, the error rate...", "type": "mcq", "options": ["Increases", "Decreases", "Stays the same", "Reaches zero"], "ans": "Increases", "explain_correct": "✅ صح! بعد النقطة المثلى، زيادة K بيزيد الـ error لأنه بيدخل فئات تانية.", "explain_wrong": "❌ غلط! في نقطة مثلى وبعدها يزيد الخطأ مع زيادة K."},
    {"q": "Which value of K is generally preferred to avoid tie voting?", "type": "mcq", "options": ["Odd K", "Even K", "K=1 always", "K=100 for stability"], "ans": "Odd K", "explain_correct": "✅ صح! K الفردي بيتجنب الـ tie voting لما يكون عندك فئتين متساويتين.", "explain_wrong": "❌ غلط! K الزوجي ممكن يسبب Tie Voting — فضل K الفردي."},
    {"q": "What problem occurs with an even value of K in binary classification?", "type": "mcq", "options": ["Tie voting", "Overfitting", "Underfitting", "Slow training"], "ans": "Tie voting", "explain_correct": "✅ صح! لو K زوجي، ممكن يطلع تعادل بين الفئتين ومش هيقدر يقرر.", "explain_wrong": "❌ غلط! المشكلة مع K الزوجي هي Tie Voting مش Overfitting."},
    {"q": "When you increase K in KNN, the bias...", "type": "mcq", "options": ["Increases", "Decreases", "Stays the same", "Becomes zero"], "ans": "Increases", "explain_correct": "✅ صح! زيادة K بيعمل smoothing أكثر وبيزيد الـ bias (underfitting).", "explain_wrong": "❌ غلط! زيادة K = زيادة bias لأن الـ model بيبقى أكثر generalization."},
    {"q": "Class-label noise in KNN means...", "type": "mcq", "options": ["The class label provided for an example is incorrect", "The feature values are missing", "The distance calculation is wrong", "The K value is too large"], "ans": "The class label provided for an example is incorrect", "explain_correct": "✅ صح! Class-label noise = الـ label المعطى للمثال غلط (مثلاً: pos بدل neg).", "explain_wrong": "❌ غلط! Class-label noise = الـ label غلط مش قيمة الـ feature."},
    {"q": "Attribute noise in KNN causes...", "type": "mcq", "options": ["The nearest neighbor may not be really the nearest one", "The class label to be wrong", "K to be selected incorrectly", "Normalization to fail"], "ans": "The nearest neighbor may not be really the nearest one", "explain_correct": "✅ صح! لو قيمة الـ attribute غلطة، حساب المسافة هيبقى غلط وهيختار neighbors مش الأقرب.", "explain_wrong": "❌ غلط! Attribute noise بتأثر على حساب المسافة — فالـ nearest neighbor مش فعلاً الأقرب."},
    {"q": "Irrelevant attributes in KNN are a problem because...", "type": "mcq", "options": ["They affect distances but not the class, causing wrong neighbors", "They slow down the algorithm significantly", "They cause K to be selected incorrectly", "They prevent Min-Max normalization"], "ans": "They affect distances but not the class, causing wrong neighbors", "explain_correct": "✅ صح! الـ attributes الغير مهمة بتأثر على المسافة رغم إنها مش مهمة للتصنيف.", "explain_wrong": "❌ غلط! مشكلة الـ irrelevant attributes = بتأثر على المسافة رغم إنها مش مهمة."},
    {"q": "The scaling problem in KNN occurs when...", "type": "mcq", "options": ["One attribute with large range overwhelms others in distance calculation", "The dataset is too large to process", "K is set to a very high value", "The model overfits the training data"], "ans": "One attribute with large range overwhelms others in distance calculation", "explain_correct": "✅ صح! x2 ∈ [0,100] هتسيطر على حساب المسافة وتخلي x1 ∈ [0,1] بلا تأثير.", "explain_wrong": "❌ غلط! Scaling problem = feature بـ range كبيرة بتطغى على باقي الـ features."},
    {"q": "k-NN works well with a small number of input variables but struggles when inputs are very large.", "type": "tf", "options": ["True", "False"], "ans": "True", "explain_correct": "✅ صح! مع زيادة الـ features (curse of dimensionality)، حساب المسافة بيبقى أقل دقة.", "explain_wrong": "❌ غلط! ده صح — KNN بيعاني مع الـ features الكتيرة."},
    {"q": "KNN makes no assumptions about the functional form of the problem being solved.", "type": "tf", "options": ["True", "False"], "ans": "True", "explain_correct": "✅ صح! KNN non-parametric — مش بيفترض أي شكل معين للبيانات.", "explain_wrong": "❌ غلط! KNN فعلاً مش بيفترض أي شكل للبيانات، وده ميزة قوية."},
    {"q": "Which of the following statements about KNN is TRUE?", "type": "mcq", "options": ["All three: same scale + small inputs + no assumptions", "KNN performs better with same-scale data only", "KNN works well with large number of inputs", "KNN makes strong assumptions about data"], "ans": "All three: same scale + small inputs + no assumptions", "explain_correct": "✅ صح! الثلاث statements صحيحة — نفس الـ scale + inputs صغيرة + no assumptions.", "explain_wrong": "❌ غلط! الإجابة all of above — الثلاث statements من السلايد صحيحة."},
    {"q": "In Weighted k-NN, why do closer neighbors get higher weights?", "type": "mcq", "options": ["Because they are more similar and more relevant", "Because they are faster to compute", "Because distant neighbors are always noise", "Because K=1 is always best"], "ans": "Because they are more similar and more relevant", "explain_correct": "✅ صح! الجيران الأقرب أكثر شبهاً، فمنطقي يكون ليهم تأثير أكبر.", "explain_wrong": "❌ غلط! الأقرب بياخد وزن أعلى لأنه أكثر شبهاً — مش بسبب السرعة."},
    {"q": "In Weighted k-NN, if all distances are equal (dk = d1), the weight wi = ...", "type": "mcq", "options": ["1", "0", "0.5", "Undefined"], "ans": "1", "explain_correct": "✅ صح! من السلايد: لو dk = d1، يبقى wi = 1 (لتجنب القسمة على صفر).", "explain_wrong": "❌ غلط! لما dk = d1، wi = 1 كـ special case."},
    {"q": "In the Weighted 5-NN example (d1=1, d2=3, d3=4, d4=5, d5=8), what is w1?", "type": "mcq", "options": ["1", "5/7", "4/7", "0"], "ans": "1", "explain_correct": "✅ صح! w1 = (8-1)/(8-1) = 7/7 = 1. الجار الأقرب دايماً بياخد وزن = 1.", "explain_wrong": "❌ غلط! w1 = (8-1)/(8-1) = 1."},
    {"q": "In the Weighted 5-NN example (d1=1, d2=3, d3=4, d4=5, d5=8), what is w5?", "type": "mcq", "options": ["0", "1", "3/7", "5/7"], "ans": "0", "explain_correct": "✅ صح! w5 = (8-8)/(8-1) = 0/7 = 0. الجار الأبعد دايماً بياخد وزن = 0.", "explain_wrong": "❌ غلط! w5 = (8-8)/(8-1) = 0."},
    {"q": "In Weighted k-NN, if Σ(POS weights) > Σ(NEG weights), the example is classified as...", "type": "mcq", "options": ["Positive", "Negative", "Neutral", "Undecided"], "ans": "Positive", "explain_correct": "✅ صح! من السلايد: لو ΣPOS > ΣNEG → الفئة = Positive.", "explain_wrong": "❌ غلط! القاعدة: لو ΣPOS > ΣNEG → Positive."},
    {"q": "In the Weighted 5-NN example, 2 nearest positive + 3 far negative, x is classified as...", "type": "mcq", "options": ["Positive (Σ+ = 12/7 > Σ- = 7/7)", "Negative (majority = 3 neg)", "Cannot be determined", "Depends on K"], "ans": "Positive (Σ+ = 12/7 > Σ- = 7/7)", "explain_correct": "✅ صح! Σ+ = 1 + 5/7 = 12/7، Σ- = 4/7 + 3/7 + 0 = 1. إذن Σ+ > Σ- → Positive!", "explain_wrong": "❌ غلط! رغم إن الأغلبية negative، الـ weighted voting بيعطي الـ positive نتيجة."},
    {"q": "A Tomek Link is defined as a pair [x,y] where...", "type": "mcq", "options": ["x is NN of y, y is NN of x, and they have DIFFERENT classes", "x and y are in the same class and far apart", "x and y have same distance to all points", "x is a statistical outlier"], "ans": "x is NN of y, y is NN of x, and they have DIFFERENT classes", "explain_correct": "✅ صح! Tomek Link = نقطتان كل منهما أقرب جار للأخرى، من فئتين مختلفتين.", "explain_wrong": "❌ غلط! Tomek Link يشترط: كل نقطة أقرب جار للتانية وهما من فئتين مختلفتين."},
    {"q": "Removing Tomek Links from training data helps to...", "type": "mcq", "options": ["Clean borderline and noisy examples near class boundaries", "Increase the size of training data", "Select optimal K automatically", "Speed up distance calculation"], "ans": "Clean borderline and noisy examples near class boundaries", "explain_correct": "✅ صح! حذف الـ Tomek Links بيزيل النقاط الحدودية والـ noise عند حدود الفئات.", "explain_wrong": "❌ غلط! حذف الـ Tomek Links بيزيل الـ borderline examples — مش بيزيد البيانات."},
    {"q": "In the algorithm for removing redundant examples, iterations stop when...", "type": "mcq", "options": ["The contents of set S do not change between iterations", "S contains all training examples", "Error rate reaches zero", "K reaches optimal value"], "ans": "The contents of set S do not change between iterations", "explain_correct": "✅ صح! الخوارزمية بتوقف لما محتوى S ما اتغيرش — وصلنا للحد الأدنى الكافي.", "explain_wrong": "❌ غلط! الخوارزمية بتوقف لما S ما يتغيرش — مش لما error = 0."},
    {"q": "In the Social Network Ads dataset, the independent variables used for KNN are...", "type": "mcq", "options": ["Age and EstimatedSalary", "Age and Purchased", "UserID and Gender", "Gender and Purchased"], "ans": "Age and EstimatedSalary", "explain_correct": "✅ صح! Age وEstimatedSalary هم الـ features للتنبؤ بـ Purchased.", "explain_wrong": "❌ غلط! Purchased هي الـ Target مش feature. الـ features هي Age وEstimatedSalary."},
    {"q": "A company built a KNN model with 100% training accuracy but very poor test accuracy. This is...", "type": "mcq", "options": ["An overfitted model", "An underfitted model", "A perfectly trained model", "A problem with test data"], "ans": "An overfitted model", "explain_correct": "✅ صح! 100% training + ضعيف testing = Overfitting. المودل حفظ بدل ما يتعلم.", "explain_wrong": "❌ غلط! ده Overfitting مش Underfitting. الـ underfitting training error بيكون عالي."},
    {"q": "Nearest neighbor classifiers struggle when...", "type": "mcq", "options": ["Data is noisy and no clear distinction exists among groups", "The dataset has too many examples", "All features are normalized", "K is set to an odd number"], "ans": "Data is noisy and no clear distinction exists among groups", "explain_correct": "✅ صح! لو البيانات noisy ومفيش فرق واضح بين الفئات، KNN بيصعب عليه تحديد الحدود.", "explain_wrong": "❌ غلط! KNN بيصعب عليه لما البيانات noisy — مش لما البيانات كبيرة."},
]

# ════════════════════════════════════════════════════════════
# ⚙️ الإعدادات
# ════════════════════════════════════════════════════════════

SUBJECTS = [
    {
        "icon": "🤖", "name": "Machine Learning", "code": "AIE121",
        "desc": "Intro, KNN, Decision Trees...", "key": "ml",
        "lectures": [
            {"num": "01", "title": "Intro to ML",    "count": "50 سؤال", "key": "ml_lec1", "available": True},
            {"num": "02", "title": "KNN Algorithm",  "count": "50 سؤال", "key": "ml_lec2", "available": True},
            # {"num": "03", "title": "Decision Trees", "count": "50 سؤال", "key": "ml_lec3", "available": False},
        ]
    },
]

QUESTIONS_DB = {
    "ml_lec1": ML_LEC1,
    "ml_lec2": ML_LEC2,
}

# ════════════════════════════════════════════════════════════
# 🔧 Session State
# ════════════════════════════════════════════════════════════

for k, v in [("sel_subj", None), ("sel_lec", None), ("answers", {})]:
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
                for j, opt in enumerate(q["options"]):
                    with opt_cols[j % 2]:
                        if st.button(opt, key=f"q{i}_o{j}", use_container_width=True):
                            st.session_state.answers[i] = opt
                            st.rerun()

            st.markdown("<div style='margin-bottom:12px'></div>", unsafe_allow_html=True)
