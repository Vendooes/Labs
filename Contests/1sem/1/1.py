a = input().split()
N = int(a[0])
M = int(a[1])
# N-длина столбца, M - длина строки

#создание двумерного массива  
l = [0] * N 
for i in range(N): 
    l[i] = [0] * M

l[0][0]=1 


for q in range (N):
    for w in range (M):
        if q+2<N and w+1<M:
            l[q+2][w+1]+=l[q][w]
        if q+1<N and w+2<M:
            l[q+1][w+2]+=l[q][w]

count = l[N-1][M-1]

print(count)

