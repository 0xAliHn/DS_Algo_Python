# O(nlogn)
def merge(left, right):
    lis = []
    li, ri = 0, 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            lis.append(left[li])
            li += 1
        else:
            lis.append(right[ri])
            ri += 1

    if li == len(left):
        lis.extend(right[ri:])

    if ri == len(right):
        lis.extend(left[li:])

    return lis


def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])

    return merge(left, right)


arr = [4, 14, 7, 16, 10, 9, 3]
n = len(arr)

result = merge_sort(arr)
print(result)
