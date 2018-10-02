# Important References
# https://www.geeksforgeeks.org/heap-sort/


# To heapify subtree rooted at index i.
# n is size of heap O(logn)
def heapify(heap, heap_size, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < heap_size and heap[i] < heap[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < heap_size and heap[largest] < heap[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, heap_size, largest)


# Build a maxheap O(nlogn)
def build_max_heap(heap):
    heap_size = len(heap)

    # As last parent is length-1/2 (means i-1/2) need to divide by 2
    for i in range(heap_size - 1 // 2, -1, -1):
        heapify(heap, heap_size, i)


# The main function to sort an array of given size
# O(nlogn)
def heapsort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1

    # One by one extract elements and decrement size
    for i in range(heap_size, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, i, 0)


if __name__ == "__main__":
    arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    heapsort(arr)
    print("Sorted array is", *arr)
