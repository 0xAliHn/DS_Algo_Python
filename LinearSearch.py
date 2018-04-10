# O(n)
def linearsearch(ar, item):
    for i in range(len(ar)):
        if ar[i] == item:
            return True

    return False


# Test array
arr = [10, 2, 38, 55, 8, 22, 34, 4, 87, 100]
x = 40

# Function call
result = linearsearch(arr, x)
print(result)
