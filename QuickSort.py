# RC: O(nlogn) WC: O(n2)
def quick_sort(ar):
    if len(ar) <= 1:
        return ar
    else:
        pivot = ar[-1]

    left = []
    right = []
    pivot_list = []

    for i in range(len(ar)):
        if ar[i] < pivot:
            left.append(ar[i])
        elif ar[i] > pivot:
            right.append(ar[i])
        else:
            pivot_list.append(ar[i])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + pivot_list + right


arr = [10, 80, 30, 90, 40, 50, 70]

result = quick_sort(arr)
print(result)
