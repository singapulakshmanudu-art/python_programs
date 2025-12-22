graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Keep track of visited nodes
    visited.add(node)
    print(node, end=" ")  # Visit the node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
dfs(graph, 'A')
