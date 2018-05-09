class stack(object):
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


if __name__ == "__main__":
    mystack = stack()
    mystack.push(10)
    print("Size = ", mystack.size())
    mystack.push(9)
    print("Size = ", mystack.size())
    mystack.push(15)
    print("Size = ", mystack.size())
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.peek())
    print(mystack.pop())
    print(mystack.is_empty())
