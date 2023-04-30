'''
Binary Tree Heap representation in an array:

Implementations:
For programming language where array index CANNOT be 0:
    Parent of a Node = floor(n/2) = n//2
    If Root = n 
    Left = 2*n
    Right = 2*n + 1

For programming language where array index can be 0:
    Parent of a Node = floor(n-1/2) = (n-1)//2
    If Root = n 
    Left = 2*n + 1
    Right = 2*n + 2

'''

class MaxHeap:
    def __init__(self):
        # The root node will be at locatiton 1.
        # Since it is a max heap, the root node will have the highest value
        self.heap = []
    
    def parent(self, i):
        return (i-1)//2
    
    def insert(self, item):
        # For a node, only its parent is important which can be found at floor(n/2) where n the the location of the child node. 
        self.heap.append(item)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    def remove(self):
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)
        return max_val

    def max_heapify(self, i):
        '''
        1. Start with root node
        2. a. If one of the child node is greater than the parent, we swap 
           b. If both the child nodes is greater than the parent, we swap between the greatest of the two
           c. If no children, there is nothing to be heapified. 
        3. Repeat step 2 going down the heap, until each nodes key must be greater than or equal to its parent
        '''
        left = 2*i + 1
        right = 2*i + 2
        largest = i  # represents parent of left and right
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

class MinHeap:
    def __init__(self):
        # The root node will be at locatiton 1.
        # Since it is a max heap, the root node will have the highest value
        self.heap = []
    
    def parent(self, i):
        return (i-1)//2

    def insert(self, item):
        if len(self.heap) == 0:
            self.heap.append(item)
            return 1
        
        self.heap.append(item)
        i = len(self.heap) - 1
        
        while i > 0:
            if (self.heap[i] < self.heap[self.parent(i)]):
                temp = self.heap[i]
                self.heap[i] = self.heap[self.parent(i)]
                self.heap[self.parent(i)] = temp
                i = self.parent(i)
    
    def remove(self):
        '''
        1. Save the data that is at our root node
        2. Replace the root node with the right most node, on the last level of our tree. 
        3. Call mean_heapify
        '''
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.min_heapify(0)
        return min_val
    
    def min_heapify(self, i):
        '''
        1. Start with root node
        2. a. If one of the child node is smaller than the parent, we swap 
           b. If both the child nodes is smaller than the parent, we swap between the smallest of the two
           c. If no children, there is nothing to be heapified. 
        3. Repeat step 2 going down the heap, until each nodes key must be lesser than or equal to its parent
        '''
        left = 2*i + 1
        right = 2*i + 2
        smallest = i # represents parent of left and right
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)


if __name__ == '__main__':

    print('\n\nTesting MaxHeap')
    heap = MaxHeap()
    heap.insert(6)
    heap.insert(5)
    heap.insert(4)
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    print(heap.heap) 
    print(heap.remove())  
    print(heap.heap) 

    print('\n\nTesting MinHeap')
    heap = MinHeap()
    heap.insert(6)
    heap.insert(5)
    heap.insert(4)
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    print(heap.heap) 
    print(heap.remove())  
    print(heap.heap) 
