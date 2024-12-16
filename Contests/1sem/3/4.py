# t = int(input())
# def section():
#     l = []
#     n_q = list(map(int,input().split()))
#     n = list(map(int,input().split()))
#     k =0
#     while k<n_q[1]:
#         i_j = list(map(int,input().split()))
#         start, end = i_j[0] - 1,  i_j[1]
#         count = {}
#         last = 0
#         sec = n[start:end]
#         for w in sec:
#             count[w] = count.get(w,0) + 1
#             if count[w] > last:
#                 last = count[w]
#             start+=count[w]
#         l.append(last)
#         k+=1
#     return l

# for i in range(t):
#     for w in section():
#         print(w)



# Оптимизация без использования сторонних библиотек
t = int(input())

def section():
    l = []
    n_q = [int(p) for p in input().split()]
    n = [int(p) for p in input().split()]
    k = 0
    while k < n_q[1]:
        i_j = [int(x) for x in input().split()]
        start, end = i_j[0]-1, i_j[1]
        dictionary = {}
        last = 0
        for w in n[start:end]:
            if w in dictionary:
                dictionary[w] += 1
            else:
                dictionary[w] = 1  
            if dictionary[w] > last:
                last = dictionary[w]
        l.append(last)
        k += 1
    return l

for i in range(t):
    for w in section():
        print(w)
