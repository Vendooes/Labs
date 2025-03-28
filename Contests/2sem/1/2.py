N_M = list(map(int, input().split()))
M = N_M[1]
N = N_M[0]
graph = [[] for i in range(N)]
sub = [0] * N

for i in range(M):
    inp = list(map(int,input().split()))
    m = inp[0]
    n = inp[1]
    graph[m -1].append(n -1)
    sub[n -1]+= 1

def topolog(graph, N):
    queue = []
    for u in range(N):
        if sub[u] == 0:
            queue.append(u)
    list = []
    one = 1 
    while queue:
        if len(queue) > 1:
            one = 0  
        u = queue.pop(0)  
        list.append(u)  
        for i in graph[u]:
            sub[i]-= 1
            if sub[i]== 0:
                queue.append(i)
    if len(list) != N:
        print(-1)  
    else:
        if one == 1:
            print("YES")  
        else:
            print("NO")  
topolog(graph, N)