'''
Implement Queue using a Stack data structure

1. Maintain an auxilury stack along with the main stack
2. For evey entry in the main stack:
    a. pop out all the existing members in the main stack and push them into the auxilury stack
    b. push the item in the main stack
    c. pop and push all the auxilury stack members back into the main stack
3. For every pop in the main stack, just pop out the top of main stack
'''

class QueueUsingStack:
    def __init__(self):
        self.stack = []
        self.aux_stack = []
    
    def insert(self, item):
        if len(self.stack) == 0:
            self.stack.append(item)
            return 
        else:
            while len(self.stack) != 0:
                self.aux_stack.append(self.stack.pop())
            self.stack.append(item)
            while len(self.aux_stack) != 0:
                self.stack.append(self.aux_stack.pop())
            return
    
    def remove(self):
        if len(self.stack) == 0:
            print('Queue empty. Nothing to remove!')
            return -9999999
        return self.stack.pop()
    
    def print_queue(self):
        if len(self.stack) == 0:
            print('Queue empty. Nothing to show!')
            return -9999999
        return str(self.stack)

if __name__ == '__main__':
    q = QueueUsingStack()

    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(4)
    print(q.print_queue())
    q.remove()
    q.remove()
    print(q.print_queue())
