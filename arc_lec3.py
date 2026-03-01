# ════════════════════════════════════════════════════════════
# 📖 arc_lec3.py
# Computer Architecture & Organization - Lecture 3
# Instruction Cycle, Registers, Program Execution
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # ✅ MCQ Questions 
    # ══════════════════════════════════════════════

    {
        "q": "What is the Instruction Cycle?",
        "type": "mcq",
        "options": [
            "The basic operation performed by the CPU to fetch, decode, and execute an instruction",
            "The time taken to store data in memory",
            "The process of transferring data between CPU and I/O",
            "The process of loading the operating system"
        ],
        "ans": "The basic operation performed by the CPU to fetch, decode, and execute an instruction",
        "explain_correct": "✅ صح! الـ Instruction Cycle هو العملية الأساسية اللي الـ CPU بيعملها عشان يجيب ويفك ويطبق الـ instruction.",
        "explain_wrong": "❌ غلط! الـ Instruction Cycle هو العملية الأساسية للـ CPU لتنفيذ التعليمات: Fetch ثم Decode ثم Execute."
    },
    {
        "q": "What is another name for the Instruction Cycle?",
        "type": "mcq",
        "options": [
            "Fetch-Decode-Execute cycle",
            "Read-Write cycle",
            "Load-Store cycle",
            "Input-Output cycle"
        ],
        "ans": "Fetch-Decode-Execute cycle",
        "explain_correct": "✅ صح! الـ Instruction Cycle بيتسمى كمان Fetch-Decode-Execute cycle.",
        "explain_wrong": "❌ غلط! الاسم التاني للـ Instruction Cycle هو Fetch-Decode-Execute cycle."
    },
    {
        "q": "How many steps does the Instruction Cycle consist of?",
        "type": "mcq",
        "options": [
            "3 steps: Fetch, Decode, Execute",
            "2 steps: Fetch and Execute",
            "4 steps: Fetch, Decode, Execute, Store",
            "5 steps"
        ],
        "ans": "3 steps: Fetch, Decode, Execute",
        "explain_correct": "✅ صح! الـ Instruction Cycle يتكون من 3 خطوات: Fetch وDecode وExecute.",
        "explain_wrong": "❌ غلط! الـ Instruction Cycle يتكون من 3 خطوات فقط: Fetch, Decode, Execute."
    },
    {
        "q": "What happens during the Fetch Cycle?",
        "type": "mcq",
        "options": [
            "The next instruction is loaded (read) from memory into the processor",
            "The CPU interprets the instruction",
            "The CPU performs the operation specified by the instruction",
            "Data is stored back to memory"
        ],
        "ans": "The next instruction is loaded (read) from memory into the processor",
        "explain_correct": "✅ صح! في الـ Fetch Cycle الـ processor بيقرأ الـ instruction الجاية من الذاكرة.",
        "explain_wrong": "❌ غلط! في الـ Fetch Cycle الـ CPU بيجيب الـ instruction من الذاكرة."
    },
    {
        "q": "What does the Program Counter (PC) hold?",
        "type": "mcq",
        "options": [
            "The address of the next instruction to fetch",
            "The current instruction being executed",
            "The result of ALU operations",
            "The data being transferred to/from memory"
        ],
        "ans": "The address of the next instruction to fetch",
        "explain_correct": "✅ صح! الـ PC بيحتوي على عنوان الـ instruction التالية اللي هيتم جلبها من الذاكرة.",
        "explain_wrong": "❌ غلط! الـ Program Counter (PC) بيحتفظ بعنوان الـ instruction التالية."
    },
    {
        "q": "After fetching an instruction, what happens to the Program Counter (PC)?",
        "type": "mcq",
        "options": [
            "It is incremented to point to the next instruction",
            "It is reset to zero",
            "It stores the result of the ALU",
            "It holds the current instruction"
        ],
        "ans": "It is incremented to point to the next instruction",
        "explain_correct": "✅ صح! بعد الـ Fetch الـ PC بيتزود بواحد عشان يشاور على الـ instruction الجاية.",
        "explain_wrong": "❌ غلط! بعد الـ Fetch الـ PC بيتزود (increment) عشان يشاور على الـ instruction التالية."
    },
    {
        "q": "After fetching, where is the instruction loaded?",
        "type": "mcq",
        "options": [
            "Instruction Register (IR)",
            "Program Counter (PC)",
            "Accumulator (AC)",
            "Memory Address Register (MAR)"
        ],
        "ans": "Instruction Register (IR)",
        "explain_correct": "✅ صح! بعد الـ Fetch الـ instruction بيتحمل في الـ Instruction Register (IR).",
        "explain_wrong": "❌ غلط! الـ instruction بعد الـ Fetch بتتحط في الـ Instruction Register (IR)."
    },
    {
        "q": "What happens during the Decode Cycle?",
        "type": "mcq",
        "options": [
            "The CPU interprets the instruction and determines what operation needs to be performed",
            "The instruction is loaded from memory",
            "The CPU performs the operation",
            "Data is stored back in memory"
        ],
        "ans": "The CPU interprets the instruction and determines what operation needs to be performed",
        "explain_correct": "✅ صح! في الـ Decode Cycle الـ CPU بيفسر الـ instruction وبيحدد العملية المطلوبة.",
        "explain_wrong": "❌ غلط! في الـ Decode Cycle الـ CPU بيفسر الـ instruction ويحدد العملية المطلوبة."
    },
    {
        "q": "An instruction is divided into two main parts. What are they?",
        "type": "mcq",
        "options": [
            "Operation code (opcode) and operand",
            "Address and data",
            "Fetch and execute",
            "Register and memory"
        ],
        "ans": "Operation code (opcode) and operand",
        "explain_correct": "✅ صح! الـ instruction بتتقسم لـ opcode (كود العملية) وoperand (البيانات أو العنوان).",
        "explain_wrong": "❌ غلط! الـ instruction بتتكون من opcode وoperand."
    },
    {
        "q": "What does the opcode in an instruction represent?",
        "type": "mcq",
        "options": [
            "The operation to be performed",
            "The data to be processed",
            "The memory address",
            "The result of the operation"
        ],
        "ans": "The operation to be performed",
        "explain_correct": "✅ صح! الـ opcode بيمثل العملية اللي هيتم تنفيذها (زي Load أو Add أو Store).",
        "explain_wrong": "❌ غلط! الـ opcode هو الجزء اللي بيحدد العملية المطلوب تنفيذها."
    },
    {
        "q": "Which component in the CPU decodes the instruction?",
        "type": "mcq",
        "options": [
            "The decoder in the Control Unit",
            "The ALU",
            "The Accumulator",
            "The Program Counter"
        ],
        "ans": "The decoder in the Control Unit",
        "explain_correct": "✅ صح! الـ decoder الموجود في الـ Control Unit هو اللي بيفك تشفير الـ instruction.",
        "explain_wrong": "❌ غلط! الـ decoder في الـ Control Unit هو المسؤول عن فك تشفير الـ instruction."
    },
    {
        "q": "What happens during the Execute Cycle?",
        "type": "mcq",
        "options": [
            "The CPU performs the operation specified by the instruction",
            "The CPU fetches the next instruction from memory",
            "The CPU decodes the instruction",
            "The PC is incremented"
        ],
        "ans": "The CPU performs the operation specified by the instruction",
        "explain_correct": "✅ صح! في الـ Execute Cycle الـ CPU بينفذ العملية اللي الـ instruction حددتها.",
        "explain_wrong": "❌ غلط! في الـ Execute Cycle الـ CPU بينفذ العملية المحددة في الـ instruction."
    },
    {
        "q": "Which of the following is a type of operation that can occur in the Execute Cycle?",
        "type": "mcq",
        "options": [
            "Processor-memory data transfer",
            "Loading the OS",
            "Incrementing the PC",
            "Reading from keyboard"
        ],
        "ans": "Processor-memory data transfer",
        "explain_correct": "✅ صح! نقل البيانات بين الـ CPU والـ Main Memory من أنواع العمليات في الـ Execute Cycle.",
        "explain_wrong": "❌ غلط! Processor-memory (نقل البيانات بين CPU والذاكرة) من أنواع عمليات الـ Execute Cycle."
    },
    {
        "q": "What does 'Processor-memory' operation in the Execute Cycle mean?",
        "type": "mcq",
        "options": [
            "Data transfer between CPU and main memory",
            "Data transfer between CPU and I/O module",
            "Arithmetic operation on data",
            "Control operation"
        ],
        "ans": "Data transfer between CPU and main memory",
        "explain_correct": "✅ صح! الـ Processor-memory operation يعني نقل البيانات بين الـ CPU والـ Main Memory.",
        "explain_wrong": "❌ غلط! الـ Processor-memory = نقل البيانات بين الـ CPU والـ Main Memory."
    },
    {
        "q": "What does 'Processor I/O' operation in the Execute Cycle mean?",
        "type": "mcq",
        "options": [
            "Data transfer between CPU and I/O module",
            "Data transfer between CPU and main memory",
            "Arithmetic operation on data",
            "Fetching the next instruction"
        ],
        "ans": "Data transfer between CPU and I/O module",
        "explain_correct": "✅ صح! الـ Processor I/O operation يعني نقل البيانات بين الـ CPU والـ I/O module.",
        "explain_wrong": "❌ غلط! الـ Processor I/O = نقل البيانات بين الـ CPU والـ I/O module."
    },
    {
        "q": "What does 'Data Processing' operation in the Execute Cycle mean?",
        "type": "mcq",
        "options": [
            "Some arithmetic or logical operation on data",
            "Data transfer between CPU and memory",
            "Data transfer between CPU and I/O",
            "Fetching the next instruction"
        ],
        "ans": "Some arithmetic or logical operation on data",
        "explain_correct": "✅ صح! الـ Data Processing في الـ Execute Cycle يعني تنفيذ عملية حسابية أو منطقية على البيانات.",
        "explain_wrong": "❌ غلط! الـ Data Processing في الـ Execute Cycle = عملية حسابية أو منطقية على البيانات."
    },
    {
        "q": "What are the two types of registers in the CPU?",
        "type": "mcq",
        "options": [
            "General purpose registers and Specific purpose registers",
            "Input registers and Output registers",
            "Data registers and Address registers",
            "Fast registers and Slow registers"
        ],
        "ans": "General purpose registers and Specific purpose registers",
        "explain_correct": "✅ صح! في نوعين من الـ registers: General purpose (لأي غرض) وSpecific purpose (لغرض محدد).",
        "explain_wrong": "❌ غلط! نوعا الـ registers هما: General purpose وSpecific purpose."
    },
    {
        "q": "What is a General Purpose Register?",
        "type": "mcq",
        "options": [
            "A register that can be used for any purpose",
            "A register used only for storing addresses",
            "A register used only for ALU results",
            "A register used only for instructions"
        ],
        "ans": "A register that can be used for any purpose",
        "explain_correct": "✅ صح! الـ General Purpose Register هو الـ register اللي ممكن يتستخدم لأي غرض.",
        "explain_wrong": "❌ غلط! الـ General Purpose Register هو اللي ممكن يُستخدم لأي غرض."
    },
    {
        "q": "What does the Memory Buffer Register (MBR) do?",
        "type": "mcq",
        "options": [
            "Stores the data being transferred to and from immediate access storage",
            "Holds the address of the next instruction",
            "Holds the current instruction being executed",
            "Stores the result of ALU operations"
        ],
        "ans": "Stores the data being transferred to and from immediate access storage",
        "explain_correct": "✅ صح! الـ MBR بيخزن البيانات اللي بتتنقل من وإلى الذاكرة.",
        "explain_wrong": "❌ غلط! الـ MBR (Memory Buffer Register) بيخزن البيانات اللي بتتنقل من/إلى الذاكرة."
    },
    {
        "q": "What is another name for the Memory Buffer Register (MBR)?",
        "type": "mcq",
        "options": [
            "Memory Data Register (MDR)",
            "Memory Address Register (MAR)",
            "Instruction Register (IR)",
            "Program Counter (PC)"
        ],
        "ans": "Memory Data Register (MDR)",
        "explain_correct": "✅ صح! الـ MBR بيتسمى كمان Memory Data Register (MDR).",
        "explain_wrong": "❌ غلط! الاسم التاني للـ MBR هو Memory Data Register (MDR)."
    },
    {
        "q": "What does the Memory Address Register (MAR) store?",
        "type": "mcq",
        "options": [
            "The memory address from which data will be fetched or to which data will be sent",
            "The data being transferred to memory",
            "The current instruction being executed",
            "The result of ALU operations"
        ],
        "ans": "The memory address from which data will be fetched or to which data will be sent",
        "explain_correct": "✅ صح! الـ MAR بيخزن عنوان الذاكرة اللي هيتم جلب البيانات منه أو إرسالها إليه.",
        "explain_wrong": "❌ غلط! الـ MAR بيحتفظ بعنوان الذاكرة للقراءة أو الكتابة."
    },
    {
        "q": "What does the Accumulator (AC) hold?",
        "type": "mcq",
        "options": [
            "The results of ALU operations",
            "The address of the next instruction",
            "The current instruction being decoded",
            "The data being transferred from memory"
        ],
        "ans": "The results of ALU operations",
        "explain_correct": "✅ صح! الـ Accumulator (AC) بيحتفظ بنتائج عمليات الـ ALU.",
        "explain_wrong": "❌ غلط! الـ Accumulator (AC) بيخزن نتائج عمليات الـ ALU."
    },
    {
        "q": "What does the Instruction Register (IR) hold?",
        "type": "mcq",
        "options": [
            "The instruction currently being executed or decoded",
            "The address of the next instruction",
            "The result of ALU operations",
            "The data being transferred to memory"
        ],
        "ans": "The instruction currently being executed or decoded",
        "explain_correct": "✅ صح! الـ IR (Instruction Register) بيحتفظ بالـ instruction اللي بيتم تنفيذها أو فك تشفيرها حالياً.",
        "explain_wrong": "❌ غلط! الـ IR بيحتفظ بالـ instruction الحالية اللي بيتم تنفيذها أو decoding بتاعتها."
    },
    {
        "q": "In which unit does the Instruction Register (IR) exist?",
        "type": "mcq",
        "options": [
            "Control Unit",
            "ALU",
            "Main Memory",
            "I/O Module"
        ],
        "ans": "Control Unit",
        "explain_correct": "✅ صح! الـ IR موجود في الـ Control Unit.",
        "explain_wrong": "❌ غلط! الـ Instruction Register (IR) موجود في الـ Control Unit."
    },
    {
        "q": "During the fetch phase, the next instruction address is copied from the PC into which register?",
        "type": "mcq",
        "options": [
            "MAR (Memory Address Register)",
            "MBR (Memory Buffer Register)",
            "IR (Instruction Register)",
            "AC (Accumulator)"
        ],
        "ans": "MAR (Memory Address Register)",
        "explain_correct": "✅ صح! في الـ Fetch Phase عنوان الـ instruction بيتنسخ من الـ PC إلى الـ MAR.",
        "explain_wrong": "❌ غلط! في الـ Fetch Phase العنوان بيتنسخ من الـ PC إلى الـ MAR."
    },
    {
        "q": "After the MAR fetches the instruction using the address bus, where is the instruction held?",
        "type": "mcq",
        "options": [
            "MDR (Memory Data Register)",
            "MAR (Memory Address Register)",
            "PC (Program Counter)",
            "AC (Accumulator)"
        ],
        "ans": "MDR (Memory Data Register)",
        "explain_correct": "✅ صح! بعد الـ fetch الـ instruction بتتحط في الـ MDR (Memory Data Register).",
        "explain_wrong": "❌ غلط! الـ instruction بعد الـ fetch بتتخزن في الـ MDR."
    },
    {
        "q": "After the instruction is held in the MDR, where is it duplicated?",
        "type": "mcq",
        "options": [
            "CIR (Current Instruction Register)",
            "PC (Program Counter)",
            "MAR (Memory Address Register)",
            "AC (Accumulator)"
        ],
        "ans": "CIR (Current Instruction Register)",
        "explain_correct": "✅ صح! الـ instruction بتتنسخ من الـ MDR إلى الـ CIR (Current Instruction Register أو IR).",
        "explain_wrong": "❌ غلط! الـ instruction بتتنسخ من الـ MDR إلى الـ CIR."
    },
    {
        "q": "During the decode stage, the instruction in which register is decoded?",
        "type": "mcq",
        "options": [
            "CIR (Current Instruction Register)",
            "MAR (Memory Address Register)",
            "MDR (Memory Data Register)",
            "PC (Program Counter)"
        ],
        "ans": "CIR (Current Instruction Register)",
        "explain_correct": "✅ صح! في مرحلة الـ Decode الـ instruction الموجودة في الـ CIR بيتم فك تشفيرها.",
        "explain_wrong": "❌ غلط! الـ instruction في الـ CIR هي اللي بيتم decoding بتاعها."
    },
    {
        "q": "In the program execution example, what does opcode 0001 mean?",
        "type": "mcq",
        "options": [
            "Load AC from Memory",
            "Store AC to Memory",
            "Add to AC from Memory",
            "Subtract from AC"
        ],
        "ans": "Load AC from Memory",
        "explain_correct": "✅ صح! الـ opcode 0001 = Load AC from Memory (تحميل القيمة من الذاكرة إلى الـ AC).",
        "explain_wrong": "❌ غلط! الـ opcode 0001 = Load AC from Memory."
    },
    {
        "q": "In the program execution example, what does opcode 0010 mean?",
        "type": "mcq",
        "options": [
            "Store AC to Memory",
            "Load AC from Memory",
            "Add to AC from Memory",
            "Subtract from AC"
        ],
        "ans": "Store AC to Memory",
        "explain_correct": "✅ صح! الـ opcode 0010 = Store AC to Memory (تخزين قيمة الـ AC في الذاكرة).",
        "explain_wrong": "❌ غلط! الـ opcode 0010 = Store AC to Memory."
    },
    {
        "q": "In the program execution example, what does opcode 0101 mean?",
        "type": "mcq",
        "options": [
            "Add to AC from Memory",
            "Load AC from Memory",
            "Store AC to Memory",
            "Subtract from AC"
        ],
        "ans": "Add to AC from Memory",
        "explain_correct": "✅ صح! الـ opcode 0101 = Add to AC from Memory (جمع قيمة من الذاكرة مع الـ AC).",
        "explain_wrong": "❌ غلط! الـ opcode 0101 = Add to AC from Memory."
    },
    {
        "q": "In the instruction format example, the instruction is 16 bits. The first 4 bits are the opcode. How many possible operations are there?",
        "type": "mcq",
        "options": [
            "16 operations (2^4)",
            "4 operations",
            "8 operations (2^3)",
            "256 operations (2^8)"
        ],
        "ans": "16 operations (2^4)",
        "explain_correct": "✅ صح! 4 bits للـ opcode = 2^4 = 16 عملية ممكنة.",
        "explain_wrong": "❌ غلط! 4 bits للـ opcode = 2^4 = 16 عملية ممكنة."
    },
    {
        "q": "In the instruction format example (16-bit instruction, 4-bit opcode), how many words can the memory hold?",
        "type": "mcq",
        "options": [
            "2^12 words",
            "2^4 words",
            "2^16 words",
            "2^8 words"
        ],
        "ans": "2^12 words",
        "explain_correct": "✅ صح! 16 - 4 = 12 bits للعنوان، إذن الذاكرة تحتوي على 2^12 كلمة.",
        "explain_wrong": "❌ غلط! 16 - 4 = 12 bits للـ address، إذن الذاكرة = 2^12 words."
    },
    {
        "q": "In Step 1 of the program execution example, what is the value of MAR?",
        "type": "mcq",
        "options": [
            "300",
            "301",
            "302",
            "940"
        ],
        "ans": "300",
        "explain_correct": "✅ صح! في الخطوة الأولى الـ MAR = 300 (عنوان الـ instruction الأولى).",
        "explain_wrong": "❌ غلط! في Step 1 الـ MAR = 300."
    },
    {
        "q": "In Step 2 of the program execution example, what operation is executed?",
        "type": "mcq",
        "options": [
            "Load AC from Memory",
            "Store AC to Memory",
            "Add to AC from Memory",
            "Subtract from AC"
        ],
        "ans": "Load AC from Memory",
        "explain_correct": "✅ صح! في Step 2 الـ opcode = 1 (0001) يعني Load AC from Memory.",
        "explain_wrong": "❌ غلط! في Step 2 العملية هي Load AC from Memory."
    },
    {
        "q": "In Step 4 of the program execution example, the result in AC is 5. How was it calculated?",
        "type": "mcq",
        "options": [
            "3 + 2 = 5 (Add to AC from Memory)",
            "5 - 0 = 5",
            "Load 5 directly from memory",
            "Store 5 to AC"
        ],
        "ans": "3 + 2 = 5 (Add to AC from Memory)",
        "explain_correct": "✅ صح! في Step 4 القيمة 3 من الذاكرة (940) + القيمة 2 من (941) = 5 في الـ AC.",
        "explain_wrong": "❌ غلط! في Step 4 الناتج = 3 + 2 = 5 باستخدام opcode 0101 (Add to AC from Memory)."
    },
    {
        "q": "Which register stores the address of the NEXT instruction to be fetched?",
        "type": "mcq",
        "options": [
            "Program Counter (PC)",
            "Instruction Register (IR)",
            "Accumulator (AC)",
            "Memory Buffer Register (MBR)"
        ],
        "ans": "Program Counter (PC)",
        "explain_correct": "✅ صح! الـ PC هو اللي بيحتفظ بعنوان الـ instruction التالية.",
        "explain_wrong": "❌ غلط! الـ Program Counter (PC) هو اللي بيحتفظ بعنوان الـ instruction التالية."
    },
    {
        "q": "Which register holds the instruction currently being executed or decoded?",
        "type": "mcq",
        "options": [
            "Instruction Register (IR) / CIR",
            "Program Counter (PC)",
            "Accumulator (AC)",
            "Memory Address Register (MAR)"
        ],
        "ans": "Instruction Register (IR) / CIR",
        "explain_correct": "✅ صح! الـ IR (أو CIR) بيحتفظ بالـ instruction الحالية اللي بيتم تنفيذها أو decoding بتاعتها.",
        "explain_wrong": "❌ غلط! الـ IR / CIR هو اللي بيحتفظ بالـ instruction الحالية."
    },
    {
        "q": "The Instruction Cycle runs continuously while the computer is:",
        "type": "mcq",
        "options": [
            "On (powered)",
            "In sleep mode",
            "Processing I/O only",
            "Storing data only"
        ],
        "ans": "On (powered)",
        "explain_correct": "✅ صح! الـ Instruction Cycle بيشتغل باستمرار طالما الكمبيوتر شغال.",
        "explain_wrong": "❌ غلط! الـ Instruction Cycle بيستمر طالما الكمبيوتر شغال (powered on)."
    },
    {
        "q": "The MAR fetches the instruction from memory using which bus?",
        "type": "mcq",
        "options": [
            "Address Bus",
            "Data Bus",
            "Control Bus",
            "System Bus"
        ],
        "ans": "Address Bus",
        "explain_correct": "✅ صح! الـ MAR بيجيب الـ instruction من الذاكرة باستخدام الـ Address Bus.",
        "explain_wrong": "❌ غلط! الـ MAR بيستخدم الـ Address Bus عشان يجيب الـ instruction من الذاكرة."
    },
    {
        "q": "What is the correct order of the Instruction Cycle?",
        "type": "mcq",
        "options": [
            "Fetch → Decode → Execute",
            "Decode → Fetch → Execute",
            "Execute → Fetch → Decode",
            "Fetch → Execute → Decode"
        ],
        "ans": "Fetch → Decode → Execute",
        "explain_correct": "✅ صح! الترتيب الصح للـ Instruction Cycle هو: Fetch ثم Decode ثم Execute.",
        "explain_wrong": "❌ غلط! الترتيب الصح هو: Fetch → Decode → Execute."
    },
    {
        "q": "What is the role of the MAR during the fetch phase?",
        "type": "mcq",
        "options": [
            "Stores the memory address to be accessed and fetches the instruction at that location",
            "Holds the instruction being executed",
            "Stores the result of ALU operations",
            "Holds the address of the next instruction"
        ],
        "ans": "Stores the memory address to be accessed and fetches the instruction at that location",
        "explain_correct": "✅ صح! الـ MAR بيخزن عنوان الذاكرة ويجيب الـ instruction الموجودة في ذلك الموقع.",
        "explain_wrong": "❌ غلط! الـ MAR بيخزن عنوان الذاكرة المطلوب ويجيب الـ instruction منها."
    },
    {
        "q": "In the program execution example (Step 3), MAR = 301 and the IR contains 5941. What is the opcode?",
        "type": "mcq",
        "options": [
            "5 (0101) = Add to AC from Memory",
            "1 (0001) = Load AC from Memory",
            "2 (0010) = Store AC to Memory",
            "9 (1001) = Unknown"
        ],
        "ans": "5 (0101) = Add to AC from Memory",
        "explain_correct": "✅ صح! الـ opcode في 5941 هو 5 (0101) اللي بيعني Add to AC from Memory.",
        "explain_wrong": "❌ غلط! الـ opcode 5 (0101) = Add to AC from Memory."
    },
    {
        "q": "In the program execution example (Step 5), MAR = 302 and the IR contains 2941. What operation will be performed?",
        "type": "mcq",
        "options": [
            "Store AC to Memory (opcode 0010)",
            "Load AC from Memory (opcode 0001)",
            "Add to AC from Memory (opcode 0101)",
            "Halt"
        ],
        "ans": "Store AC to Memory (opcode 0010)",
        "explain_correct": "✅ صح! الـ opcode في 2941 هو 2 (0010) اللي بيعني Store AC to Memory.",
        "explain_wrong": "❌ غلط! الـ opcode 2 (0010) = Store AC to Memory."
    },
    {
        "q": "Which of the following registers is used in the fetch-decode-execute cycle?",
        "type": "mcq",
        "options": [
            "PC, MAR, MDR, CIR",
            "ALU, CU, Bus, Cache",
            "ROM, RAM, HDD, SSD",
            "GPU, CPU, APU, FPU"
        ],
        "ans": "PC, MAR, MDR, CIR",
        "explain_correct": "✅ صح! الـ registers المستخدمة في الـ cycle هي: PC وMAR وMDR وCIR.",
        "explain_wrong": "❌ غلط! الـ registers المستخدمة في الـ cycle هي PC, MAR, MDR, CIR."
    },

    # ══════════════════════════════════════════════
    # ✅ True / False Questions
    # ══════════════════════════════════════════════

    {
        "q": "The Program Counter (PC) holds the current instruction being executed.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — الـ PC بيحتفظ بعنوان الـ instruction التالية، مش الـ instruction الحالية. الـ IR هو اللي بيحتفظ بالـ instruction الحالية.",
        "explain_wrong": "❌ غلط! الـ PC بيحتفظ بعنوان الـ NEXT instruction، مش الحالية."
    },
    {
        "q": "The Instruction Cycle consists of three steps: Fetch, Decode, and Execute.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! الـ Instruction Cycle فعلاً يتكون من 3 خطوات: Fetch وDecode وExecute.",
        "explain_wrong": "❌ غلط! الـ Instruction Cycle فعلاً يتكون من 3 خطوات: Fetch, Decode, Execute."
    },
    {
        "q": "The Accumulator (AC) stores the memory address for the next read or write operation.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — الـ AC بيخزن نتائج عمليات الـ ALU. الـ MAR هو اللي بيخزن عناوين الذاكرة.",
        "explain_wrong": "❌ غلط! الـ AC بيخزن نتائج الـ ALU، أما الـ MAR هو اللي بيخزن عناوين الذاكرة."
    },
    {
        "q": "In the decode cycle, the instruction is divided into opcode and operand.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! في الـ Decode Cycle الـ instruction بتتقسم لـ opcode (العملية) وoperand (البيانات أو العنوان).",
        "explain_wrong": "❌ غلط! فعلاً في الـ Decode Cycle الـ instruction بتتقسم لـ opcode وoperand."
    },
    {
        "q": "After each fetch, the Program Counter (PC) is decremented by one.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — بعد كل Fetch الـ PC بيتزود (increment) بواحد مش بيتقلل.",
        "explain_wrong": "❌ غلط! بعد كل Fetch الـ PC بيتزود (increment) بواحد عشان يشاور على الـ instruction التالية."
    }
]