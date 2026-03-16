# ==========================================
# 📖 dsp_lec4.py
# Digital Signal Processing - Lecture 4, Sec 4 & Sheet 4
# LTI Systems, Advanced Impulse Properties, and Operations
# ==========================================

QUESTIONS = [
    # ─── Part 1: Advanced Impulse & Step Properties (From Sec 4) ───
    {
        "q": "For a CONTINUOUS-time impulse function, what is the result of time scaling δ(at)?",
        "type": "mcq",
        "options": ["a * δ(t)", "δ(t)", "(1/|a|) * δ(t)", "(1/a) * δ(t)"],
        "ans": "(1/|a|) * δ(t)",
        "explain_correct": "في الزمن المتصل، الـ Scaling بيأثر على مساحة الدلتا، فبنقسم على المقياس المطلق لـ a. ✅",
        "explain_wrong": "تذكر القاعدة: δ(at) = (1/|a|) * δ(t) للإشارات المتصلة."
    },
    {
        "q": "For a DISCRETE-time impulse sequence, what is the result of time scaling δ[an] (where a is an integer)?",
        "type": "mcq",
        "options": ["(1/|a|) * δ[n]", "δ[n]", "a * δ[n]", "0"],
        "ans": "δ[n]",
        "explain_correct": "في الديسكريت، الدلتا عبارة عن عينة واحدة عند الصفر ملهاش مساحة تتأثر بالـ Scaling. طالما an = 0 إذن n = 0. ✅",
        "explain_wrong": "خصائص المتصل تختلف عن الديسكريت. في الديسكريت δ[an] = δ[n]."
    },
    {
        "q": "The relationship between the discrete-time step function u[n] and the discrete impulse δ[n] is given by:",
        "type": "mcq",
        "options": ["u[n] + u[n-1] = δ[n]", "u[n] - u[n-1] = δ[n]", "δ[n] - δ[n-1] = u[n]", "u[n] * u[n-1] = δ[n]"],
        "ans": "u[n] - u[n-1] = δ[n]",
        "explain_correct": "طرح دالة الـ Step من النسخة المتأخرة منها بخطوة واحدة بيطير كل العينات ويسيب العينة اللي عند الصفر بس (الـ Impulse). ✅",
        "explain_wrong": "عملية الطرح (Difference) في الديسكريت تعادل عملية التفاضل في المتصل."
    },
    {
        "q": "How can the continuous-time unit step u(t) be obtained from the impulse function δ(t)?",
        "type": "mcq",
        "options": ["By differentiating δ(t)", "By multiplying δ(t) by t", "By integrating δ(t) from -∞ to t", "By shifting δ(t)"],
        "ans": "By integrating δ(t) from -∞ to t",
        "explain_correct": "تكامل الدلتا من سالب مالانهاية لحد الزمن t بيعطي دالة الـ Step. (المساحة بتتراكم وتبقى 1 لما نعدي الصفر). ✅",
        "explain_wrong": "التكامل يعطي Step، بينما التفاضل للـ Step يعطي Impulse."
    },
    {
        "q": "How can the discrete-time unit step u[n] be expressed using the impulse sequence δ[n]?",
        "type": "mcq",
        "options": ["Sum of δ[n-k] from k=0 to ∞", "Sum of δ[n-k] from k=-∞ to 0", "δ[n] + δ[n-1]", "Product of δ[n-k]"],
        "ans": "Sum of δ[n-k] from k=0 to ∞",
        "explain_correct": "دالة الـ Step الديسكريت هي مجموع عدد لانهائي من الـ Impulses المتشفتة جهة اليمين. ✅",
        "explain_wrong": "u[n] تبدأ من الصفر للمالانهاية، إذن التجميع من k=0 لـ ∞."
    },
    {
        "q": "Evaluate: t * δ(t) = ?",
        "type": "mcq",
        "options": ["t", "δ(t)", "1", "0"],
        "ans": "0",
        "explain_correct": "بما إن الدلتا لا تساوي صفر إلا عند t=0، هنعوض عن t بصفر. 0 * δ(0) = 0. ✅",
        "explain_wrong": "أي دالة مضروبة في دلتا بنعوض فيها بمكان الدلتا (وهو الصفر هنا)."
    },

    # ─── Part 2: Advanced Windowing & Operations (From Sheet 4) ───
    {
        "q": "The operation x[n-2] * ( u[n] - u[n-6] ) will keep the samples of the shifted signal only in the range:",
        "type": "mcq",
        "options": ["n = 0 to 6", "n = 0 to 5", "n = 2 to 6", "n = -2 to 4"],
        "ans": "n = 0 to 5",
        "explain_correct": "النافذة (u[n] - u[n-6]) بتبدأ من 0 وتنتهي عند 5 (لأن العينة 6 مطروحة). إذن ستحتفظ بالعينات من 0 لـ 5. ✅",
        "explain_wrong": "تذكر أن الطرح u[n-6] يزيل العينة رقم 6 وما بعدها."
    },
    {
        "q": "Evaluate the discrete-time operation from Sheet 4: -x[2n] * δ[3n]",
        "type": "mcq",
        "options": ["-x[6n] * δ[n]", "-x[2n] * δ[n]", "-x[0] * δ[n]", "0"],
        "ans": "-x[0] * δ[n]",
        "explain_correct": "أولاً δ[3n] هي نفسها δ[n] (موجودة عند الصفر فقط). هنعوض في الإشارة عن n=0، هتصفي على -x[0] * δ[n]. ✅",
        "explain_wrong": "الـ Delta بتصطاد القيمة عند n=0، إذن بنعوض عن أي n بـ صفر."
    },
    {
        "q": "The windowing operation x[-n] * u[-n-2] will keep the signal samples only for:",
        "type": "mcq",
        "options": ["n >= 2", "n <= 2", "n >= -2", "n <= -2"],
        "ans": "n <= -2",
        "explain_correct": "دالة الـ Step تعمل عندما يكون ما بداخلها >= 0. أي: -n - 2 >= 0، ومنها -n >= 2، إذن n <= -2. ✅",
        "explain_wrong": "حل المتباينة: اجعل ما بداخل القوس أكبر من أو يساوي الصفر."
    },
    {
        "q": "The expression u[n+1] - u[n-1] represents a discrete window that is non-zero ONLY at:",
        "type": "mcq",
        "options": ["n = -1, 0, 1", "n = -1, 0", "n = 0, 1", "n = 1, -1"],
        "ans": "n = -1, 0",
        "explain_correct": "تبدأ من -1 وتنتهي قبل الـ 1 (لأن u[n-1] بتطرح العينة 1 وما بعدها). إذن العينات المتبقية هي -1 و 0 فقط. ✅",
        "explain_wrong": "العينة عند 1 مطروحة، فلا تدخل في النافذة."
    },
    {
        "q": "Evaluate: x[n] * δ[n - 1] simplifies to:",
        "type": "mcq",
        "options": ["x[1] * δ[n-1]", "x[n-1]", "x[1]", "0"],
        "ans": "x[1] * δ[n-1]",
        "explain_correct": "الدلتا هنا متمركزة عند n=1. إذن بناخد قيمة الإشارة x عند 1 ونضربها في نفس الدلتا. ✅",
        "explain_wrong": "الدلتا لا تختفي، بل تظل موجودة مضروبة في الثابت x[1]."
    },

    # ─── Part 3: LTI Systems Basics (Chapter 2 / Lecture 4) ───
    {
        "q": "An LTI system stands for:",
        "type": "mcq",
        "options": ["Linear Time-Independent", "Linear Time-Invariant", "Logical Time-Invariant", "Linear Transformation Interface"],
        "ans": "Linear Time-Invariant",
        "explain_correct": "LTI تعني نظام خطي (Linear) وغير متغير مع الزمن (Time-Invariant). ✅",
        "explain_wrong": "Invariant تعني لا يتغير مع الزمن."
    },
    {
        "q": "The principle of Superposition, which defines a Linear system, consists of two properties:",
        "type": "mcq",
        "options": ["Causality and Stability", "Additivity and Homogeneity (Scaling)", "Time-invariance and Memory", "Integration and Differentiation"],
        "ans": "Additivity and Homogeneity (Scaling)",
        "explain_correct": "النظام الخطي لازم يحقق الجمع (Additivity) والضرب في ثابت (Homogeneity/Scaling). ✅",
        "explain_wrong": "Superposition = Additivity + Homogeneity."
    },
    {
        "q": "A system is defined as Time-Invariant if:",
        "type": "mcq",
        "options": ["The output is always constant over time", "A time delay in the input causes the exact same time delay in the output", "It has no memory", "The input is independent of time"],
        "ans": "A time delay in the input causes the exact same time delay in the output",
        "explain_correct": "النظام لا يتغير مع الزمن يعني: لو أخرت الدخول (Input) 5 ثواني، الخروج (Output) هيتأخر 5 ثواني بنفس الشكل بالظبط. ✅",
        "explain_wrong": "Time-invariance يعني النظام سلوكه ثابت مش بيتغير بمرور الوقت."
    },
    {
        "q": "Any Linear Time-Invariant (LTI) system is COMPLETELY characterized by its:",
        "type": "mcq",
        "options": ["Input signal", "Step response", "Impulse response h(t) or h[n]", "Initial conditions"],
        "ans": "Impulse response h(t) or h[n]",
        "explain_correct": "لو عرفت استجابة النظام للنبضة (Impulse response)، تقدر تعرف استجابته لأي إشارة تانية في الدنيا عن طريق الـ Convolution! ✅",
        "explain_wrong": "الـ Impulse response هو البصمة الوراثية لأي نظام LTI."
    },
    {
        "q": "For an LTI system, the output y(t) to any arbitrary input x(t) can be found using the mathematical operation called:",
        "type": "mcq",
        "options": ["Multiplication", "Addition", "Convolution", "Correlation"],
        "ans": "Convolution",
        "explain_correct": "بنحسب الخرج y(t) عن طريق عمل Convolution (التفاف) بين الدخل x(t) والـ Impulse response h(t). ✅",
        "explain_wrong": "الـ Convolution هو العملية الأساسية لحساب خرج أنظمة الـ LTI."
    },
    {
        "q": "The Convolution operation is commutative. This means:",
        "type": "mcq",
        "options": ["x(t) * h(t) = h(t) * x(t)", "x(t) * h(t) = x(-t) * h(-t)", "x(t) * h(t) = 1", "It only works for discrete signals"],
        "ans": "x(t) * h(t) = h(t) * x(t)",
        "explain_correct": "خاصية الإبدال (Commutative): مش بتفرق مين اللي بنعمله Shift ومين الثابت في التكامل. ✅",
        "explain_wrong": "Commutative تعني الإبدال، أي يمكن عكس ترتيب الدالتين."
    },

    # ─── Part 4: System Properties (Causality, Stability, Memory) ───
    {
        "q": "A system is considered CAUSAL if its output at any time depends ONLY on:",
        "type": "mcq",
        "options": ["Future inputs", "Present and past inputs", "Present and future inputs", "Past outputs only"],
        "ans": "Present and past inputs",
        "explain_correct": "النظام السببي (Causal) مستحيل يتنبأ بالمستقبل، الخرج بيعتمد على الدخل الحالي واللي فات بس. ✅",
        "explain_wrong": "Causal = No Future dependence."
    },
    {
        "q": "For an LTI system to be CAUSAL, its impulse response h(t) or h[n] must satisfy:",
        "type": "mcq",
        "options": ["h(t) = 0 for t < 0", "h(t) = 1 for t > 0", "h(t) = h(-t)", "h(t) = 0 for t > 0"],
        "ans": "h(t) = 0 for t < 0",
        "explain_correct": "عشان النظام يكون Causal، لازم ميكونش فيه أي استجابة قبل ما الدخل يدخل (أي قبل t=0). ✅",
        "explain_wrong": "Impulse response للأنظمة السببية يجب أن يكون صفراً في الزمن السالب."
    },
    {
        "q": "A system is defined as BIBO Stable if:",
        "type": "mcq",
        "options": ["Every input produces zero output", "Every bounded input produces a bounded output", "The system has no memory", "The impulse response is infinite"],
        "ans": "Every bounded input produces a bounded output",
        "explain_correct": "الاستقرار (Bounded-Input Bounded-Output) معناه إن لو الدخل ليه حدود، الخرج كمان لازم يكون ليه حدود ومينفجرش. ✅",
        "explain_wrong": "BIBO stands for Bounded-Input Bounded-Output."
    },
    {
        "q": "For a continuous-time LTI system to be BIBO STABLE, its impulse response h(t) must be:",
        "type": "mcq",
        "options": ["Absolutely integrable (∫|h(t)|dt < ∞)", "Zero everywhere", "Equal to 1", "Periodic"],
        "ans": "Absolutely integrable (∫|h(t)|dt < ∞)",
        "explain_correct": "شرط الاستقرار في الـ LTI إن المساحة تحت مقياس الـ Impulse response تكون محدودة (Absolutely integrable). ✅",
        "explain_wrong": "إذا كان التكامل يؤول للمالانهاية، النظام يكون غير مستقر."
    },
    {
        "q": "A system is called 'Memoryless' (or Static) if its output at time t depends ONLY on:",
        "type": "mcq",
        "options": ["The input at time t (present)", "The past inputs", "The future inputs", "The past outputs"],
        "ans": "The input at time t (present)",
        "explain_correct": "النظام اللي مفيهوش ذاكرة (Memoryless) الخرج بتاعه بيعتمد على الدخل في نفس اللحظة دي بس. ✅",
        "explain_wrong": "لو الخرج اعتمد على أي لحظة سابقة أو قادمة، يصبح النظام له ذاكرة (Dynamic)."
    },
    {
        "q": "For an LTI system to be MEMORYLESS, its impulse response h(t) must be of the form:",
        "type": "mcq",
        "options": ["h(t) = K * u(t)", "h(t) = K * δ(t)", "h(t) = 1", "h(t) = e^(-t)"],
        "ans": "h(t) = K * δ(t)",
        "explain_correct": "بما إنه بيعتمد على اللحظة الحالية بس، فالـ Impulse response لازم يكون نبضة (Delta) موجودة عند الصفر بس. ✅",
        "explain_wrong": "وجود أي قيمة لـ h(t) في أي زمن غير الصفر يعني وجود ذاكرة."
    },

    # ─── Part 5: Mixed Conceptual Questions ───
    {
        "q": "Is the system defined by y(t) = x(t) + 2 a LINEAR system?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. لو دخلت x(t)=0، الخرج هيكون 2 مش صفر! وده بيكسر شرط الخطية (الـ Zero-in Zero-out property). ✅",
        "explain_wrong": "جمع ثابت (DC offset) بيخلي النظام Non-linear لأنه مبيحققش الـ Additivity."
    },
    {
        "q": "Is the system defined by y(t) = t * x(t) a TIME-INVARIANT system?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. الـ t المضروبة بره دي بتخلي سلوك النظام يتغير باختلاف اللحظة الزمنية، إذن هو Time-Varying. ✅",
        "explain_wrong": "الضرب في t يجعل النظام يعتمد صراحة على الزمن، فهو يتغير مع الزمن."
    },
    {
        "q": "Is the ideal delay system y(t) = x(t - 5) Causal?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح. الخرج بيعتمد على قيمة x من 5 ثواني فاتت (Past input)، إذن هو سببي (Causal) جداً. ✅",
        "explain_wrong": "لو كان y(t) = x(t + 5) كان هيبقى غير سببي لأنه بيعتمد على المستقبل."
    },
    {
        "q": "Evaluate the property: The convolution of any signal x(t) with the impulse function δ(t) equals:",
        "type": "mcq",
        "options": ["δ(t)", "x(t)", "1", "0"],
        "ans": "x(t)",
        "explain_correct": "الدلتا في عملية الـ Convolution بتشتغل كـ (المحايد)، يعني بتنزل الإشارة زي ما هي بالظبط! ✅",
        "explain_wrong": "Convolution مع الدلتا لا يغير الإشارة."
    },
    {
        "q": "What is the convolution of x(t) with a shifted impulse δ(t - t0)?",
        "type": "mcq",
        "options": ["x(t)", "x(t0)", "x(t - t0)", "x(t) * δ(t - t0)"],
        "ans": "x(t - t0)",
        "explain_correct": "الـ Convolution مع دلتا متشفته بيعمل Shift للإشارة كلها بنفس المقدار. ✅",
        "explain_wrong": "تذكر الفرق: الضرب في دلتا يجلب قيمة، أما الـ Convolution مع دلتا يعمل Shift."
    },
    {
        "q": "True or False: An LTI system is Stable if the sum of the absolute values of its discrete impulse response is finite (Σ|h[n]| < ∞).",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح 100%. ده شرط الـ BIBO Stability للأنظمة الديسكريت (Absolute Summability). ✅",
        "explain_wrong": "مجموع الـ Impulse response يجب أن يكون محدوداً للاستقرار."
    },
    {
        "q": "Which of the following describes an accumulator system y[n] = Σ x[k] (from k=-∞ to n)?",
        "type": "mcq",
        "options": ["Memoryless", "Stable", "Causal and with memory", "Non-causal"],
        "ans": "Causal and with memory",
        "explain_correct": "النظام بيجمع القيم السابقة والحالية (Causal)، وطالما بيحتاج القيم السابقة إذن هو بيحتوي على ذاكرة (Memory). ✅",
        "explain_wrong": "التجميع (Accumulator) هو تعريف الذاكرة."
    },
    {
        "q": "Is the system y[n] = x[n+1] Causal?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. الخرج في اللحظة n بيحتاج قيمة الدخل في اللحظة n+1 (يعني في المستقبل)، إذن النظام غير سببي (Non-causal). ✅",
        "explain_wrong": "الاعتماد على المستقبل ينفي السببية."
    },
    {
        "q": "Determine the odd and even components of a signal x(n) if x(n) is purely ODD. What is x_e(n)?",
        "type": "mcq",
        "options": ["x(n)", "-x(-n)", "0", "1"],
        "ans": "0",
        "explain_correct": "لو الإشارة فردية بالكامل، مفيش فيها أي نسبة من التماثل الزوجي، إذن الجزء الزوجي بـ 0. ✅",
        "explain_wrong": "الإشارة الفردية الخالصة خالية من الجزء الزوجي."
    },
    {
        "q": "From Sheet 4: Find the odd component of x(n). The formula is:",
        "type": "mcq",
        "options": ["0.5 * [x(n) + x(-n)]", "0.5 * [x(n) - x(-n)]", "x(n) - x(-n)", "x(n) * x(-n)"],
        "ans": "0.5 * [x(n) - x(-n)]",
        "explain_correct": "الطرح بيجيب الجزء الفردي (Odd)، والجمع بيجيب الجزء الزوجي (Even). ✅",
        "explain_wrong": "لا تنسَ القسمة على 2 في القانون."
    },
    {
        "q": "If x[n] is non-zero only for n = 0 to 4, and h[n] is non-zero only for n = 0 to 3, the length of their convolution y[n] is:",
        "type": "mcq",
        "options": ["4", "7", "8", "12"],
        "ans": "8",
        "explain_correct": "طول الـ Convolution بيساوي طول الأولى + طول التانية - 1. (5 عينات + 4 عينات - 1 = 8 عينات). ✅",
        "explain_wrong": "Length of y = L1 + L2 - 1."
    },
    {
        "q": "If an LTI system has h(t) = e^(2t) u(t), is the system stable?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. الدالة الأسية دي (e^2t) بتزيد للمالانهاية مع الزمن الموجب (Growing exponential)، فمساحتها مالانهاية، إذن غير مستقر! ✅",
        "explain_wrong": "لكي يكون مستقراً، يجب أن يكون الأُس سالباً (Decaying) لتكون المساحة محدودة."
    },
    {
        "q": "Evaluate: du(t)/dt + u(t) for t < 0 equals:",
        "type": "mcq",
        "options": ["δ(t)", "1", "0", "Infinity"],
        "ans": "0",
        "explain_correct": "في الزمن السالب (t < 0)، دالة الـ Step u(t) بـ 0، وتفاضلها δ(t) بـ 0. إذن الناتج 0. ✅",
        "explain_wrong": "في الزمن السالب، الـ Step والدلتا كلاهما يساوي صفر."
    },
    {
        "q": "To express a discrete sequence that is 1 at n=2 and n=4, and 0 otherwise, using impulses:",
        "type": "mcq",
        "options": ["δ[n-2] * δ[n-4]", "δ[n+2] + δ[n+4]", "δ[n-2] + δ[n-4]", "u[n-2] + u[n-4]"],
        "ans": "δ[n-2] + δ[n-4]",
        "explain_correct": "النبضة عند 2 هي δ[n-2]، والنبضة عند 4 هي δ[n-4]، بنجمعهم عشان نبني الإشارة. ✅",
        "explain_wrong": "الإشارة السالبة داخل القوس تعني إزاحة لليمين (تأخير)."
    }
]