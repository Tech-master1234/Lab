graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],  # Add 'E' to the graph with an empty list of neighbors
    'F': [],  # Add 'F' to the graph with an empty list of neighbors
}


visited = []  # List to keep track of visited nodes
queue = []  # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Driver code
bfs(visited, graph, 'A')
