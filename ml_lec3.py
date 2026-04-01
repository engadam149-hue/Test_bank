# ==========================================
# 📖 ml_lec3.py
# Machine Learning - Lecture 3
# Linear Regression, Gradient Descent, and Feature Scaling
# ==========================================

QUESTIONS = [
    # ─── Part 1: Basic Concepts & Notation ───
    {
        "q": "In Supervised Learning, what is the fundamental difference between Regression and Classification?",
        "type": "mcq",
        "options": [
            "Regression predicts a continuous value, Classification predicts a discrete value",
            "Regression is for unlabeled data, Classification is for labeled data",
            "Classification predicts a continuous value, Regression predicts categories",
            "There is no difference between them"
        ],
        "ans": "Regression predicts a continuous value, Classification predicts a discrete value",
        "explain_correct": "Regression is used to predict continuous numbers like house prices, while Classification is used to predict discrete categories like (sick/healthy). ✅",
        "explain_wrong": "Remember: Regression = Continuous/Real-valued, Classification = Discrete."
    },
    {
        "q": "In machine learning terminology, what does the symbol 'm' represent?",
        "type": "mcq",
        "options": [
            "Number of features",
            "Number of training examples",
            "Output variable",
            "Learning rate"
        ],
        "ans": "Number of training examples",
        "explain_correct": "The symbol 'm' always refers to the number of rows or examples in the training data. ✅",
        "explain_wrong": "The symbol 'n' refers to the number of features."
    },
    {
        "q": "What symbol represents the value of feature j in training example i?",
        "type": "mcq",
        "options": ["x_i^(j)", "x_j^(i)", "y_j^(i)", "theta_j^(i)"],
        "ans": "x_j^(i)",
        "explain_correct": "The superscript (i) in parentheses refers to the row (training example), and the subscript (j) refers to the column (feature). ✅",
        "explain_wrong": "Remember: (i) on top for row, j on bottom for column."
    },

    # ─── Part 2: Hypothesis & Cost Function ───
    {
        "q": "The equation h_θ(x) = θ_0 + θ_1 * x represents:",
        "type": "mcq",
        "options": [
            "Cost Function",
            "Gradient Descent",
            "Linear Regression Hypothesis (with one variable)",
            "Polynomial Regression"
        ],
        "ans": "Linear Regression Hypothesis (with one variable)",
        "explain_correct": "This is the simple straight-line equation (Hypothesis) that we try to fit as well as possible through the data. ✅",
        "explain_wrong": "This function is called the Hypothesis, not the Cost Function."
    },
    {
        "q": "In Linear Regression, what is the main goal of the cost function J(θ_0, θ_1)?",
        "type": "mcq",
        "options": [
            "Maximize J(θ_0, θ_1)",
            "Minimize J(θ_0, θ_1)",
            "Make J(θ_0, θ_1) always equal to 1",
            "Count the number of training examples"
        ],
        "ans": "Minimize J(θ_0, θ_1)",
        "explain_correct": "The cost function measures the error, so our goal is always to minimize that error to the lowest possible value. ✅",
        "explain_wrong": "The cost function represents error, and error must be minimized."
    },
    {
        "q": "The cost function used in Linear Regression is known as:",
        "type": "mcq",
        "options": [
            "Logistic Function",
            "Squared Error Function",
            "Absolute Error Function",
            "Sigmoid Function"
        ],
        "ans": "Squared Error Function",
        "explain_correct": "The cost function in Linear Regression is the Mean Squared Error (Squared Error), the most common and efficient choice for this problem. ✅",
        "explain_wrong": "It is called the Squared Error Function because we square the difference between the prediction and the true value."
    },
    {
        "q": "In a Contour Plot of the cost function, what does the point at the center of the concentric ellipses represent?",
        "type": "mcq",
        "options": [
            "The highest error value",
            "The minimum of the cost function",
            "The value of the learning rate",
            "The random starting point"
        ],
        "ans": "The minimum of the cost function",
        "explain_correct": "The center of the ellipses in the contour plot represents the bottom of the bowl, which is the minimum of the cost function (best parameters). ✅",
        "explain_wrong": "The center represents the Global Minimum of the Cost Function."
    },

    # ─── Part 3: Gradient Descent Algorithm ───
    {
        "q": "In the Gradient Descent algorithm, to ensure it works correctly, the parameters (θ_0, θ_1) must be updated:",
        "type": "mcq",
        "options": [
            "Sequentially (Sequential update)",
            "Simultaneously (Simultaneous update)",
            "Randomly",
            "Only update θ_1 and leave θ_0"
        ],
        "ans": "Simultaneously (Simultaneous update)",
        "explain_correct": "We must compute all new θ values into temporary variables (temp), then update all of them at the same time (Simultaneously). ✅",
        "explain_wrong": "Sequential update changes the function value while computing other derivatives, which is incorrect."
    },
    {
        "q": "What happens if the learning rate (α) is too small?",
        "type": "mcq",
        "options": [
            "The algorithm will fail to work",
            "The algorithm will overshoot the minimum",
            "Gradient Descent will be very slow to converge",
            "The cost function will increase"
        ],
        "ans": "Gradient Descent will be very slow to converge",
        "explain_correct": "A small α means very small steps, so it will take many iterations to reach the minimum. ✅",
        "explain_wrong": "Small α = very slow convergence."
    },
    {
        "q": "What happens if the learning rate (α) is too large?",
        "type": "mcq",
        "options": [
            "It will be very slow",
            "It will reach the optimal solution instantly",
            "It may overshoot the minimum and diverge",
            "Gradient Descent will turn into classification"
        ],
        "ans": "It may overshoot the minimum and diverge",
        "explain_correct": "A large α causes large steps, so it may jump to the other side of the curve and keep growing until it diverges. ✅",
        "explain_wrong": "Large α = Overshoot and fail to converge."
    },
    {
        "q": "If Gradient Descent reaches a Local Minimum, what will the value of the next update step be?",
        "type": "mcq",
        "options": [
            "The algorithm will move to a random point",
            "The parameters (θ) will not change because the derivative will be zero",
            "The parameters will increase by α",
            "The algorithm will reverse direction"
        ],
        "ans": "The parameters (θ) will not change because the derivative will be zero",
        "explain_correct": "At a Minimum, the tangent is horizontal so the derivative is zero. Therefore θ - (α * 0) = θ. The algorithm stays in place. ✅",
        "explain_wrong": "At a Local Minimum, the update stops because slope = 0."
    },
    {
        "q": "As Gradient Descent approaches the Local Minimum, the steps it takes automatically become smaller, so we do not need to decrease α over time.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "Correct! Because the derivative (slope) decreases as we approach the bottom, the value of (α * derivative) decreases on its own and steps shrink automatically. ✅",
        "explain_wrong": "You do not need to change α because the slope (Derivative) shrinks by itself."
    },
    {
        "q": "Why is applying Gradient Descent to Linear Regression considered safe from getting stuck in a bad Local Minimum?",
        "type": "mcq",
        "options": [
            "Because it does not use derivatives",
            "Because the cost function is a Convex Function (bowl shape) with only one Global Optimum",
            "Because the learning rate always changes",
            "Because it works on only one feature"
        ],
        "ans": "Because the cost function is a Convex Function (bowl shape) with only one Global Optimum",
        "explain_correct": "The Cost Function in Linear Regression is always Convex (bowl-shaped), meaning there are no local minima to get trapped in — it always descends to the single Global Minimum. ✅",
        "explain_wrong": "The cost function here is Convex (curved downward) and has a single optimal solution."
    },
    {
        "q": "What does the word 'Batch' mean in the term Batch Gradient Descent?",
        "type": "mcq",
        "options": [
            "The algorithm uses one training example per step",
            "The algorithm processes data in random groups",
            "The algorithm uses all training examples to compute the derivative at each step",
            "The algorithm uses no data"
        ],
        "ans": "The algorithm uses all training examples to compute the derivative at each step",
        "explain_correct": "At each update step, we sum the errors over all m examples (the entire dataset), and that is the meaning of the word Batch. ✅",
        "explain_wrong": "Batch means using the full Dataset in each Update."
    },

    # ─── Part 4: Multivariate Linear Regression ───
    {
        "q": "In Multivariate Linear Regression, we add the dummy feature (x_0) to simplify matrix multiplication. What is the value of x_0 always?",
        "type": "mcq",
        "options": ["0", "1", "-1", "Equal to y"],
        "ans": "1",
        "explain_correct": "We always assume x_0 = 1 so that when multiplied by the parameter θ_0, it remains θ_0 (the Y-intercept). ✅",
        "explain_wrong": "x_0 is always 1 to simplify vector computations."
    },
    {
        "q": "What is the purpose of Feature Scaling?",
        "type": "mcq",
        "options": [
            "Reduce the number of features",
            "Make Gradient Descent converge faster",
            "Increase the value of the cost function",
            "Remove x_0"
        ],
        "ans": "Make Gradient Descent converge faster",
        "explain_correct": "When all features are in the same range (e.g., -1 to 1), the contours become circular and Gradient Descent reaches the solution much faster instead of oscillating. ✅",
        "explain_wrong": "Feature Scaling speeds up convergence."
    },
    {
        "q": "In the ideal case, what is the approximate range that feature values should fall within after scaling?",
        "type": "mcq",
        "options": [
            "0 to 100",
            "-100 to 100",
            "Approximately -1 to 1",
            "Negative infinity to positive infinity"
        ],
        "ans": "Approximately -1 to 1",
        "explain_correct": "Ideally all features should be approximately between -1 and 1. A range of -3 to 3 or -1/3 to 1/3 is also acceptable. ✅",
        "explain_wrong": "The ideal range is around zero with small values (-1 to +1)."
    },
    {
        "q": "The formula x_i = (x_i - μ_i) / s_i is the formula for:",
        "type": "mcq",
        "options": [
            "Gradient Descent",
            "Cost Function",
            "Mean Normalization",
            "Polynomial Regression"
        ],
        "ans": "Mean Normalization",
        "explain_correct": "This is the Mean Normalization formula — we subtract the mean (μ) and divide by the range or standard deviation (s) to center the data around zero. ✅",
        "explain_wrong": "This formula is used to scale the data."
    },
    {
        "q": "In the Mean Normalization formula: x_i = (x_i - μ_i) / s_i, what can the symbol s_i represent?",
        "type": "mcq",
        "options": [
            "The arithmetic mean",
            "The range (Max - Min) or the Standard Deviation",
            "The number of examples m",
            "The Learning Rate"
        ],
        "ans": "The range (Max - Min) or the Standard Deviation",
        "explain_correct": "The symbol s represents the Range (max value minus min value), or we can use the Standard Deviation in the denominator. ✅",
        "explain_wrong": "s_i is a measure of spread (range or standard deviation)."
    },

    # ─── Part 5: Debugging & Polynomial Regression ───
    {
        "q": "How do we verify that Gradient Descent is working correctly (Debugging)?",
        "type": "mcq",
        "options": [
            "By plotting J(θ) vs number of iterations — it should decrease",
            "By plotting α vs number of iterations — it should increase",
            "By plotting x values vs y values",
            "By plotting J(θ) — it should be increasing"
        ],
        "ans": "By plotting J(θ) vs number of iterations — it should decrease",
        "explain_correct": "The best approach is to plot the Cost Function at each iteration. If it is working correctly, the error (J) must continuously decrease. ✅",
        "explain_wrong": "The cost function must decrease at every step."
    },
    {
        "q": "If you plot J(θ) vs number of iterations and find it is increasing (going upward), what is the likely cause?",
        "type": "mcq",
        "options": [
            "The dataset is too small",
            "The learning rate (α) is too large and should be decreased",
            "The learning rate (α) is too small and should be increased",
            "Gradient Descent is working perfectly"
        ],
        "ans": "The learning rate (α) is too large and should be decreased",
        "explain_correct": "When the error increases instead of decreasing, the algorithm is overshooting the target. The immediate fix is to decrease α. ✅",
        "explain_wrong": "An increasing J(θ) means Divergence, caused by a large α."
    },
    {
        "q": "To perform an automatic convergence test, we can stop the algorithm if J(θ) decreases by less than a very small threshold, such as:",
        "type": "mcq",
        "options": ["100", "1", "10^-3 (0.001)", "0.5"],
        "ans": "10^-3 (0.001)",
        "explain_correct": "We can program the code to stop if the change in the cost function becomes negligible (less than 0.001 for example), indicating that it has approximately reached the bottom. ✅",
        "explain_wrong": "A tiny change (such as 10^-3) represents reaching Convergence."
    },
    {
        "q": "In Polynomial Regression, we can create new features from existing ones, such as squaring x or taking its square root, to fit non-linear data.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "Correct. If the data is not a straight line, we can engineer new features like x^2, x^3, or sqrt(x) so the hypothesis takes a curve shape that fits the data. ✅",
        "explain_wrong": "Polynomial Regression relies on combining and raising existing features to higher powers."
    },
    {
        "q": "When using Polynomial Regression and transforming feature x into x, x^2, and x^3, Feature Scaling becomes unimportant.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "Completely wrong! Feature Scaling becomes even more critical here. If x has a range of 1 to 100, then x^3 will have a range of 1 to 1,000,000 — the differences will be enormous. ✅",
        "explain_wrong": "Feature Scaling is even more important in Polynomial Regression due to the extreme range differences."
    },
    {
        "q": "Which of the following learning rate (α) values is recommended to try when searching for the best value for Gradient Descent?",
        "type": "mcq",
        "options": [
            "Only 0.01 and 0.1",
            "Only negative numbers",
            "Approximate multiples of 3 such as: ..., 0.001, 0.003, 0.01, 0.03, 0.1, ...",
            "Large integers such as 10, 100, 1000"
        ],
        "ans": "Approximate multiples of 3 such as: ..., 0.001, 0.003, 0.01, 0.03, 0.1, ...",
        "explain_correct": "Andrew Ng always recommends trying values that multiply by approximately 3 each time, to quickly discover the appropriate range for α. ✅",
        "explain_wrong": "Logarithmic spacing multiplied by 3 is the best strategy for discovering a suitable α."
    }
]
