# graph = { node: (adjacent_node, adjacent_node) }

# поиск в глубину
def depth_first_search(graph, start_node, visited=None):
    if visited is None:
        visited = list()

    if start_node != visited[-1]:
        visited.append(start_node)

    for next_node in graph[start_node] - set(visited):
        depth_first_search(graph, next_node, visited)

    return visited
