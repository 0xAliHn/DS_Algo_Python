# A naive recursive approach
# O(2*n)
def LCS(X, Y, i, j):
    if i >= len(X) or j >= len(Y):
        return 0

    if X[i] == Y[j]:
        return 1 + LCS(X, Y, i + 1, j + 1)
    else:
        return max(LCS(X, Y, i + 1, j), LCS(X, Y, i, j + 1))


# Tabulation/bottom-up approach
# O(m*n)
def LCS1(X, Y):
    m = len(X)
    n = len(Y)
    mem = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                mem[i][j] = 1 + mem[i - 1][j - 1]
            else:
                mem[i][j] = max(mem[i - 1][j], mem[i][j - 1])

    # Print the LCS string
    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs += X[i - 1]
            i -= 1
            j -= 1
        elif mem[i - 1][j] > mem[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(lcs[::-1])
    return mem[m][n]


X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", LCS(X, Y, 0, 0))
print("Using Tabulation Length of LCS is ", LCS1(X, Y))
