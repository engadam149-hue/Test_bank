"""
Quiz on K-Nearest Neighbors (k-NN) Algorithm
Based on Machine Learning Lecture by Dr. Sara Sweidan
50 Questions: 35 Multiple Choice + 15 True/False
"""

import random

# =============================================
# 35 Multiple Choice Questions
# =============================================
multiple_choice = [
    {
        "q": "1. What does k-NN stand for?",
        "options": ["a) Key-Node Network", "b) k-Nearest Neighbors", "c) k-Null Nodes", "d) Key-Nearest Nodes"],
        "answer": "b"
    },
    {
        "q": "2. Why is k-NN considered a 'lazy learner'?",
        "options": [
            "a) It uses a simple algorithm",
            "b) It does not build a model during training, deferring computation to test time",
            "c) It is slow at everything",
            "d) It ignores irrelevant features"
        ],
        "answer": "b"
    },
    {
        "q": "3. In k-NN classification, how is the class of a new data point determined?",
        "options": [
            "a) By the class of the single nearest neighbor",
            "b) By the majority class among the k nearest neighbors",
            "c) By the average distance of all training points",
            "d) By a learned decision boundary"
        ],
        "answer": "b"
    },
    {
        "q": "4. What is the Euclidean distance between A(0,1) and B(2,3)?",
        "options": ["a) 1", "b) 2√2", "c) 4", "d) 8"],
        "answer": "b"
    },
    {
        "q": "5. Which formula is used for min-max normalization?",
        "options": [
            "a) x = (x + MIN) / MAX",
            "b) x = (x - MIN) / (MAX - MIN)",
            "c) x = x / MAX",
            "d) x = (x - MAX) / MIN"
        ],
        "answer": "b"
    },
    {
        "q": "6. What happens when k is very large in k-NN?",
        "options": [
            "a) The model underfits and may include points from other classes",
            "b) The model becomes more accurate",
            "c) The algorithm runs faster",
            "d) Noise has more effect"
        ],
        "answer": "a"
    },
    {
        "q": "7. What happens when k is very small (e.g., k=1)?",
        "options": [
            "a) The model underfits",
            "b) The algorithm is very sensitive to noise",
            "c) The model generalizes well",
            "d) Training time increases"
        ],
        "answer": "b"
    },
    {
        "q": "8. Which of the following is a weakness of k-NN?",
        "options": [
            "a) Simple and effective",
            "b) Fast training phase",
            "c) Slow classification phase",
            "d) Makes no assumptions about data distribution"
        ],
        "answer": "c"
    },
    {
        "q": "9. Which of the following is a strength of k-NN?",
        "options": [
            "a) Produces a model for interpretation",
            "b) Fast classification phase",
            "c) Makes no assumptions about data distribution",
            "d) Works well with missing data"
        ],
        "answer": "c"
    },
    {
        "q": "10. What does normalization achieve in k-NN?",
        "options": [
            "a) Removes noisy data",
            "b) Prevents one attribute from dominating distance calculations",
            "c) Speeds up training",
            "d) Selects the best k automatically"
        ],
        "answer": "b"
    },
    {
        "q": "11. In the Euclidean distance formula dist(p,q), what is computed?",
        "options": [
            "a) Sum of absolute differences",
            "b) Square root of the sum of squared differences",
            "c) Product of feature values",
            "d) Average of feature values"
        ],
        "answer": "b"
    },
    {
        "q": "12. What is a Tomek Link?",
        "options": [
            "a) A method to increase training data",
            "b) A pair of examples from different classes that are each other's nearest neighbor",
            "c) A technique for selecting the best k",
            "d) A distance metric"
        ],
        "answer": "b"
    },
    {
        "q": "13. Why are Tomek Links removed from training data?",
        "options": [
            "a) To speed up the algorithm",
            "b) To remove borderline/noisy examples that can harm classification",
            "c) To reduce the number of features",
            "d) To normalize the data"
        ],
        "answer": "b"
    },
    {
        "q": "14. In weighted k-NN, what weight is given to the farthest neighbor (d_k)?",
        "options": ["a) 1", "b) 0.5", "c) 0", "d) It depends on k"],
        "answer": "c"
    },
    {
        "q": "15. In weighted k-NN, what weight is given to the nearest neighbor (d_1)?",
        "options": ["a) 0", "b) 0.5", "c) 1", "d) k"],
        "answer": "c"
    },
    {
        "q": "16. What is the main benefit of using k neighbors instead of just 1?",
        "options": [
            "a) Faster computation",
            "b) Voting among neighbors overcomes noise",
            "c) Eliminates the need for normalization",
            "d) Reduces memory usage"
        ],
        "answer": "b"
    },
    {
        "q": "17. What is class-label noise in k-NN?",
        "options": [
            "a) An attribute value is incorrect",
            "b) The class provided for an example is incorrect",
            "c) Too many features in the dataset",
            "d) Missing values in features"
        ],
        "answer": "b"
    },
    {
        "q": "18. What is attribute noise in k-NN?",
        "options": [
            "a) The class label is wrong",
            "b) An attribute's value is incorrect",
            "c) Too many neighbors are selected",
            "d) Normalization is not applied"
        ],
        "answer": "b"
    },
    {
        "q": "19. Which distance axiom states d(x,x) = 0?",
        "options": [
            "a) Triangle inequality",
            "b) Symmetry",
            "c) Identity",
            "d) Non-negativity"
        ],
        "answer": "c"
    },
    {
        "q": "20. Which distance axiom is represented by d(x,y) = d(y,x)?",
        "options": [
            "a) Non-negativity",
            "b) Identity",
            "c) Symmetry",
            "d) Triangle inequality"
        ],
        "answer": "c"
    },
    {
        "q": "21. The triangle inequality for distance metrics states:",
        "options": [
            "a) d(x,y) = d(y,x)",
            "b) d(x,y) + d(y,z) >= d(x,z)",
            "c) d(x,x) = 0",
            "d) d(x,y) >= 0"
        ],
        "answer": "b"
    },
    {
        "q": "22. A k-NN model gets 100% training accuracy but fails on new data. What is the most likely problem?",
        "options": [
            "a) Underfitting",
            "b) Overfitting",
            "c) Incorrect normalization",
            "d) Too large k"
        ],
        "answer": "b"
    },
    {
        "q": "23. Which statement about k-NN is TRUE regarding all three?",
        "options": [
            "a) k-NN performs better with same-scale data, struggles with many features, and makes no functional form assumptions",
            "b) k-NN is a parametric model",
            "c) k-NN requires data to be normalized only for large k",
            "d) k-NN works best with many irrelevant features"
        ],
        "answer": "a"
    },
    {
        "q": "24. k-NN does more computation at which phase?",
        "options": ["a) Training phase", "b) Test/classification phase", "c) Both equally", "d) Neither"],
        "answer": "b"
    },
    {
        "q": "25. Given values 7, 4, 25, -5, 10 with MIN=-5, MAX=25, what is the normalized value of 7?",
        "options": ["a) 0.3", "b) 0.4", "c) 0.5", "d) 0.6"],
        "answer": "b"
    },
    {
        "q": "26. In the weighted 5-NN example with distances d1=1, d2=3, d3=4, d4=5, d5=8, what is w2?",
        "options": ["a) 4/7", "b) 5/7", "c) 3/7", "d) 1"],
        "answer": "b"
    },
    {
        "q": "27. Which step in k-NN involves finding the majority class among neighbors?",
        "options": ["a) Step 2", "b) Step 3", "c) Step 5", "d) Step 6"],
        "answer": "c"
    },
    {
        "q": "28. What type of variable is used to label categories in k-NN training data?",
        "options": ["a) Continuous", "b) Nominal", "c) Ordinal", "d) Binary only"],
        "answer": "b"
    },
    {
        "q": "29. Irrelevant attributes in k-NN cause problems because:",
        "options": [
            "a) They slow down training",
            "b) They affect example-to-example distances without affecting the class",
            "c) They prevent normalization",
            "d) They increase k"
        ],
        "answer": "b"
    },
    {
        "q": "30. In removing redundant examples, the algorithm starts with set S containing:",
        "options": [
            "a) All training examples",
            "b) One positive and one negative example",
            "c) Only positive examples",
            "d) k random examples"
        ],
        "answer": "b"
    },
    {
        "q": "31. The k-NN algorithm is best suited for problems where:",
        "options": [
            "a) Data is linear and separable",
            "b) Relationships are complex but similar classes are fairly homogeneous",
            "c) The dataset is very small",
            "d) Feature importance is known"
        ],
        "answer": "b"
    },
    {
        "q": "32. Which graph shape best describes error rate vs. k in k-NN?",
        "options": [
            "a) Linear increase",
            "b) U-shaped curve (high at both extremes, low in middle)",
            "c) Linear decrease",
            "d) Flat line"
        ],
        "answer": "b"
    },
    {
        "q": "33. In weighted k-NN, x is classified as positive when:",
        "options": [
            "a) More than half the neighbors are positive",
            "b) Sum of positive weights > sum of negative weights",
            "c) d1 belongs to a positive class",
            "d) k is odd"
        ],
        "answer": "b"
    },
    {
        "q": "34. What scaling problem can occur in k-NN?",
        "options": [
            "a) Nominal features dominate numeric features",
            "b) An attribute with large range can overwhelm others in distance calculation",
            "c) Too many classes reduce accuracy",
            "d) Normalization increases bias"
        ],
        "answer": "b"
    },
    {
        "q": "35. In the redundant example removal algorithm, examples are added to S when they:",
        "options": [
            "a) Are correctly classified by 1-NN using S",
            "b) Are incorrectly classified by 1-NN using S",
            "c) Are positive examples",
            "d) Have the smallest distance"
        ],
        "answer": "b"
    },
]

