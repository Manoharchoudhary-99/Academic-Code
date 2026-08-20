# 0/1 Knapsack Problem using Dynamic Programming

# Bottom-Up Approach
def knapsack_bottom_up(weight, value, capacity):
    n = len(weight)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weight[i - 1] <= w:
                include = value[i - 1] + dp[i - 1][w - weight[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weight[i - 1]

    selected.reverse()

    return dp[n][capacity], selected


# Top-Down Approach
def knapsack_top_down(weight, value, capacity):
    n = len(weight)

    # Memoization table
    memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

    def solve(i, w):

        if i == 0 or w == 0:
            return 0

        if memo[i][w] != -1:
            return memo[i][w]

        if weight[i - 1] > w:
            memo[i][w] = solve(i - 1, w)

        else:
            include = value[i - 1] + solve(
                i - 1, w - weight[i - 1]
            )

            exclude = solve(i - 1, w)

            memo[i][w] = max(include, exclude)

        return memo[i][w]

    maximum_value = solve(n, capacity)

    # Find selected items
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if solve(i, w) != solve(i - 1, w):
            selected.append(i)
            w -= weight[i - 1]

    selected.reverse()

    return maximum_value, selected


# Main Program
weights = [2, 3, 4, 5]
values = [15, 20, 30, 40]
capacity = 7

print("0/1 KNAPSACK PROBLEM")
print("--------------------")

print("\nItems:")
for i in range(len(weights)):
    print("Item", i + 1,
          ": Weight =", weights[i],
          ", Value =", values[i])

print("\nKnapsack Capacity:", capacity)

# Bottom-Up
max_value1, items1 = knapsack_bottom_up(
    weights, values, capacity
)

print("\n--- Bottom-Up Approach ---")
print("Maximum Value:", max_value1)
print("Selected Items:", items1)

# Top-Down
max_value2, items2 = knapsack_top_down(
    weights, values, capacity
)

print("\n--- Top-Down Approach ---")
print("Maximum Value:", max_value2)
print("Selected Items:", items2)