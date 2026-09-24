def fibonacci(n):
    if n <= 0:
        return []

    dp = [0] * n

    dp[0] = 0

    if n > 1:
        dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


n = int(input("Enter the number of terms: "))

result = fibonacci(n)

print("Fibonacci Sequence:")
print(*result)


# Fibonacci Sequence:
# 0 1 1 2 3 5 8 13 21 34