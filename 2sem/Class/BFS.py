graph = {0: [1,4], 1: [2,3], 2:[3], 3:[0], 4:[1]}

def bfs(graph, start):
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

bfs(graph,0)