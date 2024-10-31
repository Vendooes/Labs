count = int(input())
que = input().split()
q = 0
for i in que:
    q+=int(i)
Q = int(q/3)

if q%3!=0:
    print(0)
else:
    need = 0
    l=[]
    for t in que[0::]:
        if need<=Q:
            need+=int(t)
            l.append(int(t))
            if need>Q:
                need-=int(t)
                l.remove(int(t))
        need=0

        for e in l:
            que.remove(str(e))

        l.clear()
    if que==[]:
        print(1)
    else:
        print(0)


    # print(l[0])
    # print (l)
    #print(que)




