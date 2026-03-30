"""
Discrete Mathematics Quiz - CSE315
New Mansoura University
استخرجت الأمثلة من المحاضرات:
  - Lecture 1 (Ch1): Propositional Logic, Compound Propositions, Truth Tables,
                     Converse/Contrapositive/Inverse, Biconditional, Precedence
  - Lecture 2 (Ch1): Logic Circuits, Logical Equivalences, Applications of Propositional Logic
  - Lecture 3 (Ch1): Bit Strings, Translating English, Tautology
  - Lecture 4 (Ch2 Part 1): Sets, Subsets, Power Set, Cartesian Product, Set Operations
"""

import random

# ─────────────────────────────────────────────
#  COLOUR HELPERS
# ─────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ─────────────────────────────────────────────
#  QUESTION BANK
# ─────────────────────────────────────────────
QUESTIONS = [

    # ══════════════════════════════════════════
    #  CH1 – Lecture 1  (Propositions – Basics)
    # ══════════════════════════════════════════
    {
        "question": "[Lec1-p13] Which of the following is a proposition (has a truth value)?",
        "options": [
            "What time is it?",
            "Read this carefully.",
            "x + 3 = 7",
            "Cairo is the capital of Egypt",
        ],
        "answer": 3,
        "explanation": (
            "الـ Proposition هي جملة خبرية (declarative sentence) ليها قيمة صح أو غلط.\n"
            "  - 'What time is it?' → سؤال ← مش proposition\n"
            "  - 'Read this carefully.' → أمر ← مش proposition\n"
            "  - 'x + 3 = 7' → مش محدد قيمتها لأن x مجهول ← مش proposition\n"
            "  - 'Cairo is the capital of Egypt' → جملة خبرية = True ← proposition ✓\n"
            "الفرق: الـ proposition لازم تكون إما True أو False بشكل قاطع."
        ),
        "source": "Lecture 1, Slide 13",
    },
    {
        "question": "[Lec1-p13] What is the truth value of the proposition: '5 − 2 = 1'?",
        "options": ["True", "False", "Undefined", "Both True and False"],
        "answer": 1,
        "explanation": (
            "5 − 2 = 3 مش 1.\n"
            "الجملة دي proposition لأنها جملة خبرية بس قيمتها False.\n"
            "مش كل proposition لازم تكون True - ممكن تكون False وده برضو صح."
        ),
        "source": "Lecture 1, Slide 13",
    },
    {
        "question": "[Lec1-p13] Which sentence is NOT a proposition?",
        "options": [
            "2 + 3 = 5",
            "Today is Friday",
            "x + 3 = 7  (x is unknown)",
            "Cairo is the capital of Egypt",
        ],
        "answer": 2,
        "explanation": (
            "'x + 3 = 7' مش proposition لأن قيمتها بتختلف حسب قيمة x:\n"
            "  - لو x = 4 → True\n"
            "  - لو x = 5 → False\n"
            "بما إن مش عندنا قيمة محددة لـ x, الجملة مش قادرة تتحدد قيمتها ← مش proposition.\n"
            "لكن لو كتبت 'x + 3 = 7, for x = 4' ← دي proposition وقيمتها True."
        ),
        "source": "Lecture 1, Slide 13",
    },

    # ── Negation ──
    {
        "question": "[Lec1-p18] What is the negation of: 'Cairo is the capital of Egypt'?",
        "options": [
            "Cairo is the capital of France",
            "Cairo is not the capital of Egypt",
            "Egypt has no capital",
            "Alexandria is the capital of Egypt",
        ],
        "answer": 1,
        "explanation": (
            "الـ Negation (¬p) = 'It is not the case that p'\n"
            "p: 'Cairo is the capital of Egypt'\n"
            "¬p: 'Cairo is NOT the capital of Egypt'\n"
            "الـ negation بتعكس قيمة الـ proposition فقط - مش بتغير المحتوى.\n"
            "الخيار التاني هو الصح لأنه مجرد نفي للجملة الأصلية."
        ),
        "source": "Lecture 1, Slides 17-18",
    },
    {
        "question": "[Lec1-p20] From the truth table of negation: if p = F, then ¬p = ?",
        "options": ["F", "T", "F or T", "Undefined"],
        "answer": 1,
        "explanation": (
            "جدول الحقيقة للـ Negation:\n"
            "  p = T  →  ¬p = F\n"
            "  p = F  →  ¬p = T\n"
            "الـ negation دايمًا بتعكس القيمة:\n"
            "  - True يبقى False\n"
            "  - False يبقى True"
        ),
        "source": "Lecture 1, Slide 20",
    },

    # ── Conjunction (AND) ──
    {
        "question": "[Lec1-p22] When is p ∧ q (conjunction) TRUE?",
        "options": [
            "When at least one of p or q is true",
            "When p is true only",
            "When both p and q are true",
            "When p and q have different values",
        ],
        "answer": 2,
        "explanation": (
            "الـ Conjunction (p ∧ q) = 'p AND q'\n"
            "جدول الحقيقة:\n"
            "  T ∧ T = T  ← الحالة الوحيدة اللي بتطلع True\n"
            "  T ∧ F = F\n"
            "  F ∧ T = F\n"
            "  F ∧ F = F\n"
            "القاعدة: الـ AND بيطلع True بس لما الاثنين True مع بعض."
        ),
        "source": "Lecture 1, Slide 22",
    },
    {
        "question": "[Lec1-p22] p = 'Today is Friday', q = 'It is raining today'.\n"
                    "What does p ∧ q mean in English?",
        "options": [
            "Today is Friday or it is raining today",
            "Today is Friday and it is raining today",
            "If today is Friday, then it is raining",
            "Today is not Friday and it is not raining",
        ],
        "answer": 1,
        "explanation": (
            "الـ Conjunction (∧) بيترجم دايمًا بكلمة 'AND' (و).\n"
            "p ∧ q = 'Today is Friday AND it is raining today'\n"
            "الجملة دي True بس لو الاثنين صحيحين مع بعض:\n"
            "  - النهارده الجمعة فعلاً AND بتمطر فعلاً."
        ),
        "source": "Lecture 1, Slide 22",
    },

    # ── Disjunction (OR) ──
    {
        "question": "[Lec1-p23] When is p ∨ q (disjunction) FALSE?",
        "options": [
            "When both p and q are true",
            "When p is false only",
            "When both p and q are false",
            "When p and q are different",
        ],
        "answer": 2,
        "explanation": (
            "الـ Disjunction (p ∨ q) = 'p OR q'\n"
            "جدول الحقيقة:\n"
            "  T ∨ T = T\n"
            "  T ∨ F = T\n"
            "  F ∨ T = T\n"
            "  F ∨ F = F  ← الحالة الوحيدة اللي بتطلع False\n"
            "القاعدة: الـ OR بيطلع False بس لما الاثنين False مع بعض."
        ),
        "source": "Lecture 1, Slide 23",
    },

    # ── Exclusive OR (XOR) ──
    {
        "question": "[Lec1-p24] p = 'They are parents', q = 'They are children'.\n"
                    "p ⊕ q means: 'They are parents or children, but not both'.\n"
                    "What is the truth value of p ⊕ q when BOTH p and q are TRUE?",
        "options": ["True", "False", "Undefined", "Depends on context"],
        "answer": 1,
        "explanation": (
            "الـ Exclusive OR (p ⊕ q) = XOR\n"
            "بيطلع True بس لما الاثنين مختلفين (واحد True والتاني False).\n"
            "جدول الحقيقة:\n"
            "  T ⊕ T = F  ← لأن الاثنين متساويين\n"
            "  T ⊕ F = T\n"
            "  F ⊕ T = T\n"
            "  F ⊕ F = F  ← لأن الاثنين متساويين\n"
            "الفرق بين OR و XOR: الـ OR بيقبل لما الاثنين True, الـ XOR لأ."
        ),
        "source": "Lecture 1, Slide 24",
    },
    {
        "question": "[Lec1-p24] The XOR operator (⊕) gives TRUE when:",
        "options": [
            "Both propositions are true",
            "Both propositions are false",
            "Exactly one proposition is true",
            "At least one proposition is true",
        ],
        "answer": 2,
        "explanation": (
            "الـ XOR (Exclusive OR) = 'أو الواحد بالظبط'\n"
            "  T ⊕ T = F  (الاثنين true → False)\n"
            "  T ⊕ F = T  (بس واحد true → True) ✓\n"
            "  F ⊕ T = T  (بس واحد true → True) ✓\n"
            "  F ⊕ F = F  (الاثنين false → False)\n"
            "'Exactly one' معناها واحد بس مش الاثنين."
        ),
        "source": "Lecture 1, Slide 24",
    },

    # ── Conditional Statement ──
    {
        "question": "[Lec1-p25] The conditional statement p → q is FALSE only when:",
        "options": [
            "p is False and q is True",
            "p is True and q is False",
            "Both p and q are False",
            "Both p and q are True",
        ],
        "answer": 1,
        "explanation": (
            "الـ Conditional Statement (p → q) = 'If p, then q'\n"
            "جدول الحقيقة:\n"
            "  T → T = T\n"
            "  T → F = F  ← الحالة الوحيدة اللي بتطلع False\n"
            "  F → T = T  (Vacuously true)\n"
            "  F → F = T  (Vacuously true)\n"
            "القاعدة: الـ conditional بيطلع False بس لما الـ hypothesis (p) صح والـ conclusion (q) غلط.\n"
            "مثال: 'لو جبت 100% هاخد A' - لو جبت 100 بس الدكتور ما أداكش A = وعد مكسور = False."
        ),
        "source": "Lecture 1, Slide 25",
    },
    {
        "question": "[Lec1-p25] In the conditional p → q, what is p called?",
        "options": [
            "Conclusion (consequence)",
            "Hypothesis (antecedent/premise)",
            "Contrapositive",
            "Converse",
        ],
        "answer": 1,
        "explanation": (
            "في الـ Conditional Statement p → q:\n"
            "  - p = الـ Hypothesis (الفرضية) — يُسمى أيضاً antecedent أو premise\n"
            "  - q = الـ Conclusion (النتيجة) — يُسمى أيضاً consequence\n"
            "مثال: 'If it is raining (p), then the ground is wet (q)'\n"
            "  p = 'it is raining' هو الـ hypothesis\n"
            "  q = 'the ground is wet' هو الـ conclusion"
        ),
        "source": "Lecture 1, Slide 25",
    },
    {
        "question": "[Lec1-p26] 'If you get 100% on the final, then you will get an A.'\n"
                    "You got 100% but did NOT get an A. What is the truth value of this conditional?",
        "options": ["True", "False", "Undefined", "Cannot be determined"],
        "answer": 1,
        "explanation": (
            "p = 'You get 100% on the final' → True (حصل)\n"
            "q = 'You will get an A' → False (ما حصلش)\n"
            "p → q = T → F = FALSE\n"
            "لأن الوعد اتكسر: الـ hypothesis صح بس الـ conclusion غلط.\n"
            "ده زي 'الكذبة': وعدت بحاجة وما وفيتش."
        ),
        "source": "Lecture 1, Slide 26",
    },
    {
        "question": "[Lec1-p28] Let p = 'Maria learns discrete mathematics',\n"
                    "          q = 'Maria will find a good job'.\n"
                    "Express p → q as a sentence in English.",
        "options": [
            "Maria learns discrete mathematics and finds a good job",
            "If Maria learns discrete mathematics, then she will find a good job",
            "Maria will find a good job only if she does not learn discrete mathematics",
            "Maria learns discrete mathematics if she finds a good job",
        ],
        "answer": 1,
        "explanation": (
            "p → q تُقرأ بطرق كتير، أشهرها:\n"
            "  'If p, then q'\n"
            "  'p implies q'\n"
            "  'q when p'\n"
            "  'p only if q'\n"
            "هنا: 'If Maria learns discrete mathematics, then she will find a good job'\n"
            "أو: 'Maria will find a good job when she learns discrete mathematics'"
        ),
        "source": "Lecture 1, Slides 27-28",
    },

    # ── Converse, Contrapositive, Inverse ──
    {
        "question": "[Lec1-p30-32] For the conditional p → q,\n"
                    "what is the CONTRAPOSITIVE?",
        "options": [
            "q → p",
            "¬p → ¬q",
            "¬q → ¬p",
            "¬p → q",
        ],
        "answer": 2,
        "explanation": (
            "من الـ conditional p → q نستخرج 3 أشياء:\n"
            "  - Converse (عكس):        q → p\n"
            "  - Inverse (معكوس):       ¬p → ¬q\n"
            "  - Contrapositive (معاكس الجاني): ¬q → ¬p  ← ده المطلوب\n"
            "مهم جداً: الـ Contrapositive دايمًا له نفس قيمة الـ conditional الأصلي!\n"
            "يعني p → q ≡ ¬q → ¬p"
        ),
        "source": "Lecture 1, Slides 30-31",
    },
    {
        "question": "[Lec1-p32] Given: 'The home team wins whenever it is raining.' (p → q)\n"
                    "p = 'it is raining', q = 'the home team wins'\n\n"
                    "What is the CONVERSE (q → p) in English?",
        "options": [
            "If the home team does not win, then it is not raining",
            "If it is not raining, then the home team does not win",
            "If the home team wins, then it is raining",
            "If it is raining, then the home team does not win",
        ],
        "answer": 2,
        "explanation": (
            "الـ Original: p → q = 'If it is raining, then the home team wins'\n"
            "الـ Converse: q → p = 'If the home team wins, then it is raining'\n"
            "ده مجرد عكس الطرفين من غير نفي.\n"
            "ملاحظة: الـ Converse مش لازم يكون له نفس قيمة الـ original!\n"
            "الـ Contrapositive هو اللي دايمًا متكافئ مع الـ original."
        ),
        "source": "Lecture 1, Slide 32",
    },
    {
        "question": "[Lec1-p32] Given: p → q = 'If it is raining, then the home team wins'.\n"
                    "What is the INVERSE (¬p → ¬q)?",
        "options": [
            "If the home team wins, then it is raining",
            "If the home team does not win, then it is not raining",
            "If it is not raining, then the home team does not win",
            "If it is raining, then the home team does not win",
        ],
        "answer": 2,
        "explanation": (
            "الـ Inverse = ¬p → ¬q = نفي الطرفين من غير عكسهم\n"
            "p = 'it is raining'   → ¬p = 'it is NOT raining'\n"
            "q = 'home team wins'  → ¬q = 'home team does NOT win'\n"
            "الـ Inverse: 'If it is NOT raining, then the home team does NOT win'\n"
            "مهم: الـ Inverse متكافئ مع الـ Converse (مش مع الـ Original)."
        ),
        "source": "Lecture 1, Slide 32",
    },
    {
        "question": "[Lec1-p29] 'If it is sunny, then you will go to the beach.'\n"
                    "What is the truth value when it IS sunny but you do NOT go to the beach?",
        "options": ["True", "False", "Undefined", "True, because the condition is met"],
        "answer": 1,
        "explanation": (
            "p = 'it is sunny' = True\n"
            "q = 'you will go to the beach' = False\n"
            "p → q = T → F = FALSE\n"
            "الوعد اتكسر: الشرط (sunny) اتحقق بس النتيجة (go to beach) ما حصلتش."
        ),
        "source": "Lecture 1, Slide 29",
    },
    {
        "question": "[Lec1-p29] 'If today is Friday, then 2 + 3 = 6.'\n"
                    "Suppose today is NOT Friday. What is the truth value?",
        "options": [
            "False, because 2+3 ≠ 6",
            "True, because the hypothesis is false (vacuously true)",
            "False, because today is not Friday",
            "Undefined",
        ],
        "answer": 1,
        "explanation": (
            "p = 'today is Friday' = False\n"
            "p → q = F → (anything) = TRUE  ← دايمًا True لو الـ hypothesis False\n"
            "ده اللي بيسموه 'Vacuously True' (صح بالفراغ)\n"
            "القاعدة: لو الشرط (hypothesis) غلط أصلاً، الـ conditional بيبقى True تلقائياً\n"
            "مثال: 'لو الفيل طار, هو ذكي' - الفيل مش طار → الجملة صحيحة (vacuously)."
        ),
        "source": "Lecture 1, Slide 29",
    },

    # ── Biconditional ──
    {
        "question": "[Lec1-p40] The biconditional p ↔ q is TRUE when:",
        "options": [
            "p is true and q is false",
            "p is false and q is true",
            "p and q have the same truth value",
            "p and q have different truth values",
        ],
        "answer": 2,
        "explanation": (
            "الـ Biconditional (p ↔ q) = 'p if and only if q' = 'p iff q'\n"
            "جدول الحقيقة:\n"
            "  T ↔ T = T  ← نفس القيمة\n"
            "  T ↔ F = F\n"
            "  F ↔ T = F\n"
            "  F ↔ F = T  ← نفس القيمة\n"
            "القاعدة: الـ biconditional True لما الاثنين بيتساووا في القيمة.\n"
            "مثال: 'You can take the flight if and only if you buy a ticket.'"
        ),
        "source": "Lecture 1, Slide 40",
    },
    {
        "question": "[Lec1-p40] Which phrase is equivalent to the biconditional p ↔ q?",
        "options": [
            "p only if q",
            "p is necessary for q",
            "p if and only if q",
            "if p then q",
        ],
        "answer": 2,
        "explanation": (
            "طرق قراءة الـ Biconditional p ↔ q:\n"
            "  ✓ 'p if and only if q'  (أشهرها)\n"
            "  ✓ 'p is necessary and sufficient for q'\n"
            "  ✓ 'if p then q, and conversely'\n"
            "  ✓ 'p iff q'\n"
            "  ✓ 'p exactly when q'\n"
            "الاختيارات التانية:\n"
            "  'p only if q' = p → q  (مش biconditional)\n"
            "  'p is necessary for q' = q → p"
        ),
        "source": "Lecture 1, Slide 40",
    },

    # ── Truth Tables – Compound ──
    {
        "question": "[Lec1-p42-47] For the compound proposition (p ∨ ¬q) → (p ∧ q),\n"
                    "what is the result when p = T and q = F?",
        "options": ["T", "F", "T → F = T", "Cannot determine"],
        "answer": 1,
        "explanation": (
            "نحسب خطوة بخطوة لما p=T, q=F:\n"
            "  1. ¬q = ¬F = T\n"
            "  2. p ∨ ¬q = T ∨ T = T\n"
            "  3. p ∧ q = T ∧ F = F\n"
            "  4. (p ∨ ¬q) → (p ∧ q) = T → F = F\n"
            "القاعدة: T → F = FALSE دايمًا (الوعد اتكسر)."
        ),
        "source": "Lecture 1, Slides 42-47",
    },
    {
        "question": "[Lec1-p49-54] For (p ∧ ¬q) → r,\n"
                    "what is the result when p = T, q = F, r = F?",
        "options": ["T", "F", "Undefined", "T because p is True"],
        "answer": 1,
        "explanation": (
            "نحسب خطوة بخطوة لما p=T, q=F, r=F:\n"
            "  1. ¬q = ¬F = T\n"
            "  2. p ∧ ¬q = T ∧ T = T\n"
            "  3. (p ∧ ¬q) → r = T → F = F\n"
            "من جدول الحقيقة الكامل في المحاضرة: الصف p=T,q=F,r=F بيطلع F.\n"
            "الحالة دي هي الوحيدة اللي بتطلع F في السؤال ده."
        ),
        "source": "Lecture 1, Slides 49-54",
    },
    {
        "question": "[Lec1-p54] In the truth table for (p ∧ ¬q) → r,\n"
                    "how many rows give a result of FALSE?",
        "options": ["1", "2", "3", "4"],
        "answer": 0,
        "explanation": (
            "من جدول الحقيقة الكامل (8 صفوف لـ 3 متغيرات):\n"
            "  T T T → F → T\n"
            "  T T F → F → T\n"
            "  T F T → T → T  ✓\n"
            "  T F F → T → F  ← الصف الوحيد اللي بيطلع False!\n"
            "  F T T → F → T\n"
            "  F T F → F → T\n"
            "  F F T → F → T\n"
            "  F F F → F → T\n"
            "← في صف واحد بس بيطلع False."
        ),
        "source": "Lecture 1, Slide 54",
    },

    # ── Precedence of Logical Operators ──
    {
        "question": "[Lec1-p48] According to the precedence table,\n"
                    "which operator has the HIGHEST precedence (evaluated first)?",
        "options": ["∧  (AND)", "∨  (OR)", "¬  (NOT)", "→  (implies)"],
        "answer": 2,
        "explanation": (
            "ترتيب الأولوية (Precedence) من الأعلى للأقل:\n"
            "  1. ¬  (NOT)   ← الأعلى أولوية\n"
            "  2. ∧  (AND)\n"
            "  3. ∨  (OR)\n"
            "  4. →  (implies)\n"
            "  5. ↔  (biconditional)  ← الأقل أولوية\n"
            "مثل الرياضيات: × قبل + - كذلك ¬ قبل ∧ قبل ∨."
        ),
        "source": "Lecture 1, Slide 48",
    },
    {
        "question": "[Lec1-p48] How is the expression  ¬p ∧ q  parsed (which operator applies first)?",
        "options": [
            "¬(p ∧ q)  — NOT applies to the whole conjunction",
            "(¬p) ∧ q  — NOT applies to p first, then AND",
            "¬p ∧ (q)  — same as above but written differently",
            "Ambiguous without parentheses",
        ],
        "answer": 1,
        "explanation": (
            "بما إن ¬ ليها أعلى أولوية من ∧:\n"
            "¬p ∧ q  يُحسب كـ  (¬p) ∧ q\n"
            "يعني الـ NOT بيتطبق على p بس مش على الجملة كلها.\n"
            "لو عايز الـ NOT يتطبق على الكل لازم تكتب: ¬(p ∧ q)\n"
            "مثال: ¬T ∧ F = F ∧ F = F\n"
            "     ¬(T ∧ F) = ¬F = T  ← نتيجة مختلفة!"
        ),
        "source": "Lecture 1, Slide 48",
    },

    # ── Example 3 – Identify Hypothesis & Conclusion ──
    {
        "question": "[Lec1-p34] 'If two angles are adjacent, then they have a common side.'\n"
                    "What is the HYPOTHESIS of this conditional?",
        "options": [
            "They have a common side",
            "Two angles are adjacent",
            "Two angles are vertical",
            "The angles are congruent",
        ],
        "answer": 1,
        "explanation": (
            "في الجملة 'If P, then Q':\n"
            "  - الـ Hypothesis = الجزء بعد 'If' = P\n"
            "  - الـ Conclusion = الجزء بعد 'then' = Q\n"
            "هنا:\n"
            "  H (hypothesis): 'Two angles are adjacent'\n"
            "  C (conclusion):  'They have a common side'\n"
            "الـ hypothesis هو الشرط اللي لو اتحقق تحقق الـ conclusion."
        ),
        "source": "Lecture 1, Slide 34",
    },
    {
        "question": "[Lec1-p34] 'If 3x − 4 = 11, then x = 5.'\n"
                    "Is this conditional statement TRUE or FALSE?",
        "options": [
            "True, because x = 5 satisfies the equation",
            "False, because 3(5) − 4 = 11 is correct",
            "True, because 3(5) − 4 = 11 ✓ so T → T = T",
            "False, because x could be another value",
        ],
        "answer": 2,
        "explanation": (
            "نتحقق: لو x = 5, هل 3x − 4 = 11؟\n"
            "  3(5) − 4 = 15 − 4 = 11 ✓  ← True\n"
            "إذاً:\n"
            "  p = '3x − 4 = 11' = True\n"
            "  q = 'x = 5' = True\n"
            "  p → q = T → T = TRUE ✓\n"
            "الجملة صحيحة لأن الشرط والنتيجة الاثنين صح."
        ),
        "source": "Lecture 1, Slide 34",
    },

    # ── Example 4 – Rewrite in if-then form ──
    {
        "question": "[Lec1-p35-36] Rewrite in if-then form:\n"
                    "'The intersection of two planes is a line.'",
        "options": [
            "If a line intersects a plane, then two planes exist",
            "If two planes intersect, then the intersection is a line",
            "If the intersection is a line, then two planes intersect",
            "Two planes intersect if and only if the intersection is a line",
        ],
        "answer": 1,
        "explanation": (
            "لما بنكتب جملة عادية كـ if-then:\n"
            "  الموضوع الأصلي → الـ Hypothesis\n"
            "  الخبر أو النتيجة → الـ Conclusion\n"
            "'The intersection of two planes is a line'\n"
            "  H: 'two planes intersect'\n"
            "  C: 'the intersection is a line'\n"
            "← 'If two planes intersect, then the intersection is a line.'"
        ),
        "source": "Lecture 1, Slides 35-36",
    },
    {
        "question": "[Lec1-p36] Rewrite in if-then form:\n"
                    "'A right angle measures 90 degrees.'",
        "options": [
            "If an angle is 90 degrees, then it is a right angle",
            "If an angle is right, then it measures 90 degrees",
            "An angle is right if and only if it measures 90 degrees",
            "If an angle is not right, then it does not measure 90 degrees",
        ],
        "answer": 1,
        "explanation": (
            "'A right angle measures 90 degrees'\n"
            "  H: 'an angle is right'\n"
            "  C: 'the angle measures 90°'\n"
            "← 'If an angle is right, then the angle measures 90 degrees'\n"
            "الخيار الأول (If 90° → right angle) هو الـ Converse مش الـ Original."
        ),
        "source": "Lecture 1, Slide 36",
    },

    # ── Example 5 – Converse/Inverse/Contrapositive ──
    {
        "question": "[Lec1-p37-39] Statement: 'If you have five dollars, then you can buy five raffle tickets.'\n"
                    "What is the CONTRAPOSITIVE?",
        "options": [
            "If you can buy five raffle tickets, then you have five dollars",
            "If you do not have five dollars, then you cannot buy five raffle tickets",
            "If you cannot buy five raffle tickets, then you do not have five dollars",
            "If you have five dollars, then you cannot buy five raffle tickets",
        ],
        "answer": 2,
        "explanation": (
            "p = 'you have five dollars'\n"
            "q = 'you can buy five raffle tickets'\n"
            "الـ Contrapositive = ¬q → ¬p:\n"
            "'If you CANNOT buy five raffle tickets, then you do NOT have five dollars.'\n"
            "✓ الـ Contrapositive دايمًا له نفس قيمة الـ Original!\n"
            "الخيار الأول هو الـ Converse (q → p).\n"
            "الخيار الثاني هو الـ Inverse (¬p → ¬q)."
        ),
        "source": "Lecture 1, Slides 37-39",
    },
    {
        "question": "[Lec1-p39] Statement: 'If two angles are complementary, then the angles are acute.'\n"
                    "Is the CONVERSE true or false?",
        "options": [
            "True — if angles are acute, they must be complementary",
            "False — two acute angles don't have to be complementary (sum could be < 90°)",
            "True — acute angles always sum to 90°",
            "False — complementary angles are always obtuse",
        ],
        "answer": 1,
        "explanation": (
            "الـ Original: 'If complementary → acute' = True\n"
            "الـ Converse: 'If acute → complementary'\n"
            "Counterexample: زاويتين كل واحدة 40° (كلهم acute)\n"
            "  مجموعهم = 80° ≠ 90°  ← مش complementary!\n"
            "إذاً الـ Converse = False.\n"
            "ده بيثبت إن الـ Converse مش دايمًا له نفس قيمة الـ Original."
        ),
        "source": "Lecture 1, Slide 39",
    },

    # ── Computer Bit Operations (Lec1) ──
    {
        "question": "[Lec1-p55-56] In computer bit operations, which truth value corresponds to bit 1?",
        "options": ["False (F)", "True (T)", "Undefined", "Both 0 and 1"],
        "answer": 1,
        "explanation": (
            "الكمبيوتر بيمثل المنطق بـ bits:\n"
            "  T (True)  = 1\n"
            "  F (False) = 0\n"
            "وبكده الـ logical operators بيتحولوا لـ bit operations:\n"
            "  OR  (∨) → 1 OR 1 = 1\n"
            "  AND (∧) → 1 AND 0 = 0\n"
            "  XOR (⊕) → 1 XOR 1 = 0"
        ),
        "source": "Lecture 1, Slide 55",
    },
    {
        "question": "[Lec1-p56] From the bit operators table: what is  1 XOR 1?",
        "options": ["0", "1", "Undefined", "2"],
        "answer": 0,
        "explanation": (
            "جدول الـ XOR (⊕):\n"
            "  0 ⊕ 0 = 0\n"
            "  0 ⊕ 1 = 1\n"
            "  1 ⊕ 0 = 1\n"
            "  1 ⊕ 1 = 0  ← لأن الاثنين متساويين\n"
            "الـ XOR = 1 بس لما الاثنين مختلفين.\n"
            "لما الاثنين نفس القيمة (سواء 0,0 أو 1,1) النتيجة = 0."
        ),
        "source": "Lecture 1, Slide 56",
    },

    # ══════════════════════════════════════════
    #  CH1 – Lecture 3  (Bit Strings & Logic Circuits)
    # ══════════════════════════════════════════
    {
        "question": "[Lec3-p2] A bit string is a sequence of zero or more bits.\n"
                    "What is the length of the bit string  101010011 ?",
        "options": ["7", "8", "9", "10"],
        "answer": 2,
        "explanation": (
            "الـ bit string اللي هي '101010011' عندها 9 bits لو عددناهم واحد واحد:\n"
            "1-0-1-0-1-0-0-1-1  ← 9 بالظبط.\n"
            "الطول (length) = عدد الـ bits الموجودة في الـ string."
        ),
        "source": "Lecture 3, Slide 2",
    },
    {
        "question": "[Lec3-p3] Find the bitwise OR of  01 1011 0110  and  11 0001 1101.",
        "options": [
            "11 1011 1111",
            "01 0001 0100",
            "10 1010 1011",
            "00 0000 0000",
        ],
        "answer": 0,
        "explanation": (
            "الـ bitwise OR بتحط 1 لو أي واحد من الـ bits في نفس الموقع = 1.\n"
            "  01 1011 0110\n"
            "  11 0001 1101\n"
            "  ────────────\n"
            "  11 1011 1111  ← كل position فيها 1 في أي من الاثنين بتطلع 1.\n"
            "الخيار الثاني (01 0001 0100) هو الـ AND، والثالث (10 1010 1011) هو الـ XOR."
        ),
        "source": "Lecture 3, Slide 3",
    },
    {
        "question": "[Lec3-p3] Find the bitwise AND of  01 1011 0110  and  11 0001 1101.",
        "options": [
            "11 1011 1111",
            "01 0001 0100",
            "10 1010 1011",
            "11 0000 0000",
        ],
        "answer": 1,
        "explanation": (
            "الـ bitwise AND بتحط 1 بس لو الاثنين 1 في نفس الموقع.\n"
            "  01 1011 0110\n"
            "  11 0001 1101\n"
            "  ────────────\n"
            "  01 0001 0100  ← بس الـ positions اللي فيها 1 في الاثنين مع بعض.\n"
            "الخيار الأول هو الـ OR، والثالث هو الـ XOR."
        ),
        "source": "Lecture 3, Slide 3",
    },
    {
        "question": "[Lec3-p3] Find the bitwise XOR of  01 1011 0110  and  11 0001 1101.",
        "options": [
            "11 1011 1111",
            "01 0001 0100",
            "10 1010 1011",
            "00 1010 1011",
        ],
        "answer": 2,
        "explanation": (
            "الـ bitwise XOR بتحط 1 لو الاثنين مختلفين (واحد 0 والتاني 1) في نفس الموقع.\n"
            "  01 1011 0110\n"
            "  11 0001 1101\n"
            "  ────────────\n"
            "  10 1010 1011  ← الـ positions اللي فيها الاثنين زي بعض بتطلع 0."
        ),
        "source": "Lecture 3, Slide 3",
    },

    # ══════════════════════════════════════════
    #  CH1 – Lecture 3  (Translating English Sentences)
    # ══════════════════════════════════════════
    {
        "question": "[Lec3-p7-10] Let p = 'You can access the Internet from campus',\n"
                    "             q = 'You are a computer science major',\n"
                    "             r = 'You are a student'.\n\n"
                    "Translate: 'You can access the Internet from campus ONLY IF\n"
                    "            you are a computer science major or you are not a student.'",
        "options": [
            "p → (q ∨ ¬r)",
            "(q ∨ ¬r) → p",
            "p ∧ (q ∨ ¬r)",
            "¬p → (q ∧ r)",
        ],
        "answer": 0,
        "explanation": (
            "كلمة 'only if' في المنطق معناها: p → q   (p بس لو q).\n"
            "الجملة تتقرأ: (p) only if (q ∨ ¬r)\n"
            "← يعني p → (q ∨ ¬r).\n"
            "التعبير اللي بعد 'only if' هو اللي بيبقى الـ consequent (الطرف الأيمن في السهم)."
        ),
        "source": "Lecture 3, Slides 7-10",
    },
    {
        "question": "[Lec3-p11-13] Let p = 'The automated reply can be sent',\n"
                    "              q = 'The file system is full'.\n\n"
                    "Translate: 'The automated reply CANNOT be sent WHEN the file system is full.'",
        "options": [
            "p → q",
            "q → p",
            "q → ¬p",
            "¬q → ¬p",
        ],
        "answer": 2,
        "explanation": (
            "الجملة بتقول: لما (when) الـ file system ممتلية (q)، مش هيتبعت الرد التلقائي (¬p).\n"
            "'when' تكافئ 'if' هنا, فالترجمة: q → ¬p.\n"
            "لاحظ إن p تعريفها 'CAN be sent', فـ 'CANNOT' هي ¬p."
        ),
        "source": "Lecture 3, Slides 11-13",
    },

    # ══════════════════════════════════════════
    #  CH1 – Lecture 3  (Logic Circuits)
    # ══════════════════════════════════════════
    {
        "question": "[Lec3-p19] In the combinatorial circuit with inputs p, q, r:\n"
                    "  - q goes through an inverter → ¬q\n"
                    "  - r goes through an inverter → ¬r\n"
                    "  - p and ¬q go into an AND gate\n"
                    "  - result of AND and ¬r go into an OR gate\n\n"
                    "What is the final output?",
        "options": [
            "(p ∨ ¬q) ∧ ¬r",
            "(p ∧ ¬q) ∨ ¬r",
            "p ∧ (¬q ∨ ¬r)",
            "(p ∨ ¬q) ∨ ¬r",
        ],
        "answer": 1,
        "explanation": (
            "نتابع الدائرة خطوة بخطوة:\n"
            "  1. q → inverter → ¬q\n"
            "  2. r → inverter → ¬r\n"
            "  3. p و ¬q → AND gate → (p ∧ ¬q)\n"
            "  4. (p ∧ ¬q) و ¬r → OR gate → (p ∧ ¬q) ∨ ¬r\n"
            "إحنا بنتبع الـ gates من اليسار لليمين ونحط الـ output كل مرحلة."
        ),
        "source": "Lecture 3, Slides 16-19",
    },

    # ══════════════════════════════════════════
    #  CH1 – Lecture 3  (Tautology)
    # ══════════════════════════════════════════
    {
        "question": "[Lec3-p25-26] The truth table for (p ∧ q) → p has been built.\n"
                    "What type of compound proposition is  (p ∧ q) → p ?",
        "options": ["Contradiction", "Contingency", "Tautology", "Neither"],
        "answer": 2,
        "explanation": (
            "من جدول الحقيقة:\n"
            "  p=T, q=T → p∧q=T → T→T = T\n"
            "  p=T, q=F → p∧q=F → F→T = T\n"
            "  p=F, q=T → p∧q=F → F→F = T\n"
            "  p=F, q=F → p∧q=F → F→F = T\n"
            "كل الصفوف طلعت T  ← ده معناه Tautology (دايمًا صح).\n"
            "Contradiction = دايمًا غلط، Contingency = أحيانًا صح وأحيانًا غلط."
        ),
        "source": "Lecture 3, Slides 25-26",
    },

    # ══════════════════════════════════════════
    #  CH1 – Lecture 3  (Logical Equivalences - De Morgan)
    # ══════════════════════════════════════════
    {
        "question": "[Lec3-p28-34] According to the truth table proof in the lecture,\n"
                    "which pair of propositions is logically equivalent?",
        "options": [
            "¬(p ∨ q)  ≡  ¬p ∨ ¬q",
            "¬(p ∨ q)  ≡  ¬p ∧ ¬q",
            "¬(p ∧ q)  ≡  ¬p ∨ ¬q",
            "¬(p ∧ q)  ≡  ¬p ∧ ¬q",
        ],
        "answer": 1,
        "explanation": (
            "من الجدول في المحاضرة:\n"
            "  ¬(p∨q)  طلعت:  F, F, F, T\n"
            "  ¬p ∧ ¬q طلعت:  F, F, F, T\n"
            "الاثنين بيطلعوا نفس القيم في كل الحالات ← متكافئان منطقياً (≡).\n"
            "ده هو قانون De Morgan الأول: ¬(p∨q) ≡ ¬p ∧ ¬q.\n"
            "الخيار التالت هو De Morgan التاني (¬(p∧q) ≡ ¬p∨¬q) وهو صح كمان بس مش اللي في المثال."
        ),
        "source": "Lecture 3, Slides 28-34",
    },

    # ══════════════════════════════════════════
    #  CH2 – Lecture 4  (Sets – Basics)
    # ══════════════════════════════════════════
    {
        "question": "[Lec4-p4] Which notation means 'a is NOT an element of set S'?",
        "options": ["a ∈ S", "a ∉ S", "a ⊂ S", "a ⊆ S"],
        "answer": 1,
        "explanation": (
            "الرموز:\n"
            "  ∈  = ينتمي (element of)\n"
            "  ∉  = لا ينتمي (not element of)  ← ده اللي المطلوب\n"
            "  ⊂  = مجموعة جزئية حقيقية (proper subset)\n"
            "  ⊆  = مجموعة جزئية (subset)\n"
            "فـ e ∉ S تعني إن e مش موجود في S."
        ),
        "source": "Lecture 4, Slide 4",
    },
    {
        "question": "[Lec4-p11-13] What is |∅|  (the cardinality of the empty set)?",
        "options": ["1", "∞", "0", "Undefined"],
        "answer": 2,
        "explanation": (
            "الـ cardinality = عدد العناصر المختلفة في المجموعة.\n"
            "المجموعة الفارغة ∅ مفيهاش أي عناصر ← عدد عناصرها = 0.\n"
            "مهم: {∅} ≠ ∅ ؛ {∅} مجموعة عندها عنصر واحد هو نفسه المجموعة الفارغة، ← |{∅}| = 1."
        ),
        "source": "Lecture 4, Slides 11-13",
    },
    {
        "question": "[Lec4-p14-15] Given  A = {1, 2, 3, {2,3}, 9},  what is |A|?",
        "options": ["3", "4", "5", "6"],
        "answer": 2,
        "explanation": (
            "نعد العناصر المباشرة في A:\n"
            "  1 ← عنصر\n"
            "  2 ← عنصر\n"
            "  3 ← عنصر\n"
            "  {2,3} ← عنصر واحد (مجموعة كاملة بتحسب كعنصر واحد)\n"
            "  9 ← عنصر\n"
            "المجموع = 5 عناصر ← |A| = 5.\n"
            "مهم: {2,3} بتتحسب عنصر واحد مش اثنين لأنها nested set."
        ),
        "source": "Lecture 4, Slides 14-15",
    },
    {
        "question": "[Lec4-p9] Are the sets {1,3,5} and {3,5,1} equal?",
        "options": [
            "No, because the order is different",
            "Yes, because sets are unordered and have the same elements",
            "No, because set equality requires same order",
            "Yes, but only if they have the same cardinality",
        ],
        "answer": 1,
        "explanation": (
            "المجموعات (Sets) مش مرتبة (unordered).\n"
            "تعريف التساوي: A = B  لو كل عنصر في A موجود في B والعكس.\n"
            "{1,3,5} و {3,5,1} عندهم نفس العناصر (1, 3, 5) بغض النظر عن الترتيب ← هما متساويان.\n"
            "كمان {1,3,3,5,5,5} = {1,3,5} لأن التكرار مش بيفرق في الـ sets."
        ),
        "source": "Lecture 4, Slide 9",
    },
    {
        "question": "[Lec4-p17-19] For every set S, which two statements are always true?",
        "options": [
            "∅ ⊆ S  and  S ⊆ ∅",
            "∅ ⊆ S  and  S ⊆ S",
            "S ⊆ ∅  and  ∅ ⊆ ∅",
            "S ⊆ S  and  S ⊆ ∅",
        ],
        "answer": 1,
        "explanation": (
            "قاعدتان مهمتان لكل مجموعة S:\n"
            "  (i)  ∅ ⊆ S  ← المجموعة الفارغة هي subset لأي مجموعة (فيه إثبات منطقي بالـ vacuous truth)\n"
            "  (ii) S ⊆ S  ← أي مجموعة هي subset لنفسها\n"
            "أما S ⊆ ∅ صحيحة بس لو S = ∅ نفسها."
        ),
        "source": "Lecture 4, Slide 19",
    },
    {
        "question": "[Lec4-p20] What is the formal definition of a PROPER subset (A ⊂ B)?",
        "options": [
            "Every element of A is in B, and A = B",
            "Every element of A is in B, and there exists an element in B not in A",
            "There exists an element in A not in B",
            "A and B have the same cardinality",
        ],
        "answer": 1,
        "explanation": (
            "الـ Proper Subset (المجموعة الجزئية الحقيقية):\n"
            "  A ⊂ B  تعني:\n"
            "    - كل عنصر في A موجود في B (A ⊆ B)  ← الشرط الأول\n"
            "    - A ≠ B  يعني في عنصر على الأقل في B مش موجود في A  ← الشرط الثاني\n"
            "الصيغة المنطقية: A ⊂ B ↔ (∀x(x∈A→x∈B)) ∧ (∃x(x∈B ∧ x∉A))\n"
            "الفرق بين ⊂ و ⊆: ⊆ تسمح بالتساوي, ⊂ لا تسمح."
        ),
        "source": "Lecture 4, Slide 20",
    },
    {
        "question": "[Lec4-p21] For each set below, is 3 an element?\n"
                    "  (I)  {1, 2, 3, 4}    (II)  {1, 2, {3}, 4}    (III)  {1, 2, {1,3}}\n\n"
                    "Which answer is correct?",
        "options": [
            "3 ∈ I,  3 ∉ II,  3 ∉ III",
            "3 ∈ I,  3 ∈ II,  3 ∈ III",
            "3 ∉ I,  3 ∉ II,  3 ∉ III",
            "3 ∈ I,  3 ∉ II,  3 ∈ III",
        ],
        "answer": 0,
        "explanation": (
            "نفحص كل مجموعة:\n"
            "  (I)  {1, 2, 3, 4}  → 3 موجود مباشرةً كعنصر ← 3 ∈ I  ✓\n"
            "  (II) {1, 2, {3}, 4} → العنصر الموجود هو {3} (المجموعة) مش 3 نفسه ← 3 ∉ II  ✓\n"
            "  (III){1, 2, {1,3}} → العنصر الموجود هو {1,3} (المجموعة) مش 3 نفسه ← 3 ∉ III  ✓\n"
            "الفرق: {3} هي مجموعة تحتوي 3، لكن هي نفسها عنصر مختلف عن الرقم 3."
        ),
        "source": "Lecture 4, Slide 21",
    },
    {
        "question": "[Lec4-p24-25] If S = {1, 2, 3}, what is the power set P(S)?",
        "options": [
            "{∅, {1}, {2}, {3}}",
            "{∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}",
            "{{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}",
            "{∅, {1,2}, {1,3}, {2,3}, {1,2,3}}",
        ],
        "answer": 1,
        "explanation": (
            "الـ Power Set هو مجموعة كل الـ subsets الممكنة.\n"
            "عدد العناصر = 2^|S| = 2^3 = 8 عناصر.\n"
            "الـ subsets الممكنة:\n"
            "  - 0 عناصر: ∅\n"
            "  - 1 عنصر:  {1}, {2}, {3}\n"
            "  - 2 عناصر: {1,2}, {1,3}, {2,3}\n"
            "  - 3 عناصر: {1,2,3}\n"
            "← P(S) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}"
        ),
        "source": "Lecture 4, Slide 25",
    },
    {
        "question": "[Lec4-p26-27] What is P(∅)  (the power set of the empty set)?",
        "options": ["∅", "{∅}", "{∅, {∅}}", "Undefined"],
        "answer": 1,
        "explanation": (
            "المجموعة الفارغة ∅ ليها subset واحد بس وهو نفسها.\n"
            "← P(∅) = {∅}  (مجموعة فيها عنصر واحد هو المجموعة الفارغة)\n"
            "لاحظ: P(∅) ≠ ∅  ؛ لأن P(∅) فيها عنصر واحد.\n"
            "عدد العناصر = 2^|∅| = 2^0 = 1  ✓"
        ),
        "source": "Lecture 4, Slides 26-27",
    },
    {
        "question": "[Lec4-p28-29] What is P({∅})  (the power set of the set {∅})?",
        "options": ["{∅}", "{∅, {∅}}", "{{∅}}", "∅"],
        "answer": 1,
        "explanation": (
            "{∅} مجموعة فيها عنصر واحد هو ∅.\n"
            "عدد الـ subsets = 2^1 = 2:\n"
            "  - المجموعة الفارغة: ∅\n"
            "  - المجموعة كلها:    {∅}\n"
            "← P({∅}) = {∅, {∅}}"
        ),
        "source": "Lecture 4, Slides 28-29",
    },
    {
        "question": "[Lec4-p32] Let A = {1,2} and B = {a,b,c}.\n"
                    "What is A × B?",
        "options": [
            "{(1,a),(1,b),(1,c),(2,a),(2,b),(2,c)}",
            "{(a,1),(b,1),(c,1),(a,2),(b,2),(c,2)}",
            "{(1,1),(2,2),(a,b),(b,c)}",
            "{(1,a),(2,b),(1,c)}",
        ],
        "answer": 0,
        "explanation": (
            "الـ Cartesian Product A×B = مجموعة كل الـ ordered pairs (a,b) حيث a∈A و b∈B.\n"
            "A = {1,2}, B = {a,b,c}\n"
            "← A×B = {(1,a),(1,b),(1,c),(2,a),(2,b),(2,c)}\n"
            "|A×B| = |A| × |B| = 2 × 3 = 6  ✓\n"
            "الخيار الثاني هو B×A وهو مختلف (الترتيب مهم في الـ ordered pairs)."
        ),
        "source": "Lecture 4, Slides 32-33",
    },
    {
        "question": "[Lec4-p35] For A = {0,1}, B = {1,2}, C = {0,1,2},\n"
                    "how many elements does A × B × C have?",
        "options": ["6", "8", "12", "9"],
        "answer": 2,
        "explanation": (
            "|A × B × C| = |A| × |B| × |C|\n"
            "= 2 × 2 × 3 = 12\n"
            "كل 3-tuple بتاخد عنصر من A وعنصر من B وعنصر من C.\n"
            "من المحاضرة نقدر نعدهم: (0,1,0),(0,1,1),(0,1,2),(0,2,0),(0,2,1),(0,2,2),\n"
            "                         (1,1,0),(1,1,1),(1,1,2),(1,2,0),(1,2,1),(1,2,2) ← 12 بالظبط."
        ),
        "source": "Lecture 4, Slide 35",
    },
    {
        "question": "[Lec4-p38] What is the union of {1,3,5} and {1,2,3}?",
        "options": ["{1,3}", "{1,2,3,5}", "{1,3,5,1,2,3}", "{2,5}"],
        "answer": 1,
        "explanation": (
            "الـ Union (A∪B) = مجموعة كل العناصر اللي في A أو في B أو في الاثنين.\n"
            "A = {1,3,5}, B = {1,2,3}\n"
            "A∪B = {1,2,3,5}  (من غير تكرار)\n"
            "{1,3} هو الـ Intersection, {2,5} هو A - B و B - A مجتمعين."
        ),
        "source": "Lecture 4, Slide 38",
    },
    {
        "question": "[Lec4-p41] What is the intersection of {1,3,5} and {1,2,3}?",
        "options": ["{1,2,3,5}", "{1,3}", "{5}", "{2}"],
        "answer": 1,
        "explanation": (
            "الـ Intersection (A∩B) = العناصر الموجودة في A و B معاً في نفس الوقت.\n"
            "A = {1,3,5}, B = {1,2,3}\n"
            "العناصر المشتركة: 1 و 3\n"
            "← A∩B = {1,3}"
        ),
        "source": "Lecture 4, Slide 41",
    },
    {
        "question": "[Lec4-p44] Given A = {1,3,5} and B = {1,2,3},\n"
                    "what is A - B  (difference)?",
        "options": ["{1,3}", "{2}", "{5}", "{1,2,3,5}"],
        "answer": 2,
        "explanation": (
            "الـ Difference (A - B) = العناصر اللي في A بس مش في B.\n"
            "A = {1,3,5}, B = {1,2,3}\n"
            "  - 1: موجود في B ← نشيله\n"
            "  - 3: موجود في B ← نشيله\n"
            "  - 5: مش موجود في B ← يفضل\n"
            "← A - B = {5}"
        ),
        "source": "Lecture 4, Slide 44",
    },
    {
        "question": "[Lec4-p47] Given U = {1,2,3,4,5} and A = {1,3},\n"
                    "what is the complement Ā?",
        "options": ["{1,3}", "{2,4,5}", "{4,5}", "{1,2,3,4,5}"],
        "answer": 1,
        "explanation": (
            "الـ Complement (Ā) = العناصر اللي في الـ Universal Set U بس مش في A.\n"
            "Ā = {x ∈ U | x ∉ A}\n"
            "U = {1,2,3,4,5}, A = {1,3}\n"
            "  - 1: في A ← نشيله\n"
            "  - 2: مش في A ← يفضل\n"
            "  - 3: في A ← نشيله\n"
            "  - 4: مش في A ← يفضل\n"
            "  - 5: مش في A ← يفضل\n"
            "← Ā = {2,4,5}"
        ),
        "source": "Lecture 4, Slide 47",
    },
    {
        "question": "[Lec4-p53-54] Which law states that  A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)?",
        "options": [
            "Associative law",
            "Commutative law",
            "Distributive law",
            "De Morgan's law",
        ],
        "answer": 2,
        "explanation": (
            "قوانين المجموعات:\n"
            "  - Associative:   A∪(B∪C) = (A∪B)∪C  (التجميع)\n"
            "  - Commutative:   A∪B = B∪A  (التبديل)\n"
            "  - Distributive:  A∪(B∩C) = (A∪B)∩(A∪C)  ← ده هو المطلوب (التوزيع)\n"
            "  - De Morgan's:   overline(A∩B) = Ā∪B̄  (نفي المجموعات)\n"
            "الـ Distributive law بيوزع الـ union أو الـ intersection على الأقواس."
        ),
        "source": "Lecture 4, Slides 53-54",
    },
    {
        "question": "[Lec4-p54] De Morgan's law for sets states that  overline(A ∩ B) = ?",
        "options": [
            "Ā ∩ B̄",
            "Ā ∪ B̄",
            "A ∪ B",
            "A ∩ B",
        ],
        "answer": 1,
        "explanation": (
            "قانون De Morgan للمجموعات:\n"
            "  overline(A ∩ B) = Ā ∪ B̄\n"
            "  overline(A ∪ B) = Ā ∩ B̄\n"
            "ده بالظبط مثل قانون De Morgan في المنطق:\n"
            "  ¬(p ∧ q) ≡ ¬p ∨ ¬q\n"
            "  ¬(p ∨ q) ≡ ¬p ∧ ¬q\n"
            "الـ Complement بيقلب الـ ∩ لـ ∪ والعكس."
        ),
        "source": "Lecture 4, Slide 54",
    },
]


