def kuhn(graph,n,r):
    match = [-1] * n
    visited = [False] * n
    parts = graph
    def dfs(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] ==-1 or dfs(match[u]):
                    match[u] = v
                    return True
        return False
    max_matching = 0
    for v in range(r):
        visited = [False] * n
        if dfs(v):
            max_matching+= 1
    return max_matching

a = int(input())
res = []
for i in range(a):
    rows,cals,cuts = list(map(int,input().split()))
    cut = list(map(int, input().split()))
    x_c = cut[::2]
    y_c = cut[1::2]
    cut_list=set()
    for t in range(len(x_c)):
        cut_list.add((x_c[t],y_c[t]))

    graph = {} 
    for w in range(rows):
        graph[w] =[]
        for q in range(cals):
            if (w,q) not in cut_list:
                graph[w].append(q)

    res.append(kuhn(graph,cals,rows))
for i in res:
    print(i)
