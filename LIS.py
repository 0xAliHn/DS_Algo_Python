# Important References
# https://www.geeksforgeeks.org/longest-increasing-subsequence/
# https://www.youtube.com/watch?v=E6us4nmXTHs     //For finding length
# https://www.youtube.com/watch?v=SZByPn0deMY     //For printing sequence
# https://www.youtube.com/watch?v=S9oUiVYEq7E     //For nlogn solution
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/


# Tabulation/bottom-up approach
# O(n*n)
def LIS(arr):
    global i
    arrlen = len(arr)
    length = [1] * arrlen
    slist = [[i] for i in arr]

    for i in range(1, arrlen):
        for j in range(i):
            if arr[i] > arr[j] and length[i] < length[j] + 1:
                length[i] = max(length[i], length[j] + 1)
                slist[i] = slist[j] + [arr[i]]

    # Print the subsequence
    print(slist[i])

    return length[i]


# Binary Search
# O(nlogn)
def lis_otimize(arr):
    size = len(arr)

    temp = [0 for _ in range(size + 1)]

    increasingSub = [-1 for _ in range(size + 1)]

    length = 0
    for i in range(1, size):

        if arr[i] < arr[temp[0]]:

            # new smallest value
            temp[0] = i

        elif arr[i] > arr[temp[length]]:

            # arr[i] wants to extend
            # largest subsequence
            increasingSub[i] = temp[length]
            temp[length + 1] = i
            length += 1

        else:

            # arr[i] wants to be a
            # potential condidate of
            # future subsequence
            # It will replace ceil
            # value in temp
            pos = FindIndex(arr, temp, -1,
                            length, arr[i])

            increasingSub[i] = temp[pos - 1]
            temp[pos] = i

    print(temp)
    print(increasingSub)
    i = temp[length]
    while i >= 0:
        print(arr[i], " ", end="")
        i = increasingSub[i]
    print()

    return length + 1


# Binary search
def FindIndex(arr, T, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if arr[T[m]] <= key:
            l = m
        else:
            r = m

    return r


arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("1. Length of lis is", LIS(arr))
print("2. Length of lis is", lis_otimize(arr))

