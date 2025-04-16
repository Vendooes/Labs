class Graph:
    def __init__(self, graph):
        self.graph = list(map(list, graph))
        self.main_g = list(map(list, graph))
        self.ROW = len(graph)

    def BFS(self,q,w, parent):
        visited = [False]* (self.ROW)
        waiting = []
        waiting.append(q)
        visited[q] = True
        while waiting:
            u = waiting.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] ==False and val> 0:
                    waiting.append(ind)
                    visited[ind] = True
                    parent[ind] =u
        if visited[w]:
            return True
        else:
            return False

    def Fulkerson(self, source, sink):
        parent = [-1]*(self.ROW)
        maximum = 0
        self.graph = list(map(list, self.main_g))
        while self.BFS(source,sink, parent):
            second = float("Inf")
            s = sink
            while(s!= source):
                second = min(second,self.graph[parent[s]][s])
                s = parent[s]
            maximum +=second
            v = sink
            while(v!= source):
                u = parent[v]
                self.graph[u][v] -=second
                self.graph[v][u]+=second
                v = parent[v]
        return maximum

t = int(input())
fin =[]
for i in range(t):
    result =[]
    n = int(input())
    graph=[]
    for q in range(n):
        price = str(input())
        graph.append([int(q) for q in price])
    g = Graph(graph)
    for t in range(len(graph)):
        source =t
        for u in range(len(graph)):
            if t!=u:
                sink=u
                result.append(g.Fulkerson(source, sink))
    fin.append(min(result))
for i in fin:
    print(i)
