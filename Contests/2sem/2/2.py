t = int(input())
result =[]
for r in range(t):
    n =int(input())
    G ={}
    coordinates = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        coordinates.append((x,y))
    for i in range(n):
        G[i] = []
        for j in range(n):
            if i == j:
                G[i].append(float('inf'))
            else:
                x1,y1 =coordinates[i]
                x2,y2 =coordinates[j]
                distance =((x1-x2)**2 +(y1-y2)**2)**0.5
                G[i].append(distance)
    def Prim(G):
        V = len(G)
        dist =[float('inf')] * V
        dist[0] = 0
        prev =[None] * V
        S = set()
        weight =0
        while len(S) != V:
            v = None
            min_d = float('inf')
            for i in range(V):
                if i not in S and dist[i] <min_d:
                    min_d = dist[i]
                    v = i
            if v is None:
                return float('inf')
            S.add(v)
            if prev[v] is not None:
                weight += min_d
            for u in range(V):
                if u != v and u not in S:
                    if G[v][u] < dist[u]:
                        dist[u] =G[v][u]
                        prev[u] = v
        return weight
    result.append(Prim(G))
for u in result:
    if u%1 ==0 :
        a=f"{u:.2f}"
        print(a)
    else:
        print(f"{u:.2f}")