# ─────────────────────────────────────────────
#  QUIZ ENGINE
# ─────────────────────────────────────────────

def print_header():
    total = len(QUESTIONS)
    print(f"\n{BOLD}{CYAN}{'═'*62}{RESET}")
    print(f"{BOLD}{CYAN}   Discrete Mathematics Quiz – CSE315  (NMU){RESET}")
    print(f"{BOLD}{CYAN}   تفسير الإجابات باللغة العربية{RESET}")
    print(f"{BOLD}{CYAN}   إجمالي الأسئلة المتاحة: {total}{RESET}")
    print(f"{BOLD}{CYAN}{'═'*62}{RESET}\n")


def ask_question(q_num: int, total: int, q: dict) -> bool:
    print(f"{BOLD}[{q_num}/{total}] {q['question']}{RESET}")
    print(f"{YELLOW}  Source: {q['source']}{RESET}\n")

    for i, opt in enumerate(q['options']):
        print(f"  {CYAN}{i+1}.{RESET} {opt}")

    while True:
        try:
            ans = input(f"\n{BOLD}اختر رقم الإجابة (1-{len(q['options'])}): {RESET}").strip()
            idx = int(ans) - 1
            if 0 <= idx < len(q['options']):
                break
            else:
                print(f"{RED}  ↳ من فضلك ادخل رقم بين 1 و {len(q['options'])}{RESET}")
        except ValueError:
            print(f"{RED}  ↳ ادخل رقم صحيح{RESET}")

    if idx == q['answer']:
        print(f"\n{GREEN}✔  Correct! صح تماماً 🎉{RESET}")
        correct = True
    else:
        print(f"\n{RED}✘  Wrong! الإجابة الصحيحة: {q['options'][q['answer']]}{RESET}")
        correct = False

    # دايمًا بنوري التفسير سواء صح أو غلط
    print(f"\n{YELLOW}{'─'*58}")
    print(f"📖 التفسير:{RESET}")
    for line in q['explanation'].split('\n'):
        print(f"   {line}")
    print(f"{YELLOW}{'─'*58}{RESET}\n")

    input("اضغط Enter للسؤال التالي...")
    return correct


