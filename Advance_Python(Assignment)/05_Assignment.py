def find_lcs(s1, s2):
    x = len(s1)
    y = len(s2)

    lcs_table = [[0] * (y + 1) for _ in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    i, j = x, y
    ans = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans.append(s1[i - 1])
            i -= 1
            j -= 1
        elif lcs_table[i][j - 1] > lcs_table[i - 1][j]:
            j -= 1
        else:
            i -= 1

    ans.reverse()
    return "".join(ans), lcs_table[x][y]


first = input("Enter the first sequence: ")
second = input("Enter the second sequence: ")

subsequence, length = find_lcs(first, second)

print("\nLongest Common Subsequence:", subsequence)
print("Length of LCS:", length)

# comment

# Enter the first sequence: Rohit
# Enter the second sequence: Virat

# Longest Common Subsequence: it
# Length of LCS: 2