# =============================================
# 15 True/False Questions
# =============================================
true_false = [
    {"q": "1. k-NN does more computation at test time rather than train time.", "answer": "True"},
    {"q": "2. k-NN produces a model that helps understand how features relate to the class.", "answer": "False"},
    {"q": "3. Normalization ensures each attribute falls into the interval [0,1].", "answer": "True"},
    {"q": "4. When k is too small, k-NN becomes very sensitive to noise.", "answer": "True"},
    {"q": "5. In k-NN, a Tomek Link connects two examples from the SAME class.", "answer": "False"},
    {"q": "6. Irrelevant attributes do NOT affect distance calculations in k-NN.", "answer": "False"},
    {"q": "7. k-NN makes assumptions about the underlying data distribution.", "answer": "False"},
    {"q": "8. In weighted k-NN, closer neighbors get higher weights than farther ones.", "answer": "True"},
    {"q": "9. A k-NN model with 100% training accuracy but poor test accuracy is overfitted.", "answer": "True"},
    {"q": "10. The Euclidean distance satisfies d(x,y) = d(y,x).", "answer": "True"},
    {"q": "11. Noisy data causes no problems for the k-NN algorithm.", "answer": "False"},
    {"q": "12. Using k neighbors instead of 1 helps overcome noise through voting.", "answer": "True"},
    {"q": "13. The training phase of k-NN is slower than its classification phase.", "answer": "False"},
    {"q": "14. k-NN works well when similar class items tend to be homogeneous in feature space.", "answer": "True"},
    {"q": "15. In the normalization formula, MAX refers to the maximum value in the test set.", "answer": "False"},
]


