# ==========================================
# 📖 ml_lec5.py
# Machine Learning - Lecture 5
# Unsupervised Learning & K-Means Clustering
# ==========================================

QUESTIONS = [
    # ─── Part 1: Unsupervised Learning & Clustering Basics ───
    {
        "q": "In Unsupervised Learning, what is the main difference in the training data compared to Supervised Learning?",
        "type": "mcq",
        "options": [
            "The data does not contain outputs or labels (No labels y)",
            "The data contains labels only without features",
            "The data is always sorted in ascending order",
            "The number of features is variable in each example"
        ],
        "ans": "The data does not contain outputs or labels (No labels y)",
        "explain_correct": "In Unsupervised Learning, the dataset consists only of inputs (X) without any correct answers or labels (y). The algorithm's goal is to discover patterns on its own. ✅",
        "explain_wrong": "Remember: Supervised = (x, y). Unsupervised = (x) only."
    },
    {
        "q": "What is the primary function of a Clustering algorithm?",
        "type": "mcq",
        "options": [
            "To predict a continuous numerical value for new data",
            "To group data by inferring clusters or categories based on relationships between data points",
            "To classify data based on pre-existing labels",
            "To reduce the number of features in the data"
        ],
        "ans": "To group data by inferring clusters or categories based on relationships between data points",
        "explain_correct": "Clustering divides data into similar groups (Clusters), effectively creating new 'labels' that didn't exist originally, based on distances and relationships. ✅",
        "explain_wrong": "Clustering does not predict numbers; it discovers groups (Clusters)."
    },
    {
        "q": "Which of the following applications is considered an example of using Clustering?",
        "type": "mcq",
        "options": [
            "Predicting the price of a house based on its size",
            "Classifying emails as Spam or Non-Spam",
            "Market Segmentation (dividing a market into groups of similar customers)",
            "Recognizing handwritten digits"
        ],
        "ans": "Market Segmentation (dividing a market into groups of similar customers)",
        "explain_correct": "Customer segmentation, social network analysis, and organizing computing clusters are all very famous applications of Clustering. ✅",
        "explain_wrong": "Predicting price (Regression) and classifying email (Classification) are examples of Supervised Learning."
    },

    # ─── Part 2: K-Means Algorithm Steps ───
    {
        "q": "The K-Means algorithm consists of two main steps that are repeated in a loop. What are they?",
        "type": "mcq",
        "options": [
            "Calculating the cost and decreasing the learning rate",
            "Cluster Assignment and Move Centroid",
            "Initializing weights and calculating the derivative",
            "Collecting data and plotting the Elbow curve"
        ],
        "ans": "Cluster Assignment and Move Centroid",
        "explain_correct": "The algorithm works in two steps: 1. Assign each point to its closest centroid. 2. Calculate the mean of those points and move the centroid to that new location, then repeat. ✅",
        "explain_wrong": "K-Means does not use derivatives or a learning rate; it relies on distances and means."
    },
    {
        "q": "In the 'Cluster Assignment' step, how does the algorithm decide which Centroid a specific point belongs to?",
        "type": "mcq",
        "options": [
            "Randomly",
            "By choosing the farthest centroid to ensure broad distribution",
            "By calculating the distance and choosing the closest centroid to the point",
            "Based on the original label of the point"
        ],
        "ans": "By calculating the distance and choosing the closest centroid to the point",
        "explain_correct": "The algorithm calculates the distance between the point and all available centroids, and assigns the point to the closest one (Minimize distance). ✅",
        "explain_wrong": "Assignment is always done to the closest centroid."
    },
    {
        "q": "In the 'Move Centroid' step, how is the new location of the centroid calculated?",
        "type": "mcq",
        "options": [
            "By taking the mean (average) of the locations of all points assigned to that centroid",
            "By moving it a fixed distance towards the origin",
            "By choosing a new random point from the data",
            "By taking the sum of all distances"
        ],
        "ans": "By taking the mean (average) of the locations of all points assigned to that centroid",
        "explain_correct": "We gather all points assigned to this centroid, calculate the mean of their X and Y coordinates, and move the centroid to this new point. ✅",
        "explain_wrong": "The centroid moves to the mean of its points, hence the name of the algorithm (K-Means)."
    },

    # ─── Part 3: K-Means Variables & Optimization Objective ───
    {
        "q": "In the mathematical equations of the K-Means algorithm, what does the symbol c^(i) represent?",
        "type": "mcq",
        "options": [
            "The coordinates of centroid i",
            "The cluster index (from 1 to K) to which the training point x^(i) is currently assigned",
            "The total number of clusters K",
            "The cost function for data point i"
        ],
        "ans": "The cluster index (from 1 to K) to which the training point x^(i) is currently assigned",
        "explain_correct": "The symbol c^(i) stores a number (from 1 to K) that represents the cluster to which point i is currently assigned. ✅",
        "explain_wrong": "'c' stands for Cluster index."
    },
    {
        "q": "What does the symbol mu_k represent in the K-Means algorithm?",
        "type": "mcq",
        "options": [
            "The learning rate for cluster k",
            "A random training point",
            "The location (coordinates) of the centroid for cluster k",
            "The number of points inside cluster k"
        ],
        "ans": "The location (coordinates) of the centroid for cluster k",
        "explain_correct": "The symbol mu always represents the Centroid of cluster number k. ✅",
        "explain_wrong": "mu represents the Cluster Centroid."
    },
    {
        "q": "What does the symbol mu_{c^(i)} represent?",
        "type": "mcq",
        "options": [
            "The total number of centroids",
            "The location (coordinates) of the centroid of the cluster to which point x^(i) is assigned",
            "The mean of all data points",
            "The mean of the misclassified points"
        ],
        "ans": "The location (coordinates) of the centroid of the cluster to which point x^(i) is assigned",
        "explain_correct": "This is a combination of the two symbols! It means: get the coordinates of the centroid of the cluster that point i is currently attached to. ✅",
        "explain_wrong": "This symbol is used to calculate the distance between a point and its current centroid."
    },
    {
        "q": "The cost function J in K-Means is sometimes called the Distortion Function. What is the goal of the K-Means algorithm regarding this function?",
        "type": "mcq",
        "options": [
            "To maximize it",
            "To keep it constant at zero",
            "To minimize it as much as possible",
            "To make it equal to K"
        ],
        "ans": "To minimize it as much as possible",
        "explain_correct": "The K-Means algorithm is an optimization algorithm whose goal is always to reduce the sum of squared distances (Cost Function J) to the lowest possible value. ✅",
        "explain_wrong": "The goal is always to minimize the error/Distortion."
    },
    {
        "q": "How is the cost function J calculated in K-Means?",
        "type": "mcq",
        "options": [
            "The average of the product of points and centroids",
            "The average of the sum of squared distances between every point x^(i) and its assigned centroid mu_{c^(i)}",
            "The sum of distances between the centroids themselves",
            "The sum of the points divided by K"
        ],
        "ans": "The average of the sum of squared distances between every point x^(i) and its assigned centroid mu_{c^(i)}",
        "explain_correct": "The cost function is simply: measuring the distance between each point and its centroid, squaring it, and summing it up for all points. ✅",
        "explain_wrong": "The cost is the Squared Distances between points and their centroids."
    },
    {
        "q": "During the execution of the K-Means algorithm, can the cost function J increase in any iteration?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "False",
        "explain_correct": "Impossible! Mathematically, every step in K-Means (whether assigning points or moving centroids) either decreases the cost J or keeps it constant. If it increases, there is a bug in the code. ✅",
        "explain_wrong": "The cost function J must monotonically decrease or remain constant, it never increases."
    },

    # ─── Part 4: Random Initialization & Local Optima ───
    {
        "q": "What is the best and most recommended way to initialize the centroids at the beginning of the K-Means algorithm?",
        "type": "mcq",
        "options": [
            "Choosing the centroid coordinates at the origin (0,0)",
            "Randomly picking K training examples and setting them as the initial centroids",
            "Distributing the centroids on the extreme edges of the data",
            "Placing all centroids at a single point"
        ],
        "ans": "Randomly picking K training examples and setting them as the initial centroids",
        "explain_correct": "The best way is to randomly select actual data points from our dataset and consider them as the initial centroids. ✅",
        "explain_wrong": "Random initialization from within the training points is the recommended method."
    },
    {
        "q": "Can the K-Means algorithm get stuck in 'Local Optima' (suboptimal solutions) instead of reaching the best clustering (Global Optimum)?",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "Absolutely correct! Because the algorithm depends on random starting locations, it might start poorly and converge to a suboptimal clustering, getting stuck there (Local Optima). ✅",
        "explain_wrong": "K-Means does suffer from the Local Optima problem."
    },
    {
        "q": "How do we overcome the problem of Local Optima in the K-Means algorithm?",
        "type": "mcq",
        "options": [
            "By increasing the number of clusters K",
            "By using a large learning rate",
            "By running the algorithm multiple times (e.g., 50-100 times) with different random initializations, then picking the clustering with the lowest cost J",
            "By running the algorithm only once and waiting longer"
        ],
        "ans": "By running the algorithm multiple times (e.g., 50-100 times) with different random initializations, then picking the clustering with the lowest cost J",
        "explain_correct": "The practical solution is to run the algorithm many times (50 to 1000 times), calculate the Cost (J) each time, and ultimately select the clustering that resulted in the lowest Cost. ✅",
        "explain_wrong": "Multiple Random Initializations is the optimal solution."
    },
    {
        "q": "Running K-Means multiple times (Multiple Random Initializations) has a highly positive impact mostly when the number of clusters (K) is:",
        "type": "mcq",
        "options": [
            "Very large (K > 100)",
            "Small (e.g., K from 2 to 10)",
            "Equal to the number of training examples",
            "Negative"
        ],
        "ans": "Small (e.g., K from 2 to 10)",
        "explain_correct": "When the number of clusters is small (like 2 to 10), the chance of getting stuck in Local Optima is high, so running it multiple times makes a huge difference. If K is large, multiple initializations usually don't change the outcome much. ✅",
        "explain_wrong": "Multiple initializations are most effective with small numbers of K."
    },

    # ─── Part 5: Choosing the Number of Clusters (K) ───
    {
        "q": "What is the most famous graphical method for choosing the appropriate number of clusters (K)?",
        "type": "mcq",
        "options": [
            "The Elbow Method",
            "Plotting Gradient Descent",
            "Plotting the Sigmoid curve",
            "The One-vs-All method"
        ],
        "ans": "The Elbow Method",
        "explain_correct": "In the Elbow Method, we plot the Cost (J) against the number of clusters K, and we look for the point where the curve bends sharply like an elbow. ✅",
        "explain_wrong": "The Elbow Method is the standard heuristic for choosing K."
    },
    {
        "q": "In the Elbow method curve, what do the horizontal axis (X-axis) and vertical axis (Y-axis) represent?",
        "type": "mcq",
        "options": [
            "X: Number of iterations, Y: Cost J",
            "X: Number of clusters K, Y: Cost J (Distortion)",
            "X: Cost J, Y: Learning rate",
            "X: Amount of data, Y: Number of centroids"
        ],
        "ans": "X: Number of clusters K, Y: Cost J (Distortion)",
        "explain_correct": "We vary K (horizontal axis) and observe its effect on the Cost J (vertical axis) to find the best K that balances reducing error with the number of clusters. ✅",
        "explain_wrong": "The horizontal axis represents K, and the vertical represents J."
    },
    {
        "q": "What is the main drawback of the Elbow method?",
        "type": "mcq",
        "options": [
            "It always chooses K=1",
            "Sometimes the curve is smooth and decreases gradually without a clear 'elbow', making the choice of K highly ambiguous",
            "It requires supervised data",
            "It increases the value of the cost function"
        ],
        "ans": "Sometimes the curve is smooth and decreases gradually without a clear 'elbow', making the choice of K highly ambiguous",
        "explain_correct": "The curve doesn't always provide a clear elbow; sometimes it decreases very gradually, and in those cases, the Elbow method isn't very helpful. ✅",
        "explain_wrong": "The curve does not always have a clear, distinct elbow to identify."
    },
    {
        "q": "Sometimes the number of clusters (K) is chosen based on the downstream purpose of the system, even without using the Elbow method.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True",
        "explain_correct": "Very true! For example, if you are sizing T-shirts, you might choose K=3 to produce (S, M, L) or K=5 to produce (XS, S, M, L, XL) based on your business plan, regardless of the Elbow curve! ✅",
        "explain_wrong": "The business or practical goal often dictates the value of K."
    },
    {
        "q": "If we have K=3, and the training point x^(i) is assigned to the second centroid. What is the value of c^(i)?",
        "type": "mcq",
        "options": ["1", "2", "3", "K"],
        "ans": "2",
        "explain_correct": "Since the point is assigned to the second centroid, its Cluster index c^(i) equals 2. ✅",
        "explain_wrong": "The symbol 'c' represents the index of the centroid to which the point belongs."
    }
]
