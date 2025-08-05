def DFS(graph,start_node):
    visited_nodes = set()  # empty set
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited_nodes:
            print(node, end=" ")
            visited_nodes.add(node)

            for neighbour in reversed(graph[node]):
                if neighbour not in visited_nodes:
                    stack.append(neighbour)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS traversal starting from node A:")
DFS(graph, 'A')