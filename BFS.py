class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, node):
        self.queue.insert(0, node)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def bfs():
    while not queue.is_empty():
        root = queue.dequeue()
        print(root.val)
        if root.left is not None:
            queue.enqueue(root.left)
        if root.right is not None:
            queue.enqueue(root.right)


if __name__ == "__main__":
    queue = Queue()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    queue.enqueue(root)
    bfs()
