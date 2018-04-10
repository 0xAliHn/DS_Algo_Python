# O(log(n))
def binarysearch (ar, item):
    if len(ar) == 0:
        return False
    mid = len(ar) // 2
    if ar[mid] == item:
        return True
    if ar[mid] < item:
        return binarysearch(ar[mid + 1:], item)
    elif ar[mid] > item:
        return binarysearch(ar[:mid], item)
    return False


# Test array
arr = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
x = 42

# Function call
result = binarysearch(arr, x)
print(result)
