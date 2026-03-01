# ════════════════════════════════════════════════════════════
# 📖 arc_lec2.py
# Computer Architecture & Organization - Lecture 2
# CPU Structure, Bus Types, Computer Functions
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # ✅ MCQ Questions 
    # ══════════════════════════════════════════════

    {
        "q": "What is the role of the Control Unit (CU) in the CPU?",
        "type": "mcq",
        "options": [
            "Controls the operation of the CPU and hence the computer",
            "Performs arithmetic and logic operations",
            "Provides storage internal to the CPU",
            "Transfers data between CPU and memory"
        ],
        "ans": "Controls the operation of the CPU and hence the computer",
        "explain_correct": "✅ صح! الـ Control Unit (CU) بتتحكم في عمليات الـ CPU وبالتالي الكمبيوتر كله.",
        "explain_wrong": "❌ غلط! الـ Control Unit مهمتها التحكم في عمليات الـ CPU وليس معالجة البيانات."
    },
    {
        "q": "What does the ALU (Arithmetic and Logic Unit) do?",
        "type": "mcq",
        "options": [
            "Handles data processing — performs arithmetic and logic operations",
            "Controls the operation of the CPU",
            "Provides storage internal to the CPU",
            "Transfers data between components"
        ],
        "ans": "Handles data processing — performs arithmetic and logic operations",
        "explain_correct": "✅ صح! الـ ALU بتعمل العمليات الحسابية (زي الجمع والطرح) والمنطقية (زي AND وNOT).",
        "explain_wrong": "❌ غلط! الـ ALU مسؤولة عن معالجة البيانات وتنفيذ العمليات الحسابية والمنطقية."
    },
    {
        "q": "Which of the following operations does the ALU perform?",
        "type": "mcq",
        "options": [
            "Addition, subtraction, AND, NOT, and shift operations",
            "Storing data permanently",
            "Controlling memory access",
            "Managing I/O devices"
        ],
        "ans": "Addition, subtraction, AND, NOT, and shift operations",
        "explain_correct": "✅ صح! الـ ALU بتعمل عمليات حسابية زي الجمع والطرح وعمليات منطقية زي AND وNOT والـ shift.",
        "explain_wrong": "❌ غلط! الـ ALU بتعمل arithmetic operations (جمع وطرح) وlogic operations (AND وNOT وshift)."
    },
    {
        "q": "What is the role of Registers in the CPU?",
        "type": "mcq",
        "options": [
            "Provides storage internal to the CPU",
            "Controls the operation of the CPU",
            "Handles arithmetic and logic operations",
            "Transfers data between CPU and memory"
        ],
        "ans": "Provides storage internal to the CPU",
        "explain_correct": "✅ صح! الـ Registers بتوفر تخزين داخلي في الـ CPU.",
        "explain_wrong": "❌ غلط! الـ Registers مهمتها التخزين الداخلي في الـ CPU."
    },
    {
        "q": "What is the role of CPU Interconnection?",
        "type": "mcq",
        "options": [
            "Provides communication among the Control Unit, ALU, and Registers",
            "Connects the CPU to external devices",
            "Stores data permanently",
            "Controls I/O operations"
        ],
        "ans": "Provides communication among the Control Unit, ALU, and Registers",
        "explain_correct": "✅ صح! الـ CPU Interconnection بيوفر التواصل بين الـ Control Unit والـ ALU والـ Registers.",
        "explain_wrong": "❌ غلط! الـ CPU Interconnection بيربط المكونات الداخلية للـ CPU ببعض."
    },
    {
        "q": "What are the four main functions of a computer?",
        "type": "mcq",
        "options": [
            "Data processing, data storage, data movement, and control",
            "Input, output, storage, and networking",
            "Arithmetic, logic, memory, and I/O",
            "CPU, RAM, ROM, and Bus"
        ],
        "ans": "Data processing, data storage, data movement, and control",
        "explain_correct": "✅ صح! الوظائف الأربعة للكمبيوتر هي: Data processing وData storage وData movement وControl.",
        "explain_wrong": "❌ غلط! الوظائف الأربعة هي: Data processing, Data storage, Data movement, Control."
    },
    {
        "q": "What does 'Data Processing' mean as a computer function?",
        "type": "mcq",
        "options": [
            "Manipulate, compute, or transform input data according to a set of instructions",
            "Store data for short-term and long-term use",
            "Transfer data between components",
            "Coordinate and manage hardware and software activities"
        ],
        "ans": "Manipulate, compute, or transform input data according to a set of instructions",
        "explain_correct": "✅ صح! الـ Data Processing يعني معالجة وتحويل البيانات المدخلة وفق مجموعة من التعليمات (البرامج).",
        "explain_wrong": "❌ غلط! الـ Data Processing يعني معالجة وتحويل البيانات حسب التعليمات."
    },
    {
        "q": "What does 'Data Storage' mean as a computer function?",
        "type": "mcq",
        "options": [
            "Store data and instructions for both short-term and long-term use",
            "Transfer data between components",
            "Manipulate and compute data",
            "Coordinate hardware and software"
        ],
        "ans": "Store data and instructions for both short-term and long-term use",
        "explain_correct": "✅ صح! الـ Data Storage يعني تخزين البيانات والتعليمات للاستخدام المؤقت والدائم.",
        "explain_wrong": "❌ غلط! الـ Data Storage يعني تخزين البيانات والتعليمات قصيرة وطويلة الأمد."
    },
    {
        "q": "What does 'Data Movement' mean as a computer function?",
        "type": "mcq",
        "options": [
            "Transfer of data between different components of a computer system",
            "Store data permanently",
            "Manipulate and compute data",
            "Control hardware and software activities"
        ],
        "ans": "Transfer of data between different components of a computer system",
        "explain_correct": "✅ صح! الـ Data Movement يعني نقل البيانات بين المكونات المختلفة في النظام.",
        "explain_wrong": "❌ غلط! الـ Data Movement يعني نقل البيانات بين مكونات الكمبيوتر المختلفة."
    },
    {
        "q": "What does 'Control' mean as a computer function?",
        "type": "mcq",
        "options": [
            "Coordinate and manage the activities of the computer's hardware and software",
            "Store data for long-term use",
            "Transfer data between components",
            "Perform arithmetic operations"
        ],
        "ans": "Coordinate and manage the activities of the computer's hardware and software",
        "explain_correct": "✅ صح! الـ Control يعني تنسيق وإدارة أنشطة الـ hardware والـ software في الكمبيوتر.",
        "explain_wrong": "❌ غلط! الـ Control يعني تنسيق وإدارة أنشطة الـ hardware والـ software."
    },
    {
        "q": "What is a 'Processor' in the context of a multicore computer?",
        "type": "mcq",
        "options": [
            "A physical piece of silicon containing one or more cores",
            "A single processing unit on a chip",
            "A type of memory storage",
            "A bus that connects components"
        ],
        "ans": "A physical piece of silicon containing one or more cores",
        "explain_correct": "✅ صح! الـ Processor هو قطعة السيليكون الفيزيائية اللي بتحتوي على core أو أكتر.",
        "explain_wrong": "❌ غلط! الـ Processor هو القطعة الفيزيائية من السيليكون اللي بتحتوي على core أو أكتر."
    },
    {
        "q": "What is a 'Core' in a multicore processor?",
        "type": "mcq",
        "options": [
            "An individual processing unit on a processor chip",
            "A physical piece of silicon",
            "A type of memory",
            "A bus connecting CPU to memory"
        ],
        "ans": "An individual processing unit on a processor chip",
        "explain_correct": "✅ صح! الـ Core هو وحدة المعالجة الفردية على الشريحة.",
        "explain_wrong": "❌ غلط! الـ Core هو وحدة المعالجة الفردية الموجودة على الـ processor chip."
    },
    {
        "q": "What is a 'multicore processor'?",
        "type": "mcq",
        "options": [
            "A processor that contains multiple cores",
            "A processor with multiple buses",
            "A processor with multiple memory units",
            "A processor with multiple ALUs only"
        ],
        "ans": "A processor that contains multiple cores",
        "explain_correct": "✅ صح! الـ multicore processor هو المعالج اللي بيحتوي على أكتر من core.",
        "explain_wrong": "❌ غلط! الـ multicore processor هو المعالج اللي بيحتوي على multiple cores."
    },
    {
        "q": "What is a Bus in a computer system?",
        "type": "mcq",
        "options": [
            "A group of lines (wires) that serve as a connecting path for several devices",
            "A type of memory storage unit",
            "A processing unit inside the CPU",
            "A register inside the CPU"
        ],
        "ans": "A group of lines (wires) that serve as a connecting path for several devices",
        "explain_correct": "✅ صح! الـ Bus هو مجموعة من الخطوط (الأسلاك) اللي بتمثل مسار الاتصال بين الأجهزة.",
        "explain_wrong": "❌ غلط! الـ Bus هو مجموعة من الأسلاك بتوصل الأجهزة ببعض."
    },
    {
        "q": "How many bits does each line in a bus carry?",
        "type": "mcq",
        "options": [
            "One bit per line",
            "8 bits per line",
            "16 bits per line",
            "32 bits per line"
        ],
        "ans": "One bit per line",
        "explain_correct": "✅ صح! كل خط في الـ Bus بينقل bit واحد بس.",
        "explain_wrong": "❌ غلط! كل خط في الـ Bus بينقل bit واحد فقط (one bit per line)."
    },
    {
        "q": "What is the main difference between Single Bus and Multiple Bus structures?",
        "type": "mcq",
        "options": [
            "Single bus connects all units to one bus; Multiple bus uses several buses for better performance",
            "Single bus is faster than multiple bus",
            "Multiple bus is cheaper than single bus",
            "Single bus has better performance than multiple bus"
        ],
        "ans": "Single bus connects all units to one bus; Multiple bus uses several buses for better performance",
        "explain_correct": "✅ صح! الـ Single bus بيوصل كل الوحدات ببص واحد وأرخص، والـ Multiple bus فيه أكتر من بص وأسرع.",
        "explain_wrong": "❌ غلط! الـ Single bus كل الوحدات فيه متصلة ببص واحد وأرخص، بينما الـ Multiple bus أسرع وأغلى."
    },
    {
        "q": "Which bus structure has better performance?",
        "type": "mcq",
        "options": [
            "Multiple bus structure",
            "Single bus structure",
            "Both are equal in performance",
            "Depends on the CPU type"
        ],
        "ans": "Multiple bus structure",
        "explain_correct": "✅ صح! الـ Multiple bus structure أحسن في الأداء من الـ Single bus structure.",
        "explain_wrong": "❌ غلط! الـ Multiple bus structure أحسن في الـ performance."
    },
    {
        "q": "Which bus structure is cheaper?",
        "type": "mcq",
        "options": [
            "Single bus structure",
            "Multiple bus structure",
            "Both cost the same",
            "Depends on the number of devices"
        ],
        "ans": "Single bus structure",
        "explain_correct": "✅ صح! الـ Single bus structure أرخص من الـ Multiple bus structure.",
        "explain_wrong": "❌ غلط! الـ Single bus structure أرخص تكلفة."
    },
    {
        "q": "How many types of buses are there in a computer system?",
        "type": "mcq",
        "options": [
            "3 types: Data bus, Address bus, Control bus",
            "2 types: Data bus and Address bus",
            "4 types: Data, Address, Control, Power bus",
            "1 type: System bus"
        ],
        "ans": "3 types: Data bus, Address bus, Control bus",
        "explain_correct": "✅ صح! في 3 أنواع من الـ buses: Data bus وAddress bus وControl bus.",
        "explain_wrong": "❌ غلط! في 3 أنواع: Data bus, Address bus, Control bus."
    },
    {
        "q": "What is the purpose of the Data Bus?",
        "type": "mcq",
        "options": [
            "Transfer data or instructions between different components of the computer",
            "Send memory addresses to components",
            "Transmit control signals between components",
            "Connect CPU to power supply"
        ],
        "ans": "Transfer data or instructions between different components of the computer",
        "explain_correct": "✅ صح! الـ Data Bus بينقل البيانات أو التعليمات بين المكونات المختلفة في الكمبيوتر.",
        "explain_wrong": "❌ غلط! الـ Data Bus مهمته نقل البيانات والتعليمات بين المكونات."
    },
    {
        "q": "What does the number of lines in the data bus affect?",
        "type": "mcq",
        "options": [
            "The speed of data transfer between components",
            "The maximum addressable memory",
            "The number of control signals",
            "The power consumption of the CPU"
        ],
        "ans": "The speed of data transfer between components",
        "explain_correct": "✅ صح! عدد الخطوط في الـ Data Bus بيأثر على سرعة نقل البيانات بين المكونات.",
        "explain_wrong": "❌ غلط! عدد خطوط الـ Data Bus بيأثر على سرعة نقل البيانات."
    },
    {
        "q": "Which of the following is a correct size for a data bus?",
        "type": "mcq",
        "options": [
            "8, 16, 32, or 64 lines",
            "4, 8, or 12 lines only",
            "16 or 32 lines only",
            "1, 2, or 4 lines only"
        ],
        "ans": "8, 16, 32, or 64 lines",
        "explain_correct": "✅ صح! الـ Data Bus بيكون 8 أو 16 أو 32 أو 64 خط.",
        "explain_wrong": "❌ غلط! أحجام الـ Data Bus الشائعة هي 8, 16, 32, 64 خط."
    },
    {
        "q": "How many bits does a 64-line data bus transfer at the same time?",
        "type": "mcq",
        "options": [
            "64 bits",
            "32 bits",
            "128 bits",
            "8 bits"
        ],
        "ans": "64 bits",
        "explain_correct": "✅ صح! الـ 64-line data bus بينقل 64 bit في نفس الوقت.",
        "explain_wrong": "❌ غلط! الـ 64-line data bus بينقل 64 bit في نفس الوقت."
    },
    {
        "q": "The data bus lines are:",
        "type": "mcq",
        "options": [
            "Bi-directional",
            "Unidirectional",
            "Only for reading",
            "Only for writing"
        ],
        "ans": "Bi-directional",
        "explain_correct": "✅ صح! خطوط الـ Data Bus ثنائية الاتجاه (Bi-directional) يعني تقدر تنقل في الاتجاهين.",
        "explain_wrong": "❌ غلط! خطوط الـ Data Bus هي Bi-directional (ثنائية الاتجاه)."
    },
    {
        "q": "The CPU uses the data bus to:",
        "type": "mcq",
        "options": [
            "Read data from memory AND write data to memory locations",
            "Only send addresses to memory",
            "Only transmit control signals",
            "Connect to power supply"
        ],
        "ans": "Read data from memory AND write data to memory locations",
        "explain_correct": "✅ صح! الـ CPU بيستخدم الـ Data Bus لقراءة البيانات من الميموري وكتابتها فيه.",
        "explain_wrong": "❌ غلط! الـ CPU يستخدم الـ Data Bus لقراءة البيانات من الميموري وكتابتها فيه."
    },
    {
        "q": "What is the purpose of the Address Bus?",
        "type": "mcq",
        "options": [
            "Send memory addresses from the CPU to other components like RAM and I/O devices",
            "Transfer data between components",
            "Transmit control signals",
            "Connect CPU to power supply"
        ],
        "ans": "Send memory addresses from the CPU to other components like RAM and I/O devices",
        "explain_correct": "✅ صح! الـ Address Bus بيبعت عناوين الميموري من الـ CPU إلى المكونات الأخرى زي الـ RAM.",
        "explain_wrong": "❌ غلط! الـ Address Bus مهمته إرسال عناوين الذاكرة من الـ CPU إلى المكونات الأخرى."
    },
    {
        "q": "What does the Address Bus determine?",
        "type": "mcq",
        "options": [
            "The maximum addressable memory",
            "The speed of data transfer",
            "The number of control signals",
            "The size of the data bus"
        ],
        "ans": "The maximum addressable memory",
        "explain_correct": "✅ صح! الـ Address Bus بيحدد الحد الأقصى للذاكرة القابلة للعنونة.",
        "explain_wrong": "❌ غلط! الـ Address Bus بيحدد maximum addressable memory."
    },
    {
        "q": "What is the formula to calculate the maximum addressable memory using the address bus?",
        "type": "mcq",
        "options": [
            "Number of memory locations = 2^n (where n = number of address bus lines)",
            "Number of memory locations = n × 8",
            "Number of memory locations = 2 × n",
            "Number of memory locations = n^2"
        ],
        "ans": "Number of memory locations = 2^n (where n = number of address bus lines)",
        "explain_correct": "✅ صح! عدد مواقع الذاكرة = 2^n حيث n هو عدد خطوط الـ Address Bus.",
        "explain_wrong": "❌ غلط! الفورمولا الصح هي: عدد مواقع الذاكرة = 2^n حيث n = عدد خطوط الـ Address Bus."
    },
    {
        "q": "If the address bus has 4 lines, how many memory locations can it address?",
        "type": "mcq",
        "options": [
            "16 locations (2^4)",
            "4 locations",
            "8 locations (2^3)",
            "32 locations (2^5)"
        ],
        "ans": "16 locations (2^4)",
        "explain_correct": "✅ صح! 2^4 = 16 موقع في الذاكرة.",
        "explain_wrong": "❌ غلط! 2^4 = 16 موقع في الذاكرة."
    },
    {
        "q": "How much memory can a 16-bit address bus access?",
        "type": "mcq",
        "options": [
            "65,536 memory locations (2^16)",
            "32,768 memory locations (2^15)",
            "4 GB of memory",
            "1 GB of memory"
        ],
        "ans": "65,536 memory locations (2^16)",
        "explain_correct": "✅ صح! الـ 16-bit address bus يقدر يوصل لـ 2^16 = 65,536 موقع.",
        "explain_wrong": "❌ غلط! الـ 16-bit address bus = 2^16 = 65,536 موقع في الذاكرة."
    },
    {
        "q": "How much memory can a 32-bit address bus access?",
        "type": "mcq",
        "options": [
            "4 GB",
            "2 GB",
            "8 GB",
            "1 GB"
        ],
        "ans": "4 GB",
        "explain_correct": "✅ صح! الـ 32-bit address bus يقدر يوصل لـ 2^32 = 4 GB من الذاكرة.",
        "explain_wrong": "❌ غلط! الـ 32-bit address bus = 2^32 = 4 GB."
    },
    {
        "q": "A computer system has 16 GB of RAM. What is the minimum address bus size required?",
        "type": "mcq",
        "options": [
            "34 bits",
            "32 bits",
            "30 bits",
            "16 bits"
        ],
        "ans": "34 bits",
        "explain_correct": "✅ صح! 16 GB = 16 × 2^30 = 2^34 bytes، إذن الـ address bus محتاج 34 bit.",
        "explain_wrong": "❌ غلط! 16 GB = 2^34 bytes، إذن الـ address bus size = 34 bits."
    },
    {
        "q": "A computer system has 512 MB of RAM. What is the minimum address bus size required?",
        "type": "mcq",
        "options": [
            "29 bits",
            "32 bits",
            "20 bits",
            "512 bits"
        ],
        "ans": "29 bits",
        "explain_correct": "✅ صح! 512 MB = 512 × 2^20 = 2^29 bytes، إذن الـ address bus محتاج 29 bit.",
        "explain_wrong": "❌ غلط! 512 MB = 2^29 bytes، إذن الـ address bus size = 29 bits."
    },
    {
        "q": "The Address Bus is:",
        "type": "mcq",
        "options": [
            "Unidirectional — carries address only from CPU to memory",
            "Bi-directional",
            "Used for both data and addresses",
            "Used only for control signals"
        ],
        "ans": "Unidirectional — carries address only from CPU to memory",
        "explain_correct": "✅ صح! الـ Address Bus أحادي الاتجاه بينقل العناوين من الـ CPU إلى الذاكرة فقط.",
        "explain_wrong": "❌ غلط! الـ Address Bus هو Unidirectional بينقل العناوين من الـ CPU إلى الذاكرة فقط."
    },
    {
        "q": "What is the purpose of the Control Bus?",
        "type": "mcq",
        "options": [
            "Transmit control signals or commands from one component to another",
            "Transfer data between components",
            "Send memory addresses to components",
            "Store instructions temporarily"
        ],
        "ans": "Transmit control signals or commands from one component to another",
        "explain_correct": "✅ صح! الـ Control Bus بينقل إشارات التحكم والأوامر بين المكونات.",
        "explain_wrong": "❌ غلط! الـ Control Bus مهمته نقل إشارات التحكم والأوامر بين المكونات."
    },
    {
        "q": "When the CPU wants to read data from main memory, which bus does it use to send the request?",
        "type": "mcq",
        "options": [
            "Control Bus",
            "Data Bus",
            "Address Bus",
            "System Bus"
        ],
        "ans": "Control Bus",
        "explain_correct": "✅ صح! الـ CPU بيستخدم الـ Control Bus لإرسال إشارة التحكم للذاكرة عشان تقرأ البيانات.",
        "explain_wrong": "❌ غلط! الـ CPU بيستخدم الـ Control Bus عشان يبعت أوامر التحكم للذاكرة."
    },
    {
        "q": "The Control Bus is:",
        "type": "mcq",
        "options": [
            "Bidirectional",
            "Unidirectional",
            "Only from CPU to memory",
            "Only from memory to CPU"
        ],
        "ans": "Bidirectional",
        "explain_correct": "✅ صح! الـ Control Bus ثنائي الاتجاه (Bidirectional).",
        "explain_wrong": "❌ غلط! الـ Control Bus هو Bidirectional (ثنائي الاتجاه)."
    },
    {
        "q": "Which of the following correctly compares the three bus types?",
        "type": "mcq",
        "options": [
            "Data bus: bi-directional | Address bus: unidirectional | Control bus: bidirectional",
            "Data bus: unidirectional | Address bus: bi-directional | Control bus: unidirectional",
            "All three buses are unidirectional",
            "All three buses are bidirectional"
        ],
        "ans": "Data bus: bi-directional | Address bus: unidirectional | Control bus: bidirectional",
        "explain_correct": "✅ صح! الـ Data bus وال Control bus ثنائيا الاتجاه، أما الـ Address bus فأحادي الاتجاه.",
        "explain_wrong": "❌ غلط! الـ Data bus والـ Control bus = Bidirectional، الـ Address bus = Unidirectional."
    },
    {
        "q": "In the memory structure example with a 4-bit address bus, how many memory locations are available?",
        "type": "mcq",
        "options": [
            "16 locations (2^4)",
            "4 locations",
            "8 locations (2^3)",
            "32 locations (2^5)"
        ],
        "ans": "16 locations (2^4)",
        "explain_correct": "✅ صح! 4-bit address bus = 2^4 = 16 موقع في الذاكرة.",
        "explain_wrong": "❌ غلط! 4-bit address bus = 2^4 = 16 موقع."
    },
    {
        "q": "In the memory structure example with a 3-bit data bus, how many bits can be stored in each memory location?",
        "type": "mcq",
        "options": [
            "3 bits",
            "4 bits",
            "8 bits",
            "16 bits"
        ],
        "ans": "3 bits",
        "explain_correct": "✅ صح! الـ 3-bit data bus يعني كل موقع في الذاكرة بيخزن 3 bits.",
        "explain_wrong": "❌ غلط! الـ 3-bit data bus يعني كل location بيحتوي على 3 bits."
    },
    {
        "q": "Which component of the CPU controls its overall operation?",
        "type": "mcq",
        "options": [
            "Control Unit (CU)",
            "ALU",
            "Registers",
            "CPU Interconnection"
        ],
        "ans": "Control Unit (CU)",
        "explain_correct": "✅ صح! الـ Control Unit هي اللي بتتحكم في عمليات الـ CPU كلها.",
        "explain_wrong": "❌ غلط! الـ Control Unit هي المسؤولة عن التحكم في عمليات الـ CPU."
    },
    {
        "q": "What does the formula 'Address Bus Size = log₂(Memory Size in Bytes)' help calculate?",
        "type": "mcq",
        "options": [
            "The minimum number of address bus bits needed for a given memory size",
            "The maximum data transfer speed",
            "The number of control signals needed",
            "The number of registers in the CPU"
        ],
        "ans": "The minimum number of address bus bits needed for a given memory size",
        "explain_correct": "✅ صح! الفورمولا دي بتحسب الحد الأدنى لعدد bits في الـ Address Bus اللازمة لحجم ذاكرة معين.",
        "explain_wrong": "❌ غلط! الفورمولا دي بتحسب الحد الأدنى لعدد bits الـ Address Bus المطلوبة."
    },
    {
        "q": "Since 1 GB = 2^30 bytes, what is 16 GB in bytes?",
        "type": "mcq",
        "options": [
            "2^34 bytes",
            "2^32 bytes",
            "2^30 bytes",
            "2^36 bytes"
        ],
        "ans": "2^34 bytes",
        "explain_correct": "✅ صح! 16 GB = 16 × 2^30 = 2^4 × 2^30 = 2^34 bytes.",
        "explain_wrong": "❌ غلط! 16 GB = 16 × 2^30 = 2^34 bytes."
    },
    {
        "q": "Since 1 MB = 2^20 bytes, what is 512 MB in bytes?",
        "type": "mcq",
        "options": [
            "2^29 bytes",
            "2^20 bytes",
            "2^30 bytes",
            "2^32 bytes"
        ],
        "ans": "2^29 bytes",
        "explain_correct": "✅ صح! 512 MB = 512 × 2^20 = 2^9 × 2^20 = 2^29 bytes.",
        "explain_wrong": "❌ غلط! 512 MB = 512 × 2^20 = 2^29 bytes."
    },
    {
        "q": "Which bus carries information in ONE direction only — from CPU to memory?",
        "type": "mcq",
        "options": [
            "Address Bus",
            "Data Bus",
            "Control Bus",
            "System Bus"
        ],
        "ans": "Address Bus",
        "explain_correct": "✅ صح! الـ Address Bus أحادي الاتجاه بينقل العناوين من الـ CPU إلى الذاكرة فقط.",
        "explain_wrong": "❌ غلط! الـ Address Bus هو الوحيد أحادي الاتجاه (Unidirectional) من الـ buses الثلاثة."
    },

    # ══════════════════════════════════════════════
    # ✅ True / False Questions
    # ══════════════════════════════════════════════

    {
        "q": "The Data Bus is unidirectional — it carries data in one direction only.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — الـ Data Bus هو Bi-directional (ثنائي الاتجاه) مش Unidirectional.",
        "explain_wrong": "❌ غلط! الـ Data Bus هو Bi-directional وليس Unidirectional."
    },
    {
        "q": "A 32-bit address bus can access 4 GB of memory.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! 2^32 = 4,294,967,296 bytes = 4 GB.",
        "explain_wrong": "❌ غلط! الـ 32-bit address bus فعلاً يقدر يوصل لـ 2^32 = 4 GB."
    },
    {
        "q": "The Address Bus is bidirectional — it carries information in both directions.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — الـ Address Bus أحادي الاتجاه (Unidirectional) بينقل العناوين من الـ CPU إلى الذاكرة فقط.",
        "explain_wrong": "❌ غلط! الـ Address Bus هو Unidirectional وليس Bidirectional."
    },
    {
        "q": "The ALU (Arithmetic and Logic Unit) performs both arithmetic operations like addition and logic operations like AND and NOT.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! الـ ALU بتنفذ العمليات الحسابية (جمع وطرح) والمنطقية (AND وNOT والـ shift).",
        "explain_wrong": "❌ غلط! الـ ALU فعلاً بتنفذ arithmetic operations وlogic operations."
    },
    {
        "q": "A multiple bus structure is cheaper than a single bus structure.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — الـ Single bus structure أرخص من الـ Multiple bus structure.",
        "explain_wrong": "❌ غلط! الـ Single bus structure هو الأرخص، وليس الـ Multiple bus."
    }
]