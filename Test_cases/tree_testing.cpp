#include <iostream>
#include <vector>

using namespace std;

bool isCyclicUtil(int v, vector<bool>& visited, vector<int>& parent, const vector<vector<int>>& graph) {
    visited[v] = true;

    for (int neighbor : graph[v]) {
        if (!visited[neighbor]) {
            parent[neighbor] = v;
            if (isCyclicUtil(neighbor, visited, parent, graph)) {
                return true;
            }
        } else if (parent[v] != neighbor) {
            return true;
        }
    }

    return false;
}

bool isCyclic(const vector<vector<int>>& graph) {
    int vertices = graph.size();
    vector<bool> visited(vertices, false);
    vector<int> parent(vertices, -1);

    for (int i = 0; i < vertices; ++i) {
        if (!visited[i]) {
            if (isCyclicUtil(i, visited, parent, graph)) {
                return true;
            }
        }
    }

    return false;
}

int main() {
    // Example usage:
    // Create a graph and add edges
    vector<vector<int>> graph = {{1, 2}, {0, 2}, {0, 1, 3}, {2, 4}, {3}};

    // Check if the graph has a cycle
    if (isCyclic(graph)) {
        cout << "Graph contains a cycle." << endl;
    } else {
        cout << "Graph is acyclic." << endl;
    }

    return 0;
}
