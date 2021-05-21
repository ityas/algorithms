# graph = { node: (adjacent_node, adjacent_node) }

# поиск в глубину
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = list()

    if start_node not in visited:
        visited.append(start_node)

    for next_node in graph[start_node] - set(visited):
        dfs(graph, next_node, visited)

    return visited
