# ════════════════════════════════════════════════════════════
# 📖 arc_lec1.py
# Computer Architecture & Organization - Lecture 1
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # ✅ MCQ Questions 
    # ══════════════════════════════════════════════

    {
        "q": "What does Computer Organization deal with?",
        "type": "mcq",
        "options": [
            "How hardware components are interconnected and operate to execute instructions",
            "The attributes of a system visible to the programmer",
            "The instruction set of a processor",
            "The number of bits used to represent data types"
        ],
        "ans": "How hardware components are interconnected and operate to execute instructions",
        "explain_correct": "✅ صح! Computer Organization بتتكلم عن ازاي الـ hardware components بتتربط ببعض وبتشتغل عشان تنفذ الـ instructions.",
        "explain_wrong": "❌ غلط! ده تعريف Computer Organization — بيتكلم عن الـ hardware وازاي بيشتغل."
    },
    {
        "q": "Which of the following is an example of a Computer Organization attribute?",
        "type": "mcq",
        "options": [
            "Whether there is a hardware multiply unit or it is done by repeated addition",
            "Whether there is a multiply instruction",
            "The number of bits used to represent integers",
            "The instruction set of the processor"
        ],
        "ans": "Whether there is a hardware multiply unit or it is done by repeated addition",
        "explain_correct": "✅ صح! وجود hardware multiply unit من عدمه ده organizational attribute لأنه شفاف على المبرمج.",
        "explain_wrong": "❌ غلط! وجود hardware multiply unit هو مثال على الـ Organization مش الـ Architecture."
    },
    {
        "q": "What does Computer Architecture refer to?",
        "type": "mcq",
        "options": [
            "Those attributes of a system visible to the programmer",
            "How hardware components are interconnected",
            "The control signals between components",
            "The memory technology used"
        ],
        "ans": "Those attributes of a system visible to the programmer",
        "explain_correct": "✅ صح! Computer Architecture هي الـ attributes اللي بيشوفها المبرمج وبيأثر عليها مباشرة.",
        "explain_wrong": "❌ غلط! الـ Architecture بتتكلم عن الـ attributes اللي ظاهرة للمبرمج."
    },
    {
        "q": "Which term is often used interchangeably with Computer Architecture?",
        "type": "mcq",
        "options": [
            "Instruction Set Architecture (ISA)",
            "Computer Organization",
            "Operating System Design",
            "Circuit Design"
        ],
        "ans": "Instruction Set Architecture (ISA)",
        "explain_correct": "✅ صح! الـ ISA بيتقال عليها Computer Architecture في كتير من الأحيان.",
        "explain_wrong": "❌ غلط! المصطلح اللي بيتبادل مع Computer Architecture هو Instruction Set Architecture (ISA)."
    },
    {
        "q": "Which of the following is an example of an architectural attribute?",
        "type": "mcq",
        "options": [
            "Whether there is a multiply instruction",
            "Whether multiplication is done by repeated addition",
            "The type of memory technology used",
            "The control signals used"
        ],
        "ans": "Whether there is a multiply instruction",
        "explain_correct": "✅ صح! وجود multiply instruction في الـ instruction set ده architectural attribute لأن المبرمج بيشوفه.",
        "explain_wrong": "❌ غلط! وجود multiply instruction هو architectural attribute مش organizational."
    },
    {
        "q": "What is 'Structure' in the context of computer systems?",
        "type": "mcq",
        "options": [
            "The way in which components relate to each other",
            "The operation of individual components",
            "The attributes visible to the programmer",
            "The hardware details transparent to the programmer"
        ],
        "ans": "The way in which components relate to each other",
        "explain_correct": "✅ صح! الـ Structure هي الطريقة اللي بيها الـ components بتتعلق ببعض.",
        "explain_wrong": "❌ غلط! الـ Structure هي العلاقة بين الـ components مع بعض."
    },
    {
        "q": "What is 'Function' in the context of computer systems?",
        "type": "mcq",
        "options": [
            "The operation of individual components as part of the structure",
            "The way components relate to each other",
            "The instruction set visible to the programmer",
            "The memory hierarchy design"
        ],
        "ans": "The operation of individual components as part of the structure",
        "explain_correct": "✅ صح! الـ Function هي عملية كل component منفردة كجزء من الـ structure.",
        "explain_wrong": "❌ غلط! الـ Function بتتكلم عن شغل كل component لوحده كجزء من الـ structure."
    },
    {
        "q": "What is the main role of the CPU?",
        "type": "mcq",
        "options": [
            "Controls the operation of the computer and performs data processing",
            "Stores data permanently",
            "Moves data between computer and peripherals",
            "Provides communication among components"
        ],
        "ans": "Controls the operation of the computer and performs data processing",
        "explain_correct": "✅ صح! الـ CPU بيتحكم في عمليات الكمبيوتر وبينفذ عمليات معالجة البيانات.",
        "explain_wrong": "❌ غلط! الـ CPU مهمته التحكم في عمليات الكمبيوتر ومعالجة البيانات."
    },
    {
        "q": "What is the main role of Main Memory?",
        "type": "mcq",
        "options": [
            "Stores data",
            "Controls the computer operations",
            "Moves data between computer and peripherals",
            "Executes instructions"
        ],
        "ans": "Stores data",
        "explain_correct": "✅ صح! الـ Main Memory مهمتها تخزين البيانات.",
        "explain_wrong": "❌ غلط! الـ Main Memory مهمتها الأساسية هي تخزين البيانات."
    },
    {
        "q": "What is the role of I/O in a computer system?",
        "type": "mcq",
        "options": [
            "Moves data between the computer and its external environment",
            "Stores data permanently",
            "Controls the CPU operations",
            "Provides power to components"
        ],
        "ans": "Moves data between the computer and its external environment",
        "explain_correct": "✅ صح! الـ I/O بينقل البيانات بين الكمبيوتر والبيئة الخارجية (peripherals).",
        "explain_wrong": "❌ غلط! الـ I/O مهمته نقل البيانات بين الكمبيوتر والـ peripherals."
    },
    {
        "q": "What is the role of System Interconnection?",
        "type": "mcq",
        "options": [
            "Provides communication among CPU, main memory, and I/O",
            "Stores data for the CPU",
            "Controls input and output devices",
            "Executes assembly language instructions"
        ],
        "ans": "Provides communication among CPU, main memory, and I/O",
        "explain_correct": "✅ صح! الـ System Interconnection بيوفر التواصل بين الـ CPU والـ Main Memory والـ I/O.",
        "explain_wrong": "❌ غلط! الـ System Interconnection مهمته التواصل بين الـ CPU والـ Memory والـ I/O."
    },
    {
        "q": "Which of the following is a hardware detail 'transparent' to the programmer?",
        "type": "mcq",
        "options": [
            "Control signals between components",
            "The instruction set",
            "Number of bits for data types",
            "I/O mechanisms"
        ],
        "ans": "Control signals between components",
        "explain_correct": "✅ صح! الـ control signals شفافة للمبرمج يعني مش محتاج يعرفها عشان يبرمج.",
        "explain_wrong": "❌ غلط! الـ control signals هي من الـ organizational attributes الشفافة على المبرمج."
    },
    {
        "q": "Which of the following is a top-level structural component of a computer?",
        "type": "mcq",
        "options": [
            "Central Processing Unit (CPU)",
            "ALU",
            "Cache Memory",
            "Register File"
        ],
        "ans": "Central Processing Unit (CPU)",
        "explain_correct": "✅ صح! الـ CPU من أهم الـ structural components على أعلى مستوى في الكمبيوتر.",
        "explain_wrong": "❌ غلط! الـ CPU هو من الـ top-level structural components في الكمبيوتر."
    },
    {
        "q": "What does ISA stand for?",
        "type": "mcq",
        "options": [
            "Instruction Set Architecture",
            "Internal System Attributes",
            "Integrated Software Architecture",
            "Input Signal Analyzer"
        ],
        "ans": "Instruction Set Architecture",
        "explain_correct": "✅ صح! ISA اختصار لـ Instruction Set Architecture.",
        "explain_wrong": "❌ غلط! ISA اختصار لـ Instruction Set Architecture."
    },
    {
        "q": "Which of the following is an architectural attribute example?",
        "type": "mcq",
        "options": [
            "Techniques for addressing memory",
            "Memory technology used",
            "Control signals",
            "Interface between computer and peripherals"
        ],
        "ans": "Techniques for addressing memory",
        "explain_correct": "✅ صح! طرق عنونة الميموري (addressing techniques) من الـ architectural attributes اللي المبرمج بيشوفها.",
        "explain_wrong": "❌ غلط! الـ addressing techniques هي architectural attribute."
    },
    {
        "q": "Organizational attributes are described as 'transparent' to the programmer. What does this mean?",
        "type": "mcq",
        "options": [
            "The programmer does not need to know about them to write programs",
            "They are visible and important to the programmer",
            "They are stored in the instruction set",
            "They are part of the ISA"
        ],
        "ans": "The programmer does not need to know about them to write programs",
        "explain_correct": "✅ صح! معنى شفاف هنا إن المبرمج مش محتاج يعرف عنها عشان يكتب برنامج.",
        "explain_wrong": "❌ غلط! معنى transparent إن المبرمج مش محتاج يعرف عن الـ organizational details."
    },
    {
        "q": "Which component of the computer is responsible for data processing?",
        "type": "mcq",
        "options": [
            "CPU (Central Processing Unit)",
            "Main Memory",
            "I/O System",
            "System Interconnection"
        ],
        "ans": "CPU (Central Processing Unit)",
        "explain_correct": "✅ صح! الـ CPU هو المسؤول عن معالجة البيانات.",
        "explain_wrong": "❌ غلط! الـ CPU هو المسؤول عن معالجة البيانات (data processing)."
    },
    {
        "q": "Which of the following is NOT a top-level structural component of a computer?",
        "type": "mcq",
        "options": [
            "Cache Memory",
            "CPU",
            "Main Memory",
            "I/O"
        ],
        "ans": "Cache Memory",
        "explain_correct": "✅ صح! الـ Cache Memory مش من الـ top-level structural components، هي جزء داخل الـ CPU.",
        "explain_wrong": "❌ غلط! الـ Cache Memory مش top-level component، هي جزء داخل الـ CPU."
    },
    {
        "q": "Computer Architecture has a direct impact on:",
        "type": "mcq",
        "options": [
            "The logical execution of a program",
            "The physical hardware connections",
            "The control signals used",
            "The memory technology"
        ],
        "ans": "The logical execution of a program",
        "explain_correct": "✅ صح! الـ Architecture بتأثر مباشرة على التنفيذ المنطقي للبرنامج.",
        "explain_wrong": "❌ غلط! الـ Architecture بتأثر على الـ logical execution of a program."
    },
    {
        "q": "The interface between the computer and peripherals is an example of:",
        "type": "mcq",
        "options": [
            "Organizational attribute",
            "Architectural attribute",
            "ISA attribute",
            "Functional attribute"
        ],
        "ans": "Organizational attribute",
        "explain_correct": "✅ صح! الـ interface بين الكمبيوتر والـ peripherals من الـ organizational attributes الشفافة للمبرمج.",
        "explain_wrong": "❌ غلط! الـ interface مع الـ peripherals هي organizational attribute."
    },
    {
        "q": "The number of bits used to represent data types is an example of:",
        "type": "mcq",
        "options": [
            "Architectural attribute",
            "Organizational attribute",
            "Control signal",
            "Memory technology"
        ],
        "ans": "Architectural attribute",
        "explain_correct": "✅ صح! عدد الـ bits اللي بيمثل الـ data types من الـ architectural attributes اللي المبرمج بيشوفها.",
        "explain_wrong": "❌ غلط! عدد الـ bits للـ data types هو architectural attribute."
    },
    {
        "q": "What are 'peripherals' in a computer system?",
        "type": "mcq",
        "options": [
            "External devices connected to the computer via I/O",
            "Internal memory units",
            "CPU registers",
            "Cache memory blocks"
        ],
        "ans": "External devices connected to the computer via I/O",
        "explain_correct": "✅ صح! الـ peripherals هي الأجهزة الخارجية المتصلة بالكمبيوتر عن طريق الـ I/O.",
        "explain_wrong": "❌ غلط! الـ peripherals هي الأجهزة الخارجية المتصلة بالكمبيوتر."
    },
    {
        "q": "The effect of executed instructions on registers and memory is an example of:",
        "type": "mcq",
        "options": [
            "Architectural attribute",
            "Organizational attribute",
            "Functional structure",
            "Control signal"
        ],
        "ans": "Architectural attribute",
        "explain_correct": "✅ صح! تأثير الـ instructions على الـ registers والـ memory من الـ architectural attributes.",
        "explain_wrong": "❌ غلط! تأثير الـ instructions على الـ registers والـ memory هو architectural attribute."
    },
    {
        "q": "Which of the following best describes 'System Interconnection'?",
        "type": "mcq",
        "options": [
            "A mechanism that provides communication among CPU, memory, and I/O",
            "A component that stores all system data",
            "The unit that executes all arithmetic operations",
            "A device that controls only the I/O operations"
        ],
        "ans": "A mechanism that provides communication among CPU, memory, and I/O",
        "explain_correct": "✅ صح! الـ System Interconnection هو الميكانيزم اللي بيوفر التواصل بين الـ CPU والـ Memory والـ I/O.",
        "explain_wrong": "❌ غلط! الـ System Interconnection هو ميكانيزم التواصل بين أجزاء الكمبيوتر."
    },
    {
        "q": "Memory technology used in a computer is an example of:",
        "type": "mcq",
        "options": [
            "Organizational attribute",
            "Architectural attribute",
            "ISA definition",
            "Functional attribute"
        ],
        "ans": "Organizational attribute",
        "explain_correct": "✅ صح! نوع تقنية الميموري المستخدمة من الـ organizational attributes الشفافة للمبرمج.",
        "explain_wrong": "❌ غلط! نوع تقنية الميموري هو organizational attribute."
    },
    {
        "q": "What distinguishes Computer Architecture from Computer Organization?",
        "type": "mcq",
        "options": [
            "Architecture is visible to the programmer; Organization deals with hardware details transparent to the programmer",
            "Architecture deals with hardware connections; Organization is visible to the programmer",
            "They are exactly the same thing",
            "Architecture only deals with memory; Organization deals with the CPU"
        ],
        "ans": "Architecture is visible to the programmer; Organization deals with hardware details transparent to the programmer",
        "explain_correct": "✅ صح! الـ Architecture ظاهرة للمبرمج، بينما الـ Organization بتتكلم عن تفاصيل الـ hardware الشفافة عليه.",
        "explain_wrong": "❌ غلط! الفرق إن Architecture ظاهرة للمبرمج والـ Organization شفافة عليه."
    },
    {
        "q": "What is another name for CPU?",
        "type": "mcq",
        "options": [
            "Processor",
            "Main Memory",
            "System Bus",
            "I/O Controller"
        ],
        "ans": "Processor",
        "explain_correct": "✅ صح! الـ CPU بيتسمى كمان Processor.",
        "explain_wrong": "❌ غلط! الاسم التاني للـ CPU هو Processor."
    },

    # ══════════════════════════════════════════════
    # ✅ True / False Questions
    # ══════════════════════════════════════════════

    {
        "q": "Computer Organization deals with attributes of a system visible to the programmer.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — الـ Computer Organization بتتكلم عن الـ hardware details الشفافة على المبرمج، مش اللي هو شايفها.",
        "explain_wrong": "❌ غلط! الـ Computer Organization بتتكلم عن الـ hardware details الشفافة على المبرمج مش عن اللي هو شايفه."
    },
    {
        "q": "Instruction Set Architecture (ISA) is a term often used interchangeably with Computer Architecture.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! الـ ISA بيتبادل مع مصطلح Computer Architecture في كتير من الأحيان.",
        "explain_wrong": "❌ غلط! الـ ISA فعلاً بيتبادل مع Computer Architecture."
    },
    {
        "q": "Structure refers to the way in which components relate to each other in a computer system.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! الـ Structure هي الطريقة اللي بيها الـ components بتتعلق ببعض.",
        "explain_wrong": "❌ غلط! الـ Structure فعلاً هي العلاقة بين الـ components."
    },
    {
        "q": "Whether a hardware multiply unit exists or multiplication is done by repeated addition is an example of an architectural attribute.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — وجود hardware multiply unit هو organizational attribute مش architectural.",
        "explain_wrong": "❌ غلط! وجود hardware multiply unit هو organizational attribute مش architectural."
    }
]
