graph = {0: [1,4], 1: [2,3], 2:[3], 3:[0], 4:[1], 5:[4]}


def dfs_visit(graph,node, color, visited):
    color[node] =1
    visited.append(node)
    for neighbor in graph[node]:
        if color[neighbor] ==0:
            dfs_visit(graph,neighbor,color,visited)
    color[node] =2

def dfs_recursive(graph):
    comp = []
    color = [0 for _ in graph]
    for node in graph:
        if color[node] == 0:
            visited =[]
            dfs_visit(graph, node, color,visited)
            comp.append(visited)
    return comp

top_sort = []
def dfs_topological_sort_visit(graph,node, color, top_sort):
    color[node] =1
    print(node)
    for neighbor in graph[node]:
        if color[neighbor] ==0:
            dfs_topological_sort_visit(graph,neighbor,color,top_sort)
    color[node] =2
    top_sort.insert(0,node)

def topological_sort(graph):
    color = [0 for _ in graph]
    top_sort = []
    for node in graph:
        if color[node] == 0:
            dfs_topological_sort_visit(graph, node, color, top_sort)
    return top_sort

def kosoraju(graph):
    top_sort = topological_sort(graph)
    graph_t = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            graph_t[neighbor].append(node)
    color = [0 for _ in graph] 
    while top_sort:
        node = top_sort[0]

        component = []
        dfs_visit(graph_t,node,color, component)
        print(component)
        for node in component:
            top_sort.remove(node)
kosoraju(graph)