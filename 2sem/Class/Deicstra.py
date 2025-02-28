graph = {0: [1,4], 1: [2,3], 2:[3], 3:[0], 4:[1], 5:[4]}

def Dijkstra(graph,s):
    V = len(graph.keys())
    dist = [float('inf') for i in range(V)]
    prev = [None for i in range (V)]
    dist[s] = 0
    S = set()
    while len (S) < V:
        v = dist.index(min (dist))
        S.add(v)
        dist[v] = float('inf')
        for u,w in graph[v]:
            if int(u) not in S and dist[int(u)]> dist[int(v)] + int(w):
                prev[u] = v
                dist[u]= dist[v] + w
    return dist

Dijkstra(graph,0)