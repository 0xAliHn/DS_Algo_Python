class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def insertnode(root, val):
    while root:
        if val > root.val:
            if root.right is not None:
                root = root.right
            else:
                root.right = Node(val)
                root = root.right
        elif val < root.val:
            if root.left is not None:
                root = root.left
            else:
                root.left = Node(val)
                root = root.left
        else:
            return root


def searchnode(root, val):
    while root:
        if val > root.val:
            if root.right is not None:
                root = root.right
            else:
                return None
        elif val < root.val:
            if root.left is not None:
                root = root.left
            else:
                return None
        else:
            return root


if __name__ == "__main__":
    # Let us create the following BST
    #       10
    #    /      \
    #    5      14
    #   / \    / \
    #   2 8   13 17

    root = Node(10)
    root.left = Node(5)
    root.right = Node(14)
    root.left.left = Node(2)
    root.left.right = Node(8)
    root.right.left = Node(13)
    root.right.right = Node(17)

    print(insertnode(root, 6).val)
    root = searchnode(root, 8)

    if root is not None:
        print(root.val)
    else:
        print(None)
