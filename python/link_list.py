class Node:
    def __init__(self, data, address=None):
        self.data = data
        self.address = address
    
    def set_address(self, address):
        self.address = address
    
    def get_address(self):
        return self.address

class LinkedList:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        if self.size == 0:
            new_node = Node(data)
            self.top = new_node
            self.size = 1
            print(f'Item successfully inserted!\tList size: {self.size}')
        else:
            top = self.top
            new_node = Node(data=data, address=top)
            self.top = new_node
            self.size = self.size + 1
            print(f'Item successfully inserted!\tList size: {self.size}')
    
    def pop(self):
        if self.size == 0:
            #print('Error: Empty linked list. Nothing to pop.')
            return -9999999
        else:
            current_top = self.top
            current_top_data = self.top.data
            address_of_top = self.top.address
            self.top = address_of_top
            self.size = self.size - 1
            del current_top
            return current_top_data
    
    def print_list(self):
        if self.size == 0:
            print('No node in list. Nothing to print!')
            return -9999999
        top = self.top
        print()
        while(top != None):
            print(f'{top.data}', end=' ')
            top = top.address
        print()
    
    def get_top(self):
        if self.size == 0:
            print('Error: No node in list')
        else:
            print(f'Top data = {self.top.data}')
    

    def bubble_sort_link_list_by_data(self):
        if self.size == 0:
            print('Error: No node in list')

        # Sort using bubble sort with data replacement
        i = self.top
        while i.address != None:
            j = self.top
            while j.address != None:
                if j.data > j.address.data:
                    value = j.data
                    j.data = j.address.data
                    j.address.data = value
                j = j.address
            i = i.address
        # print sorted linklist
        self.print_list()
    
    def bubble_sort_link_list_by_link(self):
        if self.size == 0:
            print('Error: No node in list')

        # Sort using bubble sort with link replacement
        i = self.size
        while i != 0:
            j = self.top
            previousNode = None
            while j.address != None:
                if j.data > j.address.data:
                    if j == self.top:
                        self.top = j.address
                        previousNode = None
                    else:
                        previousNode.address = j.address
                    store_second_address = j.address 
                    j.address = store_second_address.address 
                    store_second_address.address = j
                    j = store_second_address
                else:
                    previousNode = j
                    j = j.address
            
            i = i - 1
        # print sorted linklist
        self.print_list()

if __name__ == '__main__':

    list = LinkedList()

    while(True):
        print('------------------')
        print('Options:\n1. Push item \n2. Pop item \n3. Show list \n4. Get top data\n5. Sort list')
        print('------------------')
        user_in = int(input('Enter option: '))
        if user_in == 1:
            user_in_data = int(input('Enter data to push: '))
            list.push(user_in_data)
        elif user_in == 2:
            popitem = list.pop()
            if popitem == -9999999:
                print('Error: Empty linked list. Nothing to pop.')
            else:
                print(f'Popped value: {popitem:05d}\t List size: {list.size}')
        elif user_in == 3:
            list.print_list()
        elif user_in == 4:
            list.get_top()
        elif user_in == 5:
            list.bubble_sort_link_list_by_link()
        else:
            print('Error: Enter a valid integer!')

