# ==========================================
# 📖 ml_lec4.py
# Machine Learning - Lecture 4
# Logistic Regression, Cost Function, and One-vs-All
# ==========================================

QUESTIONS = [
    # ─── Part 1: Classification & Sigmoid Function ───
    {
        "q": "Although it contains the word 'Regression', Logistic Regression is mainly used for solving:",
        "type": "mcq",
        "options": ["Classification", "Regression", "Clustering", "Dimensionality Reduction"],
        "ans": "Classification",
        "explain_correct": "Exactly! Logistic Regression is used to predict discrete classes (like sick/healthy, 0/1), so it is a classification algorithm. ✅",
        "explain_wrong": "The name is a bit misleading, but it is used for classification because it outputs probabilities between 0 and 1."
    },
    {
        "q": "What is the main function of the Sigmoid (Logistic Function) in this algorithm?",
        "type": "mcq",
        "options": ["Convert any real value into a number between 0 and 1", "Convert negative numbers to positive", "Increase Gradient Descent speed", "Calculate the error rate"],
        "ans": "Convert any real value into a number between 0 and 1",
        "explain_correct": "The Sigmoid function takes any number (from -∞ to +∞) and squashes it into a probability between 0 and 1. ✅",
        "explain_wrong": "The Sigmoid function is used to squash outputs into the probability range [0, 1]."
    },
    {
        "q": "The mathematical equation of the Sigmoid (Logistic function) g(z) is:",
        "type": "mcq",
        "options": ["1 / (1 + e^(-z))", "1 / (1 - e^(-z))", "e^(-z) / (1 + e^(-z))", "1 + e^(-z)"],
        "ans": "1 / (1 + e^(-z))",
        "explain_correct": "This is the standard formula of the Sigmoid function. As z increases, the output approaches 1. ✅",
        "explain_wrong": "Remember the denominator has a plus sign, and the exponent of e is negative z."
    },
    {
        "q": "What does the value of the hypothesis h_θ(x) represent in Logistic Regression?",
        "type": "mcq",
        "options": ["Estimated probability that y = 1 given x", "Prediction error value", "Final class directly (0 or 1)", "Feature values"],
        "ans": "Estimated probability that y = 1 given x",
        "explain_correct": "If h_θ(x) = 0.7, it means there is a 70% probability that y = 1. ✅",
        "explain_wrong": "The output is a probability, not the final class—we decide the class using a threshold."
    },
    {
        "q": "If the hypothesis gives P(y=1|x;θ) = 0.7, what is P(y=0|x;θ)?",
        "type": "mcq",
        "options": ["0.3", "0.7", "0", "1"],
        "ans": "0.3",
        "explain_correct": "Since it's binary classification, probabilities sum to 1 → 1 - 0.7 = 0.3. ✅",
        "explain_wrong": "The sum of probabilities of all classes must equal 1."
    },

    # ─── Part 2: Decision Boundary ───
    {
        "q": "By default, what threshold is used to convert h_θ(x) into a final decision (y=0 or y=1)?",
        "type": "mcq",
        "options": ["0.5", "0", "1", "0.8"],
        "ans": "0.5",
        "explain_correct": "Default rule: if probability ≥ 0.5 → y=1, else → y=0. ✅",
        "explain_wrong": "The default classification threshold is 0.5 (50%)."
    },
    {
        "q": "When is the Sigmoid function g(z) ≥ 0.5?",
        "type": "mcq",
        "options": ["When z ≥ 0", "When z ≤ 0", "When z = 1", "When z < 0.5"],
        "ans": "When z ≥ 0",
        "explain_correct": "At z = 0, g(z) = 0.5. For positive z, g(z) > 0.5. ✅",
        "explain_wrong": "If z = 0 → output = 0.5. If z > 0 → output > 0.5."
    },
    {
        "q": "The Decision Boundary depends on:",
        "type": "mcq",
        "options": ["Hypothesis and parameters θ", "Training data only", "Cost function", "Learning rate"],
        "ans": "Hypothesis and parameters θ",
        "explain_correct": "The decision boundary is determined by θ. Data helps learn θ, but the boundary itself comes from θᵀx = 0. ✅",
        "explain_wrong": "The decision boundary is a property of the model parameters, not the data itself."
    },
    {
        "q": "To obtain a non-linear decision boundary (e.g., circular), what should we do?",
        "type": "mcq",
        "options": ["Add higher-order polynomial features like x1^2, x2^2", "Use a very large learning rate", "Change the Sigmoid function", "Remove some training data"],
        "ans": "Add higher-order polynomial features like x1^2, x2^2",
        "explain_correct": "Adding polynomial features allows curved decision boundaries. ✅",
        "explain_wrong": "Non-linear features create non-linear decision boundaries."
    },

    # ─── Part 3: Logistic Regression Cost Function ───
    {
        "q": "Why don't we use the Linear Regression cost function (Squared Error) with Logistic Regression?",
        "type": "mcq",
        "options": ["It becomes non-convex with many local minima", "It becomes too slow", "It always gives zero", "There is no reason"],
        "ans": "It becomes non-convex with many local minima",
        "explain_correct": "With Sigmoid, squared error becomes wavy (non-convex), causing Gradient Descent to get stuck. ✅",
        "explain_wrong": "Squared error with Sigmoid produces a non-convex function."
    },
    {
        "q": "If y = 1 and h_θ(x) = 1, what is the cost?",
        "type": "mcq",
        "options": ["0", "Infinity", "1", "0.5"],
        "ans": "0",
        "explain_correct": "Perfect prediction → zero error → cost = 0. ✅",
        "explain_wrong": "If prediction is perfectly correct, cost is zero."
    },
    {
        "q": "If y = 1 and h_θ(x) = 0, what is the cost?",
        "type": "mcq",
        "options": ["Infinity", "0", "-1", "1"],
        "ans": "Infinity",
        "explain_correct": "Worst case → -log(0) = ∞. Huge penalty. ✅",
        "explain_wrong": "Completely wrong confident prediction leads to infinite cost."
    },
    {
        "q": "The Logistic Regression cost function is:",
        "type": "mcq",
        "options": ["Convex (one global minimum)", "Non-convex", "No minimum", "Linear"],
        "ans": "Convex (one global minimum)",
        "explain_correct": "Log-based cost creates a convex (bowl-shaped) function. ✅",
        "explain_wrong": "Logarithmic formulation ensures convexity."
    },
    {
        "q": "The unified cost function J(θ) is based on:",
        "type": "mcq",
        "options": ["y*log(h) + (1-y)*log(1-h)", "Adding y to prediction", "Squared error", "Removing y"],
        "ans": "y*log(h) + (1-y)*log(1-h)",
        "explain_correct": "If y=1 → second term cancels, if y=0 → first term cancels. Smart trick! ✅",
        "explain_wrong": "This combines both cases into one equation."
    },

    # ─── Part 4: Gradient Descent ───
    {
        "q": "Gradient Descent update rule in Logistic Regression is identical to Linear Regression.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "Correct! Same formula, only h(x) changes to Sigmoid. ✅",
        "explain_wrong": "Update rule is identical, but hypothesis differs."
    },
    {
        "q": "Is Feature Scaling important in Logistic Regression?",
        "type": "mcq",
        "options": ["Yes, it speeds up convergence", "No effect", "Causes errors", "Only for negative data"],
        "ans": "Yes, it speeds up convergence",
        "explain_correct": "Feature scaling helps Gradient Descent converge faster. ✅",
        "explain_wrong": "Feature scaling is always useful with Gradient Descent."
    },

    # ─── Part 5: Multiclass (One-vs-All) ───
    {
        "q": "Multiclass Classification involves:",
        "type": "mcq",
        "options": ["More than two classes", "Only two classes", "Continuous values", "No labels"],
        "ans": "More than two classes",
        "explain_correct": "Multiclass means more than two possible outputs. ✅",
        "explain_wrong": "Binary = 2 classes, Multiclass = more."
    },
    {
        "q": "For k classes using One-vs-All, how many models are trained?",
        "type": "mcq",
        "options": ["k models", "1 model", "k^2 models", "2 models"],
        "ans": "k models",
        "explain_correct": "One classifier per class. ✅",
        "explain_wrong": "Train k classifiers for k classes."
    },
    {
        "q": "How do we choose the final class in One-vs-All?",
        "type": "mcq",
        "options": ["Choose class with max probability", "Random", "Minimum probability", "Sum probabilities"],
        "ans": "Choose class with max probability",
        "explain_correct": "Pick the classifier with highest confidence. ✅",
        "explain_wrong": "Choose the most confident classifier."
    },
    {
        "q": "For training 'Cold' classifier (3 classes: Healthy, Cold, Flu), labels become:",
        "type": "mcq",
        "options": ["Cold=1, others=0", "All=1", "Cold=1, Healthy=2, Flu=3", "Ignore others"],
        "ans": "Cold=1, others=0",
        "explain_correct": "Target class = 1, others = 0. ✅",
        "explain_wrong": "Convert to binary problem."
    },
    {
        "q": "What happens to e^(-z) as z → +∞?",
        "type": "mcq",
        "options": ["Approaches 0", "Approaches ∞", "Equals 1", "Becomes negative"],
        "ans": "Approaches 0",
        "explain_correct": "e^(-z) → 0 → Sigmoid → 1. ✅",
        "explain_wrong": "e^(-z) = 1/e^z → goes to 0."
    },
    {
        "q": "What happens to e^(-z) as z → -∞?",
        "type": "mcq",
        "options": ["Approaches ∞", "Approaches 0", "Equals 1", "Becomes 0"],
        "ans": "Approaches ∞",
        "explain_correct": "e^(-z) = e^(+big) → ∞ → Sigmoid → 0. ✅",
        "explain_wrong": "Negative z makes exponent positive."
    }
]
