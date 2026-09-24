def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


n = int(input("Enter the number of terms: "))

print("Fibonacci Sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")


# Fibonacci Sequence:
# 0 1 1 2 3 5 8 13 21 34