# ==========================================
# 📖 dsp_lec5_6.py
# Digital Signal Processing - Lecture 5 & 6 + Sec 5 & 6
# Convolution (Continuous & Discrete) and LTI Properties
# ==========================================

QUESTIONS = [
    # ─── Part 1: Convolution Basics (Continuous & Discrete) ───
    {
        "q": "For a Continuous-Time LTI system, the output y(t) is calculated using the Convolution Integral, which is defined as:",
        "type": "mcq",
        "options": ["∫ x(τ) h(t-τ) dτ", "∫ x(t) h(τ-t) dτ", "∫ x(τ) h(τ) dτ", "∫ x(t-τ) h(t-τ) dτ"],
        "ans": "∫ x(τ) h(t-τ) dτ",
        "explain_correct": "الـ Convolution Integral بيكامل حاصل ضرب الإشارة x(τ) في الـ Impulse response بعد ما نعكسه ونعمله إزاحة h(t-τ). ✅",
        "explain_wrong": "تذكر: المتغير اللي بنكامل بالنسبة ليه هو τ، والـ t بيُعتبر ثابت (Shift) جوه التكامل."
    },
    {
        "q": "For a Discrete-Time LTI system, the output y[n] is calculated using the Convolution Sum, which is defined as:",
        "type": "mcq",
        "options": ["Σ x[k] h[n+k]", "Σ x[k] h[n-k]", "Σ x[n] h[n-k]", "Σ x[n-k] h[k-n]"],
        "ans": "Σ x[k] h[n-k]",
        "explain_correct": "الـ Convolution Sum بيجمع حاصل ضرب العينات x[k] في الـ Impulse response المعكوس والمُزاح h[n-k]. ✅",
        "explain_wrong": "في الديسكريت، بنستخدم عداد k بدل τ، وبنعكس الدالة التانية لـ h[n-k]."
    },
    {
        "q": "The Convolution operation is COMMUTATIVE. This means:",
        "type": "mcq",
        "options": ["x(t) * h(t) = 1", "x(t) * h(t) = x(-t) * h(-t)", "x(t) * h(t) = h(t) * x(t)", "x[n] * h[n] = 0"],
        "ans": "x(t) * h(t) = h(t) * x(t)",
        "explain_correct": "خاصية الإبدال (Commutative) بتسمحلك تعكس الدالتين، يعني تقدر تخلي x هي اللي تتعكس وتتشفت h(τ)x(t-τ). ✅",
        "explain_wrong": "الترتيب في الـ Convolution مش بيفرق في النتيجة النهائية."
    },
    {
        "q": "When performing graphical convolution, the step where we change h(τ) to h(-τ) is called:",
        "type": "mcq",
        "options": ["Shifting", "Multiplication", "Folding (Reversal)", "Integration"],
        "ans": "Folding (Reversal)",
        "explain_correct": "أول خطوة في الرسم هي الـ Folding (أو Reversal) عشان نعكس الإشارة حول محور الصادات. ✅",
        "explain_wrong": "عملية ضرب الزمن في سالب تُسمى Folding أو Time Reversal."
    },
    {
        "q": "In the convolution integral ∫ x(τ) h(t-τ) dτ, the variable 't' represents:",
        "type": "mcq",
        "options": ["The integration variable", "The amount of Shift applied to the folded signal", "A scaling factor", "The amplitude"],
        "ans": "The amount of Shift applied to the folded signal",
        "explain_correct": "في التكامل ده، τ هو المتغير اللي بنكامل عليه، أما t فبيحدد إحنا حركنا (Shift) الإشارة المعكوسة يمين ولا شمال بقد إيه. ✅",
        "explain_wrong": "الـ t هو الزمن اللي بنحسب عنده الخرج، وبيظهر كـ Shift للإشارة المعكوسة."
    },
    {
        "q": "If x[n] has a length of L1 samples, and h[n] has a length of L2 samples, what is the length of the resulting convolution y[n]?",
        "type": "mcq",
        "options": ["L1 + L2", "L1 * L2", "L1 + L2 - 1", "max(L1, L2)"],
        "ans": "L1 + L2 - 1",
        "explain_correct": "قاعدة ذهبية في الديسكريت: طول إشارة الخرج بيساوي مجموع طول الإشارتين ناقص 1. ✅",
        "explain_wrong": "Length = L1 + L2 - 1."
    },
    {
        "q": "If signal x[n] starts at index N1, and signal h[n] starts at index N2, at what index will the convolution y[n] start?",
        "type": "mcq",
        "options": ["N1 - N2", "N1 + N2", "min(N1, N2)", "0"],
        "ans": "N1 + N2",
        "explain_correct": "بداية إشارة الخرج هي مجموع بدايات الإشارتين المضروبين في بعض. ✅",
        "explain_wrong": "Start of y = Start of x + Start of h."
    },

    # ─── Part 2: System Interconnections ───
    {
        "q": "If two LTI systems with impulse responses h1(t) and h2(t) are connected in CASCADE (series), the overall equivalent impulse response h(t) is:",
        "type": "mcq",
        "options": ["h1(t) + h2(t)", "h1(t) * h2(t) (Convolution)", "h1(t) x h2(t) (Multiplication)", "h1(t) / h2(t)"],
        "ans": "h1(t) * h2(t) (Convolution)",
        "explain_correct": "الأنظمة المتوصلة على التوالي (Cascade) بنعمل ليهم Convolution مع بعض عشان نجيب النظام المكافئ. ✅",
        "explain_wrong": "Cascade = Convolution (ليس ضرب عادي ولا جمع)."
    },
    {
        "q": "If two LTI systems with impulse responses h1(t) and h2(t) are connected in PARALLEL, the overall equivalent impulse response h(t) is:",
        "type": "mcq",
        "options": ["h1(t) * h2(t) (Convolution)", "h1(t) + h2(t)", "h1(t) - h2(t)", "h1(t) x h2(t) (Multiplication)"],
        "ans": "h1(t) + h2(t)",
        "explain_correct": "الأنظمة المتوصلة على التوازي (Parallel) بنجمع الـ Impulse responses بتاعتهم بكل بساطة (Additivity). ✅",
        "explain_wrong": "Parallel = Addition (جمع)."
    },

    # ─── Part 3: Step Response & LTI Properties ───
    {
        "q": "The Step Response s(t) of an LTI system is defined as the output when the input is:",
        "type": "mcq",
        "options": ["δ(t)", "u(t)", "r(t)", "e^t"],
        "ans": "u(t)",
        "explain_correct": "الـ Step response (s) هو استجابة النظام لما ندخله دالة الـ Step (u) كـ Input. ✅",
        "explain_wrong": "الـ Impulse response لما الدخل δ(t)، والـ Step response لما الدخل u(t)."
    },
    {
        "q": "What is the mathematical relationship between the Impulse Response h(t) and the Step Response s(t) of an LTI system?",
        "type": "mcq",
        "options": ["h(t) = ∫ s(t) dt", "h(t) = s(t) * u(t)", "h(t) = d/dt [s(t)]", "h(t) = s(t-1)"],
        "ans": "h(t) = d/dt [s(t)]",
        "explain_correct": "بما إن الدلتا هي تفاضل الـ Step، إذن الـ Impulse response هو تفاضل الـ Step response! ✅",
        "explain_wrong": "التفاضل بيحول الـ Step لـ Impulse، وبالتالي بيحول الـ s(t) لـ h(t)."
    },
    {
        "q": "How can the Step Response s[n] be calculated from the discrete Impulse Response h[n]?",
        "type": "mcq",
        "options": ["s[n] = h[n] - h[n-1]", "s[n] = Σ h[k] (from k=-∞ to n)", "s[n] = h[n] * u[n]", "s[n] = d/dn h[n]"],
        "ans": "s[n] = Σ h[k] (from k=-∞ to n)",
        "explain_correct": "في الديسكريت، التكامل بيتحول لـ Summation (تجميع). بنجمع الـ h[k] من سالب مالانهاية لحد اللحظة الحالية n. ✅",
        "explain_wrong": "الـ Step response هو مجموع قيم الـ Impulse response السابقة والحالية."
    },
    {
        "q": "An LTI system is MEMORYLESS if and only if its impulse response h(t) is of the form:",
        "type": "mcq",
        "options": ["K * u(t)", "K * e^(-t)", "K * δ(t)", "0"],
        "ans": "K * δ(t)",
        "explain_correct": "النظام اللي مفيهوش ذاكرة (Memoryless) بيعتمد على اللحظة الحالية بس، فلازم الـ h(t) تكون Impulse عند الصفر بس. ✅",
        "explain_wrong": "لو الـ h(t) ليها قيمة في أي وقت غير الصفر، يبقى النظام ليه ذاكرة."
    },
    {
        "q": "An LTI system is CAUSAL if and only if its impulse response h(t) or h[n] satisfies:",
        "type": "mcq",
        "options": ["h(t) = 0 for t > 0", "h(t) = 0 for t < 0", "h(t) = 1 for all t", "h(t) = h(-t)"],
        "ans": "h(t) = 0 for t < 0",
        "explain_correct": "النظام السببي (Causal) مستحيل يتفاعل أو يطلع خرج قبل ما ندخله إشارة، فـ h(t) لازم تكون صفر في الزمن السالب. ✅",
        "explain_wrong": "السببية تعني أن h(t) = 0 لكل t < 0."
    },
    {
        "q": "An LTI system is BIBO STABLE if its impulse response satisfies:",
        "type": "mcq",
        "options": ["∫|h(t)|dt = 0", "∫|h(t)|dt < ∞ (Absolutely Integrable)", "h(t) is periodic", "h(t) approaches infinity"],
        "ans": "∫|h(t)|dt < ∞ (Absolutely Integrable)",
        "explain_correct": "شرط الاستقرار إن المساحة الكلية تحت القيمة المطلقة للـ impulse response تكون محدودة (مش مالانهاية). ✅",
        "explain_wrong": "الاستقرار يتطلب Absolute Integrability."
    },

    # ─── Part 4: Evaluating Examples from Lecture 5 & 6 ───
    {
        "q": "From Lecture 5-6: A system is described by y(t) = (1/8) * ∫ x(τ) dτ from (t-4) to (t+4). What is its impulse response h(t)?",
        "type": "mcq",
        "options": ["1/8 [u(t+4) - u(t-4)]", "1/8 u(t)", "1/8 δ(t-4)", "[u(t-4) + u(t+4)]"],
        "ans": "1/8 [u(t+4) - u(t-4)]",
        "explain_correct": "بما إن التكامل من t-4 لـ t+4، فالنافذة (Window) اللي بتحدد الدالة هي نبضة مستطيلة بتبدأ من -4 لتنتهي عند 4، مضروبة في 1/8. ✅",
        "explain_wrong": "الدالة عبارة عن مستطيل (Pulse) باستخدام الـ Step functions."
    },
    {
        "q": "For the system where h(t) = 1/8 [u(t+4) - u(t-4)], is this system CAUSAL?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. الإشارة h(t) موجودة في الفترة من -4 لـ 4. بما إنها ليها قيمة في الزمن السالب (-4 لـ 0)، إذن النظام Non-Causal! ✅",
        "explain_wrong": "النظام يعتمد على إشارة في الزمن السالب (أي يتنبأ بالمستقبل t+4)."
    },
    {
        "q": "For the system where h(t) = 1/8 [u(t+4) - u(t-4)], is this system STABLE?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح. لو كالملنا |h(t)| من -4 لـ 4، المساحة هتطلع (8 * 1/8) = 1. بما إن 1 < ∞، إذن النظام Stable. ✅",
        "explain_wrong": "المساحة المحدودة = استقرار."
    },
    {
        "q": "Is the system h(t) = 1/8 [u(t+4) - u(t-4)] MEMORYLESS?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. الـ Memoryless لازم يكون Impulse عند الصفر بس. هنا الـ h(t) ممتدة من -4 لـ 4، فدي ذاكرة كبيرة! ✅",
        "explain_wrong": "الاعتماد على فترات زمنية سابقة أو قادمة يعني وجود ذاكرة (Dynamic)."
    },
    {
        "q": "From Sec 5&6: Given h(t) = e^(-αt) u(t) and x(t) = e^(αt) u(-t) where α>0. For t > 0, what is the output y(t)?",
        "type": "mcq",
        "options": ["e^(αt) / 2α", "e^(-αt) / 2α", "0", "1"],
        "ans": "e^(-αt) / 2α",
        "explain_correct": "بالتكامل من -∞ لحد الصفر (لأن u(-τ) بتحدنا بالصفر)، الخرج في الزمن الموجب بيطلع المعادلة اللي فيها e^(-αt). ✅",
        "explain_wrong": "راجع خطوات التكامل في السكشن، للزمن t>0 الإشارة تضمحل."
    },
    {
        "q": "For the same signals, h(t) = e^(-αt) u(t) and x(t) = e^(αt) u(-t). For t < 0, what is the output y(t)?",
        "type": "mcq",
        "options": ["e^(αt) / 2α", "e^(-αt) / 2α", "0", "1"],
        "ans": "e^(αt) / 2α",
        "explain_correct": "في الزمن السالب t<0، حدود التكامل بتكون من -∞ لحد t، فالنتيجة بتطلع e^(αt)/2α. ✅",
        "explain_wrong": "في الزمن السالب، الإشارة تتزايد مع t."
    },
    {
        "q": "From Lec 5-6: Evaluate the discrete convolution y[n] = u[n] * u[n]. The result is:",
        "type": "mcq",
        "options": ["u[n]", "(n+1) u[n]", "n u[n]", "δ[n]"],
        "ans": "(n+1) u[n]",
        "explain_correct": "تجميع وحايد من k=0 لـ n بيدي (n+1). يعني الخرج عبارة عن Ramp ديسكريت. ✅",
        "explain_wrong": "Convolution for two step sequences gives a ramp sequence (n+1)u[n]."
    },
    {
        "q": "From Lec 5-6: If h[n] = a^n u[n] and x[n] = u[n], the output y[n] is computed using the geometric series sum Σ a^k (from k=0 to n). What is the formula for this sum?",
        "type": "mcq",
        "options": ["1 / (1-a)", "(1 - a^(n+1)) / (1 - a)", "a^n / (1-a)", "(1 - a^n) / (1 - a)"],
        "ans": "(1 - a^(n+1)) / (1 - a)",
        "explain_correct": "قانون المجموع للمتسلسلة الهندسية المحدودة (من 0 لـ n) هو: (1 - الأساس أس عدد الحدود) / (1 - الأساس). وعدد الحدود هو n+1. ✅",
        "explain_wrong": "عدد الحدود من 0 إلى n هو (n+1)، مش n."
    },
    {
        "q": "Is the discrete system with impulse response h[n] = (1/2)^n u[n] STABLE?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح. مجموع المطلق Σ (1/2)^n من 0 لـ ∞ بيساوي 1 / (1 - 0.5) = 2. بما إن 2 < ∞، النظام مستقر. ✅",
        "explain_wrong": "الأس (1/2) أقل من 1، فالمتسلسلة تقاربية ومجموعها محدود."
    },
    {
        "q": "Consider h[n] = δ[n] + (1/2)δ[n-1]. Is this system MEMORYLESS?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. وجود δ[n-1] يعني إن النظام بيحتاج العينة السابقة (Shifted)، وبالتالي هو Dynamic وليه ذاكرة. ✅",
        "explain_wrong": "Memoryless يتطلب δ[n] فقط بدون أي Shifts."
    },
    {
        "q": "Consider h[n] = δ[n] + (1/2)δ[n-1]. Is this system CAUSAL?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح. النظام بيعتمد على n=0 و n=1 (يعني الحاضر والماضي)، ومفيش فيه أي عينات سالبة في الـ h[n]، فهو Causal. ✅",
        "explain_wrong": "الـ Impulse response صفر للقيم السالبة (n<0)."
    },

    # ─── Part 5: Convolution Edge Cases & Operations ───
    {
        "q": "What is the convolution of any signal x(t) with the unit impulse δ(t)?",
        "type": "mcq",
        "options": ["1", "0", "x(t)", "δ(t)"],
        "ans": "x(t)",
        "explain_correct": "الدلتا في الـ Convolution هي العنصر المحايد (زي الواحد في الضرب). الإشارة بتنزل زي ما هي. ✅",
        "explain_wrong": "Convolution مع الدلتا لا يغير الإشارة."
    },
    {
        "q": "What is the convolution of a signal x(t) with a shifted impulse δ(t - 5)?",
        "type": "mcq",
        "options": ["x(5)", "x(t - 5)", "x(t) * δ(t - 5)", "x(t) + 5"],
        "ans": "x(t - 5)",
        "explain_correct": "الالتفاف مع دلتا متشفته بيعمل إزاحة (Shift) للإشارة الأصلية بنفس المقدار. ✅",
        "explain_wrong": "التفاف الدلتا يعمل Shift، أما الضرب في دلتا يجلب قيمة الإشارة."
    },
    {
        "q": "Evaluate the convolution of the unit step with itself: y(t) = u(t) * u(t). The result is:",
        "type": "mcq",
        "options": ["u(t)", "δ(t)", "t * u(t)", "1"],
        "ans": "t * u(t)",
        "explain_correct": "تكامل u(τ) من 0 لـ t بيدي t للقيم t>0. وده تعريف دالة الـ Ramp function r(t) = t u(t). ✅",
        "explain_wrong": "Convolution of two steps gives a Ramp."
    },
    {
        "q": "If x[n] = {1, 2} starting at n=0, and h[n] = {3, 4} starting at n=0. Using the sum method, what is y[0]?",
        "type": "mcq",
        "options": ["1", "3", "4", "7"],
        "ans": "3",
        "explain_correct": "y[0] = x[0]h[0] = 1 * 3 = 3. بقية العينات بتكون مضروبة في أصفار. ✅",
        "explain_wrong": "أول عينة في الـ Convolution هي حاصل ضرب أول عينتين."
    },
    {
        "q": "For the same sequences, x[n] = {1, 2} and h[n] = {3, 4}. What is y[1]?",
        "type": "mcq",
        "options": ["6", "4", "10", "8"],
        "ans": "10",
        "explain_correct": "y[1] = x[0]h[1] + x[1]h[0] = (1*4) + (2*3) = 4 + 6 = 10. ✅",
        "explain_wrong": "الخلايا القطرية في جدول الـ Convolution بتتجمع."
    },
    {
        "q": "For the same sequences, x[n] = {1, 2} and h[n] = {3, 4}. What is y[2]?",
        "type": "mcq",
        "options": ["4", "6", "8", "2"],
        "ans": "8",
        "explain_correct": "y[2] = x[1]h[1] = 2 * 4 = 8. وبما إن طول كل واحدة 2، الخرج طوله (2+2-1) = 3 عينات (y[0], y[1], y[2]). ✅",
        "explain_wrong": "آخر عينة هي ضرب آخر عينتين مع بعض."
    },
    {
        "q": "Is the system with h(t) = u(t+1) CAUSAL?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. الدالة دي بتبدأ من t = -1 (في الزمن السالب)، وبالتالي النظام بيستجيب قبل ما تدخله إشارة، فده غير سببي! ✅",
        "explain_wrong": "أي قيمة قبل الصفر تكسر السببية."
    },
    {
        "q": "Is the system with h(t) = u(t) STABLE?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. مساحة الـ Step function ممتدة للمالانهاية ∫(1)dt = ∞، فده نظام Unstable لأن أي دخل مستمر هيخلي الخرج ينفجر. ✅",
        "explain_wrong": "الاستقرار يحتاج مساحة محدودة (Absolute Integrable)."
    },
    {
        "q": "Discrete convolution distributes over addition: x[n] * (h1[n] + h2[n]) = (x[n] * h1[n]) + (x[n] * h2[n]).",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح 100%. دي خاصية التوزيع (Distributive property) واللي بنستخدمها لما يكون عندنا نظامين متوصلين توازي (Parallel). ✅",
        "explain_wrong": "الـ Convolution يوزع على الجمع بشكل طبيعي."
    }
]