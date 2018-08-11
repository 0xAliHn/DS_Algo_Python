# Important References
# https://www.geeksforgeeks.org/the-ubiquitous-binary-search-set-1/


# time O(logn) space O(logn)
def binarysearch(ar, item):
    if len(ar) == 0:
        return False
    mid = len(ar) // 2
    if ar[mid] == item:
        return True
    if ar[mid] < item:
        return binarysearch(ar[mid + 1:], item)
    else:
        return binarysearch(ar[:mid], item)


# time O(log(n)) space O(1)
def binarysearch_optimize(ar, l, r, item):
    while l <= r:
        m = (l + r) // 2
        if ar[m] == item:
            return m
        elif ar[m] < item:
            l = m + 1
        else:
            r = m - 1

    return -1


# time O(log(n)) space O(1)
def binarysearch_more_optimize(ar, l, r, item):
    while r - l > 1:
        m = l + (r - l) // 2
        if ar[m] <= item:
            l = m
        else:
            r = m

    if arr[l] == item:
        return l
    else:
        return -1


# Test array
arr = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
x = 87

# Function call
result = binarysearch(arr, x)
print(result)

result = binarysearch_more_optimize(arr, 0, len(arr) - 1, x)
print(result)

