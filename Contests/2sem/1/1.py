N_M = list(map(int, input().split()))
N= N_M[0]
M= N_M[1]

def BFS(N,M):
    visited = set()
    queue = [(N,0)]

    visited.add(N)

    while queue:
        win, steps = queue.pop(0)
        diff = win-2
        mult = win*3
        s=0
        for i in str(win):
            s +=int(i)
        summa = win+s

        if win ==M:
            return steps

        if diff not in visited and diff>=0 and diff<=9999:
            visited.add(diff)
            queue.append((diff,steps+1))

        if mult not in visited and mult<=9999:
            visited.add(mult)
            queue.append((mult,steps+1))

        if summa not in visited and summa<=9999:
            visited.add(summa)
            queue.append((summa,steps+1))

print(BFS(N,M))

