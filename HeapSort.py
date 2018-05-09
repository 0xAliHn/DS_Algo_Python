# To heapify subtree rooted at index i.
# n is size of heap
def heapify(heap, heap_size, i):
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < heap_size and heap[i] < heap[l]:
        largest = l
    else:
        largest = i

    # See if right child of root exists and is
    # greater than root
    if r < heap_size and heap[largest] < heap[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]  # swap
        # Heapify the root.
        heapify(heap, heap_size, largest)


# Build a maxheap.
def build_max_heap(heap):
    heap_size = len(heap)

    for i in range(heap_size//2, -1, -1):
        heapify(heap, heap_size, i)


# The main function to sort an array of given size
def heapsort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1

    # One by one extract elements
    for i in range(heap_size, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]  # swap
        heapify(heap, i, 0)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heapsort(arr)
    print("Sorted array is", *arr)

