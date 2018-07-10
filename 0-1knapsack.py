# Tabulation or Bottom-up approach
# O(n)


def knapsack(m, wt, cost, n):
    # v = [[0]*(m+1)]*(n+1)
    v = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, m + 1):
            if wt[i] <= w:
                v[i][w] = max(v[i - 1][w], cost[i] + v[i - 1][w - wt[i]])
            else:
                v[i][w] = v[i - 1][w]
    print(v[i][w])

    for i in range(n, 0, -1):
        if v[i][w] != v[i - 1][w]:
            print(i)
            w = w - wt[i]


cost = [0, 60, 100, 120]
wt = [0, 10, 20, 30]
m = 50
n = len(cost) - 1
knapsack(m, wt, cost, n)
