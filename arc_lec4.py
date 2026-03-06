# ════════════════════════════════════════════════════════════
# 📖 arc_lec4.py
# Computer Architecture & Organization - Lecture 4 (Bus Construction)
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # ✅ MCQ Questions (40 Questions)
    # ══════════════════════════════════════════════

    {
        "q": "What does a bus consist of?",
        "type": "mcq",
        "options": [
            "A set of common lines, one for each bit of a register",
            "A single line that transfers all data simultaneously",
            "A memory storage unit inside the CPU",
            "A software program that controls data flow"
        ],
        "ans": "A set of common lines, one for each bit of a register",
        "explain_correct": "✅ صح! الـ Bus هو مجموعة من الخطوط المشتركة (Common lines)، كل خط مخصص لـ bit معين من الـ Register.",
        "explain_wrong": "❌ غلط! الـ Bus بيتكون من مجموعة خطوط مشتركة (set of common lines) مش خط واحد."
    },
    {
        "q": "How is binary information transferred through a bus?",
        "type": "mcq",
        "options": [
            "One at a time",
            "All registers at exactly the same time",
            "Randomly based on clock speed",
            "In continuous analog waves"
        ],
        "ans": "One at a time",
        "explain_correct": "✅ صح! المعلومات بتتنقل عبر الـ Bus حاجة بحاجة (One at a time) من register لآخر.",
        "explain_wrong": "❌ غلط! الـ Bus بينقل البيانات (One at a time) مش كلهم في نفس اللحظة."
    },
    {
        "q": "What determines which register is selected by the bus during a register transfer?",
        "type": "mcq",
        "options": [
            "Control signals",
            "The ALU",
            "The memory size",
            "The clock speed"
        ],
        "ans": "Control signals",
        "explain_correct": "✅ صح! الـ Control signals هي اللي بتحدد انهي register هيتم اختياره لنقل البيانات.",
        "explain_wrong": "❌ غلط! إشارات التحكم (Control signals) هي المسؤولة عن اختيار الـ register."
    },
    {
        "q": "What are the two ways mentioned to construct a bus in a computer?",
        "type": "mcq",
        "options": [
            "Multiplexers and Three-state buffers",
            "Decoders and Encoders",
            "Adders and Subtractors",
            "Flip-flops and Registers"
        ],
        "ans": "Multiplexers and Three-state buffers",
        "explain_correct": "✅ صح! بناء الـ Bus بيتم إما باستخدام الـ Multiplexers أو الـ Three-state buffers.",
        "explain_wrong": "❌ غلط! الطريقتين هما الـ Multiplexers والـ Three-state buffers."
    },
    {
        "q": "What is a multiplexer (MUX)?",
        "type": "mcq",
        "options": [
            "A device that selects one of several input signals and forwards it into a single line",
            "A device that stores multiple bits of data permanently",
            "A device that performs arithmetic additions",
            "A device that converts analog signals to digital"
        ],
        "ans": "A device that selects one of several input signals and forwards it into a single line",
        "explain_correct": "✅ صح! الملتيبلكسر بيختار إشارة واحدة من بين مدخلات كتير وبيطلعها على خط واحد (single line).",
        "explain_wrong": "❌ غلط! الملتيبلكسر وظيفته يختار input واحد من ضمن اختيارات كتير ويعديه."
    },
    {
        "q": "How many select lines does a multiplexer with 2^N inputs have?",
        "type": "mcq",
        "options": [
            "N",
            "2N",
            "N^2",
            "N/2"
        ],
        "ans": "N",
        "explain_correct": "✅ صح! حسب القانون: لو عندنا 2 أس N من المداخل، هنحتاج N خطوط للاختيار (Select lines).",
        "explain_wrong": "❌ غلط! القاعدة هي إن 2^N inputs بيحتاجوا N select lines."
    },
    {
        "q": "If a computer has 16 registers, how many selection inputs are required in each multiplexer?",
        "type": "mcq",
        "options": [
            "4",
            "8",
            "16",
            "32"
        ],
        "ans": "4",
        "explain_correct": "✅ صح! بما إن عدد الـ registers هو 16، يبقى 2^s = 16، إذاً s = 4 (أربع خطوط اختيار).",
        "explain_wrong": "❌ غلط! بنحسبها بقانون 2^s = n. الـ n بـ 16 يبقى الـ s بـ 4."
    },
    {
        "q": "If a computer has a common bus system for 16 registers, what size of multiplexers are needed?",
        "type": "mcq",
        "options": [
            "16 x 1 multiplexers",
            "4 x 1 multiplexers",
            "32 x 1 multiplexers",
            "8 x 1 multiplexers"
        ],
        "ans": "16 x 1 multiplexers",
        "explain_correct": "✅ صح! حجم الملتيبلكسر بيتحدد بعدد الـ registers، فهنحتاج ملتيبلكسر بـ 16 مدخل ومخرج واحد (16 x 1).",
        "explain_wrong": "❌ غلط! الحجم بيتحدد بعدد الـ registers (المداخل). بما إنهم 16، يبقى الحجم 16x1."
    },
    {
        "q": "In a common bus system, how many multiplexers are there on the bus if the registers are 32 bits wide?",
        "type": "mcq",
        "options": [
            "32",
            "16",
            "4",
            "64"
        ],
        "ans": "32",
        "explain_correct": "✅ صح! بنحتاج ملتيبلكسر واحد لكل bit. بما إن الـ register فيه 32 bits، يبقى محتاجين 32 ملتيبلكسر.",
        "explain_wrong": "❌ غلط! عدد الملتيبلكسرات بيساوي عدد الـ bits في الـ register. يعني 32."
    },
    {
        "q": "If a system has 8 registers, how many select lines are required?",
        "type": "mcq",
        "options": [
            "3",
            "4",
            "8",
            "2"
        ],
        "ans": "3",
        "explain_correct": "✅ صح! 2^3 = 8، إذن محتاجين 3 خطوط اختيار (Select lines).",
        "explain_wrong": "❌ غلط! 2 أس كام يساوي 8؟ 2 أس 3. يبقى محتاجين 3 select lines."
    },
    {
        "q": "If a system has 64 registers, how many select lines are required?",
        "type": "mcq",
        "options": [
            "6",
            "8",
            "32",
            "4"
        ],
        "ans": "6",
        "explain_correct": "✅ صح! 2^6 = 64، إذن محتاجين 6 خطوط اختيار.",
        "explain_wrong": "❌ غلط! بقانون 2^s = n، إذن 2^6 = 64، فالاختيار الصح هو 6."
    },
    {
        "q": "If registers are 16 bits wide, how many multiplexers are needed on the bus?",
        "type": "mcq",
        "options": [
            "16",
            "8",
            "32",
            "4"
        ],
        "ans": "16",
        "explain_correct": "✅ صح! بنحتاج ملتيبلكسر واحد لكل bit، فلو العرض 16 bits هنحتاج 16 MUX.",
        "explain_wrong": "❌ غلط! عدد الملتيبلكسرات بيساوي بالظبط عرض الـ register بالـ bits. يعني 16."
    },
    {
        "q": "The size of a multiplexer (e.g., 16 x 1) is primarily defined by:",
        "type": "mcq",
        "options": [
            "The number of registers it can choose from",
            "The number of bits in a register",
            "The number of select lines",
            "The clock frequency"
        ],
        "ans": "The number of registers it can choose from",
        "explain_correct": "✅ صح! حجم الـ MUX (عدد مداخله) بيتحدد بناءً على عدد الـ registers اللي بيختار منها.",
        "explain_wrong": "❌ غلط! حجم الملتيبلكسر (عدد المداخل) بيتحدد بناءً على عدد الـ Registers."
    },
    {
        "q": "What is a three-state gate?",
        "type": "mcq",
        "options": [
            "A digital circuit that exhibits three states",
            "A gate that requires three power sources",
            "A gate that outputs only negative voltages",
            "A multiplexer with exactly three inputs"
        ],
        "ans": "A digital circuit that exhibits three states",
        "explain_correct": "✅ صح! الـ Three-state gate هي دايرة رقمية ليها 3 حالات مختلفة.",
        "explain_wrong": "❌ غلط! الـ Three-state gate هي دايرة بتمتلك 3 حالات (0, 1, High-impedance)."
    },
    {
        "q": "Which of the following is NOT a state of a three-state buffer?",
        "type": "mcq",
        "options": [
            "Logic 2",
            "Logic 1",
            "Logic 0",
            "High-impedance state"
        ],
        "ans": "Logic 2",
        "explain_correct": "✅ صح! مفيش حاجة اسمها Logic 2 في الدواير دي. الحالات هي (1, 0, High-impedance).",
        "explain_wrong": "❌ غلط! الـ Logic 2 مش موجود! الحالات هي صفر، أو واحد، أو High-impedance."
    },
    {
        "q": "What does the high-impedance state behave like?",
        "type": "mcq",
        "options": [
            "An open circuit",
            "A closed circuit",
            "A short circuit",
            "An amplifier"
        ],
        "ans": "An open circuit",
        "explain_correct": "✅ صح! الـ High-impedance بيتعامل كأنه دايرة مفتوحة (Open circuit) يعني مفيش تيار بيمر.",
        "explain_wrong": "❌ غلط! الـ High-impedance بيتصرف كأنه Open circuit."
    },
    {
        "q": "In the high-impedance state, the output is:",
        "type": "mcq",
        "options": [
            "Disconnected and has no logic significance",
            "Forced to Logic 1",
            "Forced to Logic 0",
            "Multiplying the input signal"
        ],
        "ans": "Disconnected and has no logic significance",
        "explain_correct": "✅ صح! في الحالة دي، الـ output بيكون مفصول (disconnected) وملوش أي معنى منطقي.",
        "explain_wrong": "❌ غلط! في الـ High-impedance المخرج بيكون مفصول وملوش أي logic significance."
    },
    {
        "q": "What component is used to ensure that no more than one buffer is active at any given time in a three-state bus?",
        "type": "mcq",
        "options": [
            "A decoder",
            "An encoder",
            "A multiplexer",
            "A flip-flop"
        ],
        "ans": "A decoder",
        "explain_correct": "✅ صح! الـ Decoder بيُستخدم عشان يضمن إن buffer واحد بس هو اللي شغال في نفس الوقت.",
        "explain_wrong": "❌ غلط! بنستخدم الـ Decoder عشان نضمن إن خط واحد بس اللي Active."
    },
    {
        "q": "What is a decoder?",
        "type": "mcq",
        "options": [
            "A combinational circuit that converts binary info from N inputs to max 2^N outputs",
            "A circuit that adds two binary numbers",
            "A memory element that stores a single bit",
            "A device that selects one input and forwards it to a single output"
        ],
        "ans": "A combinational circuit that converts binary info from N inputs to max 2^N outputs",
        "explain_correct": "✅ صح! ده التعريف الدقيق للـ Decoder.",
        "explain_wrong": "❌ غلط! الـ Decoder بيحول N مداخل لعدد أقصاه 2^N من المخارج."
    },
    {
        "q": "A 2 to 4 decoder has:",
        "type": "mcq",
        "options": [
            "2 inputs and 4 outputs",
            "4 inputs and 2 outputs",
            "2 inputs and 2 outputs",
            "4 inputs and 4 outputs"
        ],
        "ans": "2 inputs and 4 outputs",
        "explain_correct": "✅ صح! اسمه 2 to 4، يعني بياخد مدخلين وبيطلع 4 مخارج.",
        "explain_wrong": "❌ غلط! هو 2 to 4، يعني 2 inputs وبيطلع 4 outputs."
    },
    {
        "q": "A 3 to 8 decoder has:",
        "type": "mcq",
        "options": [
            "3 inputs and 8 outputs",
            "8 inputs and 3 outputs",
            "3 inputs and 3 outputs",
            "8 inputs and 8 outputs"
        ],
        "ans": "3 inputs and 8 outputs",
        "explain_correct": "✅ صح! بياخد 3 مداخل وبيطلع 8 مخارج (2^3 = 8).",
        "explain_wrong": "❌ غلط! الـ 3 to 8 decoder بياخد 3 مداخل ويطلع 8 مخارج."
    },
    {
        "q": "Computer architecture is classified into two types according to memory architecture. What are they?",
        "type": "mcq",
        "options": [
            "Von Neumann and Harvard",
            "RISC and CISC",
            "Static and Dynamic",
            "Synchronous and Asynchronous"
        ],
        "ans": "Von Neumann and Harvard",
        "explain_correct": "✅ صح! التقسيمة من حيث الميموري هي Von Neumann و Harvard.",
        "explain_wrong": "❌ غلط! أنواع العمارة بناءً على الميموري هما Von Neumann و Harvard."
    },
    {
        "q": "In Von Neumann architecture, where are data and instructions stored?",
        "type": "mcq",
        "options": [
            "In the same memory",
            "In completely separate memory units",
            "Inside the ALU",
            "On the hard drive only"
        ],
        "ans": "In the same memory",
        "explain_correct": "✅ صح! في الـ Von Neumann، الداتا والتعليمات بيتخزنوا مع بعض في نفس الميموري.",
        "explain_wrong": "❌ غلط! الـ Von Neumann بيخزن الـ data والـ instructions في نفس الميموري."
    },
    {
        "q": "In Von Neumann architecture, how are data and instructions accessed from memory?",
        "type": "mcq",
        "options": [
            "Via a single bus",
            "Through two separate buses",
            "Using three-state buffers only",
            "Without using any bus"
        ],
        "ans": "Via a single bus",
        "explain_correct": "✅ صح! الـ Von Neumann بيستخدم Bus واحد بس لنقل الداتا والتعليمات.",
        "explain_wrong": "❌ غلط! الـ Von Neumann بيعتمد على Single bus فقط."
    },
    {
        "q": "In Harvard architecture, where are data and instructions stored?",
        "type": "mcq",
        "options": [
            "In separate memory units",
            "In the same memory",
            "Inside the CPU registers only",
            "In the input/output devices"
        ],
        "ans": "In separate memory units",
        "explain_correct": "✅ صح! الـ Harvard بيفصل الميموري، واحدة للداتا وواحدة للتعليمات.",
        "explain_wrong": "❌ غلط! الـ Harvard بيخزن الداتا في ميموري، والتعليمات في ميموري تانية منفصلة."
    },
    {
        "q": "In Harvard architecture, how are the separate memory units accessed?",
        "type": "mcq",
        "options": [
            "Through different buses",
            "Via a single bus",
            "Through a single multiplexer",
            "Without any buses"
        ],
        "ans": "Through different buses",
        "explain_correct": "✅ صح! بما إن الميموري منفصلة، يبقى كل ميموري ليها Bus خاص بيها.",
        "explain_wrong": "❌ غلط! الـ Harvard بيستخدم Different buses لكل ميموري."
    },
    {
        "q": "Which architecture allows parallel access to data and instructions?",
        "type": "mcq",
        "options": [
            "Harvard",
            "Von Neumann",
            "Both of them",
            "Neither of them"
        ],
        "ans": "Harvard",
        "explain_correct": "✅ صح! وجود 2 buses في الـ Harvard بيسمح إننا نقرأ داتا وتعليمات في نفس اللحظة (Parallel).",
        "explain_wrong": "❌ غلط! الـ Harvard هو اللي بيسمح بالـ Parallel access عشان عنده 2 buses."
    },
    {
        "q": "In which architecture can the data memory and instruction memory use different sizes?",
        "type": "mcq",
        "options": [
            "Harvard",
            "Von Neumann",
            "Only RISC architectures",
            "Only CISC architectures"
        ],
        "ans": "Harvard",
        "explain_correct": "✅ صح! لأنهم منفصلين، كل ميموري ممكن يكون ليها حجم مختلف عن التانية في الـ Harvard.",
        "explain_wrong": "❌ غلط! الـ Harvard هو اللي بيسمح باختلاف الأحجام لأن الميموري منفصلة."
    },
    {
        "q": "Which architecture has a simpler Control Unit design due to having only one bus?",
        "type": "mcq",
        "options": [
            "Von Neumann",
            "Harvard",
            "Both have identical Control Units",
            "Neither"
        ],
        "ans": "Von Neumann",
        "explain_correct": "✅ صح! لأن فيه Bus واحد بس، فتصميم الـ Control Unit في الـ Von Neumann بيكون أبسط.",
        "explain_wrong": "❌ غلط! الـ Von Neumann تصميمه أبسط لأن فيه Bus واحد."
    },
    {
        "q": "In which architecture is the development of the Control Unit cheaper and faster?",
        "type": "mcq",
        "options": [
            "Von Neumann",
            "Harvard",
            "Both take the same time and cost",
            "None of the above"
        ],
        "ans": "Von Neumann",
        "explain_correct": "✅ صح! لبساطة التصميم، تطويره بيكون أرخص وأسرع في الـ Von Neumann.",
        "explain_wrong": "❌ غلط! الـ Von Neumann تطويره أرخص وأسرع لبساطة الـ Control Unit."
    },
    {
        "q": "Which architecture accesses data and instructions in the exact same way?",
        "type": "mcq",
        "options": [
            "Von Neumann",
            "Harvard",
            "Both of them",
            "Neither of them"
        ],
        "ans": "Von Neumann",
        "explain_correct": "✅ صح! لأنهم في نفس الميموري وبيستخدموا نفس الـ Bus، فبيتم الوصول ليهم بنفس الطريقة في الـ Von Neumann.",
        "explain_wrong": "❌ غلط! الـ Von Neumann هو اللي بيتعامل معاهم بنفس الطريقة لأنهم في نفس الميموري."
    },
    {
        "q": "Why is a computer with Von Neumann architecture generally cheaper?",
        "type": "mcq",
        "options": [
            "Because it uses one bus",
            "Because it uses two buses",
            "Because it doesn't have a CPU",
            "Because it uses Harvard memory"
        ],
        "ans": "Because it uses one bus",
        "explain_correct": "✅ صح! توفير الهاردوير واستخدام Bus واحد بيخلي التكلفة أقل.",
        "explain_wrong": "❌ غلط! هو أرخص عشان بيستخدم Bus واحد بس."
    },
    {
        "q": "What is the main bottleneck (عيب الزحمة) in Von Neumann architecture?",
        "type": "mcq",
        "options": [
            "One bus for data, instructions, and devices",
            "Too many buses",
            "Separation of memory",
            "Complicated Control Unit"
        ],
        "ans": "One bus for data, instructions, and devices",
        "explain_correct": "✅ صح! الاعتماد على Bus واحد بينقل كل حاجة بيعمل زحمة وبطء (Bottleneck).",
        "explain_wrong": "❌ غلط! الـ Bottleneck بيحصل بسبب وجود Bus واحد بينقل كل حاجة."
    },
    {
        "q": "In which architecture can a program error rewrite an instruction and crash program execution?",
        "type": "mcq",
        "options": [
            "Von Neumann",
            "Harvard",
            "Both of them",
            "Neither of them"
        ],
        "ans": "Von Neumann",
        "explain_correct": "✅ صح! لأن الداتا والتعليمات في نفس المكان، أي خطأ برمجي ممكن يخلي الداتا تكتب فوق التعليمات وتعمل Crash.",
        "explain_wrong": "❌ غلط! دي مشكلة في الـ Von Neumann لأن الداتا والتعليمات سايحين على بعض في نفس الميموري."
    },
    {
        "q": "Which architecture requires more time to develop a complicated Control Unit?",
        "type": "mcq",
        "options": [
            "Harvard",
            "Von Neumann",
            "They both require the same time",
            "None of the above"
        ],
        "ans": "Harvard",
        "explain_correct": "✅ صح! لأن الـ Control Unit في الـ Harvard لازم يتحكم في 2 Buses منفصلين، فبيكون معقد وبياخد وقت.",
        "explain_wrong": "❌ غلط! الـ Harvard هو اللي الـ Control Unit بتاعه معقد وبياخد وقت في التطوير."
    },
    {
        "q": "Which architecture's control unit is more complicated and expensive because it handles two buses?",
        "type": "mcq",
        "options": [
            "Harvard",
            "Von Neumann",
            "Both have the same complexity",
            "Neither"
        ],
        "ans": "Harvard",
        "explain_correct": "✅ صح! الـ Harvard أغلى وأعقد عشان فيه 2 Buses.",
        "explain_wrong": "❌ غلط! الـ Harvard هو اللي أعقد وأغلى بسبب الـ 2 Buses."
    },
    {
        "q": "In which architecture is it true that \"Free data memory can’t be used for instructions and vice-versa\"?",
        "type": "mcq",
        "options": [
            "Harvard",
            "Von Neumann",
            "Both of them",
            "Neither of them"
        ],
        "ans": "Harvard",
        "explain_correct": "✅ صح! لأن الميموري مقسومة هاردوير، فلو مساحة الداتا فاضية، متقدرش تستخدمها للتعليمات والعكس.",
        "explain_wrong": "❌ غلط! دي من عيوب الـ Harvard لأن الميموري مقسومة جزئين منفصلين تماماً."
    },
    {
        "q": "In which architecture is it true that a \"Program can’t write itself\"?",
        "type": "mcq",
        "options": [
            "Harvard",
            "Von Neumann",
            "Both of them",
            "Neither of them"
        ],
        "ans": "Harvard",
        "explain_correct": "✅ صح! من عيوب الـ Harvard المذكورة في المحاضرة إن الـ Program can't write itself.",
        "explain_wrong": "❌ غلط! دي من ضمن الـ Disadvantages بتاعة الـ Harvard."
    },
    {
        "q": "Application: If you have 4 registers of 8 bits each, what is the required bus configuration using MUXs?",
        "type": "mcq",
        "options": [
            "8 multiplexers of size 4x1",
            "4 multiplexers of size 8x1",
            "8 multiplexers of size 8x1",
            "4 multiplexers of size 4x1"
        ],
        "ans": "8 multiplexers of size 4x1",
        "explain_correct": "✅ صح! عدد الملتيبلكسرات = عرض الـ bit (وهو 8). وحجم الملتيبلكسر = عدد الـ registers (وهما 4). يبقى 8 ملتيبلكسرات بحجم 4x1.",
        "explain_wrong": "❌ غلط! عدد الـ MUXs بيساوي عرض الـ bits (8). وحجم الـ MUX بيساوي عدد الـ registers (4). يبقى 8 MUXs بحجم 4x1."
    },
    {
        "q": "Application: To control a 32-register bus using three-state buffers, what size of decoder is required?",
        "type": "mcq",
        "options": [
            "5 x 32 Decoder",
            "4 x 16 Decoder",
            "3 x 8 Decoder",
            "6 x 64 Decoder"
        ],
        "ans": "5 x 32 Decoder",
        "explain_correct": "✅ صح! عشان نفك شفرة 32 مخرج (32 Registers)، هنحتاج 5 مداخل لأن 2^5 = 32.",
        "explain_wrong": "❌ غلط! محتاجين Decoder يطلع 32 مخرج، يبقى لازم يكون ليه 5 مداخل (5 x 32)."
    },

    # ══════════════════════════════════════════════
    # ✅ True / False Questions (10 Questions)
    # ══════════════════════════════════════════════

    {
        "q": "A bus transfers binary information for all registers at exactly the same time.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط، الـ Bus بينقل البيانات لـ register واحد بس في المرة (One at a time).",
        "explain_wrong": "❌ غلط! الـ Bus بينقل المعلومات one at a time، مش كلهم في نفس اللحظة."
    },
    {
        "q": "A multiplexer with 2^N inputs requires N select lines.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! دي القاعدة الأساسية للملتيبلكسر.",
        "explain_wrong": "❌ غلط! العبارة صحيحة تماماً، 2^N inputs بيحتاجوا N select lines."
    },
    {
        "q": "To construct a common bus for 32 registers using multiplexers, you need 5 selection lines.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! لأن 2^5 = 32، فبنحتاج 5 خطوط اختيار.",
        "explain_wrong": "❌ غلط! العبارة صحيحة، 2 أس 5 بـ 32."
    },
    {
        "q": "The number of multiplexers required on a bus is determined by the number of registers, not the register width.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط، عدد الملتيبلكسرات بيتحدد بعرض الـ register (عدد الـ bits)، مش بعدد الـ registers.",
        "explain_wrong": "❌ غلط! العبارة خاطئة، لأن عدد الملتيبلكسرات بيعتمد على عدد الـ Bits (Register Width)."
    },
    {
        "q": "The high-impedance state in a three-state buffer behaves like an open circuit.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! الـ High-impedance بيعزل المخرج تماماً كأنه Open circuit.",
        "explain_wrong": "❌ غلط! العبارة صحيحة، الـ High-impedance فعلاً بيتصرف كأنه Open circuit."
    },
    {
        "q": "A decoder is used in a three-state buffer bus to allow multiple buffers to be active simultaneously.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط، الـ Decoder بيُستخدم عشان يضمن إن buffer **واحد بس** هو اللي شغال، مش أكتر من واحد.",
        "explain_wrong": "❌ غلط! الـ Decoder بيستخدم عشان يضمن إن buffer واحد بس يكون Active، مش كذا واحد."
    },
    {
        "q": "Von Neumann architecture uses separate memory units for data and instructions.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط، الـ Harvard هي اللي بتفصلهم. لكن الـ Von Neumann بيحطهم مع بعض في نفس الميموري.",
        "explain_wrong": "❌ غلط! العبارة خاطئة، الـ Von Neumann بيخزن الداتا والتعليمات في نفس الميموري."
    },
    {
        "q": "Harvard architecture allows parallel access to data and instructions because it uses separate buses.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! دي من أهم مميزات الـ Harvard.",
        "explain_wrong": "❌ غلط! العبارة صحيحة، وجود 2 buses بيسمح بالوصول ليهم بالتوازي (Parallel)."
    },
    {
        "q": "In Von Neumann architecture, a program error cannot rewrite instructions and crash the program.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط، لأنه ممكن فعلاً يعمل Crash لأنهم متخزنين مع بعض في نفس المكان.",
        "explain_wrong": "❌ غلط! العبارة خاطئة، في الـ Von Neumann الخطأ ممكن يكتب فوق التعليمات ويعمل Crash."
    },
    {
        "q": "A disadvantage of Harvard architecture is that free data memory cannot be used to store instructions.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! لأن الميموري مقسومة، فمساحة دي متقدرش تسلف دي.",
        "explain_wrong": "❌ غلط! العبارة صحيحة، دي فعلاً واحدة من عيوب الـ Harvard."
    }
]