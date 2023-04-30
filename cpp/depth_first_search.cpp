/*

Depth first search uses stack to keep track of the nodes to be visited.
DFS is better when target is far from source

Depth first search (DFS) algorithms:
1. Start by pushing starting vertex of the graph into the stack
2. Pop the top item of the stack and add it to the visited list
3. Check whether the popped item is the search item. If it is stop. Else proceed to next step
4. Add the non-visited neighbours of the popped item and add them in the stack. Add the neighbour along with the popped item to a predecessor list too. This will be helpful to keep track of the search path
5. Keep repeating steps 2 to 5 until the stack is empty

*/

#include <iostream>
#include <vector>

using namespace std;

vector<int> adj_list[100005];
bool visited[100005];

void dfs(int node) {
    visited[node] = true;
    cout << node << " ";

    for (int neighbor : adj_list[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor);
        }
    }
}

int main() {
    int num_nodes, num_edges;
    cin >> num_nodes >> num_edges;

    for (int i = 0; i < num_edges; i++) {
        int node1, node2;
        cin >> node1 >> node2;
        adj_list[node1].push_back(node2);
        adj_list[node2].push_back(node1); // graph is undirected
    }

    int start_node;
    cin >> start_node;

    dfs(start_node);

    return 0;
}
