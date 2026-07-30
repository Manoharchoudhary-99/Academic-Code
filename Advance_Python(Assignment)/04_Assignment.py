# Fibonacci using Memoization

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Fibonacci using Tabulation

def fibonacci_tab(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Main Program
num = int(input("Enter the value of n: "))

print("Fibonacci using Memoization:", fibonacci_memo(num))
print("Fibonacci using Tabulation :", fibonacci_tab(num))

# Output:
# Enter the value of n: 12
# Fibonacci using Memoization: 144
# Fibonacci using Tabulation : 144