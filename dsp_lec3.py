# ==========================================
# 📖 dsp_lec3.py
# Digital Signal Processing - Lecture 3, Sec 3 & Sheet 3
# Common Signals, Energy/Power, and Impulse Properties
# ==========================================

QUESTIONS = [
    # ─── Part 1: The Continuous-Time Impulse (Delta) Function ───
    {
        "q": "The continuous-time unit impulse function δ(t) has an area of:",
        "type": "mcq",
        "options": ["Zero", "Infinity", "One", "Undefined"],
        "ans": "One",
        "explain_correct": "دالة الـ Impulse أو الـ Delta (δ) مساحتها تحت المنحنى تساوي 1، بالرغم من إن قيمتها عند الصفر تؤول للمالانهاية. ✅",
        "explain_wrong": "مساحة الدلتا دائماً 1، بينما الـ Amplitude عند الصفر هو اللي Infinity."
    },
    {
        "q": "What is the value of the continuous-time unit impulse function δ(t) at t = 5?",
        "type": "mcq",
        "options": ["1", "Infinity", "0", "5"],
        "ans": "0",
        "explain_correct": "دالة الـ δ(t) قيمتها بصفر في أي مكان ما عدا t = 0. ✅",
        "explain_wrong": "الـ Delta بتظهر فقط عند النقطة اللي بتخلي اللي جوه القوس يساوي صفر."
    },
    {
        "q": "According to the multiplication property of the impulse function, x(t) * δ(t - t0) is equal to:",
        "type": "mcq",
        "options": ["x(t)", "x(t0)", "x(t0) * δ(t - t0)", "x(t) * δ(t0)"],
        "ans": "x(t0) * δ(t - t0)",
        "explain_correct": "عند ضرب إشارة في دلتا، الدلتا بتـ 'تصطاد' قيمة الإشارة عند نقطة النبضة (t0) وتفضل الدلتا موجودة. ✅",
        "explain_wrong": "الناتج بيكون نبضة (Impulse) مضروبة في رقم ثابت وهو قيمة x عند t0."
    },
    {
        "q": "According to the sifting (integration) property, the integral of [x(t) * δ(t - t0)] from -∞ to ∞ equals:",
        "type": "mcq",
        "options": ["x(t0) * δ(t-t0)", "x(t0)", "x(t)", "1"],
        "ans": "x(t0)",
        "explain_correct": "التكامل بياخد المساحة، وبما إن مساحة الدلتا = 1، فالناتج بيكون قيمة الإشارة المضروبة فيها عند t0 فقط. ✅",
        "explain_wrong": "التكامل بيطير الدلتا وبيسيب الرقم الثابت (قيمة الإشارة عند t0)."
    },
    {
        "q": "Evaluate the expression from Sheet 3: t * δ(t)",
        "type": "mcq",
        "options": ["t", "δ(t)", "1", "0"],
        "ans": "0",
        "explain_correct": "بما إن الدلتا موجودة عند t=0 فقط، هنعوض عن t بصفر. إذن 0 * δ(0) = 0. ✅",
        "explain_wrong": "عوض بقيمة الـ t اللي بتخلي الدلتا بصفر، هتلاقي الناتج صفر."
    },
    {
        "q": "Evaluate the expression from Sheet 3: sin(t) * δ(t)",
        "type": "mcq",
        "options": ["1", "sin(t)", "δ(t)", "0"],
        "ans": "0",
        "explain_correct": "بنعوض عن t بصفر لأن الدلتا عند الصفر: sin(0) * δ(t) = 0 * δ(t) = 0. ✅",
        "explain_wrong": "ساين الصفر بصفر، بالتالي التعبير كله بيختفي."
    },
    {
        "q": "Evaluate the expression from Sheet 3: cos(t) * δ(t - π)",
        "type": "mcq",
        "options": ["δ(t - π)", "-δ(t - π)", "0", "-1"],
        "ans": "-δ(t - π)",
        "explain_correct": "الدلتا هنا عند t = π. هنعوض في الكوزاين: cos(π) = -1. إذن الناتج -1 * δ(t - π) = -δ(t - π). ✅",
        "explain_wrong": "عوض بالزاوية π في دالة الـ cos، الناتج -1، واضربه في الدلتا."
    },

    # ─── Part 2: Unit Step, Ramp, and Signum Functions ───
    {
        "q": "The Unit Step function u(t) is equal to 1 for:",
        "type": "mcq",
        "options": ["t < 0", "All t", "t > 0", "t = 0 only"],
        "ans": "t > 0",
        "explain_correct": "دالة الـ Step u(t) تشتغل (بتكون 1) لما الزمن يكون موجب (t > 0) وتفصل (تكون 0) لما الزمن يكون سالب. ✅",
        "explain_wrong": "الـ Unit step تعني خطوة تبدأ من الصفر وتستمر للمالانهاية."
    },
    {
        "q": "The mathematical relationship between the unit step u(t) and the impulse δ(t) is:",
        "type": "mcq",
        "options": ["u(t) = d/dt δ(t)", "δ(t) = d/dt u(t)", "δ(t) = u(t) * t", "u(t) = δ(t) + 1"],
        "ans": "δ(t) = d/dt u(t)",
        "explain_correct": "تفاضل دالة الـ Step u(t) يعطي دالة الـ Impulse δ(t) لأن الـ Step فيها قفزة مفاجئة عند الصفر. ✅",
        "explain_wrong": "تفاضل الخطوة (Step) هو نبضة (Impulse)."
    },
    {
        "q": "What is the result of the derivative: d/dt [ u(t) - u(t-a) ]? (From Sheet 3)",
        "type": "mcq",
        "options": ["δ(t) + δ(t-a)", "δ(t) - δ(t-a)", "1", "0"],
        "ans": "δ(t) - δ(t-a)",
        "explain_correct": "تفاضل u(t) هو δ(t)، وتفاضل u(t-a) هو δ(t-a). والاشارة بينهم طرح تنزل زي ما هي. ✅",
        "explain_wrong": "وزع التفاضل على القوس، تفاضل الـ Step دائماً يعطي Impulse."
    },
    {
        "q": "The Ramp function r(t) is mathematically defined as:",
        "type": "mcq",
        "options": ["t * u(t)", "d/dt u(t)", "u(t) - u(t-1)", "t^2 * u(t)"],
        "ans": "t * u(t)",
        "explain_correct": "دالة الـ Ramp هي خط مستقيم ميله 1 بيبدأ من الصفر، فبنضرب t في دالة الـ Step u(t) عشان نقطع الجزء السالب. ✅",
        "explain_wrong": "الـ Ramp = الزمن t مضروب في الـ Step function."
    },
    {
        "q": "The first derivative of the Ramp function r(t) equals:",
        "type": "mcq",
        "options": ["δ(t)", "r(t)", "u(t)", "1"],
        "ans": "u(t)",
        "explain_correct": "ميل خط الـ Ramp هو 1 للزمن الموجب، وصفر للزمن السالب، وهو ده بالظبط تعريف دالة الـ u(t). ✅",
        "explain_wrong": "تفاضل الـ Ramp يعطي Step، وتفاضل الـ Step يعطي Impulse."
    },
    {
        "q": "The Signum function sgn(t) is equal to:",
        "type": "mcq",
        "options": ["1 for t>0, 0 for t<0", "1 for t>0, -1 for t<0", "t for t>0, -t for t<0", "1 for all t"],
        "ans": "1 for t>0, -1 for t<0",
        "explain_correct": "دالة الإشارة Signum بتعطي 1 للقيم الموجبة و -1 للقيم السالبة. ✅",
        "explain_wrong": "الـ Signum بتميز إشارة الرقم (موجب أم سالب)."
    },
    {
        "q": "How can the Signum function sgn(t) be expressed using the unit step function u(t)?",
        "type": "mcq",
        "options": ["sgn(t) = 2u(t) - 1", "sgn(t) = u(t) + 1", "sgn(t) = u(t) - u(-t)", "Both A and C are correct"],
        "ans": "Both A and C are correct",
        "explain_correct": "ممكن نكتبها sgn(t) = 2u(t) - 1، وممكن u(t) - u(-t). الإجابتين صح رياضياً. ✅",
        "explain_wrong": "عوض بقيم t موجبة وسالبة في المعادلتين هتلاقيهم بيطلعوا نفس الناتج (1 و -1)."
    },
    {
        "q": "What is the first derivative of the Signum function sgn(t)? (From Sheet 3)",
        "type": "mcq",
        "options": ["δ(t)", "2δ(t)", "0", "u(t)"],
        "ans": "2δ(t)",
        "explain_correct": "بما إن sgn(t) = 2u(t) - 1، بتفاضل الطرفين: تفاضل 2u(t) هو 2δ(t)، وتفاضل الـ 1 بصفر. إذن الناتج 2δ(t). ✅",
        "explain_wrong": "الـ Signum بتقفز من -1 لـ 1 (مقدار القفزة 2)، إذن تفاضلها 2δ(t)."
    },
    {
        "q": "Express a rectangular pulse of amplitude 1 that starts at t = 2 and ends at t = 5 using step functions:",
        "type": "mcq",
        "options": ["u(t+2) - u(t+5)", "u(t-2) - u(t-5)", "u(t-2) + u(t-5)", "u(t) - u(t-3)"],
        "ans": "u(t-2) - u(t-5)",
        "explain_correct": "بنشغل الإشارة عند t=2 عن طريق u(t-2)، ونطفيها عند t=5 عن طريق طرح u(t-5). ✅",
        "explain_wrong": "لبناء نبضة مستطيلة، اطرح Step البداية من Step النهاية."
    },
    {
        "q": "From Sheet 3: Evaluate the derivative d/dt [ t * ( u(t) - u(t-a) ) ]. (Hint: Apply product rule)",
        "type": "mcq",
        "options": ["u(t) - u(t-a)", "u(t) - u(t-a) - a*δ(t-a)", "δ(t) - δ(t-a)", "t*δ(t) - t*δ(t-a)"],
        "ans": "u(t) - u(t-a) - a*δ(t-a)",
        "explain_correct": "تفاضل الأول × الثاني + الأول × تفاضل الثاني: 1*(u(t)-u(t-a)) + t*(δ(t)-δ(t-a)). وبما إن t*δ(t)=0 و t*δ(t-a)=a*δ(t-a)، ينتج u(t) - u(t-a) - a*δ(t-a). ✅",
        "explain_wrong": "لازم تستخدم قاعدة ضرب دالتين (Product Rule)، وتفتكر إن t مضروبة في δ(t-a) تساوي a*δ(t-a)."
    },

    # ─── Part 3: Discrete-Time Standard Signals ───
    {
        "q": "The discrete-time unit impulse δ[n] is defined as:",
        "type": "mcq",
        "options": ["1 for n>=0, 0 otherwise", "Infinity at n=0, 0 otherwise", "1 at n=0, 0 otherwise", "n for n>=0"],
        "ans": "1 at n=0, 0 otherwise",
        "explain_correct": "في الديسكريت، الدلتا مش بمالانهاية، هي عينة واحدة قيمتها 1 عند الصفر وبس. ✅",
        "explain_wrong": "الدلتا الديسكريت قيمتها 1، عكس الكونتينيوس اللي قيمتها بمالانهاية."
    },
    {
        "q": "The discrete-time unit step u[n] can be expressed as a sum of shifted impulses:",
        "type": "mcq",
        "options": ["Sum of δ[n-k] from k=0 to ∞", "Sum of δ[n-k] from k=-∞ to 0", "Sum of δ[n] from k=0 to ∞", "δ[n] + δ[n-1]"],
        "ans": "Sum of δ[n-k] from k=0 to ∞",
        "explain_correct": "الـ u[n] هي عبارة عن وحايد من صفر لمالانهاية، يعني مجموع نبضات (Impulses) متفتة عند كل رقم صحيح موجب. ✅",
        "explain_wrong": "u[n] = δ[n] + δ[n-1] + δ[n-2] + ..."
    },
    {
        "q": "The discrete-time operation x[n] * δ[n - 3] results in:",
        "type": "mcq",
        "options": ["x[n-3]", "x[3] * δ[n-3]", "x[3]", "0"],
        "ans": "x[3] * δ[n-3]",
        "explain_correct": "الدلتا عند n=3، إذن بتاخد قيمة الإشارة عند n=3 وتحتفظ بالدلتا زي ما هي. ✅",
        "explain_wrong": "الإشارة المضروبة في دلتا بتتحول لثابت (قيمة الإشارة عند مكان الدلتا) مضروب في الدلتا."
    },

    # ─── Part 4: Energy and Power Signals ───
    {
        "q": "A signal is classified as an Energy Signal if its total energy E satisfies:",
        "type": "mcq",
        "options": ["E = 0", "E is infinite", "0 < E < ∞", "E = Power"],
        "ans": "0 < E < ∞",
        "explain_correct": "الإشارة تعتبر Energy Signal لو طاقتها رقم محدود أكبر من الصفر وأقل من المالانهاية. ✅",
        "explain_wrong": "إشارة الطاقة (Energy Signal) يجب أن تكون طاقتها محدودة."
    },
    {
        "q": "For an Energy Signal, what is the value of its average Power (P)?",
        "type": "mcq",
        "options": ["P is infinite", "P = 0", "0 < P < ∞", "P = E"],
        "ans": "P = 0",
        "explain_correct": "أي Energy Signal (إشارة طاقتها محدودة) بتكون الـ Power بتاعتها بصفر لأننا بنقسم طاقة محدودة على زمن مالانهاية. ✅",
        "explain_wrong": "Energy signal -> E is finite, P = 0."
    },
    {
        "q": "A signal is classified as a Power Signal if its average power P satisfies:",
        "type": "mcq",
        "options": ["P = 0", "P is infinite", "0 < P < ∞", "P = Energy"],
        "ans": "0 < P < ∞",
        "explain_correct": "إشارة القدرة (Power Signal) بيكون ليها قدرة متوسطة محدودة (رقم ثابت غير الصفر والمالانهاية). ✅",
        "explain_wrong": "إشارة القدرة (Power Signal) يجب أن تكون قدرتها محدودة."
    },
    {
        "q": "For a Power Signal, what is the value of its total Energy (E)?",
        "type": "mcq",
        "options": ["E = 0", "E is infinite", "0 < E < ∞", "E = P"],
        "ans": "E is infinite",
        "explain_correct": "بما إن الإشارة ممتدة للمالانهاية ولها Power ثابتة، فطاقتها الإجمالية بتجمع للمالانهاية. ✅",
        "explain_wrong": "Power signal -> P is finite, E = ∞."
    },
    {
        "q": "Can a signal be BOTH an Energy signal and a Power signal at the same time?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "مستحيل! الإشارة يا إما Energy (P=0) يا إما Power (E=∞) يا إما Neither. متجمعش الاتنين أبداً. ✅",
        "explain_wrong": "التصنيفين عكس بعض تماماً."
    },
    {
        "q": "The continuous-time unit step function u(t) is classified as:",
        "type": "mcq",
        "options": ["Energy signal", "Power signal", "Neither", "Both"],
        "ans": "Power signal",
        "explain_correct": "الـ u(t) ممتدة للمالانهاية، الـ Power بتاعتها = 1/2، والـ Energy بتاعتها = ∞. إذن هي Power Signal. ✅",
        "explain_wrong": "أي إشارة ممتدة بقيمة ثابتة للمالانهاية بتكون Power Signal."
    },
    {
        "q": "Periodic signals (like sine and cosine waves) are generally classified as:",
        "type": "mcq",
        "options": ["Energy signals", "Power signals", "Neither", "Both"],
        "ans": "Power signals",
        "explain_correct": "الإشارات الدورية بتكرر نفسها للمالانهاية، فمساحتها الإجمالية (الطاقة) مالانهاية، وبالتالي هي Power signals. ✅",
        "explain_wrong": "الإشارات الدورية دائماً Power Signals."
    },
    {
        "q": "Transient signals (signals that start and eventually decay to zero, like e^(-at)u(t)) are generally classified as:",
        "type": "mcq",
        "options": ["Energy signals", "Power signals", "Neither", "Periodic"],
        "ans": "Energy signals",
        "explain_correct": "الإشارة اللي بتموت وتختفي بمرور الزمن مساحتها بتكون محدودة، وبالتالي هي Energy Signal. ✅",
        "explain_wrong": "الإشارات المضمحلة (Decaying) طاقتها محدودة."
    },
    {
        "q": "How do you calculate the Power of a PERIODIC continuous-time signal?",
        "type": "mcq",
        "options": ["Integrate |x(t)|^2 from -∞ to ∞", "Integrate |x(t)|^2 over one period T0, then divide by T0", "Integrate x(t) over one period", "It is always zero"],
        "ans": "Integrate |x(t)|^2 over one period T0, then divide by T0",
        "explain_correct": "في الإشارات الدورية، بنحسب الـ Power على دورة واحدة بس (T0) ونقسم على T0 للتسهيل. ✅",
        "explain_wrong": "الدورية بتسمح لنا نكتفي بدورة واحدة لحساب المتوسط."
    },
    {
        "q": "What is the average Power of the complex exponential signal x(t) = A * e^{j(w0 t + θ)}?",
        "type": "mcq",
        "options": ["A^2", "A^2 / 2", "0", "Infinity"],
        "ans": "A^2",
        "explain_correct": "معيار |e^{j...}| يساوي 1، إذن |x(t)|^2 = A^2. وتكامل رقم ثابت متوسطه هو الرقم نفسه A^2. ✅",
        "explain_wrong": "الـ Power للـ Complex exponential تساوي مربع الـ Amplitude."
    },
    {
        "q": "What is the average Power of the sinusoidal signal x(t) = A * cos(w0 t + θ)?",
        "type": "mcq",
        "options": ["A^2", "A^2 / 2", "A", "A / 2"],
        "ans": "A^2 / 2",
        "explain_correct": "الـ Power للـ Sin أو Cos دايماً بتساوي مربع الـ Amplitude مقسوم على 2. ✅",
        "explain_wrong": "تذكر: الـ Power للـ Sinusoids = (A^2)/2."
    },
    {
        "q": "From Lecture 3 notes: Evaluate the Energy of the discrete signal x[n] = (-0.5)^n * u[n].",
        "type": "mcq",
        "options": ["Infinity", "1.333 (or 4/3)", "0.5", "2"],
        "ans": "1.333 (or 4/3)",
        "explain_correct": "E = Σ |(-0.5)^n|^2 = Σ (0.25)^n من n=0 لـ ∞. المجموع = 1 / (1 - 0.25) = 1 / 0.75 = 4/3. ✅",
        "explain_wrong": "استخدم قانون المجموع للمتسلسلة الهندسية: 1 / (1 - r)."
    },
    {
        "q": "From Lecture 3 notes: Evaluate the Power of the discrete unit step sequence x[n] = u[n].",
        "type": "mcq",
        "options": ["0", "1", "0.5", "Infinity"],
        "ans": "0.5",
        "explain_correct": "الـ Power = Limit (N->∞) [ (1 / (2N+1)) * Σ 1 (from 0 to N) ] = Limit (N+1)/(2N+1) = 1/2. ✅",
        "explain_wrong": "دالة u[n] تغطي نصف الزمن الكلي (الجانب الموجب)، لذلك متوسط قدرتها 0.5."
    },
    {
        "q": "If the energy of x(t) is E, what is the energy of the scaled signal y(t) = 2x(t)?",
        "type": "mcq",
        "options": ["E", "2E", "4E", "0.5E"],
        "ans": "4E",
        "explain_correct": "الطاقة تتناسب مع مربع الإشارة |x(t)|^2. إذن ضرب الإشارة في 2 يضرب طاقتها في 2^2 = 4. ✅",
        "explain_wrong": "Energy is proportional to Amplitude SQUARED."
    },
    
    # ─── Part 5: Assorted Pulse Operations (Sheet 3) ───
    {
        "q": "The rectangular pulse function, rect(t/T), has a total width of:",
        "type": "mcq",
        "options": ["T/2", "T", "2T", "1"],
        "ans": "T",
        "explain_correct": "دالة الـ rect(t/T) بتمتد من -T/2 إلى T/2، فإجمالي عرضها بيساوي T. ✅",
        "explain_wrong": "المقام T يمثل العرض الكلي للنبضة المستطيلة."
    },
    {
        "q": "The triangular pulse function, Δ(t/T), has a total width at the base of:",
        "type": "mcq",
        "options": ["T", "T/2", "2T", "1"],
        "ans": "2T",
        "explain_correct": "دالة الـ Triangle بتمتد من -T إلى T، فإجمالي عرض القاعدة بيساوي 2T. ✅",
        "explain_wrong": "المقام T يمثل نصف العرض في المثلث، فالعرض الكلي 2T."
    },
    {
        "q": "If a continuous signal is defined as a straight line from (0,0) to (1,2) and 0 elsewhere, it can be written as:",
        "type": "mcq",
        "options": ["2t * [u(t) - u(t-1)]", "t * u(t-1)", "2t * u(t)", "u(t) - 2u(t-1)"],
        "ans": "2t * [u(t) - u(t-1)]",
        "explain_correct": "معادلة الخط هي 2t. وبما إنه موجود من 0 لـ 1 بس، بنضربه في النافذة [u(t) - u(t-1)]. ✅",
        "explain_wrong": "النافذة [u(t)-u(t-1)] بتخلي الإشارة تشتغل في الفترة من 0 لـ 1 بس."
    },
    {
        "q": "To express the signal x(t) = |t| for -1 <= t <= 1 using step functions, we write:",
        "type": "mcq",
        "options": ["t*u(t)", "-t[u(t+1)-u(t)] + t[u(t)-u(t-1)]", "t[u(t+1)-u(t-1)]", "|t|*u(t)"],
        "ans": "-t[u(t+1)-u(t)] + t[u(t)-u(t-1)]",
        "explain_correct": "الـ Absolute value في السالب معادلته (-t) وفي الموجب معادلته (t). بنضرب كل جزء في النافذة بتاعته. ✅",
        "explain_wrong": "قسّم الـ |t| لجزئين: جزء من -1 لـ 0، وجزء من 0 لـ 1."
    }
]