def explore(a, b):
    if a[b-1] != b:
        a[b-1] = explore(a, a[b-1])
    return a[b-1]

def app(a, t, x, y):
    x = explore(a, x)
    y = explore(a, y)
    if x == y:
        return
    if t[x-1] == t[y-1]:
        t[x-1] += 1
    if t[x-1] < t[y-1]:
        a[x-1] = y
    else:
        a[y-1] = x
n, m, k = map(int, input().split())
graph = [i for i in range(1, n+ 1)]
dim = [0]* n
for i in range(m):
    input()
doing = [input() for q in range(k)]
doing = reversed(doing)

ans = []
for do in doing:
    char, x, y = do.split()
    x,y = int(x), int(y)

    if char == 'ask':
        if explore(graph, x) == explore(graph, y):
            ans.insert(0,'YES')
        else:
            ans.insert(0,'NO')

    if char == 'cut':
        app(graph, dim, x, y)
for i in ans:
    print(i)