import numpy as np 

graph = {0: [1,4], 1: [2,3], 2:[3], 3:[0], 4:[1], 5:[4]}

def bfs(graph, start):
    visited = set()
    queue = []

    dist = [np.inf for i in graph.keys()]
    parent = [None for i in graph.keys()]

    visited.add(start)
    queue.append(start)
    dist[start] = 0

    while queue:
        node = queue.pop(0)

        for u in graph[node]:

            if u not in visited:
                visited.add(u)
                queue.append(u)
                dist[u] = dist[node] +1
                parent[u] = node

    return dist

print(bfs(graph, 5))