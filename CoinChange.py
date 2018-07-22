# We can implement coin change problem using both dp mechanism
# 1. Optimal substructures
# 2. Overlapping subproblems (3 approach)


# Find the minimum coin required to make the value and print items index
# This solution using Optimal substructures O(n * m)
def coin_change1(coin, n, m):
    coin_index = 0
    j = 0
    c = [0 for _ in range(m + 1)]
    s = [0 for _ in range(m + 1)]

    if m == 0:
        return 0

    for j in range(1, m + 1):
        min = 999999999
        for i in range(1, n):
            if coin[i] <= j:
                if 1 + c[j - coin[i]] < min:
                    min = 1 + c[j - coin[i]]
                    coin_index = i
        c[j] = min
        s[j] = coin_index

    # Print the items index
    while m > 0:
        print(coin[s[m]])
        m = m - coin[s[m]]

    return c[j]


# Find number of ways to make the value (Two approaches)
# This solution using Overlapping subproblems (Tabulation/Bottom-up and Recursive with state)
# Tabulation/Bottom-up  O(n * m)
def coin_change2(coin, n, m):
    # v = [[0]*(m+1)]*(n+1)
    v = [[0 for c in range(m + 1)] for r in range(n)]

    if n == 0 and m == 0:
        return 0
    elif m == 0:
        return 1

    i, j = 0, 0

    for i in range(1, n):
        v[i][0] = 1

    for i in range(1, n):
        for j in range(1, m + 1):
            if j - coin[i] >= 0:
                v[i][j] = v[i][j - coin[i]] + v[i - 1][j]
            else:
                v[i][j] = v[i - 1][j]

    return v[i][j]


# Optimized space complexity to O(n)
def coin_change3(coin, n, m):
    v = [0 for i in range(m + 1)]

    v[0] = 1

    for i in range(1, n):
        for j in range(coin[i], m + 1):
            v[j] += v[j - coin[i]]

    return v[m]


coin = [0, 1, 2, 5]
n = len(coin)
m = 6
print(coin_change1(coin, n, m))
print(coin_change2(coin, n, m))
print(coin_change3(coin, n, m))
