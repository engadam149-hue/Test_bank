# ==========================================
# 📖 dsp_lec1.py
# Digital Signal Processing - Lecture 1
# 40 Unique Concepts from Hand Notes & Slides
# ==========================================

QUESTIONS = [
    {
        "q": "A signal is mathematically represented as a function of one or more...",
        "type": "mcq",
        "options": ["Independent variables", "Dependent variables", "Constant parameters", "Frequencies"],
        "ans": "Independent variables",
        "explain_correct": "الإشارة تُمثل رياضياً كدالة في متغير مستقل واحد (زي الزمن t) أو أكتر. ✅",
        "explain_wrong": "تذكر: الزمن t أو n هو المتغير المستقل (Independent variable)."
    },
    {
        "q": "If the independent variable 't' can take any real value, the signal is classified as...",
        "type": "mcq",
        "options": ["Discrete-time signal", "Continuous-time signal", "Digital signal", "Quantized signal"],
        "ans": "Continuous-time signal",
        "explain_correct": "بما إن الزمن t متصل (Continuous)، فالإشارة كلها Continuous-time. ✅",
        "explain_wrong": "الإشارة بتكون Discrete لو كانت متعرفة عند نقط زمنية محددة فقط."
    },
    {
        "q": "Discrete-time signals are defined only at discrete times and are identified as a sequence of numbers. The independent variable 'n' must be...",
        "type": "mcq",
        "options": ["Any real number", "A fraction", "An integer", "A complex number"],
        "ans": "An integer",
        "explain_correct": "في الـ Discrete signals، المتغير n بيمثل رقم العينة (Sample index) ولازم يكون رقم صحيح (Integer). ✅",
        "explain_wrong": "مفيش حاجة اسمها العينة رقم 1.5، لازم n يكون رقم صحيح."
    },
    {
        "q": "The process of converting a continuous-time signal x(t) into a discrete-time signal x[n] is called...",
        "type": "mcq",
        "options": ["Aliasing", "Sampling", "Reversal", "Scaling"],
        "ans": "Sampling",
        "explain_correct": "عملية أخذ عينات من الإشارة المتصلة لتحويلها لـ Discrete تسمى الـ Sampling. ✅",
        "explain_wrong": "الـ Sampling هو عملية التقطيع الزمني للحصول على عينات."
    },
    {
        "q": "During uniform sampling, the relationship between continuous time 't', discrete index 'n', and the sampling interval 'Ts' is given by...",
        "type": "mcq",
        "options": ["t = n + Ts", "t = n / Ts", "t = n * Ts", "n = t * Ts"],
        "ans": "t = n * Ts",
        "explain_correct": "الزمن الكلي t بيساوي رقم العينة n مضروب في زمن العينة الواحدة Ts. ✅",
        "explain_wrong": "القاعدة الأساسية للتحويل: بنعوض عن كل t بـ nTs."
    },
    {
        "q": "If a signal is sampled with a sampling interval (Ts) of 0.25 seconds, what is the sampling frequency (fs)?",
        "type": "mcq",
        "options": ["0.25 Hz", "4 Hz", "2 Hz", "1 Hz"],
        "ans": "4 Hz",
        "explain_correct": "التردد هو مقلوب الزمن: fs = 1/Ts = 1/0.25 = 4 Hz. ✅",
        "explain_wrong": "استخدم القانون: fs = 1 / Ts."
    },
    {
        "q": "For an operation y(t) = x(t - T) where T is a POSITIVE real number, the signal x(t) is...",
        "type": "mcq",
        "options": ["Advanced in time", "Delayed in time", "Compressed in time", "Expanded in time"],
        "ans": "Delayed in time",
        "explain_correct": "طرح قيمة موجبة من الزمن (t - T) معناه إن الإشارة اتأخرت (Delayed). ✅",
        "explain_wrong": "إشارة السالب (t - T) بتعني تأخير أو إزاحة لليمين."
    },
    {
        "q": "Graphically, advancing a signal y(t) = x(t + 2) means the original signal x(t) will shift to the...",
        "type": "mcq",
        "options": ["Right by 2 units", "Left by 2 units", "Up by 2 units", "Down by 2 units"],
        "ans": "Left by 2 units",
        "explain_correct": "الـ Advance (t + 2) بيحرك الإشارة لليسار على محور الزمن. ✅",
        "explain_wrong": "الموجب (Advance) بيحرك لليسار، والسالب (Delay) بيحرك لليمين."
    },
    {
        "q": "The mathematical operation y[n] = x[-n] represents which of the following?",
        "type": "mcq",
        "options": ["Time Scaling", "Time Shifting", "Time Reversal", "Amplitude Reversal"],
        "ans": "Time Reversal",
        "explain_correct": "ضرب الزمن في سالب بيعمل انعكاس زمني (Time Reversal). ✅",
        "explain_wrong": "عكس الإشارة الزمنية هو Time Reversal."
    },
    {
        "q": "Visually, time reversal x(-t) is equivalent to mirroring the signal across the...",
        "type": "mcq",
        "options": ["Horizontal axis (t-axis)", "Vertical axis (y-axis)", "Origin", "Line y = t"],
        "ans": "Vertical axis (y-axis)",
        "explain_correct": "عكس الزمن بيخلي اليمين شمال والشمال يمين، يعني Mirroring حول محور الصادات (y-axis). ✅",
        "explain_wrong": "الـ Time reversal بيعكس حول المحور الرأسي."
    },
    {
        "q": "Time scaling is given by y(t) = x(αt). If α > 1 (e.g., α = 2), the signal is...",
        "type": "mcq",
        "options": ["Expanded in time", "Compressed in time", "Delayed in time", "Reversed in time"],
        "ans": "Compressed in time",
        "explain_correct": "لما بنضرب الزمن في رقم أكبر من 1، الإشارة بتنضغط وتسرع (Compressed). ✅",
        "explain_wrong": "الضرب في رقم كبير بيسرع الإشارة يعني بيضغطها."
    },
    {
        "q": "Playing a tape recording at a slower speed than the nominal speed is an analogy for which operation?",
        "type": "mcq",
        "options": ["Time Compression (α > 1)", "Time Expansion (0 < α < 1)", "Time Reversal (α < 0)", "Time Shifting"],
        "ans": "Time Expansion (0 < α < 1)",
        "explain_correct": "التبطيء معناه إن الإشارة بتاخد وقت أطول، وده Expansion بيحصل لما تكون α كسر بين 0 و 1. ✅",
        "explain_wrong": "تبطئ السرعة = تمدد زمني (Expansion)."
    },
    {
        "q": "Which operation modifies the amplitude of the signal rather than its timing?",
        "type": "mcq",
        "options": ["x(2t)", "x(t-2)", "2x(t)", "x(-t)"],
        "ans": "2x(t)",
        "explain_correct": "الرقم 2 المضروب برا الدالة بيغير الـ Amplitude، الباقي كله بيغير في الـ Time. ✅",
        "explain_wrong": "التغيير برا الدالة بيأثر على الـ Y-axis (Amplitude)."
    },
    {
        "q": "A continuous-time signal is defined as an 'Even Signal' if it satisfies the condition...",
        "type": "mcq",
        "options": ["x(t) = -x(t)", "x(t) = -x(-t)", "x(t) = x(-t)", "x(-t) = -x(t)"],
        "ans": "x(t) = x(-t)",
        "explain_correct": "الإشارة الزوجية (Even) بتكون متماثلة تماماً لو عكسنا الزمن: x(t) = x(-t). ✅",
        "explain_wrong": "تذكر الـ Even function لا تتأثر بعكس إشارة الزمن."
    },
    {
        "q": "A discrete-time signal is defined as an 'Odd Signal' if it satisfies...",
        "type": "mcq",
        "options": ["x[n] = x[-n]", "x[n] = -x[-n]", "x[-n] = x[n]", "x[n] = x[n-1]"],
        "ans": "x[n] = -x[-n]",
        "explain_correct": "الإشارة الفردية (Odd) بتعكس قيمتها لما بنعكس الزمن: x[n] = -x[-n]. ✅",
        "explain_wrong": "الإشارة الفردية تتغير إشارتها بالكامل عند عكس الزمن."
    },
    {
        "q": "The standard cosine function, x(t) = cos(πt), is a classic example of...",
        "type": "mcq",
        "options": ["An Odd Signal", "An Even Signal", "A Random Signal", "Neither even nor odd"],
        "ans": "An Even Signal",
        "explain_correct": "دالة الجتا (Cos) بتبتلع الإشارة السالبة cos(-t) = cos(t)، لذلك هي Even. ✅",
        "explain_wrong": "Cos هي دائماً Even، بينما Sin هي Odd."
    },
    {
        "q": "The sine function, x(n) = sin(4n), is an example of...",
        "type": "mcq",
        "options": ["An Even Signal", "An Odd Signal", "A strictly positive signal", "A delayed signal"],
        "ans": "An Odd Signal",
        "explain_correct": "دالة الجا (Sin) بتطرد الإشارة السالبة sin(-n) = -sin(n)، لذلك هي Odd. ✅",
        "explain_wrong": "دالة الساين دايماً فردية (Odd)."
    },
    {
        "q": "Any arbitrary signal x(t) can always be expressed as the sum of...",
        "type": "mcq",
        "options": ["Two even signals", "Two odd signals", "An even component and an odd component", "A continuous and a discrete signal"],
        "ans": "An even component and an odd component",
        "explain_correct": "قاعدة أساسية: أي إشارة في الدنيا هي مجموع جزئين (Even + Odd). ✅",
        "explain_wrong": "x(t) = Xe(t) + Xo(t) دائماً وأبداً."
    },
    {
        "q": "What is the mathematical formula used to extract the EVEN component x_e(t) of a signal?",
        "type": "mcq",
        "options": ["0.5 * [x(t) - x(-t)]", "0.5 * [x(t) + x(-t)]", "x(t) + x(-t)", "x(t) - x(-t)"],
        "ans": "0.5 * [x(t) + x(-t)]",
        "explain_correct": "الجزء الزوجي هو متوسط الإشارة مع معكوسها الزمني (المجموع على 2). ✅",
        "explain_wrong": "استخدم الجمع للـ Even، والطرح للـ Odd."
    },
    {
        "q": "What is the mathematical formula to extract the ODD component x_o(t) of a signal?",
        "type": "mcq",
        "options": ["0.5 * [x(t) + x(-t)]", "x(t) - x(-t)", "0.5 * [x(t) - x(-t)]", "0.5 * [x(-t) - x(t)]"],
        "ans": "0.5 * [x(t) - x(-t)]",
        "explain_correct": "الجزء الفردي بييجي من طرح المعكوس الزمني من الإشارة الأصلية مقسوم على 2. ✅",
        "explain_wrong": "ركز في الإشارة: الطرح بيجيب الجزء الفردي (Odd)."
    },
    {
        "q": "For any purely ODD continuous-time signal x(t), what MUST be its value at the origin (t = 0)?",
        "type": "mcq",
        "options": ["Infinity", "1", "0", "Depends on the signal"],
        "ans": "0",
        "explain_correct": "بما إن x(0) = -x(-0)، إذن 2x(0) = 0، وبالتالي لازم x(0) = 0 في أي إشارة Odd. ✅",
        "explain_wrong": "الإشارة الفردية المتصلة لازم تمر بنقطة الأصل (0,0)."
    },
    {
        "q": "If x(t) = 4*e^(-0.5t), and x(-t) = 4*e^(0.5t), this signal is classified as...",
        "type": "mcq",
        "options": ["Even only", "Odd only", "Neither even nor odd", "Both even and odd"],
        "ans": "Neither even nor odd",
        "explain_correct": "الإشارة مش متساوية مع معكوسها ولا مع سالب معكوسها، يبقى لا Even ولا Odd. ✅",
        "explain_wrong": "دالة الـ Exponential العادية بتكون Neither."
    },
    {
        "q": "If a signal is already perfectly EVEN, applying Time Reversal x(-t) to it will result in...",
        "type": "mcq",
        "options": ["The inverted signal -x(t)", "Zero", "The exact same signal x(t)", "A delayed signal"],
        "ans": "The exact same signal x(t)",
        "explain_correct": "دي خاصية الإشارة الزوجية أساساً، عكس الزمن مبيغيرش فيها حاجة. ✅",
        "explain_wrong": "الـ Even متماثل، فلو عكسته هيفضل زي ما هو."
    },
    {
        "q": "If you apply Time Reversal to a perfectly ODD signal, the result is equivalent to...",
        "type": "mcq",
        "options": ["Amplitude Reversal -x(t)", "The same signal x(t)", "Zero", "Time scaling"],
        "ans": "Amplitude Reversal -x(t)",
        "explain_correct": "لأن x(-t) = -x(t) في الإشارة الفردية، فعكس الزمن كأنك ضربت الـ Amplitude في سالب. ✅",
        "explain_wrong": "في الـ Odd، عكس الزمن يعادل عكس القيمة."
    },
    {
        "q": "In the expression y[n] = x[-n + 2], what two transformations are applied to x[n]?",
        "type": "mcq",
        "options": ["Time shifting and Time scaling", "Time reversal and Time shifting", "Amplitude scaling and Time reversal", "Sampling and Time shifting"],
        "ans": "Time reversal and Time shifting",
        "explain_correct": "السالب بيعمل Reversal، والموجب 2 بيعمل Shifting. ✅",
        "explain_wrong": "مفيش ضرب في رقم لـ n، يبقى مفيش Scaling."
    },
    {
        "q": "The operation y[n] = x[2n] on a discrete signal results in keeping only the EVEN-indexed samples. This is a form of...",
        "type": "mcq",
        "options": ["Time Expansion", "Decimation (Compression)", "Time Delay", "Aliasing"],
        "ans": "Decimation (Compression)",
        "explain_correct": "ضرب الـ n في 2 بيخلينا ناخد عينة ونسيب عينة، فكده الإشارة بتنضغط (Compression/Decimation). ✅",
        "explain_wrong": "في الـ Discrete، الـ x[2n] بيقلل عدد العينات فبيضغطها."
    },
    {
        "q": "If you sample a continuous signal x(t) with a sampling interval Ts = 1.0 sec, the resulting discrete signal x[n] is exactly...",
        "type": "mcq",
        "options": ["x(0.5n)", "x(2n)", "x(n)", "x(1/n)"],
        "ans": "x(n)",
        "explain_correct": "بالتعويض في t = n*Ts، ولأن Ts = 1، إذن t = n مباشر. ✅",
        "explain_wrong": "عوض بـ Ts = 1 في القانون t = n*Ts."
    },
    {
        "q": "A continuous signal x(t) is sampled at Ts = 0.5 sec. The discrete sample x[4] corresponds to what time 't' in the original signal?",
        "type": "mcq",
        "options": ["t = 0.5 sec", "t = 2.0 sec", "t = 4.0 sec", "t = 8.0 sec"],
        "ans": "t = 2.0 sec",
        "explain_correct": "باستخدام القانون t = n * Ts -> إذن t = 4 * 0.5 = 2.0 ثانية. ✅",
        "explain_wrong": "اضرب رقم العينة n في زمن العينة Ts."
    },
    {
        "q": "To sketch the signal y[n] = -x[-n], you must mirror the signal horizontally (time) and then...",
        "type": "mcq",
        "options": ["Shift it right", "Mirror it vertically (amplitude)", "Expand it", "Add 1 to all values"],
        "ans": "Mirror it vertically (amplitude)",
        "explain_correct": "السالب اللي جوه بيعمل Time reversal، والسالب اللي بره بيعمل Amplitude reversal (انعكاس رأسي). ✅",
        "explain_wrong": "السالب الخارجي بيعكس الإشارة على محور Y."
    },
    {
        "q": "For the operation y(t) = x(t/2), the temporal duration of the non-zero part of the signal will...",
        "type": "mcq",
        "options": ["Remain unchanged", "Halve (decrease by factor of 2)", "Double (increase by factor of 2)", "Become zero"],
        "ans": "Double (increase by factor of 2)",
        "explain_correct": "القسمة على 2 في الزمن (α=0.5) بتعمل Expansion، فبتخلي الإشارة تاخد ضعف الوقت. ✅",
        "explain_wrong": "لما نقسم الزمن على رقم، الإشارة بتتباطأ وتمط (Expansion)."
    },
    {
        "q": "What is the relationship between the EVEN component evaluated at t=0, x_e(0), and the original signal x(0)?",
        "type": "mcq",
        "options": ["x_e(0) = 0", "x_e(0) = 0.5 * x(0)", "x_e(0) = x(0)", "x_e(0) = -x(0)"],
        "ans": "x_e(0) = x(0)",
        "explain_correct": "بالتعويض: x_e(0) = 0.5*[x(0)+x(-0)] = 0.5*[2*x(0)] = x(0). ✅",
        "explain_wrong": "الجزء الفردي بياخد 0، فالجزء الزوجي بياخد قيمة الإشارة كلها عند الصفر."
    },
    {
        "q": "True or False: The Odd component of a strictly EVEN signal is zero everywhere.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح، لو الإشارة زوجية 100%، مفيش فيها أي جزء فردي وبالتالي x_o(t) = 0. ✅",
        "explain_wrong": "الإشارة الزوجية النقية لا تحتوي على جزء فردي."
    },
    {
        "q": "If x[n] = {1, 2, 3} defined at n = 0, 1, 2 respectively. What is the value of x[-n] at n = -1?",
        "type": "mcq",
        "options": ["1", "2", "3", "0"],
        "ans": "2",
        "explain_correct": "عند n = -1، إحنا محتاجين قيمة x[-(-1)] يعني x[1]، وقيمتها في المعطيات هي 2. ✅",
        "explain_wrong": "عوض بـ n = -1 في الدالة المقلوبة x[-n] وشوف هتديك x لكام."
    },
    {
        "q": "Given a signal x(t) = 1 - |t| for -1 <= t <= 1, and 0 otherwise. What is the value of x(0)?",
        "type": "mcq",
        "options": ["0", "1", "-1", "Undefined"],
        "ans": "1",
        "explain_correct": "عوض بـ t=0 في المعادلة: 1 - |0| = 1. ✅",
        "explain_wrong": "مجرد تعويض مباشر في فترة التعريف المتاحة."
    },
    {
        "q": "Which symmetry applies to an ODD signal?",
        "type": "mcq",
        "options": ["Symmetry about the X-axis", "Symmetry about the Y-axis", "Symmetry about the Origin", "No symmetry"],
        "ans": "Symmetry about the Origin",
        "explain_correct": "الإشارة الفردية (Odd) بتكون متماثلة حول نقطة الأصل (Origin). ✅",
        "explain_wrong": "التماثل حول الصادات للزوجي، وحول نقطة الأصل للفردي."
    },
    {
        "q": "If an operation evaluates to y[n] = -x[-n-2], the correct sequence of drawing it graphically is:",
        "type": "mcq",
        "options": ["Shift right by 2, then time reverse, then amplitude reverse", "Shift left by 2, then time reverse, then amplitude reverse", "Time reverse, shift left by 2, amplitude reverse", "Amplitude reverse only"],
        "ans": "Shift left by 2, then time reverse, then amplitude reverse",
        "explain_correct": "دايماً بنبدأ بالـ Shift (n+2 يعني يسار)، وبعدين Time Reversal، وبعدين الـ Amplitude الخارجي. ✅",
        "explain_wrong": "القاعدة الأفضل: نفذ الإزاحة الأول بناءً على الإشارة (n+2)، ثم الانعكاس."
    },
    {
        "q": "If x(t) is an odd signal, and y(t) = x(t) * x(t), what is the classification of y(t)?",
        "type": "mcq",
        "options": ["Odd signal", "Even signal", "Neither even nor odd", "Zero signal"],
        "ans": "Even signal",
        "explain_correct": "ضرب دالتين فرديتين بيدي دالة زوجية (سالب × سالب = موجب). ✅",
        "explain_wrong": "جرب تعوض: y(-t) = x(-t)*x(-t) = (-x(t))*(-x(t)) = x(t)^2 = y(t)."
    },
    {
        "q": "In discrete-time signals, why can't we compress a signal by an arbitrary fractional factor like x[n/2] directly without interpolation?",
        "type": "mcq",
        "options": ["Because amplitude will overflow", "Because 'n' must always be an integer", "Because it becomes continuous", "Because sampling rate decreases"],
        "ans": "Because 'n' must always be an integer",
        "explain_correct": "لو قسمنا n على 2، هيطلع قيم فردية بكسور (زي n=1 -> 0.5)، وده مرفوض في الـ Discrete. ✅",
        "explain_wrong": "الـ Discrete signals متعرفة للـ Integers بس."
    },
    {
        "q": "If the discrete signal x[n] has non-zero values only for n = -2 to 2, what is the non-zero range for y[n] = x[n-3]?",
        "type": "mcq",
        "options": ["n = 1 to 5", "n = -5 to -1", "n = -2 to 2", "n = -1 to 3"],
        "ans": "n = 1 to 5",
        "explain_correct": "دي إزاحة لليمين (Delay) بمقدار 3، فنجمع 3 على حدود الإشارة: (-2+3=1) و (2+3=5). ✅",
        "explain_wrong": "إزاحة لليمين تعني جمع مقدار الشيفت على حدود الـ n."
    },
    {
        "q": "The concept of 'decimation' (throwing away samples) occurs during which operation?",
        "type": "mcq",
        "options": ["x[n/2]", "x[n-2]", "x[2n]", "2x[n]"],
        "ans": "x[2n]",
        "explain_correct": "الـ x[2n] بتاخد العينات الزوجية بس وبترمي الفردية، فبتقلل عدد العينات (Decimation). ✅",
        "explain_wrong": "الضرب للـ index بيوقع عينات، والقسمة بتحتاج عينات جديدة."
    }
]