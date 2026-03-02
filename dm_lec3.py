# ════════════════════════════════════════════════════════════
# 📖 dm_lec3.py
# Discrete Mathematics - Lecture 3
# Bit Strings, Translating English, Logic Circuits & Equivalences
# 50 Questions (45 MCQ + 5 TF)
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # 🔹 SECTION 1: Bit Strings 
    # ══════════════════════════════════════════════
    {
        "q": "A bit string is defined as:",
        "type": "mcq",
        "options": [
            "A sequence of alphabetical characters",
            "A sequence of zero or more bits",
            "A sequence of real numbers",
            "A sequence of integers only"
        ],
        "ans": "A sequence of zero or more bits",
        "explain_correct": "✅ صح! تعريف الـ bit string هو سلسلة تتكون من صفر أو أكثر من الـ bits (اللي هما 0 أو 1 بس).",
        "explain_wrong": "❌ غلط! الـ bit string بيتكون من 0 أو 1 فقط، مش أرقام حقيقية ولا حروف."
    },
    {
        "q": "What is the length of the bit string 101010011?",
        "type": "mcq",
        "options": ["7", "8", "9", "10"],
        "ans": "9",
        "explain_correct": "✅ صح! طول السلسلة بيساوي عدد الـ bits اللي فيها، لو عديت (1-0-1-0-1-0-0-1-1) هتلاقيهم 9.",
        "explain_wrong": "❌ غلط! عد الخانات في السلسلة هتلاقيهم 9 bits."
    },
    {
        "q": "What is the bitwise OR of 01 1011 0110 and 11 0001 1101?",
        "type": "mcq",
        "options": [
            "10 1010 1011",
            "01 0001 0100",
            "11 1011 1111",
            "00 0001 0000"
        ],
        "ans": "11 1011 1111",
        "explain_correct": "✅ صح! في الـ OR، الناتج بيكون 1 لو على الأقل واحد من الـ bits المتقابلة بـ 1.",
        "explain_wrong": "❌ غلط! في الـ OR لو أي واحد فيهم بـ 1 الناتج بيكون 1. الإجابة هي 11 1011 1111."
    },
    {
        "q": "What is the bitwise AND of 01 1011 0110 and 11 0001 1101?",
        "type": "mcq",
        "options": [
            "11 1011 1111",
            "10 1010 1011",
            "11 0001 1101",
            "01 0001 0100"
        ],
        "ans": "01 0001 0100",
        "explain_correct": "✅ صح! في الـ AND، الناتج بيكون 1 فقط لو التو bits المتقابلين بـ 1.",
        "explain_wrong": "❌ غلط! الـ AND بيطلع 1 بس لو الاتنين بـ 1. الإجابة هي 01 0001 0100."
    },
    {
        "q": "What is the bitwise XOR of 01 1011 0110 and 11 0001 1101?",
        "type": "mcq",
        "options": [
            "11 1011 1111",
            "01 0001 0100",
            "01 1011 0110",
            "10 1010 1011"
        ],
        "ans": "10 1010 1011",
        "explain_correct": "✅ صح! في الـ XOR، الناتج بيكون 1 فقط لو الـ bits مختلفة عن بعض.",
        "explain_wrong": "❌ غلط! الـ XOR بيطلع 1 لما يكونوا مختلفين عن بعض. الإجابة هي 10 1010 1011."
    },
    {
        "q": "Bitwise OR of bits 0 and 0 equals:",
        "type": "mcq",
        "options": ["1", "0", "Undefined", "Depends on context"],
        "ans": "0",
        "explain_correct": "✅ صح! الـ OR بيحتاج على الأقل واحد يكون 1 عشان يطلع 1. هنا الاتنين بـ 0 فالناتج 0.",
        "explain_wrong": "❌ غلط! الاتنين بـ 0 فمفيش حاجة تطلع 1، النتيجة 0."
    },
    {
        "q": "Bitwise AND of bits 1 and 0 equals:",
        "type": "mcq",
        "options": ["1", "Undefined", "0", "2"],
        "ans": "0",
        "explain_correct": "✅ صح! الـ AND بيحتاج الاتنين يكونوا 1. هنا واحد فيهم بـ 0 فالناتج 0.",
        "explain_wrong": "❌ غلط! الـ AND بيشترط إن الاتنين يبقوا 1، النتيجة 0."
    },
    {
        "q": "Bitwise XOR of bits 1 and 1 equals:",
        "type": "mcq",
        "options": ["1", "2", "0", "Undefined"],
        "ans": "0",
        "explain_correct": "✅ صح! الـ XOR بيطلع 0 لما يكونوا متشابهين (1 و 1 زي بعض).",
        "explain_wrong": "❌ غلط! الـ XOR بيطلع 1 بس لما يكونوا مختلفين، إذن النتيجة 0."
    },
    {
        "q": "Which bitwise operation corresponds to logical disjunction (OR)?",
        "type": "mcq",
        "options": [
            "Bitwise AND",
            "Bitwise XOR",
            "Bitwise NOT",
            "Bitwise OR"
        ],
        "ans": "Bitwise OR",
        "explain_correct": "✅ صح! الـ logical disjunction (OR) بيقابله الـ Bitwise OR مباشرة.",
        "explain_wrong": "❌ غلط! الـ disjunction هو الـ OR، فبيقابله Bitwise OR."
    },
    {
        "q": "If a bit string has length zero, it contains:",
        "type": "mcq",
        "options": [
            "One bit equal to 0",
            "One bit equal to 1",
            "No bits at all",
            "Two bits"
        ],
        "ans": "No bits at all",
        "explain_correct": "✅ صح! طول صفر معناه إن السلسلة مفيهاش أي bits خالص.",
        "explain_wrong": "❌ غلط! السلسلة اللي طولها 0 يعني فاضية تماماً (No bits at all)."
    },

    # ══════════════════════════════════════════════
    # 🔹 SECTION 2: Translating English Sentences 
    # ══════════════════════════════════════════════
    {
        "q": "The main reason for translating English sentences into propositional logic is:",
        "type": "mcq",
        "options": [
            "To make sentences shorter",
            "To add more ambiguity",
            "To remove the ambiguity present in natural language",
            "To convert sentences into code"
        ],
        "ans": "To remove the ambiguity present in natural language",
        "explain_correct": "✅ صح! اللغة الإنجليزية أحياناً بتكون غامضة (ambiguous)، المنطق بيشيل الغموض ده.",
        "explain_wrong": "❌ غلط! الهدف الأساسي هو إزالة الغموض (remove ambiguity) من اللغة."
    },
    {
        "q": "In Example 1, proposition p represents:",
        "type": "mcq",
        "options": [
            "You are a CS major",
            "You are a student",
            "You can access the Internet from campus",
            "You are not a student"
        ],
        "ans": "You can access the Internet from campus",
        "explain_correct": "✅ صح! حسب مثال المحاضرة، p بترمز لجملة 'You can access the Internet from campus'.",
        "explain_wrong": "❌ غلط! الـ p كانت بترمز لـ You can access the Internet from campus."
    },
    {
        "q": "In Example 1, proposition q represents:",
        "type": "mcq",
        "options": [
            "You can access the Internet",
            "You are a computer science major",
            "You are a student",
            "You are not a student"
        ],
        "ans": "You are a computer science major",
        "explain_correct": "✅ صح! حسب المحاضرة، q بترمز لجملة 'You are a computer science major'.",
        "explain_wrong": "❌ غلط! الـ q كانت بترمز لـ You are a computer science major."
    },
    {
        "q": "In Example 1, proposition r represents:",
        "type": "mcq",
        "options": [
            "You can access the Internet",
            "You are a CS major",
            "You are a student",
            "You are not a CS major"
        ],
        "ans": "You are a student",
        "explain_correct": "✅ صح! حسب المحاضرة، r بترمز لـ 'You are a student'.",
        "explain_wrong": "❌ غلط! الـ r كانت بترمز لـ You are a student."
    },
    {
        "q": "'You can access the Internet only if you are a CS major or not a student' translates to:",
        "type": "mcq",
        "options": [
            "(q or neg-r) -> p",
            "p and (q or neg-r)",
            "p <-> (q or neg-r)",
            "p -> (q or neg-r)"
        ],
        "ans": "p -> (q or neg-r)",
        "explain_correct": "✅ صح! صيغة 'p only if q' بتترجم لـ p -> q. وهنا الـ q عبارة عن (q or neg-r).",
        "explain_wrong": "❌ غلط! الترجمة الصحيحة هي p -> (q or neg-r)."
    },
    {
        "q": "The phrase 'p only if q' translates to:",
        "type": "mcq",
        "options": [
            "q -> p",
            "p <-> q",
            "p -> q",
            "neg-p -> q"
        ],
        "ans": "p -> q",
        "explain_correct": "✅ صح! جملة 'p only if q' معناها إن p مش هتحصل غير لو q حصلت، فبتترجم لـ p -> q.",
        "explain_wrong": "❌ غلط! جملة 'p only if q' ديما بتترجم لـ p -> q."
    },
    {
        "q": "In Example 2, proposition p is defined as:",
        "type": "mcq",
        "options": [
            "The file system is full",
            "The automated reply cannot be sent",
            "The file system is not full",
            "The automated reply can be sent"
        ],
        "ans": "The automated reply can be sent",
        "explain_correct": "✅ صح! حسب المحاضرة، p هي الإثبات 'can be sent'.",
        "explain_wrong": "❌ غلط! الـ p بتعبر عن حالة الإثبات: The automated reply can be sent."
    },
    {
        "q": "In Example 2, proposition q is defined as:",
        "type": "mcq",
        "options": [
            "The automated reply can be sent",
            "The automated reply cannot be sent",
            "The file system is full",
            "The file system is not full"
        ],
        "ans": "The file system is full",
        "explain_correct": "✅ صح! الـ q بتعبر عن 'The file system is full'.",
        "explain_wrong": "❌ غلط! الـ q بتعبر عن The file system is full."
    },
    {
        "q": "'The automated reply cannot be sent when the file system is full' translates to:",
        "type": "mcq",
        "options": [
            "p -> q",
            "p -> neg-q",
            "neg-p -> q",
            "q -> neg-p"
        ],
        "ans": "q -> neg-p",
        "explain_correct": "✅ صح! الشرط هنا 'when the file system is full' (q)، والنتيجة 'cannot be sent' (neg-p)، إذن q -> neg-p.",
        "explain_wrong": "❌ غلط! الترجمة الصحيحة هي q -> neg-p."
    },
    {
        "q": "The phrase 'q when p' translates to:",
        "type": "mcq",
        "options": [
            "q and p",
            "q <-> p",
            "p -> q",
            "q -> p"
        ],
        "ans": "p -> q",
        "explain_correct": "✅ صح! جملة 'q when p' معناها 'لما p تحصل، q هتحصل'، يعني p تؤدي إلى q (p -> q).",
        "explain_wrong": "❌ غلط! دي بتترجم لـ p -> q."
    },
    {
        "q": "Which is NOT listed as an application of propositional logic in the lecture?",
        "type": "mcq",
        "options": [
            "Boolean Searches",
            "Logic Circuits",
            "Database Design",
            "System Specifications"
        ],
        "ans": "Database Design",
        "explain_correct": "✅ صح! تصميم قواعد البيانات (Database Design) مش من ضمن التطبيقات اللي اتذكرت.",
        "explain_wrong": "❌ غلط! Database Design مش من التطبيقات المذكورة في المحاضرة."
    },
    {
        "q": "How many applications of propositional logic does the lecture list?",
        "type": "mcq",
        "options": ["3", "4", "5", "6"],
        "ans": "5",
        "explain_correct": "✅ صح! المحاضرة ذكرت 5 تطبيقات بالظبط.",
        "explain_wrong": "❌ غلط! هما 5 تطبيقات."
    },

    # ══════════════════════════════════════════════
    # 🔹 SECTION 3: Logic Circuits 
    # ══════════════════════════════════════════════
    {
        "q": "How many basic gates are sufficient to build any complicated digital circuit?",
        "type": "mcq",
        "options": ["2", "3", "4", "5"],
        "ans": "3",
        "explain_correct": "✅ صح! بنحتاج 3 بوابات أساسية بس عشان نبني أي دايرة معقدة: OR, AND, Inverter.",
        "explain_wrong": "❌ غلط! هما 3 بوابات بس."
    },
    {
        "q": "The three basic gates presented in the lecture are:",
        "type": "mcq",
        "options": [
            "OR, AND, XOR",
            "NAND, NOR, NOT",
            "OR, AND, Inverter (NOT)",
            "OR, XOR, Inverter"
        ],
        "ans": "OR, AND, Inverter (NOT)",
        "explain_correct": "✅ صح! البوابات الأساسية اللي اتشرحت هي OR و AND و Inverter.",
        "explain_wrong": "❌ غلط! البوابات هما OR, AND, Inverter (NOT)."
    },
    {
        "q": "What output does the Inverter (NOT gate) produce for input p?",
        "type": "mcq",
        "options": [
            "p unchanged",
            "p and 1",
            "neg-p",
            "p or 0"
        ],
        "ans": "neg-p",
        "explain_correct": "✅ صح! الـ Inverter بيعكس الإشارة، فبيدخل p بيطلع neg-p.",
        "explain_wrong": "❌ غلط! الـ Inverter بيطلع neg-p."
    },
    {
        "q": "What output does an OR gate with inputs p and q produce?",
        "type": "mcq",
        "options": [
            "p and q",
            "neg-p",
            "p xor q",
            "p or q"
        ],
        "ans": "p or q",
        "explain_correct": "✅ صح! الـ OR gate بتنفذ عملية الـ logical disjunction (p or q).",
        "explain_wrong": "❌ غلط! بتطلع p or q."
    },
    {
        "q": "What output does an AND gate with inputs p and q produce?",
        "type": "mcq",
        "options": [
            "p or q",
            "p and q",
            "neg-p",
            "neg(p or q)"
        ],
        "ans": "p and q",
        "explain_correct": "✅ صح! الـ AND gate بتنفذ عملية الـ logical conjunction (p and q).",
        "explain_wrong": "❌ غلط! بتطلع p and q."
    },
    {
        "q": "In Example 1 circuit, input q passes through an Inverter. The output is:",
        "type": "mcq",
        "options": ["q", "neg-p", "neg-q", "neg-r"],
        "ans": "neg-q",
        "explain_correct": "✅ صح! الـ Inverter بيعكس الـ q وبيطلعها neg-q.",
        "explain_wrong": "❌ غلط! المخرج هيكون neg-q."
    },
    {
        "q": "In Example 1 circuit, the AND gate receives p and neg-q. Its output is:",
        "type": "mcq",
        "options": [
            "p or neg-q",
            "p and q",
            "neg-p and q",
            "p and neg-q"
        ],
        "ans": "p and neg-q",
        "explain_correct": "✅ صح! الـ AND gate بتاخد المدخلات وتعملهم AND مع بعض (p and neg-q).",
        "explain_wrong": "❌ غلط! الإجابة هي p and neg-q."
    },
    {
        "q": "In Example 1 circuit, the FINAL output after the last OR gate is:",
        "type": "mcq",
        "options": [
            "(p or neg-q) and neg-r",
            "p and (neg-q or neg-r)",
            "(p and neg-q) or r",
            "(p and neg-q) or neg-r"
        ],
        "ans": "(p and neg-q) or neg-r",
        "explain_correct": "✅ صح! الخرج الأخير من بوابة الـ OR بيجمع (p and neg-q) مع neg-r.",
        "explain_wrong": "❌ غلط! الإجابة الصح هي (p and neg-q) or neg-r."
    },
    {
        "q": "In Example 2, the first OR gate receives p and neg-r. Its output is:",
        "type": "mcq",
        "options": [
            "p and neg-r",
            "neg-p or r",
            "p or r",
            "p or neg-r"
        ],
        "ans": "p or neg-r",
        "explain_correct": "✅ صح! بوابة الـ OR بتعمل OR بين الـ p والـ neg-r فبيطلع p or neg-r.",
        "explain_wrong": "❌ غلط! الناتج p or neg-r."
    },
    {
        "q": "The full Boolean expression to implement in Example 2 is:",
        "type": "mcq",
        "options": [
            "(p and neg-r) or (neg-p and (q and neg-r))",
            "(p or r) and (p or (q or r))",
            "(p or neg-r) and (neg-p or (q or neg-r))",
            "(p and r) or (neg-p and (q and r))"
        ],
        "ans": "(p or neg-r) and (neg-p or (q or neg-r))",
        "explain_correct": "✅ صح! دي المعادلة المطلوبة في المثال التاني بالظبط زي ما موجودة في المحاضرة.",
        "explain_wrong": "❌ غلط! الإجابة هي (p or neg-r) and (neg-p or (q or neg-r))."
    },
    {
        "q": "Each input/output signal in a logic circuit is:",
        "type": "mcq",
        "options": [
            "A real number between 0 and 1",
            "An alphabetical character",
            "An integer from 0 to 9",
            "A bit: either 0 (off) or 1 (on)"
        ],
        "ans": "A bit: either 0 (off) or 1 (on)",
        "explain_correct": "✅ صح! الإشارات في الـ logic circuits بتتعامل مع bits، يا 0 (off) يا 1 (on).",
        "explain_wrong": "❌ غلط! الدوائر المنطقية بتتعامل مع bits بس (0 أو 1)."
    },

    # ══════════════════════════════════════════════
    # 🔹 SECTION 4: Compound Propositions 
    # ══════════════════════════════════════════════
    {
        "q": "A compound proposition that is ALWAYS TRUE is called:",
        "type": "mcq",
        "options": [
            "Contradiction",
            "Contingency",
            "Tautology",
            "Equivalence"
        ],
        "ans": "Tautology",
        "explain_correct": "✅ صح! الجملة اللي دايماً بتطلع True في أي حالة اسمها Tautology.",
        "explain_wrong": "❌ غلط! اسمها Tautology."
    },
    {
        "q": "A compound proposition that is ALWAYS FALSE is called:",
        "type": "mcq",
        "options": [
            "Tautology",
            "Contingency",
            "Implication",
            "Contradiction"
        ],
        "ans": "Contradiction",
        "explain_correct": "✅ صح! الجملة اللي دايماً بتطلع False في كل الحالات اسمها Contradiction.",
        "explain_wrong": "❌ غلط! اسمها Contradiction (تناقض)."
    },
    {
        "q": "A compound proposition that is SOMETIMES TRUE and SOMETIMES FALSE is called:",
        "type": "mcq",
        "options": [
            "Tautology",
            "Contradiction",
            "Contingency",
            "Biconditional"
        ],
        "ans": "Contingency",
        "explain_correct": "✅ صح! الجملة اللي بتعتمد على المدخلات (ممكن True أو False) اسمها Contingency.",
        "explain_wrong": "❌ غلط! اسمها Contingency."
    },
    {
        "q": "In the truth table for (p and q)->p, when p=T and q=T, the result is:",
        "type": "mcq",
        "options": ["F", "T", "Undefined", "Depends on q"],
        "ans": "T",
        "explain_correct": "✅ صح! بما إن p and q = T، إذن T -> T نتيجتها دايماً T.",
        "explain_wrong": "❌ غلط! التعبير T -> T نتيجته T."
    },
    {
        "q": "In the truth table for (p and q)->p, when p=F and q=T, the result is:",
        "type": "mcq",
        "options": [
            "F",
            "T",
            "Same as p and q",
            "Undefined"
        ],
        "ans": "T",
        "explain_correct": "✅ صح! هنا (p and q) هتكون F. وفي الـ Implication (->) لو البداية F فالنتيجة دايماً T.",
        "explain_wrong": "❌ غلط! الـ Implication اللي بيبدأ بـ False نتيجته دايماً True."
    },
    {
        "q": "All four rows of the truth table for (p and q)->p are TRUE. This means it is a:",
        "type": "mcq",
        "options": [
            "Contradiction",
            "Contingency",
            "Tautology",
            "Satisfiable but not a tautology"
        ],
        "ans": "Tautology",
        "explain_correct": "✅ صح! مادام كل الصفوف نتيجتها True في الـ truth table، إذن التعبير ده Tautology.",
        "explain_wrong": "❌ غلط! أي تعبير دايماً نتيجته True بيسمى Tautology."
    },
    {
        "q": "Which is a classic example of a CONTRADICTION?",
        "type": "mcq",
        "options": [
            "p or neg-p",
            "p -> q",
            "p and neg-p",
            "p <-> p"
        ],
        "ans": "p and neg-p",
        "explain_correct": "✅ صح! مفيش حاجة ممكن تكون صح وعكسها صح في نفس الوقت، عشان كده (p and neg-p) دايماً False.",
        "explain_wrong": "❌ غلط! الإجابة هي p and neg-p لأنها مستحيل تكون صح."
    },

    # ══════════════════════════════════════════════
    # 🔹 SECTION 5: Logical Equivalences 
    # ══════════════════════════════════════════════
    {
        "q": "Two propositions p and q are logically equivalent when:",
        "type": "mcq",
        "options": [
            "p->q is always true",
            "p<->q is a tautology",
            "p and q is always true",
            "They have the same number of variables"
        ],
        "ans": "p<->q is a tautology",
        "explain_correct": "✅ صح! بيكونوا متكافئين منطقياً لو الـ biconditional بينهم (p <-> q) عبارة عن Tautology.",
        "explain_wrong": "❌ غلط! التكافؤ بيحصل لما الـ biconditional يكون Tautology."
    },
    {
        "q": "The notation used to denote logical equivalence is:",
        "type": "mcq",
        "options": [
            "->",
            "and",
            "equiv (or <=>)",
            "or"
        ],
        "ans": "equiv (or <=>)",
        "explain_correct": "✅ صح! رمز التكافؤ المنطقي هو equiv (≡) أو <=>.",
        "explain_wrong": "❌ غلط! الرمز الصحيح هو equiv (or <=>)."
    },
    {
        "q": "In the truth table for neg(p or q) and neg-p and neg-q, when p=F and q=F, both values are:",
        "type": "mcq",
        "options": [
            "F and F",
            "T and F",
            "F and T",
            "T and T"
        ],
        "ans": "T and T",
        "explain_correct": "✅ صح! لو عوضت بـ F في التعبيرين، الأول هيطلع T والتاني هيطلع T، وده بيثبت تكافؤهم.",
        "explain_wrong": "❌ غلط! التعبيرين هيطلعوا T."
    },
    {
        "q": "In the truth table for neg(p or q) and neg-p and neg-q, when p=T and q=T, both values are:",
        "type": "mcq",
        "options": [
            "T and T",
            "T and F",
            "F and F",
            "F and T"
        ],
        "ans": "F and F",
        "explain_correct": "✅ صح! لو عوضت بـ T، التعبيرين هيطلعوا F، وده مطابق لقاعدة دي مورجان.",
        "explain_wrong": "❌ غلط! التعبيرين هيطلعوا F."
    },
    {
        "q": "The equivalence neg(p or q) equiv neg-p and neg-q is known as:",
        "type": "mcq",
        "options": [
            "Commutative Law",
            "Associative Law",
            "De Morgan's Law",
            "Distributive Law"
        ],
        "ans": "De Morgan's Law",
        "explain_correct": "✅ صح! دي قاعدة دي مورجان الشهيرة، اللي بتوزع النفي وتقلب الـ OR لـ AND والعكس.",
        "explain_wrong": "❌ غلط! دي قاعدة De Morgan's Law."
    },

    # ══════════════════════════════════════════════
    # 🔹 True / False Questions 
    # ══════════════════════════════════════════════
    {
        "q": "The bit string 101010011 has a length of nine.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! لو عديناهم هنلاقيهم فعلاً 9 أرقام (bits).",
        "explain_wrong": "❌ غلط! العبارة صحيحة، طولها 9."
    },
    {
        "q": "The sentence 'The automated reply cannot be sent when the file system is full' is correctly represented as p->q (where p=automated reply CAN be sent, q=file system is full).",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! التمثيل الصح هو q -> neg-p، لأن امتلاء النظام (q) هو اللي بيؤدي لعدم الإرسال (neg-p).",
        "explain_wrong": "❌ غلط! التمثيل الصح هو q -> neg-p مش p -> q."
    },
    {
        "q": "A tautology is a compound proposition that is always false.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! العبارة غلط، الـ Tautology دايماً True. الـ Contradiction هي اللي دايماً False.",
        "explain_wrong": "❌ غلط! الـ Tautology بتكون دايماً True."
    },
    {
        "q": "According to De Morgan's Law, neg(p or q) is logically equivalent to neg-p and neg-q.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! دي واحدة من قواعد دي مورجان الأساسية.",
        "explain_wrong": "❌ غلط! العبارة صحيحة، دي قاعدة دي مورجان."
    },
    {
        "q": "Any complicated digital circuit can be built using only three basic gates: OR gate, AND gate, and Inverter.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! أي دايرة مهما كانت معقدة نقدر نبنيها بالـ 3 بوابات دول بس.",
        "explain_wrong": "❌ غلط! العبارة دي صحيحة."
    }
]