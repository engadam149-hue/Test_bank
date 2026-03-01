# ════════════════════════════════════════════════════════════
# 📖 dm_lec2.py
# Discrete Mathematics - Lecture 2
# Bit Strings, Translating English, Logic Circuits & Equivalences
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # ✅ MCQ Questions
    # ══════════════════════════════════════════════

    {
        "q": "What is a bit string?",
        "type": "mcq",
        "options": [
            "A sequence of characters",
            "A sequence of zero or more bits",
            "A sequence of integers",
            "A sequence of real numbers"
        ],
        "ans": "A sequence of zero or more bits",
        "explain_correct": "✅ صح! الـ Bit String هي سلسلة تتكون من صفر أو أكثر من الـ bits.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي: A sequence of zero or more bits."
    },
    {
        "q": "What is the length of the bit string 101010011?",
        "type": "mcq",
        "options": [
            "7",
            "8",
            "9",
            "10"
        ],
        "ans": "9",
        "explain_correct": "✅ صح! طول السلسلة هو عدد الـ bits اللي فيها، ودول 9.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 9 لأن عدد الـ bits فيها 9."
    },
    {
        "q": "What is the bitwise OR of 01 1011 0110 and 11 0001 1101?",
        "type": "mcq",
        "options": [
            "01 0001 0100",
            "11 1011 1111",
            "10 1010 1011",
            "00 0001 0100"
        ],
        "ans": "11 1011 1111",
        "explain_correct": "✅ صح! في الـ OR، لو أي بت بـ 1 الناتج بيكون 1.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 11 1011 1111."
    },
    {
        "q": "What is the bitwise AND of 01 1011 0110 and 11 0001 1101?",
        "type": "mcq",
        "options": [
            "11 1011 1111",
            "10 1010 1011",
            "01 0001 0100",
            "11 0001 1101"
        ],
        "ans": "01 0001 0100",
        "explain_correct": "✅ صح! في الـ AND، الناتج بيكون 1 بس لو الاتنين 1.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 01 0001 0100."
    },
    {
        "q": "What is the bitwise XOR of 01 1011 0110 and 11 0001 1101?",
        "type": "mcq",
        "options": [
            "11 1011 1111",
            "01 0001 0100",
            "10 1010 1011",
            "01 1011 0110"
        ],
        "ans": "10 1010 1011",
        "explain_correct": "✅ صح! في الـ XOR، الناتج بيكون 1 لما يكونوا مختلفين فقط.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 10 1010 1011."
    },
    {
        "q": "Bitwise OR outputs 1 when:",
        "type": "mcq",
        "options": [
            "Both bits are 0",
            "Both bits are 1",
            "At least one bit is 1",
            "Exactly one bit is 1"
        ],
        "ans": "At least one bit is 1",
        "explain_correct": "✅ صح! الـ OR بيطلع 1 لو على الأقل واحد فيهم بـ 1.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي: At least one bit is 1."
    },
    {
        "q": "Bitwise AND outputs 1 when:",
        "type": "mcq",
        "options": [
            "At least one bit is 1",
            "Both bits are 1",
            "Both bits are 0",
            "Exactly one bit is 1"
        ],
        "ans": "Both bits are 1",
        "explain_correct": "✅ صح! الـ AND بيطلع 1 بس لو الاتنين بـ 1.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي: Both bits are 1."
    },
    {
        "q": "Bitwise XOR outputs 1 when:",
        "type": "mcq",
        "options": [
            "Both bits are 1",
            "Both bits are 0",
            "Exactly one bit is 1",
            "At least one bit is 1"
        ],
        "ans": "Exactly one bit is 1",
        "explain_correct": "✅ صح! الـ XOR بيطلع 1 لما يكونوا مختلفين، يعني بالظبط واحد فيهم بس اللي بـ 1.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي: Exactly one bit is 1."
    },
    {
        "q": "What is the length of the bit string 0000?",
        "type": "mcq",
        "options": [
            "0",
            "2",
            "4",
            "8"
        ],
        "ans": "4",
        "explain_correct": "✅ صح! دي سلسلة مكونة من 4 أصفار، يبقى طولها 4.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 4."
    },
    {
        "q": "Which operation on bit strings corresponds to logical conjunction (AND)?",
        "type": "mcq",
        "options": [
            "Bitwise OR",
            "Bitwise XOR",
            "Bitwise AND",
            "Bitwise NOT"
        ],
        "ans": "Bitwise AND",
        "explain_correct": "✅ صح! الـ logical conjunction هو نفسه الـ Bitwise AND.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Bitwise AND."
    },
    {
        "q": "The sentence 'You can access the Internet from campus only if you are a CS major or you are not a student' is represented as:",
        "type": "mcq",
        "options": [
            "p ↔ (q ∨ ¬r)",
            "p → (q ∨ ¬r)",
            "(q ∨ ¬r) → p",
            "p ∧ (q ∨ ¬r)"
        ],
        "ans": "p → (q ∨ ¬r)",
        "explain_correct": "✅ صح! التركيبة 'p only if q' معناها p → q.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي p → (q ∨ ¬r)."
    },
    {
        "q": "In the sentence 'You can access the Internet from campus only if you are a CS major or you are not a student', what does p represent?",
        "type": "mcq",
        "options": [
            "You are a CS major",
            "You are a student",
            "You can access the Internet from campus",
            "You are not a student"
        ],
        "ans": "You can access the Internet from campus",
        "explain_correct": "✅ صح! الجزء الأول (p) هو 'You can access the Internet from campus'.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي: You can access the Internet from campus."
    },
    {
        "q": "In the sentence 'You can access the Internet from campus only if you are a CS major or you are not a student', what does r represent?",
        "type": "mcq",
        "options": [
            "You can access the Internet",
            "You are a CS major",
            "You are not a student",
            "You are a student"
        ],
        "ans": "You are a student",
        "explain_correct": "✅ صح! الجملة فيها ¬r (not a student)، يبقى الأساس (r) هو 'You are a student'.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي: You are a student."
    },
    {
        "q": "The phrase 'p only if q' is logically equivalent to:",
        "type": "mcq",
        "options": [
            "q → p",
            "p ↔ q",
            "p → q",
            "¬p → q"
        ],
        "ans": "p → q",
        "explain_correct": "✅ صح! 'p only if q' تعني p → q.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي p → q."
    },
    {
        "q": "The sentence 'The automated reply cannot be sent when the file system is full' is represented as:",
        "type": "mcq",
        "options": [
            "p → q",
            "¬p → q",
            "q → ¬p",
            "p ∧ ¬q"
        ],
        "ans": "q → ¬p",
        "explain_correct": "✅ صح! التركيبة دي بتعني: إذا كان الـ file system مليان (q)، إذن لا يمكن إرسال الرد (¬p).",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي q → ¬p."
    },
    {
        "q": "In the sentence 'The automated reply cannot be sent when the file system is full', what does p represent?",
        "type": "mcq",
        "options": [
            "The file system is full",
            "The automated reply cannot be sent",
            "The automated reply can be sent",
            "The file system is not full"
        ],
        "ans": "The automated reply can be sent",
        "explain_correct": "✅ صح! الجملة فيها نفي لـ p، إذن p الأصلية هي 'The automated reply can be sent'.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي: The automated reply can be sent."
    },
    {
        "q": "The phrase 'q when p' is logically equivalent to:",
        "type": "mcq",
        "options": [
            "q → p",
            "p → q",
            "p ↔ q",
            "¬p → q"
        ],
        "ans": "p → q",
        "explain_correct": "✅ صح! 'q when p' معناها 'لو p حصلت، q هتحصل'، يعني p → q.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي p → q."
    },
    {
        "q": "Why is it useful to translate English sentences into propositional logic?",
        "type": "mcq",
        "options": [
            "To make sentences longer",
            "To remove ambiguity",
            "To add ambiguity",
            "To simplify grammar"
        ],
        "ans": "To remove ambiguity",
        "explain_correct": "✅ صح! اللغات الطبيعية ممكن تتفهم بأكتر من طريقة، لكن المنطق بيشيل الغموض (ambiguity) ده.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي To remove ambiguity."
    },
    {
        "q": "How many basic gates are used to build complicated digital circuits?",
        "type": "mcq",
        "options": [
            "2",
            "3",
            "4",
            "5"
        ],
        "ans": "3",
        "explain_correct": "✅ صح! هما 3 بوابات أساسية: AND, OR, NOT (Inverter).",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 3."
    },
    {
        "q": "Which gate corresponds to the logical OR operation?",
        "type": "mcq",
        "options": [
            "AND gate",
            "Inverter",
            "OR gate",
            "XOR gate"
        ],
        "ans": "OR gate",
        "explain_correct": "✅ صح! الـ OR gate هي اللي بتمثل الـ logical OR.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي OR gate."
    },
    {
        "q": "Which gate corresponds to the logical NOT operation?",
        "type": "mcq",
        "options": [
            "AND gate",
            "OR gate",
            "Inverter",
            "NOR gate"
        ],
        "ans": "Inverter",
        "explain_correct": "✅ صح! الـ Inverter هو اللي بيعكس القيمة زي الـ NOT.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Inverter."
    },
    {
        "q": "Which gate corresponds to the logical AND operation?",
        "type": "mcq",
        "options": [
            "OR gate",
            "Inverter",
            "XOR gate",
            "AND gate"
        ],
        "ans": "AND gate",
        "explain_correct": "✅ صح! الـ AND gate بتمثل الـ logical AND.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي AND gate."
    },
    {
        "q": "What is the output of the combinatorial circuit with inputs p, q, r that passes p and ¬q through an AND gate, then ORs the result with ¬r?",
        "type": "mcq",
        "options": [
            "(p ∧ q) ∨ r",
            "(p ∧ ¬q) ∨ ¬r",
            "(p ∨ ¬q) ∧ ¬r",
            "p ∧ (q ∨ r)"
        ],
        "ans": "(p ∧ ¬q) ∨ ¬r",
        "explain_correct": "✅ صح! التركيبة بالترتيب هتكون: (p AND ¬q) وبعدين OR مع ¬r.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي (p ∧ ¬q) ∨ ¬r."
    },
    {
        "q": "A logic circuit receives input signals that are each:",
        "type": "mcq",
        "options": [
            "Real numbers",
            "Characters",
            "Bits (0 or 1)",
            "Integers only"
        ],
        "ans": "Bits (0 or 1)",
        "explain_correct": "✅ صح! الـ logic circuits بتتعامل مع Bits (0 و 1).",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Bits (0 or 1)."
    },
    {
        "q": "In this course, logic circuits are restricted to how many output signals?",
        "type": "mcq",
        "options": [
            "Zero",
            "Two",
            "Three",
            "One"
        ],
        "ans": "One",
        "explain_correct": "✅ صح! الدوائر اللي بندرسها في الجزء ده بيكون ليها مخرج واحد (One output signal).",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي One."
    },
    {
        "q": "To build a circuit for (p ∨ ¬r) ∧ (¬p ∨ (q ∨ ¬r)), how many inverters are needed at minimum?",
        "type": "mcq",
        "options": [
            "1",
            "2",
            "3",
            "4"
        ],
        "ans": "2",
        "explain_correct": "✅ صح! محتاجين inverter للـ p و inverter للـ r. إذن 2.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 2."
    },
    {
        "q": "The output of an AND gate with inputs p and ¬q is:",
        "type": "mcq",
        "options": [
            "p ∨ ¬q",
            "p ∧ q",
            "p ∧ ¬q",
            "¬p ∧ q"
        ],
        "ans": "p ∧ ¬q",
        "explain_correct": "✅ صح! الدخلين هما p و ¬q، وبما إنها AND gate فالخرج هيكون p ∧ ¬q.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي p ∧ ¬q."
    },
    {
        "q": "What does an inverter (NOT gate) do to input p?",
        "type": "mcq",
        "options": [
            "Outputs p unchanged",
            "Outputs ¬p",
            "Outputs p ∧ 1",
            "Outputs p ∨ 0"
        ],
        "ans": "Outputs ¬p",
        "explain_correct": "✅ صح! الـ inverter بيعكس الإشارة، فبيطلع ¬p.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Outputs ¬p."
    },
    {
        "q": "A compound proposition that is ALWAYS true is called:",
        "type": "mcq",
        "options": [
            "Contingency",
            "Contradiction",
            "Tautology",
            "Equivalence"
        ],
        "ans": "Tautology",
        "explain_correct": "✅ صح! الجملة اللي دايماً True في كل الحالات اسمها Tautology.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Tautology."
    },
    {
        "q": "A compound proposition that is ALWAYS false is called:",
        "type": "mcq",
        "options": [
            "Tautology",
            "Contingency",
            "Implication",
            "Contradiction"
        ],
        "ans": "Contradiction",
        "explain_correct": "✅ صح! الجملة اللي دايماً False اسمها Contradiction (تناقض).",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Contradiction."
    },
    {
        "q": "A compound proposition that is sometimes true and sometimes false is called:",
        "type": "mcq",
        "options": [
            "Tautology",
            "Contradiction",
            "Contingency",
            "Equivalence"
        ],
        "ans": "Contingency",
        "explain_correct": "✅ صح! الجملة اللي ممكن تكون True أو False حسب الدخل اسمها Contingency.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Contingency."
    },
    {
        "q": "Is (p ∧ q) → p a tautology?",
        "type": "mcq",
        "options": [
            "No, it is a contradiction",
            "No, it is a contingency",
            "Yes, it is always true",
            "Cannot be determined"
        ],
        "ans": "Yes, it is always true",
        "explain_correct": "✅ صح! لأن (p ∧ q) مش هتكون True غير لو p نفسها True، فبالتالي الجملة كلها دايماً True.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Yes, it is always true."
    },
    {
        "q": "In the truth table for (p ∧ q) → p, when p = F and q = T, what is (p ∧ q)?",
        "type": "mcq",
        "options": [
            "T",
            "F",
            "Undefined",
            "T only if q = T"
        ],
        "ans": "F",
        "explain_correct": "✅ صح! الـ AND بيحتاج الاتنين يكونوا True، فلو p بـ False الناتج هيكون False.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي F."
    },
    {
        "q": "In the truth table for (p ∧ q) → p, when p = T and q = T, what is the result of (p ∧ q) → p?",
        "type": "mcq",
        "options": [
            "F",
            "Undefined",
            "T",
            "F only if p = T"
        ],
        "ans": "T",
        "explain_correct": "✅ صح! (T ∧ T) = T، و T → T بيطلع T.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي T."
    },
    {
        "q": "How many rows does a truth table for a compound proposition with 2 variables have?",
        "type": "mcq",
        "options": [
            "2",
            "4",
            "6",
            "8"
        ],
        "ans": "4",
        "explain_correct": "✅ صح! عدد الصفوف بيساوي 2 أُس عدد المتغيرات (2^2 = 4).",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي 4."
    },
    {
        "q": "p ∧ ¬p is an example of a:",
        "type": "mcq",
        "options": [
            "Tautology",
            "Contingency",
            "Implication",
            "Contradiction"
        ],
        "ans": "Contradiction",
        "explain_correct": "✅ صح! مفيش حاجة ممكن تكون صح وعكسها صح في نفس الوقت، فدايماً هتديك False.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Contradiction."
    },
    {
        "q": "p ∨ ¬p is an example of a:",
        "type": "mcq",
        "options": [
            "Contradiction",
            "Tautology",
            "Contingency",
            "Equivalence"
        ],
        "ans": "Tautology",
        "explain_correct": "✅ صح! أكيد يا الحاجه يا عكسها هتكون True، فدايماً هتديك True.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Tautology."
    },
    {
        "q": "Two propositions are logically equivalent if:",
        "type": "mcq",
        "options": [
            "They have the same number of variables",
            "p ↔ q is a tautology",
            "p → q is always true",
            "They have the same number of connectives"
        ],
        "ans": "p ↔ q is a tautology",
        "explain_correct": "✅ صح! لو الـ Biconditional بينهم دايماً True، يبقى هما متكافئين منطقياً.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي p ↔ q is a tautology."
    },
    {
        "q": "Which symbol denotes logical equivalence?",
        "type": "mcq",
        "options": [
            "→",
            "∧",
            "≡",
            "∨"
        ],
        "ans": "≡",
        "explain_correct": "✅ صح! الرمز ده (≡) معناه إن الحاجتين متكافئين.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي ≡."
    },
    {
        "q": "Are ¬(p ∨ q) and ¬p ∧ ¬q logically equivalent?",
        "type": "mcq",
        "options": [
            "No, they have different truth values",
            "Only when p = T",
            "Yes, they have the same truth values in all cases",
            "Only when q = F"
        ],
        "ans": "Yes, they have the same truth values in all cases",
        "explain_correct": "✅ صح! ودي اللي بنسميها De Morgan's Laws.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Yes, they have the same truth values in all cases."
    },
    {
        "q": "In the truth table for ¬(p ∨ q) and ¬p ∧ ¬q, when p = F and q = F, what are both values?",
        "type": "mcq",
        "options": [
            "Both F",
            "Both T",
            "First T, second F",
            "First F, second T"
        ],
        "ans": "Both T",
        "explain_correct": "✅ صح! لما الاتنين بـ False، التعبيرين بيطلعوا True.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Both T."
    },
    {
        "q": "In the truth table for ¬(p ∨ q) and ¬p ∧ ¬q, when p = T and q = T, what are both values?",
        "type": "mcq",
        "options": [
            "Both T",
            "Both F",
            "First T, second F",
            "First F, second T"
        ],
        "ans": "Both F",
        "explain_correct": "✅ صح! لما الاتنين True، التعبيرين بيطلعوا False.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Both F."
    },
    {
        "q": "De Morgan's Law states that ¬(p ∨ q) ≡:",
        "type": "mcq",
        "options": [
            "¬p ∨ ¬q",
            "p ∧ q",
            "¬p ∧ ¬q",
            "¬(p ∧ q)"
        ],
        "ans": "¬p ∧ ¬q",
        "explain_correct": "✅ صح! النفي بيدخل على القوس، يقلب الـ OR لـ AND، وينفي الـ p والـ q.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي ¬p ∧ ¬q."
    },
    {
        "q": "The notation p ⇔ q means:",
        "type": "mcq",
        "options": [
            "p implies q",
            "p and q are logically equivalent",
            "p is the negation of q",
            "p OR q"
        ],
        "ans": "p and q are logically equivalent",
        "explain_correct": "✅ صح! ده رمز تاني للـ logical equivalence.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي p and q are logically equivalent."
    },
    {
        "q": "Which of the following is one of the five main applications of propositional logic covered in the lecture?",
        "type": "mcq",
        "options": [
            "Sorting algorithms",
            "Logic Circuits",
            "Database indexing",
            "Graph traversal"
        ],
        "ans": "Logic Circuits",
        "explain_correct": "✅ صح! الـ Logic Circuits من أهم تطبيقات الـ propositional logic في الكمبيوتر.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي Logic Circuits."
    },
    {
        "q": "When p = T, q = F in the truth table for ¬(p ∨ q), what is the value of ¬(p ∨ q)?",
        "type": "mcq",
        "options": [
            "T",
            "Undefined",
            "F",
            "T only if ¬q = T"
        ],
        "ans": "F",
        "explain_correct": "✅ صح! (T ∨ F) = T، ونفي الـ T هو F.",
        "explain_wrong": "❌ غلط! الإجابة الصحيحة هي F."
    },

    # ══════════════════════════════════════════════
    # ✅ True / False Questions
    # ══════════════════════════════════════════════

    {
        "q": "A bit string is a sequence of zero or more bits, and its length is the number of bits in the string.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! ده التعريف السليم للـ bit string.",
        "explain_wrong": "❌ غلط! العبارة دي صحيحة."
    },
    {
        "q": "The sentence 'The automated reply cannot be sent when the file system is full' is represented logically as p → q (where p = automated reply can be sent, q = file system is full).",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! العبارة غلط، لأن التمثيل السليم ليها هو q → ¬p.",
        "explain_wrong": "❌ غلط! التمثيل السليم هو q → ¬p مش p → q."
    },
    {
        "q": "A tautology is a compound proposition that is always false.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! العبارة غلط، الـ Tautology بتكون دايماً True. الـ Contradiction هي اللي دايماً False.",
        "explain_wrong": "❌ غلط! الـ Tautology بتكون دايماً True."
    },
    {
        "q": "¬(p ∨ q) and ¬p ∧ ¬q are logically equivalent (De Morgan's Law).",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! دي واحدة من قواعد دي مورجان (De Morgan's Laws).",
        "explain_wrong": "❌ غلط! دي فعلاً قاعدة دي مورجان."
    },
    {
        "q": "Complicated digital circuits can be constructed from three basic gates: OR gate, AND gate, and Inverter.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! أي دايرة رقمية معقدة نقدر نبنيها باستخدام الـ 3 بوابات الأساسية دول.",
        "explain_wrong": "❌ غلط! العبارة دي صحيحة."
    }
]