# ════════════════════════════════════════════════════════════
# 📖 ml_lec2.py
# Machine Learning - Lecture 2: K-Nearest Neighbors (k-NN)
# Dr. Sara Sweidan
# 35 MCQ + 15 True/False = 50 Questions
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # ✅ MCQ Questions (1–35)
    # ══════════════════════════════════════════════

    {
        "q": "What does k-NN stand for?",
        "type": "mcq",
        "options": [
            "Key-Node Network",
            "k-Nearest Neighbors",
            "k-Null Nodes",
            "Key-Nearest Nodes"
        ],
        "ans": "k-Nearest Neighbors",
        "explain_correct": "✅ صح! k-NN اختصار لـ k-Nearest Neighbors.",
        "explain_wrong": "❌ غلط! الاختصار الصحيح هو k-Nearest Neighbors."
    },
    {
        "q": "Why is k-NN considered a 'lazy learner'?",
        "type": "mcq",
        "options": [
            "It uses a simple algorithm",
            "It does not build a model during training, deferring computation to test time",
            "It is slow at everything",
            "It ignores irrelevant features"
        ],
        "ans": "It does not build a model during training, deferring computation to test time",
        "explain_correct": "✅ صح! الـ Lazy learner مش بيبني model وقت التدريب وبيأجل الحسابات لوقت الاختبار.",
        "explain_wrong": "❌ غلط! السبب إنه مش بيبني model وقت الـ training."
    },
    {
        "q": "In k-NN classification, how is the class of a new data point determined?",
        "type": "mcq",
        "options": [
            "By the class of the single nearest neighbor",
            "By the majority class among the k nearest neighbors",
            "By the average distance of all training points",
            "By a learned decision boundary"
        ],
        "ans": "By the majority class among the k nearest neighbors",
        "explain_correct": "✅ صح! الكلاس بيتحدد بتصويت الأغلبية (Majority class) لأقرب k جيران.",
        "explain_wrong": "❌ غلط! الكلاس بيتحدد بأغلبية أقرب k جيران."
    },
    {
        "q": "What is the Euclidean distance between A(0,1) and B(2,3)?",
        "type": "mcq",
        "options": [
            "1",
            "2√2",
            "4",
            "8"
        ],
        "ans": "2√2",
        "explain_correct": "✅ صح! بحساب قانون المسافة الإقليدية: جذر((2-0)^2 + (3-1)^2) = 2√2.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 2√2."
    },
    {
        "q": "Which formula is used for min-max normalization?",
        "type": "mcq",
        "options": [
            "x = (x + MIN) / MAX",
            "x = (x - MIN) / (MAX - MIN)",
            "x = x / MAX",
            "x = (x - MAX) / MIN"
        ],
        "ans": "x = (x - MIN) / (MAX - MIN)",
        "explain_correct": "✅ صح! ده قانون الـ min-max normalization لتحويل الداتا.",
        "explain_wrong": "❌ غلط! القانون هو: (x - MIN) / (MAX - MIN)."
    },
    {
        "q": "What happens when k is very large in k-NN?",
        "type": "mcq",
        "options": [
            "The model underfits and may include points from other classes",
            "The model becomes more accurate",
            "The algorithm runs faster",
            "Noise has more effect"
        ],
        "ans": "The model underfits and may include points from other classes",
        "explain_correct": "✅ صح! الـ k الكبيرة بتعمل underfitting وبتدخل كلاسات تانية في الحساب.",
        "explain_wrong": "❌ غلط! الـ k الكبيرة بتؤدي للـ underfitting."
    },
    {
        "q": "What happens when k is very small (e.g., k=1)?",
        "type": "mcq",
        "options": [
            "The model underfits",
            "The algorithm is very sensitive to noise",
            "The model generalizes well",
            "Training time increases"
        ],
        "ans": "The algorithm is very sensitive to noise",
        "explain_correct": "✅ صح! الـ k الصغيرة بتخلي الخوارزمية حساسة جداً للـ noise (Overfitting).",
        "explain_wrong": "❌ غلط! الـ k الصغيرة بتخلي الموديل حساس جداً للـ noise."
    },
    {
        "q": "Which of the following is a weakness of k-NN?",
        "type": "mcq",
        "options": [
            "Simple and effective",
            "Fast training phase",
            "Slow classification phase",
            "Makes no assumptions about data distribution"
        ],
        "ans": "Slow classification phase",
        "explain_correct": "✅ صح! الـ k-NN بطيء جداً وقت الـ classification لأنه بيحسب المسافة مع كل الداتا.",
        "explain_wrong": "❌ غلط! العيب الرئيسي هو بُطء الـ classification phase."
    },
    {
        "q": "Which of the following is a strength of k-NN?",
        "type": "mcq",
        "options": [
            "Produces a model for interpretation",
            "Fast classification phase",
            "Makes no assumptions about data distribution",
            "Works well with missing data"
        ],
        "ans": "Makes no assumptions about data distribution",
        "explain_correct": "✅ صح! من مميزاته إنه non-parametric ومش بيفترض أي توزيع للداتا.",
        "explain_wrong": "❌ غلط! الميزة الأهم إنه لا يفترض شكل معين لتوزيع البيانات."
    },
    {
        "q": "What does normalization achieve in k-NN?",
        "type": "mcq",
        "options": [
            "Removes noisy data",
            "Prevents one attribute from dominating distance calculations",
            "Speeds up training",
            "Selects the best k automatically"
        ],
        "ans": "Prevents one attribute from dominating distance calculations",
        "explain_correct": "✅ صح! الـ normalization بيمنع الخصائص ذات الأرقام الكبيرة إنها تسيطر على الحسابات.",
        "explain_wrong": "❌ غلط! بيُستخدم لمنع attribute واحد من السيطرة على حساب المسافة."
    },
    {
        "q": "In the Euclidean distance formula dist(p,q), what is computed?",
        "type": "mcq",
        "options": [
            "Sum of absolute differences",
            "Square root of the sum of squared differences",
            "Product of feature values",
            "Average of feature values"
        ],
        "ans": "Square root of the sum of squared differences",
        "explain_correct": "✅ صح! المسافة الإقليدية هي الجذر التربيعي لمجموع الفروق المربعة.",
        "explain_wrong": "❌ غلط! هي الجذر التربيعي لمجموع الفروق المربعة."
    },
    {
        "q": "What is a Tomek Link?",
        "type": "mcq",
        "options": [
            "A method to increase training data",
            "A pair of examples from different classes that are each other's nearest neighbor",
            "A technique for selecting the best k",
            "A distance metric"
        ],
        "ans": "A pair of examples from different classes that are each other's nearest neighbor",
        "explain_correct": "✅ صح! الـ Tomek Link هو نقطتين من كلاسين مختلفين وهما أقرب جيران لبعض.",
        "explain_wrong": "❌ غلط! هو النقطتين اللي من فئات مختلفة وأقرب حاجة لبعض."
    },
    {
        "q": "Why are Tomek Links removed from training data?",
        "type": "mcq",
        "options": [
            "To speed up the algorithm",
            "To remove borderline/noisy examples that can harm classification",
            "To reduce the number of features",
            "To normalize the data"
        ],
        "ans": "To remove borderline/noisy examples that can harm classification",
        "explain_correct": "✅ صح! بنشيلهم عشان ننضف الداتا من الأمثلة الحدودية المزعجة (noisy).",
        "explain_wrong": "❌ غلط! إزالتهم بتساعد في التخلص من الـ borderline examples."
    },
    {
        "q": "In weighted k-NN, what weight is given to the farthest neighbor (d_k)?",
        "type": "mcq",
        "options": [
            "1",
            "0.5",
            "0",
            "It depends on k"
        ],
        "ans": "0",
        "explain_correct": "✅ صح! في الـ weighted k-NN، الجار الأبعد بياخد وزن صفر.",
        "explain_wrong": "❌ غلط! الجار الأبعد بيأخد وزن 0."
    },
    {
        "q": "In weighted k-NN, what weight is given to the nearest neighbor (d_1)?",
        "type": "mcq",
        "options": [
            "0",
            "0.5",
            "1",
            "k"
        ],
        "ans": "1",
        "explain_correct": "✅ صح! الجار الأقرب بياخد أعلى وزن وهو 1.",
        "explain_wrong": "❌ غلط! الجار الأقرب بياخد وزن 1."
    },
    {
        "q": "What is the main benefit of using k neighbors instead of just 1?",
        "type": "mcq",
        "options": [
            "Faster computation",
            "Voting among neighbors overcomes noise",
            "Eliminates the need for normalization",
            "Reduces memory usage"
        ],
        "ans": "Voting among neighbors overcomes noise",
        "explain_correct": "✅ صح! التصويت بين كذا جار بيساعد في التغلب على تأثير الـ noise.",
        "explain_wrong": "❌ غلط! استخدام k جيران بيساعدنا نتغلب على الـ noise من خلال التصويت."
    },
    {
        "q": "What is class-label noise in k-NN?",
        "type": "mcq",
        "options": [
            "An attribute value is incorrect",
            "The class provided for an example is incorrect",
            "Too many features in the dataset",
            "Missing values in features"
        ],
        "ans": "The class provided for an example is incorrect",
        "explain_correct": "✅ صح! لما الكلاس (الـ label) بتاع الداتا يكون متسجل غلط.",
        "explain_wrong": "❌ غلط! الـ class-label noise هو وجود تصنيف غلط للداتا."
    },
    {
        "q": "What is attribute noise in k-NN?",
        "type": "mcq",
        "options": [
            "The class label is wrong",
            "An attribute's value is incorrect",
            "Too many neighbors are selected",
            "Normalization is not applied"
        ],
        "ans": "An attribute's value is incorrect",
        "explain_correct": "✅ صح! لما الخصائص (attributes) نفسها تكون قيمتها غلط.",
        "explain_wrong": "❌ غلط! هو لما تكون قيمة الـ attribute غير صحيحة."
    },
    {
        "q": "Which distance axiom states d(x,x) = 0?",
        "type": "mcq",
        "options": [
            "Triangle inequality",
            "Symmetry",
            "Identity",
            "Non-negativity"
        ],
        "ans": "Identity",
        "explain_correct": "✅ صح! قاعدة الـ Identity بتنص على أن المسافة بين النقطة ونفسها صفر.",
        "explain_wrong": "❌ غلط! دي قاعدة الـ Identity."
    },
    {
        "q": "Which distance axiom is represented by d(x,y) = d(y,x)?",
        "type": "mcq",
        "options": [
            "Non-negativity",
            "Identity",
            "Symmetry",
            "Triangle inequality"
        ],
        "ans": "Symmetry",
        "explain_correct": "✅ صح! قاعدة الـ Symmetry (التماثل).",
        "explain_wrong": "❌ غلط! دي خاصية الـ Symmetry."
    },
    {
        "q": "The triangle inequality for distance metrics states:",
        "type": "mcq",
        "options": [
            "d(x,y) = d(y,x)",
            "d(x,y) + d(y,z) >= d(x,z)",
            "d(x,x) = 0",
            "d(x,y) >= 0"
        ],
        "ans": "d(x,y) + d(y,z) >= d(x,z)",
        "explain_correct": "✅ صح! مجموع أي مسافتين بيكون أكبر من أو يساوي المسافة التالتة.",
        "explain_wrong": "❌ غلط! المعادلة الصحيحة هي d(x,y) + d(y,z) >= d(x,z)."
    },
    {
        "q": "A k-NN model gets 100% training accuracy but fails on new data. What is the most likely problem?",
        "type": "mcq",
        "options": [
            "Underfitting",
            "Overfitting",
            "Incorrect normalization",
            "Too large k"
        ],
        "ans": "Overfitting",
        "explain_correct": "✅ صح! دي الحالة المثالية لتعريف الـ Overfitting (حفظ مش فهم).",
        "explain_wrong": "❌ غلط! الفشل على بيانات جديدة معناه Overfitting."
    },
    {
        "q": "Which statement about k-NN is TRUE regarding all three?",
        "type": "mcq",
        "options": [
            "k-NN performs better with same-scale data, struggles with many features, and makes no functional form assumptions",
            "k-NN is a parametric model",
            "k-NN requires data to be normalized only for large k",
            "k-NN works best with many irrelevant features"
        ],
        "ans": "k-NN performs better with same-scale data, struggles with many features, and makes no functional form assumptions",
        "explain_correct": "✅ صح! بيحتاج داتا scaled، بيتأثر بالـ features الكتير (curse of dimensionality)، وهو non-parametric.",
        "explain_wrong": "❌ غلط! k-NN بيتأثر سلباً بالخصائص الكتيرة، وبيحتاج normalization."
    },
    {
        "q": "k-NN does more computation at which phase?",
        "type": "mcq",
        "options": [
            "Training phase",
            "Test/classification phase",
            "Both equally",
            "Neither"
        ],
        "ans": "Test/classification phase",
        "explain_correct": "✅ صح! العمليات الحسابية كلها بتحصل وقت الاختبار.",
        "explain_wrong": "❌ غلط! الحسابات الأكبر بتكون في الـ Test phase."
    },
    {
        "q": "Given values 7, 4, 25, -5, 10 with MIN=-5, MAX=25, what is the normalized value of 7?",
        "type": "mcq",
        "options": [
            "0.3",
            "0.4",
            "0.5",
            "0.6"
        ],
        "ans": "0.4",
        "explain_correct": "✅ صح! القانون: (7 - (-5)) / (25 - (-5)) = 12 / 30 = 0.4.",
        "explain_wrong": "❌ غلط! النتيجة هي 0.4."
    },
    {
        "q": "In the weighted 5-NN example with distances d1=1, d2=3, d3=4, d4=5, d5=8, what is w2?",
        "type": "mcq",
        "options": [
            "4/7",
            "5/7",
            "3/7",
            "1"
        ],
        "ans": "5/7",
        "explain_correct": "✅ صح! باستخدام قانون الوزن (w) للجار التاني.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 5/7."
    },
    {
        "q": "Which step in k-NN involves finding the majority class among neighbors?",
        "type": "mcq",
        "options": [
            "Step 2",
            "Step 3",
            "Step 5",
            "Step 6"
        ],
        "ans": "Step 5",
        "explain_correct": "✅ صح! في الخطوة الخامسة بنحسب الأغلبية.",
        "explain_wrong": "❌ غلط! الأغلبية بتتحسب في الخطوة رقم 5."
    },
    {
        "q": "What type of variable is used to label categories in k-NN training data?",
        "type": "mcq",
        "options": [
            "Continuous",
            "Nominal",
            "Ordinal",
            "Binary only"
        ],
        "ans": "Nominal",
        "explain_correct": "✅ صح! الفئات في التصنيف بتبقى Nominal.",
        "explain_wrong": "❌ غلط! بنستخدم متغيرات Nominal للفئات."
    },
    {
        "q": "Irrelevant attributes in k-NN cause problems because:",
        "type": "mcq",
        "options": [
            "They slow down training",
            "They affect example-to-example distances without affecting the class",
            "They prevent normalization",
            "They increase k"
        ],
        "ans": "They affect example-to-example distances without affecting the class",
        "explain_correct": "✅ صح! الخصائص الغير مهمة بتبوظ حساب المسافة من غير ما تفيد في التصنيف.",
        "explain_wrong": "❌ غلط! لأنهم بيغيروا حسابات المسافة بلا داعٍ."
    },
    {
        "q": "In removing redundant examples, the algorithm starts with set S containing:",
        "type": "mcq",
        "options": [
            "All training examples",
            "One positive and one negative example",
            "Only positive examples",
            "k random examples"
        ],
        "ans": "One positive and one negative example",
        "explain_correct": "✅ صح! الخوارزمية بتبدأ بمثال واحد من كل نوع.",
        "explain_wrong": "❌ غلط! بتبدأ بـ one positive and one negative example."
    },
    {
        "q": "The k-NN algorithm is best suited for problems where:",
        "type": "mcq",
        "options": [
            "Data is linear and separable",
            "Relationships are complex but similar classes are fairly homogeneous",
            "The dataset is very small",
            "Feature importance is known"
        ],
        "ans": "Relationships are complex but similar classes are fairly homogeneous",
        "explain_correct": "✅ صح! بيبدع في البيانات المعقدة اللي فيها الكلاسات متجمعة (homogeneous).",
        "explain_wrong": "❌ غلط! هو الأفضل لما تكون العلاقات معقدة والفئات متجانسة."
    },
    {
        "q": "Which graph shape best describes error rate vs. k in k-NN?",
        "type": "mcq",
        "options": [
            "Linear increase",
            "U-shaped curve (high at both extremes, low in middle)",
            "Linear decrease",
            "Flat line"
        ],
        "ans": "U-shaped curve (high at both extremes, low in middle)",
        "explain_correct": "✅ صح! معدل الخطأ بيبقى عالي جداً مع k الصغيرة (overfitting) والـ k الكبيرة (underfitting) وبيقل في النص.",
        "explain_wrong": "❌ غلط! بياخد شكل الـ U-curve."
    },
    {
        "q": "In weighted k-NN, x is classified as positive when:",
        "type": "mcq",
        "options": [
            "More than half the neighbors are positive",
            "Sum of positive weights > sum of negative weights",
            "d1 belongs to a positive class",
            "k is odd"
        ],
        "ans": "Sum of positive weights > sum of negative weights",
        "explain_correct": "✅ صح! في الـ weighted k-NN بنجمع الأوزان مش بنعد الأصوات.",
        "explain_wrong": "❌ غلط! الكلاس بيتحدد لما مجموع الأوزان الإيجابية يكون أكبر."
    },
    {
        "q": "What scaling problem can occur in k-NN?",
        "type": "mcq",
        "options": [
            "Nominal features dominate numeric features",
            "An attribute with large range can overwhelm others in distance calculation",
            "Too many classes reduce accuracy",
            "Normalization increases bias"
        ],
        "ans": "An attribute with large range can overwhelm others in distance calculation",
        "explain_correct": "✅ صح! الأرقام الكبيرة بتبلع الأرقام الصغيرة في حساب المسافة، عشان كده بنحتاج normalization.",
        "explain_wrong": "❌ غلط! المشكلة بتحصل لما attribute مداه كبير يسيطر على حسابات المسافة."
    },
    {
        "q": "In the redundant example removal algorithm, examples are added to S when they:",
        "type": "mcq",
        "options": [
            "Are correctly classified by 1-NN using S",
            "Are incorrectly classified by 1-NN using S",
            "Are positive examples",
            "Have the smallest distance"
        ],
        "ans": "Are incorrectly classified by 1-NN using S",
        "explain_correct": "✅ صح! بنضيف الأمثلة للمجموعة S لما الخوارزمية تغلط في تصنيفهم.",
        "explain_wrong": "❌ غلط! بيتم إضافتهم لما يتصنفوا بشكل خاطئ."
    },

    # ══════════════════════════════════════════════
    # ✅ True / False Questions (36–50)
    # ══════════════════════════════════════════════

    {
        "q": "k-NN does more computation at test time rather than train time.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! كونه Lazy learner بيخليه يعمل كل العمليات الحسابية وقت الاختبار.",
        "explain_wrong": "❌ غلط! العبارة صحيحة تماماً."
    },
    {
        "q": "k-NN produces a model that helps understand how features relate to the class.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! k-NN مش بيطلع model نقدر نفهم منه العلاقات بسهولة زي الـ Decision Trees.",
        "explain_wrong": "❌ غلط! k-NN لا ينتج نموذج تفسيري."
    },
    {
        "q": "Normalization ensures each attribute falls into the interval [0,1].",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! دي وظيفة الـ Min-Max Normalization الأساسية.",
        "explain_wrong": "❌ غلط! الـ Normalization فعلاً بتخلي القيم بين 0 و 1."
    },
    {
        "q": "When k is too small, k-NN becomes very sensitive to noise.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! k الصغيرة جداً بتسبب Overfitting وبتتأثر بالـ Noise.",
        "explain_wrong": "❌ غلط! العبارة صحيحة تماماً."
    },
    {
        "q": "In k-NN, a Tomek Link connects two examples from the SAME class.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! الـ Tomek Link بيربط بين نقطتين من كلاسين مختلفين.",
        "explain_wrong": "❌ غلط! بيربط أمثلة من فئات مختلفة (Different class)."
    },
    {
        "q": "Irrelevant attributes do NOT affect distance calculations in k-NN.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! الخصائص غير المهمة بتأثر جداً وتبوظ الحسابات.",
        "explain_wrong": "❌ غلط! الخصائص غير المهمة بتأثر سلبياً على حساب المسافة."
    },
    {
        "q": "k-NN makes assumptions about the underlying data distribution.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! هو Non-parametric يعني مش بيفترض أي توزيع.",
        "explain_wrong": "❌ غلط! k-NN لا يضع افتراضات عن التوزيع."
    },
    {
        "q": "In weighted k-NN, closer neighbors get higher weights than farther ones.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! عشان كده بنستخدمه، لإعطاء أهمية أكبر للجار القريب.",
        "explain_wrong": "❌ غلط! العبارة صحيحة تماماً."
    },
    {
        "q": "A k-NN model with 100% training accuracy but poor test accuracy is overfitted.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! دي سمات الـ Overfitting بالظبط.",
        "explain_wrong": "❌ غلط! العبارة صحيحة 100%."
    },
    {
        "q": "The Euclidean distance satisfies d(x,y) = d(y,x).",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! دي خاصية التماثل (Symmetry).",
        "explain_wrong": "❌ غلط! العبارة صحيحة."
    },
    {
        "q": "Noisy data causes no problems for the k-NN algorithm.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! الـ Noise بتسبب مشاكل كبيرة في k-NN خصوصاً لو k صغيرة.",
        "explain_wrong": "❌ غلط! الـ Noise بتعمل مشكلة كبيرة للـ k-NN."
    },
    {
        "q": "Using k neighbors instead of 1 helps overcome noise through voting.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! التصويت بيقلل تأثير الـ Outliers والـ Noise.",
        "explain_wrong": "❌ غلط! العبارة صحيحة."
    },
    {
        "q": "The training phase of k-NN is slower than its classification phase.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! الـ Classification هو اللي أبطأ بكتير لأن التدريب تقريباً مفيش.",
        "explain_wrong": "❌ غلط! مرحلة الـ Classification هي الأبطأ."
    },
    {
        "q": "k-NN works well when similar class items tend to be homogeneous in feature space.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! لما الكلاسات المتشابهة تكون قريبة من بعضها في المسافة.",
        "explain_wrong": "❌ غلط! العبارة صحيحة."
    },
    {
        "q": "In the normalization formula, MAX refers to the maximum value in the test set.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! الـ MAX هو أقصى قيمة في الـ Training set مش الـ Test set.",
        "explain_wrong": "❌ غلط! تشير إلى القيمة العظمى في بيانات التدريب (Training set)."
    }
]