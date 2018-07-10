class PriorityQueue:
    def __init__(self):
        self.qlist = []

    # O(logn)
    def insert(self, i, p):
        if len(self.qlist) == 0:
            return self.qlist.append((i, p))
        for j in range(len(self.qlist)):
            if self.qlist[j][1] > p:
                return self.qlist.insert(j, (i, p))
        return self.qlist.append((i, p))

    # O(1)
    def pop(self):
        if len(self.qlist) == 0:
            return "Queue Empty"
        else:
            return self.qlist.pop(0)

    def peek(self):
        if len(self.qlist) == 0:
            return "Queue Empty"
        else:
            return self.qlist[0]

    def __repr__(self):
        return str(self.qlist)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(('John', 'flu'), 1)
    pq.insert(('Sally', 'cut on arm'), 3)
    print(pq)
    print(pq.pop())
