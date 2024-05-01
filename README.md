**Description:**
This repository contains Python code for solving the knapsack problem using various algorithms. We have implemented two approaches for the 0/1 knapsack problem: brute force and dynamic programming. Additionally, we have included an implementation for the fractional knapsack problem using the greedy algorithm. These algorithms were applied to a dataset representing a restaurant inventory consisting of 798 elements.

**Algorithms Implemented:**

1. **Brute Force:** This approach involves checking every possible combination of items to find the optimal solution. While it provides accurate results, it can be inefficient for large datasets due to its exponential time complexity.
2. **Dynamic Programming:** Dynamic programming optimizes the brute force approach by storing solutions to overlapping subproblems, leading to a more efficient solution. It has a time complexity of O(nW), where n is the number of items and W is the capacity of the knapsack.
3. **Greedy (Fractional Knapsack):** The greedy approach selects items based on their value-to-weight ratio, adding as much of each item as possible until the knapsack is full. While not always providing the optimal solution for the 0/1 knapsack, it does for the fractional knapsack, and it has a time complexity of O(n log n).

****Dataset:**
The restaurant inventory dataset used in this project is taken from Kaggle and it consists of 798. Each element represents an item in the inventory, including its weight, Unit Price, and other relevant information. This dataset serves as the input for testing the knapsack algorithms.
