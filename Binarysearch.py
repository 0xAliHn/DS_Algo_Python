# Returns index of x in arr if present, else -1
def binarySearch (arr, x):
    if len(arr) == 0:
        return False
    mid = len(arr)//2
    if arr[mid] == x:
        return True
    if arr[mid] < x:
        return binarySearch(arr[mid+1:], x)
    elif arr[mid] > x:
        return binarySearch(arr[:mid], x)
    return False


# Test array
arr = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
x = 42

# Function call
result = binarySearch(arr, x)
print(result)
