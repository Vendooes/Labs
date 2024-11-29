count = input().split()
norm =[int(i) for i in count]

typ = []
fin = []
for q in range(0,10):
    for i in norm:
        rt = i
        while len(str(rt))!=1:
            summ = 0
            for w in str(rt):
                summ+=int(w)
            rt =summ

        if rt == q:
            fin.append(i)
            typ.append(rt)

finf = []
for t in fin:
    finf.append(str(t))


for i in typ:
    if typ.count(i)>2:
        sl1 = fin[typ.index(i):typ.index(i)+typ.count(i)]
        sl2 = fin[typ.index(i)+typ.count(i):]
        fir = 0
        sec = 1
        for i in range(len(sl1)):
            fir = 0
            sec = 1
            for q in range(len(sl1)):
                if sec<len(sl1) and fir<len(sl1) and sl1[sec]<sl1[fir]:
                    sl1[fir],sl1[sec] = sl1[sec],sl1[fir]
                fir+=1
                sec+=1
        finf1 = (sl1+sl2)
        finf.clear()
        for t in finf1:
            finf.append(str(t))
    else:
        for k in fin:
            if len(str(k))>1 and len(norm)>fin.index(k)+1 and k>fin[fin.index(k)+1] and len(str(fin[fin.index(k)+1]))==1:
                finf[fin.index(k)],finf[fin.index(k)+1] = finf[fin.index(k)+1], finf[fin.index(k)]

        
k = 0
for i in typ:
    if typ.index(i)+1<len(typ) and typ[0]==typ[typ.index(i)+1]:
        k+=1

if k == len(norm):
    def sort(count):
        if len(count) < 2:
            return count

        count = list(map(int, count))
    
        med_index = (len(count) - 1) // 2
        medi = count[med_index]

        mini = []
        ser = []
        big = []

        for i in count:
            if i < medi:
                mini.append(i)
            elif i == medi:
                ser.append(i)
            else:
                big.append(i)

        return sort(mini) + ser + sort(big)
    g = sort(count)
    gg= []
    for i in g:
        gg.append(str(i))

    print(' '.join(gg))
else:
    print(' '.join(finf))

