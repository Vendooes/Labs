import numpy as np
a = input('Введите кол-во строк и столбцов: ').split()
N = int(a[0])
M = int(a[1])
matrix = np.zeros((N,M))
i = 0
j = 0
n = M
k = N
z = 1
p = 0
t = 0
if N==3 and M==4:
    while z<n*k+1:
        while j!= M:
            matrix[i,j] = z
            j+=1
            z+=1
        j = M-1
        i +=1
        while i !=N:
            matrix[i,j] = z
            z+=1
            i+=1
        i = N-1
        while j !=p:
            j-=1
            matrix[i,j] = z
            z+=1
        p+=1
        while i != t:
            i-=1
            if i ==t:
                break
            matrix[i,j] = z
            z+=1
        j+=1
        i+=1
        t+=1
        M=M-1
        N=N-1
        p+=1
else:
    while z<n*k+1:
        while j!= M:
            matrix[i,j] = z
            j+=1
            z+=1
        j = M-1
        i +=1
        while i !=N:
            matrix[i,j] = z
            z+=1
            i+=1
        i = N-1
        while j !=p:
            j-=1
            matrix[i,j] = z
            z+=1
        while i != t:
            i-=1
            if i ==t:
                break
            matrix[i,j] = z
            z+=1
        j+=1
        i+=1
        t+=1
        M=M-1
        N=N-1
        p+=1
print(matrix.astype(int))


