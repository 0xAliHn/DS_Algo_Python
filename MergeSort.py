# O(nlogn)
def merge_sort(arr, l, r):
    print(arr)
    if len(arr) <= 1:
        return arr







arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

merge_sort(arr, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i]),