def run_quiz():
    print("=" * 60)
    print("   K-Nearest Neighbors (k-NN) Quiz")
    print("   Based on Dr. Sara Sweidan's Machine Learning Lecture")
    print("=" * 60)
    print(f"\nTotal Questions: 50 (35 MCQ + 15 True/False)\n")

    score = 0
    total = 0

    # --- Multiple Choice ---
    print("\n" + "=" * 60)
    print("  PART 1: Multiple Choice Questions (35 Questions)")
    print("=" * 60)

    for i, q in enumerate(multiple_choice, 1):
        print(f"\n{q['q']}")
        for opt in q['options']:
            print(f"   {opt}")
        user = input("Your answer (a/b/c/d): ").strip().lower()
        total += 1
        if user == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    # --- True/False ---
    print("\n" + "=" * 60)
    print("  PART 2: True / False Questions (15 Questions)")
    print("=" * 60)

    for i, q in enumerate(true_false, 1):
        print(f"\n{q['q']}")
        user = input("Your answer (True/False): ").strip().capitalize()
        total += 1
        if user == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    # --- Final Score ---
    print("\n" + "=" * 60)
    print(f"  FINAL SCORE: {score} / {total}")
    percentage = (score / total) * 100
    print(f"  Percentage: {percentage:.1f}%")
    if percentage >= 90:
        print("  Grade: Excellent! 🌟")
    elif percentage >= 75:
        print("  Grade: Very Good! 👍")
    elif percentage >= 60:
        print("  Grade: Good 😊")
    else:
        print("  Grade: Needs More Study 📚")
    print("=" * 60)


if __name__ == "__main__":
    run_quiz()