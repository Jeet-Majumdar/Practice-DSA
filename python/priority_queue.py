import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return not self.elements
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self):
        return str(self.elements)


if __name__ == '__main__':
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # item, priority
    pq.put('play', 4)
    pq.put('sleep', 2)
    pq.put('dance', 3)
    pq.put('study', 1)
    pq.put('code', 6)
    pq.put('eat', 5)
    pq.put('read', 7)
    print(pq)

    print(pq.get())
    print(pq.get())
    print(pq.get())
    print(pq.get())
    print(pq)

