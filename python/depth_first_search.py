
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
                print(f'\n\nFound! Printing the path... ', end='  ')
                found = True
                break
            else:
                count = 0
                for edge in self.edge_list:
                    if pop_value == edge[0]:
                        if edge[1] not in visited_nodes:
                            stack.append(edge[1])
                            predecessors.append((pop_value, edge[1]))
                visited_nodes.append(pop_value)

        if(found==True):
            print(visited_nodes)



if __name__=='__main__':
    graph = Graph(6)

    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 1)
    graph.add_edge(4, 2, 1)
    graph.add_edge(4, 3, 1)
    graph.add_edge(3, 5, 1)

    graph.get_edge_list()

    start_node = int(input('Enter starting node: '))
    search_item = int(input('Enter ending node: '))

    graph.node_search(search_item, start_node)   # (To, From)
    



