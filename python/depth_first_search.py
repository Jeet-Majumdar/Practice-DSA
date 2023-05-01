'''
Depth first search uses stack to keep track of the nodes to be visited.
DFS is better when target is far from source

Depth first search (DFS) algorithms:
1. Start by pushing starting vertex of the graph into the stack
2. Pop the top item of the stack and add it to the visited list
3. Check whether the popped item is the search item. If it is stop. Else proceed to next step
4. Add the non-visited neighbours of the popped item and add them in the stack. Add the neighbour along with the popped item to a predecessor list too. This will be helpful to keep track of the search path
5. Keep repeating steps 2 to 5 until the stack is empty

Concise algo:
Stack: [A] # first entry is the starting point

Pop
Is this is goal?
If so, we are done. 
Otherwise:
    push undiscovered neighbours
    update predecessors 
Repeat until stack is empty
'''
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
        
        # Do a depth-first search using stack list

        stack = [from_node_number]
        predecessors = []
        visited_nodes = []
        found = False
        while (len(stack)!=0):
            pop_value = stack.pop()
            
            if pop_value == to_node_number:
                visited_nodes.append(pop_value)
                print(f'\n\nFound! Printing the path... \n')
                found = True
                break
            else:
                for edge in self.edge_list:
                    if pop_value == edge[0]:
                        if edge[1] not in visited_nodes and edge[1] not in stack:
                            stack.append(edge[1])
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
    



