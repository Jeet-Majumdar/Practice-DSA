/*

Breadth first search uses Queue to keep track of the nodes to be visited.
BFS is better when target is closer to Source

Breadth-First Search (BFS) Algorithm:

1. Choose a starting vertex, mark it as visited, and add it to a queue (Enqueue operation).
2. While the queue is not empty:
    Dequeue a vertex from the queue and check whether it is the search variable.
    If it is, stop the code and display the predecessor list, else, Enqueue all its adjacent vertices \
    that have not been visited, as well as including them in a predecessor list and a visited list.
3. Repeat step 2 until the queue is empty.

*/

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> adj_list[100005];
bool visited[100005];

void bfs(int start_node) {
    queue<int> q;
    visited[start_node] = true;
    q.push(start_node);

    while (!q.empty()) {
        int curr_node = q.front();
        q.pop();
        cout << curr_node << " ";

        for (int neighbor : adj_list[curr_node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
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

    bfs(start_node);

    return 0;
}