def show_score(score: int, total: int):
    pct = score / total * 100
    print(f"\n{BOLD}{CYAN}{'═'*62}{RESET}")
    print(f"{BOLD}  النتيجة النهائية: {score}/{total}  ({pct:.1f}%){RESET}")
    if pct == 100:
        print(f"{GREEN}  🏆 ممتاز! أنت أتقنت المادة! مبروك يا بطل!{RESET}")
    elif pct >= 80:
        print(f"{GREEN}  👍 جيد جداً! استمر في المذاكرة{RESET}")
    elif pct >= 60:
        print(f"{YELLOW}  📚 مقبول – راجع الـ slides المذكورة{RESET}")
    else:
        print(f"{RED}  💪 محتاج مراجعة أكثر – ارجع للمحاضرات{RESET}")
    print(f"{BOLD}{CYAN}{'═'*62}{RESET}\n")


def select_by_lecture(pool):
    """Filter questions by lecture."""
    lectures = {}
    for q in pool:
        src = q['source'].split(',')[0]  # e.g. "Lecture 1"
        lectures.setdefault(src, []).append(q)

    print(f"\n{BOLD}المحاضرات المتاحة:{RESET}")
    lec_list = sorted(lectures.keys())
    for i, lec in enumerate(lec_list, 1):
        print(f"  {CYAN}{i}.{RESET} {lec}  ({len(lectures[lec])} سؤال)")
    print(f"  {CYAN}{len(lec_list)+1}.{RESET} كل المحاضرات")

    while True:
        try:
            choice = int(input(f"\nاختار: ").strip())
            if 1 <= choice <= len(lec_list):
                return lectures[lec_list[choice - 1]]
            elif choice == len(lec_list) + 1:
                return pool
            else:
                print(f"{RED}اختار رقم صح{RESET}")
        except ValueError:
            print(f"{RED}ادخل رقم{RESET}")


