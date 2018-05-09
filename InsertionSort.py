# O(n2)
arr = [3, 9, 6, 5, 7]
n = len(arr)

for i in range(1, n):
    item = arr[i]
    j = i-1
    while j >= 0 and arr[j] > item:
            arr[j+1] = arr[j]
            j = j-1
    arr[j+1] = item

print(arr)


