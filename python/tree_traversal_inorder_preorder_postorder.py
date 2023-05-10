'''
5 + 4 = Left + Root + Right
In-order = Left, Root, Right
Pre-order: Root, Left, Right
Post-order: Left, Right, Root

This code just binds the in-order, pre-order, and post-order with the MaxHeap class
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

    def in_order(self, arr, i=0):
        if i < len(arr):
            value_at_i = arr[i]
            left = 2 * i + 1
            right = 2 * i + 2
            self.in_order(arr, left)
            print(f'{value_at_i}', end='  ')
            self.in_order(arr, right)
    
    def pre_order(self, arr, i=0):
        if i < len(arr):
            value_at_i = arr[i]
            left = 2 * i + 1
            right = 2 * i + 2
            print(f'{value_at_i}', end='  ')
            self.pre_order(arr, left)
            self.pre_order(arr, right)
    
    def post_order(self, arr, i=0):
        if i < len(arr):
            value_at_i = arr[i]
            left = 2 * i + 1
            right = 2 * i + 2
            self.post_order(arr, left)
            self.post_order(arr, right)
            print(f'{value_at_i}', end='  ')

if __name__ == '__main__':

    print('\n\nTesting MaxHeap')
    heap = MaxHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    print(heap.heap) 
    heap.in_order(heap.heap)
    print() 
    heap.pre_order(heap.heap) 
    print() 
    heap.post_order(heap.heap) 
 
