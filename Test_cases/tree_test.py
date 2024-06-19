def is_cyclic_util(v, visited, parent, graph):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            parent[neighbor] = v
            if is_cyclic_util(neighbor, visited, parent, graph):
                return True
        elif parent[v] != neighbor:
            return True

    return False

def is_cyclic(graph):
    vertices = len(graph)
    visited = [False] * vertices
    parent = [-1] * vertices

    for i in range(vertices):
        if not visited[i]:
            if is_cyclic_util(i, visited, parent, graph):
                return True

    return False

def main():
    # Open the file in read mode
    with open("test_cases.txt", "r") as file:
        # Read the first line and split the values
        n, c1, c2 = map(int, file.readline().split())

        # Read the second line and split the values
        milestones = list(map(int, file.readline().split()))

    # Print the read values
    
    graph = []
    for i in range(n+1):
        graph.append([])

    iter = 0
    for i in range(1,n+1):
        if(i!=c1):
            v = milestones[iter]
            iter+=1

            graph[i].append(v)
            graph[v].append(i)
    
    # Check if the graph has a cycle
    if is_cyclic(graph):
        print("Graph contains a cycle.")
    else:
        print("Graph is acyclic.")

if __name__ == "__main__":
    main()
