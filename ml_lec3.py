# ==========================================
# 📖 ml_lec3.py
# Machine Learning - Lecture 3
# Linear Regression, Gradient Descent, and Feature Scaling
# ==========================================

QUESTIONS = [
    # ─── Part 1: Basic Concepts & Notation ───
    {
        "q": "في التعلم الخاضع للإشراف (Supervised Learning)، ما هو الفرق الأساسي بين مشكلة الانحدار (Regression) والتصنيف (Classification)؟",
        "type": "mcq",
        "options": ["الانحدار يتوقع قيمة متصلة (Continuous)، والتصنيف يتوقع قيمة منفصلة (Discrete)", "الانحدار للبيانات غير المسماة، والتصنيف للبيانات المسماة", "التصنيف يتوقع قيمة متصلة، والانحدار يتوقع فئات", "لا يوجد فرق بينهما"],
        "ans": "الانحدار يتوقع قيمة متصلة (Continuous)، والتصنيف يتوقع قيمة منفصلة (Discrete)",
        "explain_correct": "الانحدار (Regression) بيُستخدم لتوقع أرقام متصلة زي أسعار البيوت، أما التصنيف (Classification) بيُستخدم لتوقع فئات محددة زي (مريض/سليم). ✅",
        "explain_wrong": "تذكر: Regression = Continuous/Real-valued، Classification = Discrete."
    },
    {
        "q": "في مصطلحات تعلم الآلة، ماذا يمثل الرمز 'm'؟",
        "type": "mcq",
        "options": ["عدد الخصائص (Features)", "عدد أمثلة التدريب (Training examples)", "متغير الخرج (Output variable)", "معدل التعلم (Learning rate)"],
        "ans": "عدد أمثلة التدريب (Training examples)",
        "explain_correct": "الرمز 'm' دايماً بيعبر عن عدد الصفوف أو الأمثلة في الداتا اللي بنتدرب عليها. ✅",
        "explain_wrong": "الرمز 'n' هو اللي بيعبر عن عدد الخصائص (Features)."
    },
    {
        "q": "ما هو الرمز الذي يعبر عن قيمة الخاصية رقم j في مثال التدريب رقم i؟",
        "type": "mcq",
        "options": ["x_i^(j)", "x_j^(i)", "y_j^(i)", "theta_j^(i)"],
        "ans": "x_j^(i)",
        "explain_correct": "الأس بين قوسين (i) بيعبر عن رقم الصف (مثال التدريب)، والـ subscript (j) بيعبر عن رقم العمود (الخاصية). ✅",
        "explain_wrong": "تذكر: الـ (i) فوق للصف، والـ j تحت للعمود."
    },
    
    # ─── Part 2: Hypothesis & Cost Function ───
    {
        "q": "المعادلة h_θ(x) = θ_0 + θ_1 * x تمثل:",
        "type": "mcq",
        "options": ["Cost Function", "Gradient Descent", "Linear Regression Hypothesis (بمتغير واحد)", "Polynomial Regression"],
        "ans": "Linear Regression Hypothesis (بمتغير واحد)",
        "explain_correct": "دي معادلة الخط المستقيم البسيطة (Hypothesis) اللي بنحاول نخليها تمر بأفضل شكل في البيانات. ✅",
        "explain_wrong": "هذه الدالة تسمى الفرضية (Hypothesis) وليست دالة التكلفة."
    },
    {
        "q": "في الـ Linear Regression، ما هو الهدف الأساسي لدالة التكلفة J(θ_0, θ_1)؟",
        "type": "mcq",
        "options": ["تعظيم قيمة J(θ_0, θ_1)", "تقليل (Minimize) قيمة J(θ_0, θ_1)", "جعل J(θ_0, θ_1) تساوي 1 دائماً", "حساب عدد أمثلة التدريب"],
        "ans": "تقليل (Minimize) قيمة J(θ_0, θ_1)",
        "explain_correct": "دالة التكلفة (Cost Function) بتحسب مقدار الخطأ، فهدفنا دايماً هو تقليل الخطأ ده لأقل قيمة ممكنة (Minimize). ✅",
        "explain_wrong": "دالة التكلفة تمثل الخطأ، والخطأ يجب تقليله."
    },
    {
        "q": "تُعرف دالة التكلفة المستخدمة في الانحدار الخطي باسم:",
        "type": "mcq",
        "options": ["Logistic Function", "Squared Error Function", "Absolute Error Function", "Sigmoid Function"],
        "ans": "Squared Error Function",
        "explain_correct": "دالة التكلفة في الانحدار الخطي هي متوسط مربعات الأخطاء (Squared Error)، وهي الأشهر والأكثر كفاءة لحل هذه المشكلة. ✅",
        "explain_wrong": "تسمى Squared error function لأننا نُربع الفرق بين التوقع والقيمة الحقيقية."
    },
    {
        "q": "في رسم الـ Contour Plot لدالة التكلفة، ماذا تمثل النقطة الموجودة في مركز الدوائر متحدة المركز؟",
        "type": "mcq",
        "options": ["أعلى قيمة للخطأ", "أقل قيمة لدالة التكلفة (Minimum)", "قيمة معدل التعلم", "نقطة البداية العشوائية"],
        "ans": "أقل قيمة لدالة التكلفة (Minimum)",
        "explain_correct": "مركز الدوائر (الـ Ellipses) في الـ Contour plot بيمثل قاع الـ Bowl، وهو أقل قيمة لدالة التكلفة (أفضل parameters). ✅",
        "explain_wrong": "المركز يمثل الـ Global Minimum للـ Cost function."
    },

    # ─── Part 3: Gradient Descent Algorithm ───
    {
        "q": "في خوارزمية الـ Gradient Descent، لضمان عمل الخوارزمية بشكل صحيح، يجب تحديث المعاملات (θ_0, θ_1) بشكل:",
        "type": "mcq",
        "options": ["متسلسل (Sequential update)", "متزامن (Simultaneous update)", "عشوائي", "فقط تحديث θ_1 وترك θ_0"],
        "ans": "متزامن (Simultaneous update)",
        "explain_correct": "لازم نحسب كل القيم الجديدة للـ θ في متغيرات مؤقتة (temp)، وبعدين نحدثهم كلهم مع بعض في نفس الوقت (Simultaneously). ✅",
        "explain_wrong": "التحديث المتسلسل يغير قيمة الدالة أثناء حساب المشتقات الأخرى، وهو خطأ."
    },
    {
        "q": "ماذا يحدث إذا كان معدل التعلم (Learning Rate α) صغيراً جداً؟",
        "type": "mcq",
        "options": ["الخوارزمية ستفشل في العمل", "الخوارزمية ستتجاوز الحد الأدنى (Overshoot)", "الـ Gradient Descent سيكون بطيئاً جداً في الوصول للحل", "دالة التكلفة ستزداد"],
        "ans": "الـ Gradient Descent سيكون بطيئاً جداً في الوصول للحل",
        "explain_correct": "الـ Alpha الصغيرة معناها خطوات صغيرة جداً، وبالتالي هياخد وقت (Iterations) كتير جداً عشان يوصل للـ Minimum. ✅",
        "explain_wrong": "الـ Alpha الصغيرة = بطء شديد (Slow convergence)."
    },
    {
        "q": "ماذا يحدث إذا كان معدل التعلم (Learning Rate α) كبيراً جداً؟",
        "type": "mcq",
        "options": ["سيكون بطيئاً جداً", "سيصل للحل المثالي فوراً", "قد يتجاوز الحد الأدنى (Overshoot) ولا يصل للحل أبداً (Diverge)", "الـ Gradient Descent سيتحول لتصنيف"],
        "ans": "قد يتجاوز الحد الأدنى (Overshoot) ولا يصل للحل أبداً (Diverge)",
        "explain_correct": "الـ Alpha الكبيرة بتخلي الخطوة واسعة، فممكن تنط الناحية التانية من المنحنى وتفضل تكبر لحد ما تنفجر (Diverge). ✅",
        "explain_wrong": "الـ Alpha الكبيرة = Overshoot and fail to converge."
    },
    {
        "q": "إذا وصل الـ Gradient Descent إلى نقطة الـ Local Minimum، ماذا ستكون قيمة خطوة التحديث التالية؟",
        "type": "mcq",
        "options": ["ستتحرك الخوارزمية لنقطة عشوائية", "لن تتغير المعاملات (θ) لأن المشتقة ستكون صفراً", "ستزداد المعاملات بمقدار α", "ستعكس الخوارزمية اتجاهها"],
        "ans": "لن تتغير المعاملات (θ) لأن المشتقة ستكون صفراً",
        "explain_correct": "عند نقطة الـ Minimum، المماس بيكون أفقي فالمشتقة (Derivative) بتكون صفر. إذن θ - (α * 0) = θ. الخوارزمية بتثبت مكانها. ✅",
        "explain_wrong": "عند الـ Local minimum، التحديث يتوقف لأن الـ slope = 0."
    },
    {
        "q": "كلما اقترب الـ Gradient Descent من الـ Local Minimum، فإن الخطوات التي يتخذها تُصبح أصغر تلقائياً، لذلك لا نحتاج لتقليل الـ α مع مرور الوقت.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح جداً! لأن المشتقة (Slope) بتقل كل ما بنقرب من القاع، فبالتالي قيمة (α * المشتقة) بتقل لوحدها والخطوات بتصغر تلقائياً. ✅",
        "explain_wrong": "لست بحاجة لتغيير α لأن الميل (Derivative) يصغر من نفسه."
    },
    {
        "q": "لماذا يُعتبر تطبيق Gradient Descent على Linear Regression آمناً من الوقوع في Local Minimum سيء؟",
        "type": "mcq",
        "options": ["لأنه لا يستخدم مشتقات", "لأن دالة التكلفة فيه هي Convex Function (شكل الوعاء) ولها Global Optimum واحد فقط", "لأن معدل التعلم يتغير دائماً", "لأنه يعمل على ميزة واحدة فقط"],
        "ans": "لأن دالة التكلفة فيه هي Convex Function (شكل الوعاء) ولها Global Optimum واحد فقط",
        "explain_correct": "الـ Cost function في الـ Linear Regression دايماً بتكون Convex (على شكل وعاء)، يعني مفيهاش أي Local minimum يخدعها، هي دايماً بتنزل للـ Global Minimum الوحيد. ✅",
        "explain_wrong": "دالة التكلفة هنا Convex (مُحدبة للأسفل) ولها حل مثالي واحد."
    },
    {
        "q": "ماذا تعني كلمة 'Batch' في مصطلح Batch Gradient Descent؟",
        "type": "mcq",
        "options": ["أن الخوارزمية تستخدم مثال تدريب واحد في كل خطوة", "أن الخوارزمية تعالج البيانات في مجموعات عشوائية", "أن الخوارزمية تستخدم كل أمثلة التدريب (All training examples) لحساب المشتقة في كل خطوة", "أن الخوارزمية لا تستخدم بيانات"],
        "ans": "أن الخوارزمية تستخدم كل أمثلة التدريب (All training examples) لحساب المشتقة في كل خطوة",
        "explain_correct": "في كل خطوة تحديث، بنجمع الأخطاء على كل الـ m أمثلة (كل الداتا)، وده معنى كلمة Batch. ✅",
        "explain_wrong": "Batch تعني استخدام Dataset كاملة في كل Update."
    },

    # ─── Part 4: Multivariate Linear Regression ───
    {
        "q": "في الـ Multivariate Linear Regression، نقوم بإضافة الخاصية الوهمية (x_0) لتبسيط ضرب المصفوفات. ما هي قيمة x_0 دائماً؟",
        "type": "mcq",
        "options": ["0", "1", "-1", "تساوي قيمة y"],
        "ans": "1",
        "explain_correct": "بنفترض دايماً إن x_0 = 1 عشان لما نضربها في المعامل θ_0 يفضل θ_0 زي ما هو (الـ Y-intercept). ✅",
        "explain_wrong": "x_0 دايماً بواحد لتسهيل العمليات الحسابية بالـ Vectors."
    },
    {
        "q": "ما هو الهدف من عملية الـ Feature Scaling؟",
        "type": "mcq",
        "options": ["تقليل عدد الخصائص", "جعل الـ Gradient Descent يتقارب (Converge) بشكل أسرع", "زيادة قيمة دالة التكلفة", "إزالة الـ x_0"],
        "ans": "جعل الـ Gradient Descent يتقارب (Converge) بشكل أسرع",
        "explain_correct": "لما تكون الخصائص كلها في نفس الـ Range (مثلاً من -1 لـ 1)، الـ Contours بتبقى دائرية والـ Gradient Descent بيوصل للحل بسرعة جداً بدل ما يتذبذب. ✅",
        "explain_wrong": "الـ Feature Scaling بيسرع الوصول للحل."
    },
    {
        "q": "في أفضل الحالات (Ideal case)، ما هو النطاق التقريبي الذي يجب أن تتواجد فيه قيم الخصائص (Features) بعد عملية الـ Scaling؟",
        "type": "mcq",
        "options": ["من 0 إلى 100", "من -100 إلى 100", "تقريباً من -1 إلى 1", "من المالانهاية السالبة إلى الموجبة"],
        "ans": "تقريباً من -1 إلى 1",
        "explain_correct": "المثالي إن كل الخصائص تكون تقريباً بين -1 و 1. لو كانت من -3 لـ 3 أو -1/3 لـ 1/3 برضه مقبول. ✅",
        "explain_wrong": "الرينج المثالي هو حول الصفر بقيم صغيرة (-1 to +1)."
    },
    {
        "q": "المعادلة x_i = (x_i - μ_i) / s_i هي قانون لـ:",
        "type": "mcq",
        "options": ["Gradient Descent", "Cost Function", "Mean Normalization", "Polynomial Regression"],
        "ans": "Mean Normalization",
        "explain_correct": "هذا هو قانون الـ Mean Normalization، بنطرح المتوسط (μ) ونقسم على المدى أو الانحراف المعياري (s) عشان نخلي متوسط الداتا بصفر. ✅",
        "explain_wrong": "هذا القانون يستخدم لعمل Scaling للبيانات."
    },
    {
        "q": "في قانون الـ Mean Normalization: x_i = (x_i - μ_i) / s_i، ماذا يمكن أن يمثل الرمز s_i؟",
        "type": "mcq",
        "options": ["المتوسط الحسابي", "المدى (Max - Min) أو الانحراف المعياري (Standard Deviation)", "عدد الأمثلة m", "الـ Learning Rate"],
        "ans": "المدى (Max - Min) أو الانحراف المعياري (Standard Deviation)",
        "explain_correct": "الرمز s بيمثل الـ Range (أكبر قيمة ناقص أصغر قيمة) أو ممكن نستخدم الـ Standard Deviation في القسمة. ✅",
        "explain_wrong": "s_i هو مقياس التشتت (المدى أو الانحراف المعياري)."
    },

    # ─── Part 5: Debugging & Polynomial Regression ───
    {
        "q": "كيف نتأكد أن الـ Gradient Descent يعمل بشكل صحيح (Debugging)؟",
        "type": "mcq",
        "options": ["برسم قيمة J(θ) مع عدد الـ Iterations ويجب أن يتناقص", "برسم قيمة α مع عدد الـ Iterations ويجب أن تتزايد", "برسم قيم x مع قيم y", "برسم J(θ) ويجب أن يكون متزايداً"],
        "ans": "برسم قيمة J(θ) مع عدد الـ Iterations ويجب أن يتناقص",
        "explain_correct": "الطريقة الأفضل هي رسم الـ Cost function مع كل خطوة (Iteration). لو شغال صح، لازم الخطأ (J) يقل باستمرار. ✅",
        "explain_wrong": "دالة التكلفة يجب أن تتناقص في كل خطوة."
    },
    {
        "q": "إذا رسمت J(θ) مع عدد الـ Iterations ووجدته يزداد (يتجه للأعلى)، فما هو السبب المحتمل؟",
        "type": "mcq",
        "options": ["البيانات صغيرة جداً", "قيمة معدل التعلم (α) كبيرة جداً ويجب تصغيرها", "قيمة (α) صغيرة جداً ويجب تكبيرها", "الـ Gradient Descent يعمل بشكل ممتاز"],
        "ans": "قيمة معدل التعلم (α) كبيرة جداً ويجب تصغيرها",
        "explain_correct": "لما الخطأ يزيد بدل ما يقل، ده معناه إن الخوارزمية بتعمل Overshoot (بتعدي الهدف)، وحلها الفوري إنك تصغر قيمة α. ✅",
        "explain_wrong": "زيادة J(θ) تعني Divergence، وسببها α كبيرة."
    },
    {
        "q": "لإجراء اختبار تقارب تلقائي (Automatic Convergence Test)، يمكننا إيقاف الخوارزمية إذا انخفضت قيمة J(θ) بمقدار أقل من رقم صغير جداً، مثل:",
        "type": "mcq",
        "options": ["100", "1", "10^-3 (0.001)", "0.5"],
        "ans": "10^-3 (0.001)",
        "explain_correct": "ممكن نبرمج الكود إنه يوقف لو التغيير في دالة التكلفة بقى تافه جداً (أقل من 0.001 مثلاً)، وده معناه إنه وصل للقاع تقريباً. ✅",
        "explain_wrong": "التغيير الضئيل (مثل 10^-3) يمثل الوصول لـ Convergence."
    },
    {
        "q": "في الـ Polynomial Regression، يمكننا إنشاء خصائص جديدة (Features) من الخصائص الموجودة، مثل تربيع x أو أخذ الجذر التربيعي له لتناسب البيانات غير الخطية.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح. لو البيانات شكلها مش خط مستقيم، ممكن نخترع خصائص جديدة زي x^2 أو x^3 أو sqrt(x) عشان الفرضية تاخد شكل منحنى يناسب الداتا. ✅",
        "explain_wrong": "الـ Polynomial Regression يعتمد على دمج ورفع الأس للخصائص الموجودة."
    },
    {
        "q": "عند استخدام الـ Polynomial Regression وتحويل خاصية x إلى x و x^2 و x^3، تصبح عملية الـ Feature Scaling غير مهمة.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ تماماً! بالعكس، الـ Feature Scaling بيكون ضروري وحتمي هنا! لأن لو x مداها من 1 لـ 100، فـ x^3 هيكون مداها من 1 لـ 1,000,000! الفروق هتبقى ضخمة جداً. ✅",
        "explain_wrong": "الـ Feature Scaling أهم بكثير في الـ Polynomial regression لاختلاف الـ Ranges الشديد."
    },
    {
        "q": "أي من القيم التالية لمعدل التعلم (α) يُنصح بتجربتها عند البحث عن أفضل قيمة للـ Gradient Descent؟",
        "type": "mcq",
        "options": ["فقط 0.01 و 0.1", "أرقام سالبة فقط", "مضاعفات تقريبية بزيادة 3 أضعاف مثل: ..., 0.001, 0.003, 0.01, 0.03, 0.1, ...", "أرقام صحيحة كبيرة مثل 10, 100, 1000"],
        "ans": "مضاعفات تقريبية بزيادة 3 أضعاف مثل: ..., 0.001, 0.003, 0.01, 0.03, 0.1, ...",
        "explain_correct": "أندرو نج (Andrew Ng) بينصح دايماً إنك تجرب تضرب الألفا في 3 (تقريباً) في كل تجربة عشان تكتشف الرينج المناسب بسرعة. ✅",
        "explain_wrong": "التدرج بلوغاريتم مضروب في 3 هو أفضل طريقة لاكتشاف α."
    }
]