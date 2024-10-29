N, K = tuple(map(int, input().split()))
l = []
for _ in range(N):
    l.append(list(map(int, input().split())))
def check_section(l, coord, len):
    quit = 1
    for i in range(len):
        for j in range(len):
            quit *= l[coord[0] + i][coord[1] + j]
    return quit
max_len = min(N, K)
result = max_len
for length in range(1, max_len + 1):
    free_sec = []
    for j in range(N - length + 1):
        for m in range(K - length + 1):
            if check_section(l, (j, m), length):
                free_sec.append((j, m))
    if len(free_sec) == 0:
        res = length - 1
        break
print(res)