def main():
    print_header()

    print(f"{BOLD}اختار الوضع:{RESET}")
    print(f"  {CYAN}1.{RESET} كل الأسئلة بالترتيب")
    print(f"  {CYAN}2.{RESET} أسئلة عشوائية")
    print(f"  {CYAN}3.{RESET} عدد محدد من الأسئلة العشوائية")
    print(f"  {CYAN}4.{RESET} اختار محاضرة معينة")
    mode = input(f"{BOLD}اختيارك: {RESET}").strip()

    pool = list(QUESTIONS)

    if mode == "2":
        random.shuffle(pool)
    elif mode == "3":
        random.shuffle(pool)
        while True:
            try:
                n = int(input(f"كام سؤال؟ (1-{len(pool)}): "))
                if 1 <= n <= len(pool):
                    pool = pool[:n]
                    break
                else:
                    print(f"{RED}ادخل رقم بين 1 و {len(pool)}{RESET}")
            except ValueError:
                print(f"{RED}ادخل رقم صحيح{RESET}")
    elif mode == "4":
        pool = select_by_lecture(pool)
        random.shuffle(pool)

    print()
    score = 0
    for i, q in enumerate(pool, 1):
        if ask_question(i, len(pool), q):
            score += 1

    show_score(score, len(pool))


if __name__ == "__main__":
    main()