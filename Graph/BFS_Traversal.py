from collections import deque

def bfs(graph, start_node):
    visited_nodes = set()
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited_nodes:
            print(node, end=" ")
            visited_nodes.add(node)
            for neighbors in graph[node]:
                if neighbors not in visited_nodes:
                    queue.append(neighbors)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F
#        \
#         F


print("BFS traversal starting from node A:")
bfs(graph, 'A')