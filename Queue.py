class queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.insert(0, val)

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


if __name__ == "__main__":
    myqueue = queue()
    myqueue.enqueue(10)
    print("Size = ", myqueue.size())
    myqueue.enqueue(9)
    print("Size = ", myqueue.size())
    myqueue.enqueue(15)
    print("Size = ", myqueue.size())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.peek())
    print(myqueue.dequeue())
    print(myqueue.is_empty())
