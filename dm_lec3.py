# ════════════════════════════════════════════════════════════
# 📖 dm_lec3.py
# Discrete Mathematics - Lecture 3
# Logical Equivalences, Quantifiers, and Proof Techniques
# 50 Questions (45 MCQ + 5 TF)
# ════════════════════════════════════════════════════════════

QUESTIONS = [

    # ══════════════════════════════════════════════
    # 🔹 SECTION 1: Logical Equivalences
    # ══════════════════════════════════════════════
    {
        "q": "According to the Identity laws, p ∧ T is logically equivalent to:",
        "type": "mcq",
        "options": ["p", "T", "F", "¬p"],
        "ans": "p",
        "explain_correct": "✅ صح! قانون الـ Identity بيقول إن (p ∧ T ≡ p) لأن النتيجة بتعتمد على قيمة p.",
        "explain_wrong": "❌ غلط! الإجابة الصح هي p. الـ T مبيأثرش في عملية الـ AND."
    },
    {
        "q": "According to the Domination laws, p ∨ T is logically equivalent to:",
        "type": "mcq",
        "options": ["T", "F", "p", "¬p"],
        "ans": "T",
        "explain_correct": "✅ صح! قانون الـ Domination بيقول إن (p ∨ T ≡ T) لأن أي حاجة OR مع True بتطلع True.",
        "explain_wrong": "❌ غلط! الإجابة الصح هي T."
    },
    {
        "q": "The equivalence (p ∨ p ≡ p) and (p ∧ p ≡ p) is known as:",
        "type": "mcq",
        "options": [
            "Idempotent laws",
            "Identity laws",
            "Domination laws",
            "Absorption laws"
        ],
        "ans": "Idempotent laws",
        "explain_correct": "✅ صح! ده قانون الـ Idempotent اللي معناه إن تكرار المتغير مع نفسه مش بيغير النتيجة.",
        "explain_wrong": "❌ غلط! ده يُسمى الـ Idempotent laws."
    },
    {
        "q": "De Morgan's laws state that ¬(p ∧ q) is logically equivalent to:",
        "type": "mcq",
        "options": [
            "¬p ∨ ¬q",
            "¬p ∧ ¬q",
            "p ∨ q",
            "p ∧ q"
        ],
        "ans": "¬p ∨ ¬q",
        "explain_correct": "✅ صح! النفي بيدخل على القوس فبيعكس المتغيرات ويقلب الـ AND لـ OR.",
        "explain_wrong": "❌ غلط! الإجابة الصح هي ¬p ∨ ¬q."
    },
    {
        "q": "The conditional statement (p → q) is logically equivalent to:",
        "type": "mcq",
        "options": [
            "¬p ∨ q",
            "¬p ∧ q",
            "p ∨ ¬q",
            "p ∧ ¬q"
        ],
        "ans": "¬p ∨ q",
        "explain_correct": "✅ صح! من أهم القوانين: (p → q) تكافئ نفي الأول OR التاني (¬p ∨ q).",
        "explain_wrong": "❌ غلط! الإجابة هي ¬p ∨ q."
    },
    {
        "q": "The contrapositive of (p → q) is:",
        "type": "mcq",
        "options": [
            "¬q → ¬p",
            "q → p",
            "¬p → ¬q",
            "q → ¬p"
        ],
        "ans": "¬q → ¬p",
        "explain_correct": "✅ صح! الـ Contrapositive بيعكس الاتجاه وينفي الاتنين (¬q → ¬p).",
        "explain_wrong": "❌ غلط! الإجابة الصح هي ¬q → ¬p."
    },
    {
        "q": "The biconditional (p ↔ q) is logically equivalent to:",
        "type": "mcq",
        "options": [
            "(p → q) ∧ (q → p)",
            "(p → q) ∨ (q → p)",
            "¬p ↔ ¬q",
            "¬(p ↔ q)"
        ],
        "ans": "(p → q) ∧ (q → p)",
        "explain_correct": "✅ صح! الـ Biconditional معناه إن الطرفين بيأدوا لبعض، يعني (p → q) AND (q → p).",
        "explain_wrong": "❌ غلط! الإجابة الصح هي (p → q) ∧ (q → p)."
    },
    {
        "q": "The equivalence (p ∨ ¬p ≡ T) and (p ∧ ¬p ≡ F) is known as:",
        "type": "mcq",
        "options": [
            "Negation laws",
            "Absorption laws",
            "Associative laws",
            "Commutative laws"
        ],
        "ans": "Negation laws",
        "explain_correct": "✅ صح! دي قوانين النفي (Negation laws).",
        "explain_wrong": "❌ غلط! دي تُسمى Negation laws."
    },

    # ══════════════════════════════════════════════
    # 🔹 SECTION 2: Predicates and Propositions
    # ══════════════════════════════════════════════
    {
        "q": "In the statement 'x is greater than 5', the phrase 'is greater than 5' is called the:",
        "type": "mcq",
        "options": [
            "Predicate",
            "Subject",
            "Quantifier",
            "Variable"
        ],
        "ans": "Predicate",
        "explain_correct": "✅ صح! المتغير (x) هو الـ Subject، والجزء التاني اللي بيوصفه هو الـ Predicate.",
        "explain_wrong": "❌ غلط! الجزء ده بيسمى Predicate."
    },
    {
        "q": "Let P(x) denote the statement 'x > 3'. What is the truth value of P(2)?",
        "type": "mcq",
        "options": ["False", "True", "Undefined", "Cannot be determined"],
        "ans": "False",
        "explain_correct": "✅ صح! لما نعوض بـ 2 هتبقى (2 > 3)، ودي طبعاً عبارة خاطئة (False).",
        "explain_wrong": "❌ غلط! الـ 2 مش أكبر من 3، إذن الإجابة False."
    },
    {
        "q": "Let Q(x,y) denote the statement '4x = y + 3'. What is the truth value of Q(1, 2)?",
        "type": "mcq",
        "options": ["False", "True", "Undefined", "Depends on z"],
        "ans": "False",
        "explain_correct": "✅ صح! هنعوض عن x بـ 1 و y بـ 2: 4(1) = 2 + 3، يعني 4 = 5 ودي عبارة خاطئة.",
        "explain_wrong": "❌ غلط! بالتعويض هتطلع 4 = 5، يبقى الإجابة False."
    },
    {
        "q": "Let P(x) denote 'x ≤ 4'. What is the truth value of P(0)?",
        "type": "mcq",
        "options": ["True", "False", "Undefined", "Null"],
        "ans": "True",
        "explain_correct": "✅ صح! الصفر أقل من أو يساوي 4، إذن العبارة صحيحة (True).",
        "explain_wrong": "❌ غلط! الصفر فعلاً أقل من 4، إذن True."
    },
    {
        "q": "Let P(x) be the statement 'the word x contains the letter a'. What is the truth value of P(lemon)?",
        "type": "mcq",
        "options": ["False", "True", "Undefined", "Depends on language"],
        "ans": "False",
        "explain_correct": "✅ صح! كلمة lemon مفهاش حرف a، إذن العبارة False.",
        "explain_wrong": "❌ غلط! كلمة lemon مفهاش حرف a."
    },

    # ══════════════════════════════════════════════
    # 🔹 SECTION 3: Quantifiers
    # ══════════════════════════════════════════════
    {
        "q": "The quantifier that expresses 'for all values of x in the domain' is called the:",
        "type": "mcq",
        "options": [
            "Universal quantifier",
            "Existential quantifier",
            "Uniqueness quantifier",
            "Predicate quantifier"
        ],
        "ans": "Universal quantifier",
        "explain_correct": "✅ صح! الـ Universal quantifier (∀) هو اللي بيعبر عن 'كل القيم' في الدومين.",
        "explain_wrong": "❌ غلط! الإجابة الصح هي Universal quantifier."
    },
    {
        "q": "The existential quantification of P(x) is denoted by:",
        "type": "mcq",
        "options": [
            "∃x P(x)",
            "∀x P(x)",
            "∃!x P(x)",
            "∀!x P(x)"
        ],
        "ans": "∃x P(x)",
        "explain_correct": "✅ صح! الـ Existential بنرمز ليه بالرمز (∃).",
        "explain_wrong": "❌ غلط! الرمز بتاعه هو ∃x P(x)."
    },
    {
        "q": "The uniqueness quantifier ∃!x P(x) means:",
        "type": "mcq",
        "options": [
            "There exists a unique x such that P(x) is true",
            "There exists at least one x such that P(x) is true",
            "For all x P(x) is true",
            "There is no x such that P(x) is true"
        ],
        "ans": "There exists a unique x such that P(x) is true",
        "explain_correct": "✅ صح! علامة التعجب مع الـ ∃ معناها إن فيه عنصر 'وحيد' فقط هو اللي بيحقق الشرط.",
        "explain_wrong": "❌ غلط! معناها 'يوجد عنصر وحيد فقط' (unique)."
    },
    {
        "q": "The statement ∀x P(x) is False when:",
        "type": "mcq",
        "options": [
            "There is an x for which P(x) is false",
            "P(x) is true for every x",
            "There is an x for which P(x) is true",
            "P(x) is false for every x"
        ],
        "ans": "There is an x for which P(x) is false",
        "explain_correct": "✅ صح! الـ Universal بيكون False لو لقينا عنصر واحد بس (Counterexample) بيخلي العبارة غلط.",
        "explain_wrong": "❌ غلط! بيكفي إيجاد قيمة واحدة تخليها False عشان تكون العبارة كلها False."
    },
    {
        "q": "The statement ∃x P(x) is False when:",
        "type": "mcq",
        "options": [
            "P(x) is false for every x",
            "There is an x for which P(x) is false",
            "P(x) is true for every x",
            "There is an x for which P(x) is true"
        ],
        "ans": "P(x) is false for every x",
        "explain_correct": "✅ صح! الـ Existential بتكون False لو مفيش ولا عنصر واحد حقق الشرط (كلهم False).",
        "explain_wrong": "❌ غلط! بتكون False لو كل القيم اللي في الدومين طلعت False."
    },
    {
        "q": "Let P(x) be the statement 'x + 1 > x'. What is the truth value of ∀x P(x) for all real numbers?",
        "type": "mcq",
        "options": ["True", "False", "Undefined", "Contingency"],
        "ans": "True",
        "explain_correct": "✅ صح! أي رقم حقيقي لو زودت عليه 1 هيكون أكبر من نفسه، فالجملة دايماً صحيحة.",
        "explain_wrong": "❌ غلط! الجملة دي صحيحة لكل الأرقام، يبقى الإجابة True."
    },
    {
        "q": "Let Q(x) be the statement 'x < 2'. What is the truth value of ∀x Q(x) for all real numbers?",
        "type": "mcq",
        "options": ["False", "True", "Undefined", "Cannot be determined"],
        "ans": "False",
        "explain_correct": "✅ صح! الجملة بتقول 'كل الأرقام الحقيقية أقل من 2'، وده غلط، الـ 3 مثلاً مش أقل من 2.",
        "explain_wrong": "❌ غلط! في أرقام أكبر من 2، إذن العبارة False."
    },
    {
        "q": "Let P(x) be the statement 'x² > 10'. What is the truth value of ∃x P(x) if the domain is {1, 2, 3, 4}?",
        "type": "mcq",
        "options": ["True", "False", "Undefined", "0"],
        "ans": "True",
        "explain_correct": "✅ صح! الـ ∃ محتاجة رقم واحد بس يحقق الشرط. لو عوضنا بـ 4 (4² = 16 > 10)، إذن العبارة True.",
        "explain_wrong": "❌ غلط! الرقم 4 بيحقق الشرط، يبقى الإجابة True."
    },
    {
        "q": "Let P(x) be 'x = x²'. If the domain is the integers, what is the truth value of ∀x P(x)?",
        "type": "mcq",
        "options": ["False", "True", "Undefined", "Depends on x"],
        "ans": "False",
        "explain_correct": "✅ صح! هل كل الأرقام بتساوي مربعها؟ لأ طبعاً (2 مش بتساوي 4)، إذن العبارة False.",
        "explain_wrong": "❌ غلط! الجملة مش صحيحة لكل الأرقام، إذن False."
    },
    {
        "q": "Let P(x) be 'x = x²'. If the domain is the integers, what is the truth value of ∃x P(x)?",
        "type": "mcq",
        "options": ["True", "False", "Undefined", "Depends on x"],
        "ans": "True",
        "explain_correct": "✅ صح! الـ ∃ محتاجة رقم واحد بس يحقق الشرط. هنا الصفر والواحد بيحققوه (1 = 1²)، إذن True.",
        "explain_wrong": "❌ غلط! في أرقام بتحقق الشرط زي 0 و 1، يبقى الإجابة True."
    },

    # ══════════════════════════════════════════════
    # 🔹 SECTION 4: Translation and Negation
    # ══════════════════════════════════════════════
    {
        "q": "Translate: 'Every student in this class has studied calculus' where S(x) is 'x is in this class' and P(x) is 'x has studied calculus'.",
        "type": "mcq",
        "options": [
            "∀x (S(x) → P(x))",
            "∀x (S(x) ∧ P(x))",
            "∃x (S(x) → P(x))",
            "∃x (S(x) ∧ P(x))"
        ],
        "ans": "∀x (S(x) → P(x))",
        "explain_correct": "✅ صح! مع الـ ∀ بنستخدم دايماً الـ Implication (→) لترجمة الجمل الشرطية.",
        "explain_wrong": "❌ غلط! الترجمة الصح هي ∀x (S(x) → P(x))."
    },
    {
        "q": "Translate: 'Some comedians are funny' where C(x) is 'x is a comedian' and F(x) is 'x is funny'.",
        "type": "mcq",
        "options": [
            "∃x (C(x) ∧ F(x))",
            "∃x (C(x) → F(x))",
            "∀x (C(x) ∧ F(x))",
            "∀x (C(x) → F(x))"
        ],
        "ans": "∃x (C(x) ∧ F(x))",
        "explain_correct": "✅ صح! مع الـ ∃ بنستخدم دايماً الـ AND (∧) عشان نقول إن فيه شخص بيحمل الصفتين مع بعض.",
        "explain_wrong": "❌ غلط! الترجمة الصح هي ∃x (C(x) ∧ F(x))."
    },
    {
        "q": "Translate: 'Every comedian is funny'.",
        "type": "mcq",
        "options": [
            "∀x (C(x) → F(x))",
            "∀x (C(x) ∧ F(x))",
            "∃x (C(x) → F(x))",
            "∃x (C(x) ∧ F(x))"
        ],
        "ans": "∀x (C(x) → F(x))",
        "explain_correct": "✅ صح! هنا بنقول 'لكل x، لو كان كوميديان، إذن هو مضحك' (استخدام → مع ∀).",
        "explain_wrong": "❌ غلط! الترجمة الصح هي ∀x (C(x) → F(x))."
    },
    {
        "q": "Translate: 'No one is perfect' where P(x) is 'x is perfect' and domain is all people.",
        "type": "mcq",
        "options": [
            "∀x ¬P(x)",
            "¬∀x P(x)",
            "∃x P(x)",
            "∃x ¬P(x)"
        ],
        "ans": "∀x ¬P(x)",
        "explain_correct": "✅ صح! الجملة بتقول 'كل الناس مش كاملين'، فبتتكتب ∀x ¬P(x).",
        "explain_wrong": "❌ غلط! الإجابة هي ∀x ¬P(x)."
    },
    {
        "q": "Translate: 'Not everyone is perfect'.",
        "type": "mcq",
        "options": [
            "¬∀x P(x)",
            "∀x ¬P(x)",
            "∃x P(x)",
            "¬∃x P(x)"
        ],
        "ans": "¬∀x P(x)",
        "explain_correct": "✅ صح! دي ترجمة حرفية: نفي (Not) للـ ∀x P(x). وممكن تتكتب برضه ∃x ¬P(x).",
        "explain_wrong": "❌ غلط! الترجمة الصح هي ¬∀x P(x)."
    },
    {
        "q": "Which has higher precedence in logical expressions?",
        "type": "mcq",
        "options": [
            "Quantifiers (∀, ∃)",
            "Logical operators (AND, OR)",
            "They have equal precedence",
            "Relational operators"
        ],
        "ans": "Quantifiers (∀, ∃)",
        "explain_correct": "✅ صح! الـ Quantifiers ليها الأولوية الأعلى وبتتنفذ قبل أي logical operator.",
        "explain_wrong": "❌ غلط! الـ Quantifiers (∀, ∃) ليها أولوية أعلى."
    },
    {
        "q": "According to De Morgan's laws for quantifiers, the negation of ∀x P(x) is logically equivalent to:",
        "type": "mcq",
        "options": [
            "∃x ¬P(x)",
            "∀x ¬P(x)",
            "¬∃x P(x)",
            "∃x P(x)"
        ],
        "ans": "∃x ¬P(x)",
        "explain_correct": "✅ صح! لما ننفي الـ ∀ بتتحول لـ ∃ والنفي بيدخل على الـ P(x).",
        "explain_wrong": "❌ غلط! الإجابة الصح هي ∃x ¬P(x)."
    },
    {
        "q": "The negation of ∃x P(x) is logically equivalent to:",
        "type": "mcq",
        "options": [
            "∀x ¬P(x)",
            "∃x ¬P(x)",
            "¬∀x P(x)",
            "∀x P(x)"
        ],
        "ans": "∀x ¬P(x)",
        "explain_correct": "✅ صح! لما ننفي الـ ∃ بتتحول لـ ∀ والنفي بيدخل جوا.",
        "explain_wrong": "❌ غلط! الإجابة الصح هي ∀x ¬P(x)."
    },
    {
        "q": "What is the negation of the statement ∀x (x² > x)?",
        "type": "mcq",
        "options": [
            "∃x (x² ≤ x)",
            "∀x (x² ≤ x)",
            "∃x (x² < x)",
            "∃x (x² = x)"
        ],
        "ans": "∃x (x² ≤ x)",
        "explain_correct": "✅ صح! الـ ∀ بتتقلب ∃، وعلامة (>) نفيها بيكون (≤).",
        "explain_wrong": "❌ غلط! الإجابة الصح هي ∃x (x² ≤ x)."
    },
    {
        "q": "What is the negation of the statement ∃x (x² = 2)?",
        "type": "mcq",
        "options": [
            "∀x (x² ≠ 2)",
            "∀x (x² = 2)",
            "∃x (x² ≠ 2)",
            "¬∀x (x² = 2)"
        ],
        "ans": "∀x (x² ≠ 2)",
        "explain_correct": "✅ صح! الـ ∃ بتتقلب ∀، وعلامة (=) نفيها بيكون (≠).",
        "explain_wrong": "❌ غلط! الإجابة الصح هي ∀x (x² ≠ 2)."
    },

    # ══════════════════════════════════════════════
    # 🔹 SECTION 5: Rules of Inference & Proofs
    # ══════════════════════════════════════════════
    {
        "q": "An argument in propositional logic is defined as:",
        "type": "mcq",
        "options": [
            "A sequence of propositions",
            "A single true proposition",
            "A false statement",
            "A mathematical equation"
        ],
        "ans": "A sequence of propositions",
        "explain_correct": "✅ صح! الـ argument هو تسلسل من العبارات المنطقية (propositions).",
        "explain_wrong": "❌ غلط! هو عبارة عن A sequence of propositions."
    },
    {
        "q": "In an argument, the final proposition is called the:",
        "type": "mcq",
        "options": [
            "Conclusion",
            "Premise",
            "Lemma",
            "Theorem"
        ],
        "ans": "Conclusion",
        "explain_correct": "✅ صح! الجملة الأخيرة اللي بنستنتجها اسمها الـ Conclusion (النتيجة).",
        "explain_wrong": "❌ غلط! الجملة الأخيرة تُسمى Conclusion."
    },
    {
        "q": "In an argument, all propositions before the final one are called:",
        "type": "mcq",
        "options": [
            "Premises",
            "Conclusions",
            "Variables",
            "Quantifiers"
        ],
        "ans": "Premises",
        "explain_correct": "✅ صح! الجمل اللي بنبني عليها استنتاجنا اسمها الـ Premises (المقدمات أو المعطيات).",
        "explain_wrong": "❌ غلط! تُسمى Premises."
    },
    {
        "q": "The argument with premises (p → q) and (p), and conclusion (q) is valid if which of the following is a tautology?",
        "type": "mcq",
        "options": [
            "((p → q) ∧ p) → q",
            "(p → q) → (p ∧ q)",
            "(p ∧ q) → p",
            "p → (q ∧ p)"
        ],
        "ans": "((p → q) ∧ p) → q",
        "explain_correct": "✅ صح! بنعمل AND للـ Premises وبعدين Implication للـ Conclusion، ولازم الناتج يكون Tautology.",
        "explain_wrong": "❌ غلط! الإجابة الصح هي ((p → q) ∧ p) → q."
    },
    {
        "q": "A statement that can be shown to be true is called a:",
        "type": "mcq",
        "options": [
            "Theorem",
            "Proof",
            "Variable",
            "Quantifier"
        ],
        "ans": "Theorem",
        "explain_correct": "✅ صح! الـ Theorem (النظرية) هي جملة نقدر نثبت صحتها.",
        "explain_wrong": "❌ غلط! تُسمى Theorem."
    },
    {
        "q": "A valid argument that establishes the truth of a theorem is called a:",
        "type": "mcq",
        "options": [
            "Proof",
            "Lemma",
            "Proposition",
            "Predicate"
        ],
        "ans": "Proof",
        "explain_correct": "✅ صح! الـ Proof (الإثبات) هو اللي بيأكد صحة النظرية.",
        "explain_wrong": "❌ غلط! يُسمى Proof."
    },
    {
        "q": "A 'helping theorem' or a result which is needed to prove a theorem is called a:",
        "type": "mcq",
        "options": [
            "Lemma",
            "Conclusion",
            "Premise",
            "Predicate"
        ],
        "ans": "Lemma",
        "explain_correct": "✅ صح! الـ Lemma هي نظرية مساعدة بنستخدمها عشان نثبت نظرية أكبر.",
        "explain_wrong": "❌ غلط! تُسمى Lemma."
    },
    {
        "q": "If 'a' is an even integer, it can be written as:",
        "type": "mcq",
        "options": [
            "a = 2n",
            "a = 2n + 1",
            "a = n²",
            "a = n/m"
        ],
        "ans": "a = 2n",
        "explain_correct": "✅ صح! أي رقم زوجي هو عبارة عن 2 مضروبة في أي رقم صحيح (2n).",
        "explain_wrong": "❌ غلط! الرقم الزوجي بيتكتب على صورة 2n."
    },
    {
        "q": "If 'a' is an odd integer, it can be written as:",
        "type": "mcq",
        "options": [
            "a = 2m + 1",
            "a = 2m",
            "a = m²",
            "a = m/2"
        ],
        "ans": "a = 2m + 1",
        "explain_correct": "✅ صح! أي رقم فردي هو رقم زوجي زائد واحد (2m + 1).",
        "explain_wrong": "❌ غلط! الرقم الفردي بيتكتب على صورة 2m + 1."
    },
    {
        "q": "If 'a' is a perfect square, it can be written as:",
        "type": "mcq",
        "options": [
            "a = n²",
            "a = 2n",
            "a = 2n+1",
            "a = √n"
        ],
        "ans": "a = n²",
        "explain_correct": "✅ صح! المربع الكامل هو رقم مضروب في نفسه (n²).",
        "explain_wrong": "❌ غلط! المربع الكامل بيتكتب a = n²."
    },
    {
        "q": "In a Direct Proof of the theorem (p → q), what is the first step?",
        "type": "mcq",
        "options": [
            "Assume that p is true",
            "Assume that q is true",
            "Assume that p is false",
            "Assume that q is false"
        ],
        "ans": "Assume that p is true",
        "explain_correct": "✅ صح! في الإثبات المباشر بنبدأ بافتراض إن المعطى (p) صحيح، ونحاول نوصل لـ (q).",
        "explain_wrong": "❌ غلط! أول خطوة هي Assume that p is true."
    },
    {
        "q": "In an Indirect Proof by Contraposition of (p → q), what is the first step?",
        "type": "mcq",
        "options": [
            "Assume that ¬q is true",
            "Assume that ¬p is true",
            "Assume that p is true",
            "Assume that q is true"
        ],
        "ans": "Assume that ¬q is true",
        "explain_correct": "✅ صح! في الـ Contraposition بنعكس الجملة، فبنبأ بافتراض نفي النتيجة (¬q).",
        "explain_wrong": "❌ غلط! بنبدأ بافتراض Assume that ¬q is true."
    },
    {
        "q": "In an Indirect Proof by Contradiction, to prove p, we show that:",
        "type": "mcq",
        "options": [
            "¬p → F",
            "p → F",
            "¬p → T",
            "p → T"
        ],
        "ans": "¬p → F",
        "explain_correct": "✅ صح! في الإثبات بالتناقض (Contradiction) عشان نثبت p، بنفترض إن عكسها (¬p) صح، ولازم ده يوصلنا لتناقض أو نتيجة غلط (F).",
        "explain_wrong": "❌ غلط! الإجابة الصح هي ¬p → F."
    },

    # ══════════════════════════════════════════════
    # 🔹 True / False Questions
    # ══════════════════════════════════════════════
    {
        "q": "A rational number can be written as n/m where n and m are integers with no common factor and m ≠ 0.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! ده التعريف الرياضي السليم للرقم النسبي (Rational Number).",
        "explain_wrong": "❌ غلط! العبارة صحيحة، المقام (m) مستحيل يساوي صفر."
    },
    {
        "q": "The equivalence p ∨ ¬p ≡ F is known as the Negation law.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! العبارة دي غلط لأن قانون النفي بيقول إن p ∨ ¬p ≡ T (بيساوي True مش False).",
        "explain_wrong": "❌ غلط! قانون النفي بيقول إن p ∨ ¬p ≡ T."
    },
    {
        "q": "The statement 'Not everyone is perfect' is logically equivalent to 'There is at least one person who is not perfect'.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! حسب قوانين دي مورجان للـ Quantifiers: ¬∀x P(x) ≡ ∃x ¬P(x).",
        "explain_wrong": "❌ غلط! العبارة صحيحة تماماً."
    },
    {
        "q": "An indirect proof by contradiction of (p → q) starts by assuming (p ∧ ¬q) is true.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "✅ صح! لأننا بنفترض نفي الجملة كلها، ونفي (p → q) هو (p ∧ ¬q).",
        "explain_wrong": "❌ غلط! العبارة صحيحة، بنفترض (p ∧ ¬q) وندور على تناقض."
    },
    {
        "q": "The associative laws state that p ∨ q ≡ q ∨ p.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "✅ صح! العبارة غلط، لأن ده قانون التبديل (Commutative law) مش الـ Associative.",
        "explain_wrong": "❌ غلط! ده قانون الـ Commutative مش الـ Associative."
    }
]
