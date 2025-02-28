# G = {0: [1,4], 1: [2,3], 2:[3], 3:[0], 4:[1], 5:[4]}
# G = {
#     0: [(1, 1), (4, 1)],
#     1: [(2, 1), (3, 1)],
#     2: [ (3, 1)],
#     3: [ (0, 1)],
#     4: [ (1, 1)],
#     5: [(4, 1)]
# }

G = {
    0: [(1, 1), (2, 2)],
    1: [(3, 7), (2, 10)],
    2: [ (4, 5)],
    3: [ (0, 3),(5,6)],
    4: [ (5, 2)],
    5: [(0, 4)]
}

def Prim(G):
    MST = []
    V = len(G.keys())
    dist = [float('inf')] * V
    dist[0] = 0
    prev = [None] * V
    S = set()
    while len(S) != V:
        v = min((d, i) for i, d in enumerate(dist) if i not in S)[1]
        S.add(v)
        # print(S)
        if prev[v] is not None:
            MST.append([prev[v],v])
        for u, w in G[v]:
            if u not in S and dist[u]> w: 
                prev[u] = v
                dist[u]= w

        dist[v] = float('inf')
    return MST
print(Prim(G))


