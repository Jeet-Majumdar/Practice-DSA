'''

A* algorithm
To find the shortest path from one point in space to another point.
Calculates the cost of every node (f-values) by adding two quantities: f-values = g-values and h-values
g-values is the cost of moving to a certain node from starting point. Essentially the more the number of nodes in between this node and starting point, the more is the cost. 
h-values is the heuristic cost. This is an estimate how much is left from the current node to the end node. This is an estimate. So can be approximated with taxicab distance or euclidean distance formula for two given coordinates in space
Uses a priority queue containing f-values and (i, j) tuples along with dictionaries for predecessors and g-values. 

PR: [(Cell, F-value)]

Get highest priority item from 
PQ (min F-value):
Is it the goal?
If so, we are done
Otherwise:
    find undiscovered neighbours 
    calculate f-values of undiscovered neighbours
    put these undiscovered neighbours along with their f-values in the PQ 
    update predecessors. 
Repeat until queue is empty
'''

from priority_queue import PriorityQueue

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def read_maze(file_name):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze
    except IOError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path

def heuristic(a, b):
    '''
    Calculates the Manhattan distance between the two pair of grid coordinates
    '''
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}

    while not pq.is_empty():
        
        current_cell = pq.get()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in g_values:
                new_cost = g_values[current_cell] + 1
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
    return None


if __name__ == '__main__':
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    print(result) # [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
