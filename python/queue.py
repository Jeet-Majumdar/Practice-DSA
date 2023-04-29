class Node:
    def __init__(self, data, addressL=None, addressR = None):
        self.data = data
        self.addressL = addressL
        self.addressR = addressR
    
    def set_addressL(self, addressL):
        self.addressL = addressL
    def set_addressL(self, addressR):
        self.addressR = addressR
    def get_addressL(self):
        return self.addressL
    def get_addressR(self):
        return self.addressR

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, data):
        if self.size == 0:
            new_node = Node(data)
            self.tail = new_node
            self.head = new_node
            self.size = 1
            #print(f'Item successfully inserted!\tList size: {self.size}')
        else:
            tail = self.tail
            new_node = Node(data=data)
            new_node.addressL = tail
            tail.addressR = new_node
            self.tail = new_node
            self.size = self.size + 1
            #print(f'Item successfully inserted!\tList size: {self.size}')
    
    def dequeue(self):
        if self.size == 0:
            #print('Error: Empty linked list. Nothing to pop.')
            return -9999999
        elif self.size == 1:
            data = self.head.data
            nodeObj = self.head
            self.head = None
            self.tail = None 
            self.size = 0
            del nodeObj
            return data 
        else:
            current_head = self.head
            current_head_data = self.head.data
            address_of_head = self.head.addressR
            self.head = address_of_head
            self.size = self.size - 1
            del current_head 
            return current_head_data
    
    def list_size(self):
        return int(self.size)
    
    def search(self, data):
        if self.size == 0:
            #print('No node in list. Nothing to print!')
            return False
        else:
            head = self.head
            found = False
            while(head != None):
                if head.data == data:
                    found = True
                head = head.addressR
            return found
    
    def print_list(self):
        if self.size == 0:
            #print('No node in list. Nothing to print!')
            return -9999999
        head = self.head
        while(head != None):
            print(head.data)
            head = head.addressR
    
    def get_head_data(self):
        if self.size == 0:
            #print('Error: No node in list')
            return -9999999
        else:
            #print({self.head.data})
            return {self.head.data}
    
    def get_tail_data(self):
        if self.size == 0:
            #print('Error: No node in list')
            return -9999999
        else:
            #print({self.tail.data})
            return {self.tail.data}


if __name__ == '__main__':

    list = Queue()

    while(True):
        print('------------------')
        print('Options:\n1. Enqueue item \n2. Dequeue item \n3. Show list \n4. Get head data \n5. Get tail data \n6. Get Queue size \n7. Search item')
        print('------------------')
        user_in = int(input('Enter option: '))
        if user_in == 1:
            user_in_data = int(input('Enter data to push: '))
            list.enqueue(user_in_data)
        elif user_in == 2:
            popitem = list.dequeue()
            if popitem == -9999999:
                print('Error: Empty Queue list. Nothing to pop.')
            else:
                print(f'Popped value: {popitem:05d}\t List size: {list.size}')
        elif user_in == 3:
            list.print_list()
        elif user_in == 4:
            list.get_head_data()
        elif user_in == 5:
            list.get_tail_data()
        elif user_in == 6:
            size = list.list_size()
            print(f'List size: {size}')
        elif user_in == 7:
            if list.size != 0:
                found_or_not = int(input('Enter item to search: ')) 
                print(list.search(found_or_not))
            else:
                print('Empty queue. Nothing to search here!')
        else:
            print('Error: Enter a valid integer!')
