n, m, p = list(map(int, input().split()))
hacks = set([x for x in list(map(int, input().split()))])
good=[]
good=set(i for i in range(1,n+1) if i not in hacks )
graph = {}
for i in range(m):
    xi,yi,li = list(map(int,input().split()))
    if xi not in graph:
        graph[xi]=[(yi,li)]
    else:
        graph[xi].append((yi,li))
    if yi not in graph:
        graph[yi]=[(xi,li)]
    else:
        graph[yi].append((xi,li))

def Prim(graph,good):
    visited =set()
    start = min(good)
    visited.add(start)
    active =[]
    price = 0
    price1 = 0

    for second,wes in graph.get(start,[]):
        if second in good: 
            active.append((wes,second))
    act_sort= sorted(active)
   
    while act_sort and len(visited)<len(good):
        wei,nod =act_sort.pop(0)
        
        if nod in good and nod not in visited:
            visited.add(nod)
            price+=wei

            for nei,w in graph[nod]:
                if nei in good and nei not in visited:
                    act_sort.append((w,nei))
                    
            act_sort.sort()
    if len(visited)!=len(good):
        print("impossible1")
        return
    for o in hacks:
        mini = 9999999
        for nei,wes in graph[o]:
            if wes<mini and nei in good:
                mini= wes
        if mini ==9999999:
            print("impossible2")
            return
        price1+=mini

    print(price+price1)

Prim(graph,good)