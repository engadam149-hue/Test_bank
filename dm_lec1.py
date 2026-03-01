# ════════════════════════════════════════════════════════════
# 📖 dm_lec1.py
# Discrete Mathematics - Lecture 1
# Logic and Proofs: Propositional Logic & Compound Propositions
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # ✅ MCQ Questions
    # ══════════════════════════════════════════════

    {
        "q": "What is Logic?",
        "type": "mcq",
        "options": [
            "The discipline that deals with the methods of reasoning",
            "The study of numbers and equations",
            "The process of storing data in memory",
            "The rules of programming languages"
        ],
        "ans": "The discipline that deals with the methods of reasoning",
        "explain_correct": "✅ صح! الـ Logic هي العلم اللي بيتعامل مع طرق الاستدلال والتفكير المنطقي.",
        "explain_wrong": "❌ غلط! الـ Logic هي العلم الخاص بطرق الاستدلال والتفكير المنطقي."
    },
    {
        "q": "What is the basic building block of logic?",
        "type": "mcq",
        "options": [
            "Proposition",
            "Variable",
            "Operator",
            "Truth Table"
        ],
        "ans": "Proposition",
        "explain_correct": "✅ صح! الـ Proposition (القضية) هي اللبنة الأساسية للمنطق.",
        "explain_wrong": "❌ غلط! اللبنة الأساسية للمنطق هي الـ Proposition."
    },
    {
        "q": "What is a Proposition (or Statement)?",
        "type": "mcq",
        "options": [
            "A declarative sentence that is either true or false, but not both",
            "Any sentence that asks a question",
            "A command given to a computer",
            "A sentence that is always true"
        ],
        "ans": "A declarative sentence that is either true or false, but not both",
        "explain_correct": "✅ صح! الـ Proposition هي جملة خبرية إما صح أو غلط، مش الاتنين مع بعض.",
        "explain_wrong": "❌ غلط! الـ Proposition هي جملة خبرية (declarative) تكون إما True أو False فقط."
    },
    {
        "q": "Which of the following is a Proposition?",
        "type": "mcq",
        "options": [
            "Cairo is the capital of Egypt",
            "What time is it?",
            "Read this carefully.",
            "x + 3 = 7"
        ],
        "ans": "Cairo is the capital of Egypt",
        "explain_correct": "✅ صح! 'Cairo is the capital of Egypt' جملة خبرية ليها قيمة حقيقية (True)، فهي Proposition.",
        "explain_wrong": "❌ غلط! الـ Proposition لازم تكون جملة خبرية ليها قيمة True أو False. السؤال والأمر مش propositions."
    },
    {
        "q": "Which of the following is NOT a Proposition?",
        "type": "mcq",
        "options": [
            "What time is it?",
            "2 + 3 = 5",
            "Today is Friday",
            "5 - 2 = 1"
        ],
        "ans": "What time is it?",
        "explain_correct": "✅ صح! 'What time is it?' سؤال مش جملة خبرية، فمش Proposition.",
        "explain_wrong": "❌ غلط! الأسئلة والأوامر مش Propositions لأنها مش جمل خبرية."
    },
    {
        "q": "What is the truth value of the proposition '2 + 3 = 5'?",
        "type": "mcq",
        "options": [
            "True",
            "False",
            "Neither true nor false",
            "Both true and false"
        ],
        "ans": "True",
        "explain_correct": "✅ صح! 2 + 3 = 5 صحيحة رياضياً، فقيمتها الحقيقية True.",
        "explain_wrong": "❌ غلط! 2 + 3 = 5 صحيحة رياضياً، فقيمتها True."
    },
    {
        "q": "What letters are commonly used to denote propositional variables?",
        "type": "mcq",
        "options": [
            "p, q, r, s",
            "a, b, c, d",
            "x, y, z",
            "i, j, k"
        ],
        "ans": "p, q, r, s",
        "explain_correct": "✅ صح! الحروف المستخدمة عادةً للـ propositional variables هي p, q, r, s.",
        "explain_wrong": "❌ غلط! الحروف المستخدمة عادةً للـ propositional variables هي p, q, r, s."
    },
    {
        "q": "What are the two types of Propositions?",
        "type": "mcq",
        "options": [
            "Primitive and Compound",
            "True and False",
            "Simple and Complex",
            "Logical and Mathematical"
        ],
        "ans": "Primitive and Compound",
        "explain_correct": "✅ صح! نوعا الـ Propositions هما: Primitive (بسيطة) وCompound (مركبة).",
        "explain_wrong": "❌ غلط! نوعا الـ Propositions هما Primitive وCompound."
    },
    {
        "q": "How are Compound Propositions formed?",
        "type": "mcq",
        "options": [
            "From existing propositions using logical operators",
            "By asking questions",
            "From mathematical equations only",
            "By combining numbers"
        ],
        "ans": "From existing propositions using logical operators",
        "explain_correct": "✅ صح! الـ Compound Propositions بتتكون من propositions موجودة باستخدام logical operators.",
        "explain_wrong": "❌ غلط! الـ Compound Propositions بتتكون من propositions موجودة باستخدام logical operators."
    },
    {
        "q": "What is the Negation of a proposition p?",
        "type": "mcq",
        "options": [
            "The statement 'It is not the case that p', denoted by ¬p",
            "The statement 'p and q'",
            "The statement 'p or q'",
            "The statement 'if p then q'"
        ],
        "ans": "The statement 'It is not the case that p', denoted by ¬p",
        "explain_correct": "✅ صح! الـ Negation بتاعت p هي 'It is not the case that p' ورمزها ¬p.",
        "explain_wrong": "❌ غلط! الـ Negation بتاعت p هي ¬p وبتعني 'It is not the case that p'."
    },
    {
        "q": "If p is True, what is the truth value of ¬p?",
        "type": "mcq",
        "options": [
            "False",
            "True",
            "Unknown",
            "Both True and False"
        ],
        "ans": "False",
        "explain_correct": "✅ صح! لو p = True فـ ¬p = False، الـ Negation بتعكس القيمة الحقيقية.",
        "explain_wrong": "❌ غلط! لو p = True فـ ¬p = False لأن الـ Negation بتعكس القيمة."
    },
    {
        "q": "What is the negation of 'Cairo is the capital of Egypt'?",
        "type": "mcq",
        "options": [
            "Cairo is not the capital of Egypt",
            "Cairo is the capital of France",
            "Egypt has no capital",
            "It is not raining in Cairo"
        ],
        "ans": "Cairo is not the capital of Egypt",
        "explain_correct": "✅ صح! الـ Negation بتاعت 'Cairo is the capital of Egypt' هي 'Cairo is NOT the capital of Egypt'.",
        "explain_wrong": "❌ غلط! الـ Negation بتاعت أي جملة هي نفيها المباشر."
    },
    {
        "q": "What is the Conjunction of two propositions p and q?",
        "type": "mcq",
        "options": [
            "p ∧ q, the proposition 'p and q'",
            "p ∨ q, the proposition 'p or q'",
            "p → q, the proposition 'if p then q'",
            "¬p, the proposition 'not p'"
        ],
        "ans": "p ∧ q, the proposition 'p and q'",
        "explain_correct": "✅ صح! الـ Conjunction هو p ∧ q ويعني 'p and q'.",
        "explain_wrong": "❌ غلط! الـ Conjunction هو p ∧ q ويعني 'p and q'."
    },
    {
        "q": "When is the Conjunction p ∧ q TRUE?",
        "type": "mcq",
        "options": [
            "When both p and q are true",
            "When at least one of p or q is true",
            "When p is true and q is false",
            "When both p and q are false"
        ],
        "ans": "When both p and q are true",
        "explain_correct": "✅ صح! الـ Conjunction p ∧ q بتكون True فقط لما p وq الاتنين True.",
        "explain_wrong": "❌ غلط! الـ p ∧ q بتكون True فقط لما الاتنين True مع بعض."
    },
    {
        "q": "What is the truth value of p ∧ q when p = True and q = False?",
        "type": "mcq",
        "options": [
            "False",
            "True",
            "Unknown",
            "Depends on context"
        ],
        "ans": "False",
        "explain_correct": "✅ صح! p ∧ q = True ∧ False = False، لأن الـ AND محتاج الاتنين True.",
        "explain_wrong": "❌ غلط! p ∧ q = False لو أي واحد فيهم False."
    },
    {
        "q": "What is the Disjunction of two propositions p and q?",
        "type": "mcq",
        "options": [
            "p ∨ q, the proposition 'p or q'",
            "p ∧ q, the proposition 'p and q'",
            "p → q, the proposition 'if p then q'",
            "¬p, the proposition 'not p'"
        ],
        "ans": "p ∨ q, the proposition 'p or q'",
        "explain_correct": "✅ صح! الـ Disjunction هو p ∨ q ويعني 'p or q'.",
        "explain_wrong": "❌ غلط! الـ Disjunction هو p ∨ q ويعني 'p or q'."
    },
    {
        "q": "When is the Disjunction p ∨ q FALSE?",
        "type": "mcq",
        "options": [
            "When both p and q are false",
            "When both p and q are true",
            "When p is true and q is false",
            "When p is false and q is true"
        ],
        "ans": "When both p and q are false",
        "explain_correct": "✅ صح! الـ Disjunction p ∨ q بتكون False فقط لما p وq الاتنين False.",
        "explain_wrong": "❌ غلط! الـ p ∨ q بتكون False فقط لما الاتنين False."
    },
    {
        "q": "What is the Exclusive Or (XOR) of two propositions p and q?",
        "type": "mcq",
        "options": [
            "p ⊕ q, true when exactly one of p and q is true",
            "p ∧ q, true when both are true",
            "p ∨ q, true when at least one is true",
            "¬p ∧ ¬q, true when both are false"
        ],
        "ans": "p ⊕ q, true when exactly one of p and q is true",
        "explain_correct": "✅ صح! الـ XOR (p ⊕ q) بتكون True لما واحد بس منهم True، مش الاتنين.",
        "explain_wrong": "❌ غلط! الـ XOR (p ⊕ q) بتكون True لما بالظبط واحد منهم True."
    },
    {
        "q": "What is the truth value of p ⊕ q when both p and q are True?",
        "type": "mcq",
        "options": [
            "False",
            "True",
            "Unknown",
            "Both True and False"
        ],
        "ans": "False",
        "explain_correct": "✅ صح! p ⊕ q = False لما الاتنين True، لأن الـ XOR محتاج واحد بس يكون True.",
        "explain_wrong": "❌ غلط! الـ XOR بتكون False لما الاتنين True أو الاتنين False."
    },
    {
        "q": "What is the Conditional Statement p → q?",
        "type": "mcq",
        "options": [
            "The proposition 'if p, then q'",
            "The proposition 'p and q'",
            "The proposition 'p or q'",
            "The proposition 'not p'"
        ],
        "ans": "The proposition 'if p, then q'",
        "explain_correct": "✅ صح! الـ Conditional Statement p → q يعني 'if p, then q'.",
        "explain_wrong": "❌ غلط! الـ Conditional Statement p → q يعني 'if p, then q'."
    },
    {
        "q": "In the conditional statement p → q, what is p called?",
        "type": "mcq",
        "options": [
            "The hypothesis (or antecedent or premise)",
            "The conclusion (or consequence)",
            "The negation",
            "The contrapositive"
        ],
        "ans": "The hypothesis (or antecedent or premise)",
        "explain_correct": "✅ صح! في p → q الـ p بيتسمى hypothesis أو antecedent أو premise.",
        "explain_wrong": "❌ غلط! الـ p في p → q هو الـ hypothesis (or antecedent or premise)."
    },
    {
        "q": "In the conditional statement p → q, what is q called?",
        "type": "mcq",
        "options": [
            "The conclusion (or consequence)",
            "The hypothesis (or antecedent)",
            "The negation",
            "The converse"
        ],
        "ans": "The conclusion (or consequence)",
        "explain_correct": "✅ صح! في p → q الـ q بيتسمى conclusion أو consequence.",
        "explain_wrong": "❌ غلط! الـ q في p → q هو الـ conclusion (or consequence)."
    },
    {
        "q": "When is the Conditional Statement p → q FALSE?",
        "type": "mcq",
        "options": [
            "When p is true and q is false",
            "When p is false and q is true",
            "When both p and q are false",
            "When both p and q are true"
        ],
        "ans": "When p is true and q is false",
        "explain_correct": "✅ صح! الـ p → q بتكون False فقط لما p = True وq = False.",
        "explain_wrong": "❌ غلط! الـ p → q بتكون False في حالة واحدة فقط: لما p = True وq = False."
    },
    {
        "q": "What is the Converse of the conditional statement p → q?",
        "type": "mcq",
        "options": [
            "q → p",
            "¬p → ¬q",
            "¬q → ¬p",
            "p ∧ q"
        ],
        "ans": "q → p",
        "explain_correct": "✅ صح! الـ Converse بتاع p → q هو q → p (عكس الاتجاه).",
        "explain_wrong": "❌ غلط! الـ Converse بتاع p → q هو q → p."
    },
    {
        "q": "What is the Contrapositive of the conditional statement p → q?",
        "type": "mcq",
        "options": [
            "¬q → ¬p",
            "q → p",
            "¬p → ¬q",
            "p ∧ ¬q"
        ],
        "ans": "¬q → ¬p",
        "explain_correct": "✅ صح! الـ Contrapositive بتاع p → q هو ¬q → ¬p (عكس الاتنين وقلب الاتجاه).",
        "explain_wrong": "❌ غلط! الـ Contrapositive بتاع p → q هو ¬q → ¬p."
    },
    {
        "q": "What is the Inverse of the conditional statement p → q?",
        "type": "mcq",
        "options": [
            "¬p → ¬q",
            "q → p",
            "¬q → ¬p",
            "p ∨ q"
        ],
        "ans": "¬p → ¬q",
        "explain_correct": "✅ صح! الـ Inverse بتاع p → q هو ¬p → ¬q (نفي الاتنين من غير قلب الاتجاه).",
        "explain_wrong": "❌ غلط! الـ Inverse بتاع p → q هو ¬p → ¬q."
    },
    {
        "q": "Given p → q is 'If it is raining, then the home team wins', what is the Contrapositive?",
        "type": "mcq",
        "options": [
            "If the home team does not win, then it is not raining",
            "If the home team wins, then it is raining",
            "If it is not raining, then the home team does not win",
            "If it is raining, then the home team does not win"
        ],
        "ans": "If the home team does not win, then it is not raining",
        "explain_correct": "✅ صح! الـ Contrapositive هو ¬q → ¬p = 'If the home team does not win, then it is not raining'.",
        "explain_wrong": "❌ غلط! الـ Contrapositive = ¬q → ¬p = 'If the home team does not win, then it is not raining'."
    },
    {
        "q": "Given p → q is 'If it is raining, then the home team wins', what is the Converse?",
        "type": "mcq",
        "options": [
            "If the home team wins, then it is raining",
            "If the home team does not win, then it is not raining",
            "If it is not raining, then the home team does not win",
            "If it is raining, then the home team does not win"
        ],
        "ans": "If the home team wins, then it is raining",
        "explain_correct": "✅ صح! الـ Converse هو q → p = 'If the home team wins, then it is raining'.",
        "explain_wrong": "❌ غلط! الـ Converse = q → p = 'If the home team wins, then it is raining'."
    },
    {
        "q": "What is the Biconditional Statement p ↔ q?",
        "type": "mcq",
        "options": [
            "The proposition 'p if and only if q'",
            "The proposition 'if p then q'",
            "The proposition 'p and q'",
            "The proposition 'p or q'"
        ],
        "ans": "The proposition 'p if and only if q'",
        "explain_correct": "✅ صح! الـ Biconditional p ↔ q يعني 'p if and only if q' أو 'p iff q'.",
        "explain_wrong": "❌ غلط! الـ Biconditional p ↔ q يعني 'p if and only if q'."
    },
    {
        "q": "When is the Biconditional Statement p ↔ q TRUE?",
        "type": "mcq",
        "options": [
            "When p and q have the same truth values",
            "When p is true and q is false",
            "When p is false and q is true",
            "When both p and q are false only"
        ],
        "ans": "When p and q have the same truth values",
        "explain_correct": "✅ صح! الـ p ↔ q بتكون True لما p وq ليهم نفس القيمة (كلهم True أو كلهم False).",
        "explain_wrong": "❌ غلط! الـ Biconditional بتكون True لما الاتنين ليهم نفس القيمة."
    },
    {
        "q": "What is the truth value of p ↔ q when p = True and q = False?",
        "type": "mcq",
        "options": [
            "False",
            "True",
            "Unknown",
            "Both"
        ],
        "ans": "False",
        "explain_correct": "✅ صح! p ↔ q = False لما p وq مختلفين في القيمة.",
        "explain_wrong": "❌ غلط! الـ Biconditional بتكون False لما الاتنين مختلفين."
    },
    {
        "q": "Another name for the Biconditional Statement is:",
        "type": "mcq",
        "options": [
            "Bi-implication",
            "Double negation",
            "Exclusive OR",
            "Conjunction"
        ],
        "ans": "Bi-implication",
        "explain_correct": "✅ صح! الـ Biconditional بيتسمى كمان Bi-implication.",
        "explain_wrong": "❌ غلط! الـ Biconditional بيتسمى كمان Bi-implication."
    },
    {
        "q": "What is the precedence (priority) of the ¬ (Negation) operator?",
        "type": "mcq",
        "options": [
            "1 (highest priority)",
            "2",
            "4",
            "5 (lowest priority)"
        ],
        "ans": "1 (highest priority)",
        "explain_correct": "✅ صح! الـ ¬ (Negation) ليه أعلى أولوية (precedence = 1).",
        "explain_wrong": "❌ غلط! الـ ¬ ليه أعلى أولوية بـ precedence = 1."
    },
    {
        "q": "What is the correct order of precedence for logical operators (from highest to lowest)?",
        "type": "mcq",
        "options": [
            "¬, ∧, ∨, →, ↔",
            "∧, ∨, ¬, →, ↔",
            "↔, →, ∨, ∧, ¬",
            "¬, ∨, ∧, →, ↔"
        ],
        "ans": "¬, ∧, ∨, →, ↔",
        "explain_correct": "✅ صح! الترتيب الصح للأولوية من الأعلى للأقل: ¬ ثم ∧ ثم ∨ ثم → ثم ↔.",
        "explain_wrong": "❌ غلط! الترتيب الصح: ¬ (1) ، ∧ (2) ، ∨ (3) ، → (4) ، ↔ (5)."
    },
    {
        "q": "In computers, how is True (T) represented as a bit?",
        "type": "mcq",
        "options": [
            "1",
            "0",
            "2",
            "-1"
        ],
        "ans": "1",
        "explain_correct": "✅ صح! في الكمبيوتر True = 1 وFalse = 0.",
        "explain_wrong": "❌ غلط! في الكمبيوتر True = 1."
    },
    {
        "q": "What is a bit string?",
        "type": "mcq",
        "options": [
            "A sequence of zero or more bits",
            "A single binary digit",
            "A string of letters",
            "A sequence of decimal numbers"
        ],
        "ans": "A sequence of zero or more bits",
        "explain_correct": "✅ صح! الـ Bit String هي سلسلة من صفر أو أكثر من الـ bits.",
        "explain_wrong": "❌ غلط! الـ Bit String هي سلسلة من الـ bits."
    },
    {
        "q": "What is the length of the bit string '101010011'?",
        "type": "mcq",
        "options": [
            "9",
            "8",
            "7",
            "10"
        ],
        "ans": "9",
        "explain_correct": "✅ صح! '101010011' فيها 9 bits، فطولها 9.",
        "explain_wrong": "❌ غلط! عدد الـ bits في '101010011' هو 9."
    },
    {
        "q": "What is the result of bitwise OR for bits 0 and 1?",
        "type": "mcq",
        "options": [
            "1",
            "0",
            "2",
            "Undefined"
        ],
        "ans": "1",
        "explain_correct": "✅ صح! Bitwise OR: 0 ∨ 1 = 1 (لو واحد منهم 1 فالناتج 1).",
        "explain_wrong": "❌ غلط! Bitwise OR: 0 ∨ 1 = 1."
    },
    {
        "q": "What is the result of bitwise AND for bits 1 and 0?",
        "type": "mcq",
        "options": [
            "0",
            "1",
            "2",
            "Undefined"
        ],
        "ans": "0",
        "explain_correct": "✅ صح! Bitwise AND: 1 ∧ 0 = 0 (الـ AND محتاج الاتنين 1).",
        "explain_wrong": "❌ غلط! Bitwise AND: 1 ∧ 0 = 0."
    },
    {
        "q": "What is the result of bitwise XOR for bits 1 and 1?",
        "type": "mcq",
        "options": [
            "0",
            "1",
            "2",
            "Undefined"
        ],
        "ans": "0",
        "explain_correct": "✅ صح! Bitwise XOR: 1 ⊕ 1 = 0 (الـ XOR بيطلع 0 لما الاتنين متساويين).",
        "explain_wrong": "❌ غلط! Bitwise XOR: 1 ⊕ 1 = 0."
    },
    {
        "q": "For the bit strings '01 1011 0110' and '11 0001 1101', what is the bitwise OR?",
        "type": "mcq",
        "options": [
            "11 1011 1111",
            "01 0001 0100",
            "10 1010 1011",
            "00 1010 0001"
        ],
        "ans": "11 1011 1111",
        "explain_correct": "✅ صح! الـ Bitwise OR بتاخد كل bit تحت بعض: 01 1011 0110 ∨ 11 0001 1101 = 11 1011 1111.",
        "explain_wrong": "❌ غلط! الـ Bitwise OR بتحسب كل bit لحاله: 11 1011 1111."
    },
    {
        "q": "For the bit strings '01 1011 0110' and '11 0001 1101', what is the bitwise AND?",
        "type": "mcq",
        "options": [
            "01 0001 0100",
            "11 1011 1111",
            "10 1010 1011",
            "11 0001 1101"
        ],
        "ans": "01 0001 0100",
        "explain_correct": "✅ صح! الـ Bitwise AND: 01 1011 0110 ∧ 11 0001 1101 = 01 0001 0100.",
        "explain_wrong": "❌ غلط! الـ Bitwise AND: 01 0001 0100."
    },
    {
        "q": "In the truth table of (p ∨ ¬q) → (p ∧ q), what is the result when p = T and q = F?",
        "type": "mcq",
        "options": [
            "False",
            "True",
            "Unknown",
            "Depends"
        ],
        "ans": "False",
        "explain_correct": "✅ صح! لما p=T, q=F: ¬q=T, p∨¬q = T∨T = T, p∧q = T∧F = F, T→F = False.",
        "explain_wrong": "❌ غلط! p=T, q=F: ¬q=T, p∨¬q=T, p∧q=F, T→F = False."
    },
    {
        "q": "In the truth table of (p ∧ ¬q) → r, what is the result when p=T, q=F, r=F?",
        "type": "mcq",
        "options": [
            "False",
            "True",
            "Unknown",
            "Depends"
        ],
        "ans": "False",
        "explain_correct": "✅ صح! لما p=T, q=F, r=F: ¬q=T, p∧¬q = T∧T = T, T→F = False.",
        "explain_wrong": "❌ غلط! p=T, q=F, r=F: ¬q=T, p∧¬q=T, T→F = False."
    },
    {
        "q": "Which logical operator is used to represent 'p only if q'?",
        "type": "mcq",
        "options": [
            "Conditional (p → q)",
            "Conjunction (p ∧ q)",
            "Disjunction (p ∨ q)",
            "Biconditional (p ↔ q)"
        ],
        "ans": "Conditional (p → q)",
        "explain_correct": "✅ صح! 'p only if q' هي طريقة تانية لقول p → q (الـ Conditional).",
        "explain_wrong": "❌ غلط! 'p only if q' تعني p → q."
    },

    # ══════════════════════════════════════════════
    # ✅ True / False Questions
    # ══════════════════════════════════════════════

    {
        "q": "The sentence 'x + 3 = 7' (without specifying x) is a Proposition.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — 'x + 3 = 7' من غير تحديد قيمة x مش Proposition لأنها مش ليها قيمة حقيقية محددة (True أو False).",
        "explain_wrong": "❌ غلط! 'x + 3 = 7' من غير تحديد x مش Proposition لأن قيمتها الحقيقية مش محددة."
    },
    {
        "q": "The Conditional Statement p → q is false only when p is true and q is false.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! فعلاً الـ p → q بتكون False في حالة واحدة فقط: p=True وq=False.",
        "explain_wrong": "❌ غلط! فعلاً الـ Conditional Statement بتكون False في حالة واحدة بس: p=True وq=False."
    },
    {
        "q": "The Contrapositive of p → q is equivalent (has the same truth values) to p → q.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! الـ Contrapositive (¬q → ¬p) ليه نفس جدول الحقيقة بالظبط زي p → q، فهما متكافئان.",
        "explain_wrong": "❌ غلط! فعلاً الـ Contrapositive مكافئ للـ Conditional Statement الأصلية."
    },
    {
        "q": "The Biconditional p ↔ q is true when p is true and q is false.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — الـ Biconditional p ↔ q بتكون False لما p وq مختلفين. بتكون True فقط لما ليهم نفس القيمة.",
        "explain_wrong": "❌ غلط! الـ Biconditional بتكون False لما الاتنين مختلفين في القيمة."
    },
    {
        "q": "The Converse of p → q is logically equivalent to the original statement p → q.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! ده غلط — الـ Converse (q → p) مش مكافئ للـ p → q الأصلي. الـ Contrapositive هو اللي مكافئ.",
        "explain_wrong": "❌ غلط! الـ Converse (q → p) مش مكافئ للـ Conditional الأصلي. الـ Contrapositive هو المكافئ."
    }
]