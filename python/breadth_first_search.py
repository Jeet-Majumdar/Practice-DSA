'''
Breadth first search uses Queue to keep track of the nodes to be visited.
BFS is better when target is closer to Source

Breadth-First Search (BFS) Algorithm:

1. Choose a starting vertex, mark it as visited, and add it to a queue (Enqueue operation).
2. While the queue is not empty:
    Dequeue a vertex from the queue and check whether it is the search variable.
    If it is, stop the code and display the predecessor list, else, Enqueue all its adjacent vertices \
    that have not been visited, as well as including them in a predecessor list and a visited list.
3. Repeat step 2 until the queue is empty.

Concise algo:
Queue: [A]  # first entry is the starting point

Dequeue
Is this is goal?
If so, we are done. 
Otherwise:
    Enqueue undiscovered neighbours
    update predecessors 
Repeat until queue is empty
'''

from queue import Queue 

class Graph:
    def __init__(self, nNodes, directed=False):
        self.nNodes = nNodes
        self.directed = directed

        self.edge_list = []
    
    def add_edge(self, node1, node2, weight=1):
        self.edge_list.append([node1, node2, weight])

        if not self.directed:
            self.edge_list.append([node2, node1, weight])
    
    def get_edge_list(self):
        length_of_edge_list = len(self.edge_list)
        for i in range(length_of_edge_list):
            print(f'edge {i+1}    :    {self.edge_list[i]}')
    
    def node_search(self, to_node_number, from_node_number=0):     # Depth-first search
        # Check whether the numbers entered are within the numbers in the Graph.
        if from_node_number >= 0 and to_node_number >= 0 and from_node_number < self.nNodes and to_node_number < self.nNodes:
             pass
        else:
            print('Entered node numbers is/are not a part of the Graph :(')
            return 0
        
        # Do a breadth-first search using queue list
        queue = Queue()
        queue.enqueue(from_node_number)
        predecessors = []
        visited_nodes = []
        found = False
        while (queue.list_size()!=0):
            pop_value = int(queue.dequeue())
            if pop_value == to_node_number:
                visited_nodes.append(pop_value)
                print(f'\n\nFound! Printing the path... \n')
                found = True
                break
            else:
                for edge in self.edge_list:
                    if pop_value == edge[0]:
                        if edge[1] not in visited_nodes and queue.search(edge[1])==False:
                            queue.enqueue(edge[1])
                            predecessors.append((pop_value, edge[1]))
                visited_nodes.append(pop_value)

        if(found==True):
            
            # from predecessors list, analyze the jumps that that make it continuous, and print the path
            
            len_predecessors = len(predecessors)
            path = f'{to_node_number}'
            index = len_predecessors - 1
            flag = False

            while index >= 0:
                if predecessors[index][1] != to_node_number and flag == False:
                    index = index - 1
                    continue
                if flag == False:
                    from_node = predecessors[index][0]
                    path = f'{from_node} --> {path}'
                    flag = True
                
                if from_node == from_node_number:
                    break
                
                if predecessors[index][1] == from_node:
                    from_node = predecessors[index][0]
                    path = f'{from_node} --> {path}'
                
                index = index - 1
            
            print(f'Path:\n     {path}')
            print()
        
        else:
            print('Not found')

        



if __name__=='__main__':
    graph = Graph(10)

    graph.add_edge(1, 4, 1)
    graph.add_edge(3, 6, 1)
    graph.add_edge(4, 5, 1)
    graph.add_edge(4, 7, 1)
    graph.add_edge(5, 6, 1)
    graph.add_edge(5, 8, 1)
    graph.add_edge(6, 9, 1)
    graph.add_edge(7, 8, 1)
    graph.add_edge(8, 9, 1)
    

    graph.get_edge_list()

    start_node = int(input('Enter starting node: '))
    search_item = int(input('Enter ending node: '))

    graph.node_search(search_item, start_node)   # (To, From)
    



