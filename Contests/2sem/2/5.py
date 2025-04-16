def maximum(graph, maxi):
    count = {}
    def justdo(v, visited):
        for u, q in graph.get(v, []):
            if q > maxi or u in visited:
                continue
            visited.add(u)
            if u not in count or justdo(count[u],visited):
                count[u] = v
                return True
        return False
    res = 0
    for w in graph:
        res += justdo(w, set())
    return res

def bfs(zone,x, y):
    v, b = len(zone), len(zone[0])
    rast=[]
    for i in range(v):
        rast.append([-1]* b)

    later = [(x, y, 0)]
    main = [(1, 0),(-1, 0), (0, 1),(0, -1)]
    
    for xx, yy, d in later:
        if rast[xx][yy] == -1:
            rast[xx][yy] = d
            for xx1, yy1 in main:
                Xx, Yy = xx + xx1, yy + yy1
                if 0 <= Xx < v and 0 <= Yy < b and zone[Xx][Yy] != 'X'and rast[Xx][Yy] == -1:
                    later.append((Xx, Yy, d + 1))
    result = {}

    for i in range(v):
        for j in range(b):
            if zone[i][j] == 'T':
                result[(i, j)] = rast[i][j]
    return result

p = int(input())
result =[]
for i in range(p):
    rows, cols = map(int, input().split())
    zone = [input().strip() for i in range(rows)]
    machine, animy = [], {}
    
    for i in range(rows):
        for j in range(cols):
            if zone[i][j] == 'R':
                machine.append((i, j))
            elif zone[i][j] == 'T':
                animy[(i, j)] = len(animy)
    
    graph={}
    for q in range(len(machine)):
        graph[q]=[]

    for i, (rasx,rasy) in enumerate(machine):
        rastances = bfs(zone, rasx, rasy)
        for (onex,oney), xx1 in animy.items():
            if (onex,oney) in rastances:
                graph[i].append((xx1, rastances[(onex, oney)]))
    l, r =0, rows*cols
    while l <r:
        z = (l +r)// 2
        if maximum(graph,z)<len(machine):
            l =z+1
        else:
            r =z
    if l< rows *cols and l>0:
        result.append(l)
    else:
        result.append(-1)
for i in result:
    print(i)