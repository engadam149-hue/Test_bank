# ==========================================
# 📖 dsp_lec2.py
# Digital Signal Processing - Lecture 2 & Quiz 1
# Comprehensive 51 Questions Bank
# ==========================================

QUESTIONS = [
    # ─── Section 1: Even & Odd Properties (From Slides & Hand Notes) ───
    {
        "q": "A continuous-time signal is defined as an EVEN signal if it satisfies:",
        "type": "mcq",
        "options": ["x(-t) = -x(t)", "x(-t) = x(t)", "x(t) = x(t-1)", "x(t) = -x(-t)"],
        "ans": "x(-t) = x(t)",
        "explain_correct": "الإشارة الزوجية متماثلة حول محور الصادات، يعني قيمتها عند الزمن السالب تساوي قيمتها عند الموجب. ✅",
        "explain_wrong": "الإشارة الزوجية تبتلع الإشارة السالبة للزمن."
    },
    {
        "q": "A discrete-time sequence is defined as an ODD signal if it satisfies:",
        "type": "mcq",
        "options": ["x[-n] = x[n]", "x[n] = x[n+1]", "x[-n] = -x[n]", "x[-n] = 0"],
        "ans": "x[-n] = -x[n]",
        "explain_correct": "الإشارة الفردية متماثلة حول نقطة الأصل، يعني لو عكسنا الزمن، قيمة الإشارة بتتعكس. ✅",
        "explain_wrong": "في الـ Odd signal، الإشارة السالبة بتخرج بره الدالة."
    },
    {
        "q": "Any arbitrary signal x(t) can be expressed mathematically as:",
        "type": "mcq",
        "options": ["Only an even signal", "Only an odd signal", "The sum of an even and an odd component", "The product of an even and an odd component"],
        "ans": "The sum of an even and an odd component",
        "explain_correct": "أهم قاعدة: أي إشارة هي مجموع جزئين x(t) = x_e(t) + x_o(t). ✅",
        "explain_wrong": "الإشارة دائماً تتكون من مجموع مركَبة زوجية ومركَبة فردية."
    },
    {
        "q": "The formula used to extract the EVEN component x_e(t) of a signal is:",
        "type": "mcq",
        "options": ["0.5 * [x(t) - x(-t)]", "0.5 * [x(t) + x(-t)]", "x(t) + x(-t)", "x(t) - x(-t)"],
        "ans": "0.5 * [x(t) + x(-t)]",
        "explain_correct": "الجزء الزوجي هو متوسط جمع الإشارة الأصلية مع معكوسها الزمني. ✅",
        "explain_wrong": "تذكر: الجمع يٌستخدم لاستخراج الجزء الزوجي."
    },
    {
        "q": "The formula used to extract the ODD component x_o(t) of a signal is:",
        "type": "mcq",
        "options": ["0.5 * [x(t) + x(-t)]", "x(t) - x(-t)", "0.5 * [x(t) - x(-t)]", "0.5 * [x(-t) - x(t)]"],
        "ans": "0.5 * [x(t) - x(-t)]",
        "explain_correct": "الجزء الفردي يأتي من طرح المعكوس الزمني من الإشارة الأصلية مقسوماً على 2. ✅",
        "explain_wrong": "تذكر: الطرح يٌستخدم لاستخراج الجزء الفردي."
    },
    {
        "q": "What is the result of multiplying two EVEN signals together?",
        "type": "mcq",
        "options": ["An Odd signal", "An Even signal", "A Zero signal", "A periodic signal"],
        "ans": "An Even signal",
        "explain_correct": "موجب × موجب = موجب. ضرب دالتين زوجيتين بيطلع دالة زوجية. ✅",
        "explain_wrong": "تشابه التماثل في الضرب يُنتج إشارة Even."
    },
    {
        "q": "What is the result of multiplying two ODD signals together?",
        "type": "mcq",
        "options": ["An Odd signal", "An Even signal", "A Zero signal", "None of the above"],
        "ans": "An Even signal",
        "explain_correct": "سالب × سالب = موجب. ضرب دالتين فرديتين بيدي دالة زوجية! ✅",
        "explain_wrong": "لو ضربت x(-t)=-x(t) في نفسها، السالب هيطير وتبقى Even."
    },
    {
        "q": "What is the result of multiplying an EVEN signal by an ODD signal?",
        "type": "mcq",
        "options": ["An Odd signal", "An Even signal", "A periodic signal", "A constant signal"],
        "ans": "An Odd signal",
        "explain_correct": "موجب × سالب = سالب. ضرب زوجي في فردي بيطلع فردي. ✅",
        "explain_wrong": "اختلاف التماثل في الضرب يُنتج إشارة Odd."
    },
    {
        "q": "What must be the value of any purely ODD signal at the origin (t = 0 or n = 0)?",
        "type": "mcq",
        "options": ["Infinity", "1", "0", "Undefined"],
        "ans": "0",
        "explain_correct": "بما إن x(0) = -x(0)، إذن 2x(0) = 0، وبالتالي لازم تساوي صفر. ✅",
        "explain_wrong": "الإشارة الفردية يجب أن تمر بنقطة الأصل."
    },
    {
        "q": "If a signal x[n] = 5 for all n, how is this signal classified?",
        "type": "mcq",
        "options": ["Even", "Odd", "Neither", "Both"],
        "ans": "Even",
        "explain_correct": "الرقم الثابت مبيهتمش بالزمن، فـ x[n] هتساوي x[-n] دايماً، إذن هي Even. ✅",
        "explain_wrong": "الثوابت دائماً دوال زوجية."
    },

    # ─── Section 2: Complex Exponentials (From Sheet 2) ───
    {
        "q": "Find the EVEN component of the complex exponential signal x(t) = e^{jt}.",
        "type": "mcq",
        "options": ["sin(t)", "cos(t)", "j sin(t)", "j cos(t)"],
        "ans": "cos(t)",
        "explain_correct": "من قانون أويلر: e^{jt} = cos(t) + j sin(t). وبما إن cos زوجية، فهي الـ Even component. ✅",
        "explain_wrong": "الـ cos هي الجزء الزوجي، والـ sin هي الجزء الفردي."
    },
    {
        "q": "Find the ODD component of the complex exponential signal x(t) = e^{jt}.",
        "type": "mcq",
        "options": ["cos(t)", "j cos(t)", "j sin(t)", "sin(t)"],
        "ans": "j sin(t)",
        "explain_correct": "في مفكوك أويلر e^{jt} = cos(t) + j sin(t)، دالة sin فردية، إذن الجزء الفردي هو j sin(t). ✅",
        "explain_wrong": "لا تنسَ حرف الـ j المضروب في الدالة."
    },

    # ─── Section 3: Continuous-Time Periodicity (From Slides & Sheet 2) ───
    {
        "q": "A continuous-time signal x(t) is periodic with fundamental period T if it satisfies:",
        "type": "mcq",
        "options": ["x(t+T) = -x(t)", "x(t+T) = x(t)", "x(T) = x(0)", "x(t) = 0"],
        "ans": "x(t+T) = x(t)",
        "explain_correct": "الإشارة الدورية تكرر نفسها تماماً كل فترة زمنية T. ✅",
        "explain_wrong": "يجب أن تعود الدالة لنفس قيمتها بعد إضافة الزمن T."
    },
    {
        "q": "Are ALL continuous-time sinusoidal signals (like sin and cos) periodic?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "نعم، في الزمن المتصل (Continuous)، أي دالة جيبية تكون دورية دائماً. ✅",
        "explain_wrong": "لا يوجد شرط إضافي للدورية في الزمن المتصل للدوال الجيبية."
    },
    {
        "q": "What is the fundamental period T_0 of the signal x(t) = cos(w_0 t + theta)?",
        "type": "mcq",
        "options": ["pi / w_0", "w_0 / 2pi", "2pi / w_0", "2pi w_0"],
        "ans": "2pi / w_0",
        "explain_correct": "التردد الزاوي w_0 = 2*pi/T_0، إذن الزمن الدوري T_0 = 2*pi / w_0. ✅",
        "explain_wrong": "اقسم 2pi على معامل الـ t."
    },
    {
        "q": "For the sum of two CONTINUOUS-TIME periodic signals to be periodic, what condition must be met?",
        "type": "mcq",
        "options": ["T1 = T2", "T1 / T2 must be an integer", "T1 / T2 must be a rational number", "They must have the same phase"],
        "ans": "T1 / T2 must be a rational number",
        "explain_correct": "لضمان الدورية، يجب أن تكون النسبة بين الزمنين الدوريين (T1/T2) رقماً نسبياً (Rational). ✅",
        "explain_wrong": "لو كانت النسبة تحتوي على جذور أو Pi، المجموع لن يكون دورياً."
    },
    {
        "q": "Determine the fundamental period of x(t) = sin( (2pi/3) t ).",
        "type": "mcq",
        "options": ["3", "2pi/3", "1.5", "Not periodic"],
        "ans": "3",
        "explain_correct": "w_0 = 2pi/3. إذن T = 2pi / (2pi/3) = 3. ✅",
        "explain_wrong": "عوض في القانون T = 2pi / w_0."
    },
    {
        "q": "Determine the fundamental period of x(t) = cos(t + pi/4).",
        "type": "mcq",
        "options": ["pi/4", "pi", "2pi", "Not periodic"],
        "ans": "2pi",
        "explain_correct": "معامل t هنا هو 1 (أي w_0 = 1). إذن T = 2pi / 1 = 2pi. إزاحة الـ Phase (pi/4) لا تؤثر على الدورية. ✅",
        "explain_wrong": "الـ Phase shift لا يغير الزمن الدوري."
    },
    {
        "q": "Is the signal x(t) = cos(t) + sin(sqrt(2) t) periodic?",
        "type": "mcq",
        "options": ["Periodic with T = 2pi", "Periodic with T = sqrt(2)pi", "Not periodic", "Periodic with T = 1"],
        "ans": "Not periodic",
        "explain_correct": "T1 = 2pi, T2 = 2pi/sqrt(2). النسبة T1/T2 = sqrt(2) وهو رقم غير نسبي (Irrational)، إذن المجموع غير دوري. ✅",
        "explain_wrong": "وجود الجذر يمنع النسبة من أن تكون Rational."
    },
    {
        "q": "Find the fundamental period of x(t) = cos(pi/3 t) + sin(pi/4 t).",
        "type": "mcq",
        "options": ["12", "24", "48", "Not periodic"],
        "ans": "24",
        "explain_correct": "T1 = 2pi/(pi/3) = 6. و T2 = 2pi/(pi/4) = 8. المضاعف المشترك الأصغر (LCM) للـ 6 والـ 8 هو 24. ✅",
        "explain_wrong": "احسب T1 و T2 ثم أوجد الـ LCM لهما."
    },

    # ─── Section 4: Discrete-Time Periodicity (From Slides & Sheet 2) ───
    {
        "q": "A discrete-time sequence x[n] is periodic with period N if:",
        "type": "mcq",
        "options": ["x[n+N] = -x[n]", "x[n+N] = x[n]", "x[N] = x[0]", "x[n+N] = 0"],
        "ans": "x[n+N] = x[n]",
        "explain_correct": "في الزمن الديسكريت، الإشارة تكرر نفسها بعد عدد صحيح N من العينات. ✅",
        "explain_wrong": "يجب أن تكون N عدداً صحيحاً للعينات."
    },
    {
        "q": "Are ALL discrete-time sinusoidal sequences periodic?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. في الديسكريت، يجب أن تحقق الإشارة الجيبية شرطاً رياضياً صارماً لتكون دورية. ✅",
        "explain_wrong": "عكس الـ Continuous، ليست كل دوال الـ discrete sinusoids دورية."
    },
    {
        "q": "For a discrete complex exponential x[n] = e^{j Omega_0 n} to be periodic, the value (Omega_0 / 2pi) must be:",
        "type": "mcq",
        "options": ["An integer", "A rational number (m/N)", "An irrational number", "Pi"],
        "ans": "A rational number (m/N)",
        "explain_correct": "شرط الدورية الأساسي: يجب أن تكون النسبة بين تردد الإشارة و 2pi عبارة عن كسر نسبي (Rational). ✅",
        "explain_wrong": "لازم النسبة تطلع m/N حيث m و N أرقام صحيحة."
    },
    {
        "q": "Is the sequence x[n] = e^{j(n/4 - pi)} periodic?",
        "type": "mcq",
        "options": ["Periodic, N=8", "Not periodic", "Periodic, N=4", "Periodic, N=8pi"],
        "ans": "Not periodic",
        "explain_correct": "التردد هنا 1/4. عند قسمته على 2pi ينتج 1/(8pi). وجود Pi في المقام يجعله غير نسبي، إذن غير دوري. ✅",
        "explain_wrong": "الـ Phase shift (-pi) ملوش دعوة، بنبص على معامل n بس."
    },
    {
        "q": "Is the sequence x[n] = e^{j(pi/4 n)} periodic? What is its fundamental period N?",
        "type": "mcq",
        "options": ["Not periodic", "Periodic, N = 4", "Periodic, N = 8", "Periodic, N = 2"],
        "ans": "Periodic, N = 8",
        "explain_correct": "التردد pi/4. النسبة: (pi/4) / 2pi = 1/8. إذن N = 8 و m = 1. ✅",
        "explain_wrong": "اقسم معامل n على 2pi وشوف المقام."
    },
    {
        "q": "True or False: The summation of TWO periodic DISCRETE-TIME signals is ALWAYS periodic.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح جداً! لأن أي N1 و N2 هما أرقام صحيحة، فنسبتهم دائماً رقم نسبي، وبالتالي المجموع دائماً دوري. ✅",
        "explain_wrong": "في الـ Discrete، المجموع دائماً دوري بشرط أن تكون الإشارات الأصلية دورية."
    },
    {
        "q": "Find the fundamental period of x[n] = cos(pi/3 n) + sin(pi/4 n).",
        "type": "mcq",
        "options": ["6", "8", "24", "12"],
        "ans": "24",
        "explain_correct": "N1 = 2pi/(pi/3) = 6. N2 = 2pi/(pi/4) = 8. المضاعف المشترك الأصغر (LCM) لـ 6 و 8 هو 24. ✅",
        "explain_wrong": "احسب N لكل إشارة لوحدها، ثم هات الـ LCM."
    },
    {
        "q": "Is the signal x[n] = cos^2(pi/8 n) periodic? If so, what is N?",
        "type": "mcq",
        "options": ["Not periodic", "Periodic, N = 8", "Periodic, N = 16", "Periodic, N = 4"],
        "ans": "Periodic, N = 8",
        "explain_correct": "بفك التربيع: 0.5 + 0.5 cos(pi/4 n). التردد الجديد pi/4. النسبة (pi/4)/2pi = 1/8. إذن N = 8. ✅",
        "explain_wrong": "تربيع الـ cos يضاعف التردد (الزاوية تُضرب في 2)."
    },

    # ─── Section 5: Operations & Transformations (Sheet 1, Quiz 1, Hand Notes) ───
    {
        "q": "The operation y_1[n] = x_1[n] + x_2[n] represents:",
        "type": "mcq",
        "options": ["Signal Addition (Point-by-point)", "Signal Convolution", "Signal Multiplication", "Amplitude Scaling"],
        "ans": "Signal Addition (Point-by-point)",
        "explain_correct": "تُجمع العينات المتقابلة في نفس الزمن n مباشرة. ✅",
        "explain_wrong": "علامة الزائد تعني جمع مباشر Point-by-point."
    },
    {
        "q": "The operation y_2[n] = 2 * x_2[n] represents:",
        "type": "mcq",
        "options": ["Time scaling", "Amplitude scaling", "Time shifting", "Time reversal"],
        "ans": "Amplitude scaling",
        "explain_correct": "الرقم 2 مضروب بره الدالة، فبيغير الـ Amplitude (طول العينة) مش الزمن. ✅",
        "explain_wrong": "التعديل خارج القوس يؤثر على الـ Y-axis فقط."
    },
    {
        "q": "The operation y_3[n] = x_1[n] * x_2[n] represents:",
        "type": "mcq",
        "options": ["Signal Addition", "Signal Convolution", "Signal Multiplication (point-by-point)", "Amplitude Scaling"],
        "ans": "Signal Multiplication (point-by-point)",
        "explain_correct": "تُضرب كل عينة في اللي قصادها في نفس الزمن. ✅",
        "explain_wrong": "علامة الضرب العادية تعني Point-by-point multiplication."
    },
    {
        "q": "Given x_1[n] is defined for n=0 to 6, and x_2[n] is defined for n=-3 to 4. What is the range of y[n] = x_1[n] + x_2[n]?",
        "type": "mcq",
        "options": ["n=0 to 4", "n=-3 to 6", "n=3 to 10", "n=-3 to 4"],
        "ans": "n=-3 to 6",
        "explain_correct": "في الجمع، الإشارة الناتجة تمتد لأبعد حدود الإشارتين، يعني من أصغر بداية (-3) لأكبر نهاية (6). ✅",
        "explain_wrong": "الجمع يأخذ النطاق الأوسع (Union)."
    },
    {
        "q": "Given x_1[n] is defined for n=0 to 6, and x_2[n] is defined for n=-3 to 4. What is the range of y[n] = x_1[n] * x_2[n]?",
        "type": "mcq",
        "options": ["n=-3 to 6", "n=0 to 4", "n=0 to 6", "n=-3 to 4"],
        "ans": "n=0 to 4",
        "explain_correct": "في الضرب، أي شيء يُضرب في صفر يعطي صفراً، فالناتج يظهر في منطقة التقاطع فقط (Intersection). ✅",
        "explain_wrong": "الضرب يتطلب وجود الإشارتين معاً."
    },
    {
        "q": "Evaluate the expression: x[n] * u[1-n]. This operation will keep the samples of x[n] only for:",
        "type": "mcq",
        "options": ["n >= 1", "n <= 1", "n >= 0", "n <= 0"],
        "ans": "n <= 1",
        "explain_correct": "دالة الـ Step u[1-n] تكون 1 عندما (1-n >= 0)، يعني 1 >= n. ستحتفظ بالعينات اليسرى حتى n=1. ✅",
        "explain_wrong": "الـ reversal في u[-n] يوجه الدالة لليسار."
    },
    {
        "q": "Evaluate the expression: x[n] * delta[2n-4]. This simplifies to:",
        "type": "mcq",
        "options": ["x[2] * delta[2n-4]", "x[4] * delta[2n-4]", "x[0]", "0"],
        "ans": "x[2] * delta[2n-4]",
        "explain_correct": "دالة الـ Delta لها قيمة فقط عندما 2n-4 = 0، أي n=2. فنحتفظ بـ x[2] مضروبة في الدلتا. ✅",
        "explain_wrong": "حل المعادلة داخل الدلتا وساوها بالصفر."
    },
    {
        "q": "The operation y[n] = x[n] * x[2n] implies:",
        "type": "mcq",
        "options": ["Squaring the signal", "Multiplying the signal by itself shifted", "Multiplying the original signal by its compressed version", "Multiplying the signal by 2"],
        "ans": "Multiplying the original signal by its compressed version",
        "explain_correct": "x[2n] هي النسخة المضغوطة (Decimated) من الإشارة، تُضرب نقطة بنقطة في الإشارة الأصلية. ✅",
        "explain_wrong": "x[2n] تعني Compression في الزمن."
    },
    {
        "q": "Calculate the summation: Sum of [ x(n) * delta(5-n) ] from n=-infinity to infinity.",
        "type": "mcq",
        "options": ["0", "x(0)", "x(-5)", "x(5)"],
        "ans": "x(5)",
        "explain_correct": "حسب خاصية الـ Sifting للدلتا، المجموع يقتنص قيمة الدالة عند نقطة الدلتا (5-n=0 -> n=5). إذن الناتج x(5). ✅",
        "explain_wrong": "الـ Delta تقوم بـ 'اصطياد' العينة عند نقطة الصفر الخاصة بها."
    },
    {
        "q": "Calculate the non-zero window of the function: [ u(n) - u(n-3) ]",
        "type": "mcq",
        "options": ["1 for n = 0, 1, 2", "1 for n = 1, 2, 3", "1 for n = 0, 1, 2, 3", "0 everywhere"],
        "ans": "1 for n = 0, 1, 2",
        "explain_correct": "u(n) تبدأ من 0، و u(n-3) تبدأ من 3. طرحهما يُبقي العينات عند 0, 1, 2 فقط (النافذة). ✅",
        "explain_wrong": "العينة عند 3 تُطرح (1-1=0)."
    },
    {
        "q": "Based on the previous question, evaluate the summation: Sum of [ x(n) * (u(n) - u(n-3)) ] from n=-infinity to infinity.",
        "type": "mcq",
        "options": ["x(0)", "x(3)", "x(0) + x(1) + x(2)", "x(1) + x(2) + x(3)"],
        "ans": "x(0) + x(1) + x(2)",
        "explain_correct": "بما أن النافذة قيمتها 1 عند n=0,1,2، فالمجموع هو جمع هذه العينات الثلاثة من الإشارة x. ✅",
        "explain_wrong": "اضرب الإشارة في النافذة واجمع القيم المتبقية."
    },
    {
        "q": "Is a finite-duration discrete sequence (like the one in Quiz 1) classified as an Energy or Power signal?",
        "type": "mcq",
        "options": ["Power Signal", "Energy Signal", "Both", "Neither"],
        "ans": "Energy Signal",
        "explain_correct": "أي إشارة طولها محدود وقيمتها محدودة تمتلك طاقة محدودة، فهي Energy Signal (وقدرتها = 0). ✅",
        "explain_wrong": "إشارات الـ Power تكون عادة دورية أو ممتدة للمالانهاية."
    },

    # ─── Section 6: Sampling & Miscellaneous (Sec 1&2, Sheet 1) ───
    {
        "q": "If a continuous signal x(t) = 1 - |t| for -1 <= t <= 1 is sampled at Ts = 0.5 s, how many non-zero samples are produced?",
        "type": "mcq",
        "options": ["3", "5", "4", "2"],
        "ans": "5",
        "explain_correct": "التعويض: t = n*0.5. الحدود: -1 <= 0.5n <= 1 -> -2 <= n <= 2. العينات هي (-2,-1,0,1,2) وعددهم 5. ✅",
        "explain_wrong": "اقسم حدود الزمن على Ts لمعرفة حدود n."
    },
    {
        "q": "If the same signal x(t) = 1 - |t| for -1 <= t <= 1 is sampled at Ts = 1.0 s, how many non-zero samples are produced?",
        "type": "mcq",
        "options": ["1", "2", "3", "5"],
        "ans": "3",
        "explain_correct": "التعويض: t = n*1. الحدود: -1 <= n <= 1. العينات هي (-1, 0, 1) وعددهم 3. ✅",
        "explain_wrong": "عوض بـ Ts = 1 في القانون t = n*Ts."
    },
    {
        "q": "When calculating the EVEN component x_e(t) graphically, what geometric operation corresponds to x(-t)?",
        "type": "mcq",
        "options": ["Mirroring around the X-axis", "Mirroring around the Y-axis", "Shifting to the right", "Shifting to the left"],
        "ans": "Mirroring around the Y-axis",
        "explain_correct": "عكس إشارة الزمن x(-t) يعني أن اليمين يصبح يساراً والعكس، وهو تماثل حول محور الصادات Y. ✅",
        "explain_wrong": "الـ Time reversal ينعكس على المحور الرأسي."
    },
    {
        "q": "If x(t) = 4 * e^{-0.5t} * u(t), for what values of 't' is its time-reversed version x(-t) non-zero?",
        "type": "mcq",
        "options": ["t >= 0", "t <= 0", "All t", "t > 0.5"],
        "ans": "t <= 0",
        "explain_correct": "الإشارة الأصلية مضروبة في u(t) يعني موجودة في الموجب. إذاً x(-t) ستكون موجودة في السالب (t <= 0). ✅",
        "explain_wrong": "الـ Reversal يعكس مكان تواجد الإشارة بالكامل."
    },
    {
        "q": "Based on the signal x(t) = 4 * e^{-0.5t} * u(t), calculate the value of its EVEN component x_e(t) at t = 0.",
        "type": "mcq",
        "options": ["0", "2", "4", "8"],
        "ans": "4",
        "explain_correct": "x_e(0) = 0.5 * [x(0) + x(-0)] = 0.5 * [4 + 4] = 4. ✅",
        "explain_wrong": "عوض بـ t=0 في معادلة الـ Even component."
    },
    {
        "q": "In the process of sampling $x[n] = x(nT_s)$, the independent variable 'n' must always be:",
        "type": "mcq",
        "options": ["Any real number", "A fraction", "An integer", "A complex number"],
        "ans": "An integer",
        "explain_correct": "في الإشارات الـ Discrete، المتغير n يمثل 'رقم العينة' ويجب أن يكون عدداً صحيحاً. ✅",
        "explain_wrong": "لا يوجد شيء اسمه العينة رقم 1.5."
    },
    {
        "q": "True or False: If a continuous signal x(t) is periodic, its sampled discrete version x[n] is ALWAYS guaranteed to be periodic.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "خطأ. يجب أن يحقق الـ sampling interval شرطاً محدداً: (Ts/T0) يجب أن يكون رقماً نسبياً (Rational) لتكون x[n] دورية. ✅",
        "explain_wrong": "عملية الـ Sampling قد تدمر الدورية إذا لم يتم اختيار Ts بعناية."
    },
    {
        "q": "What is the fundamental period definition for any periodic signal?",
        "type": "mcq",
        "options": ["The largest positive value of T", "The smallest positive value of T", "Any multiple of T", "Zero"],
        "ans": "The smallest positive value of T",
        "explain_correct": "الزمن الدوري الأساسي (Fundamental Period) هو أصغر زمن ممكن تكرر فيه الإشارة نفسها. ✅",
        "explain_wrong": "كلمة Fundamental تعني الأصغر."
    },
    {
        "q": "Evaluate: delta[n-2] is equivalent to delta[2n-4] in terms of the position of the non-zero impulse.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "صح. الدلتا الأولى تكون 1 عند n=2، والدلتا الثانية تكون 1 عندما 2n-4=0 (أي n=2 أيضاً). ✅",
        "explain_wrong": "ساوي ما بداخل القوس بالصفر لتعرف مكان الـ Impulse."
    },
    {
        "q": "If x(t) is a continuous signal, the operation x(t/2) causes the signal to be:",
        "type": "mcq",
        "options": ["Compressed in time", "Expanded in time", "Advanced in time", "Delayed in time"],
        "ans": "Expanded in time",
        "explain_correct": "القسمة على رقم (أو الضرب في كسر) في الزمن يجعل الإشارة تتباطأ، أي تتمدد (Expansion). ✅",
        "explain_wrong": "تصغير معامل الـ t يمد الإشارة."
    },
    {
        "q": "The unit step sequence u[n+2] has its first non-zero value at which index?",
        "type": "mcq",
        "options": ["n = 2", "n = 0", "n = -2", "n = 1"],
        "ans": "n = -2",
        "explain_correct": "دالة الـ Step تبدأ عندما يكون ما بداخلها >= 0. أي n+2 >= 0 -> n >= -2. ✅",
        "explain_wrong": "الموجب داخل القوس يعني إزاحة لليسار."
    }
]