class Stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def dfs(root):
    if root:
        mystack.push(root.val)
        print(mystack.pop())
        dfs(root.left)
        dfs(root.right)


if __name__ == "__main__":
    mystack = Stack()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    dfs(root)
