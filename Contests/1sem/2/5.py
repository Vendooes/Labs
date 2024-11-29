words = input().split()
l = []
need = []
for i in range(len(words)):
    if words[i] not in l:
        z=[]
        l2 =[]
        for q in range(len(words)):         
            for w in words[i]:
                for e in words[q]:
                    if words[i].count(w)==words[q].count(e) and words[i].count(w)>1 and str(w)==str(e) and e not in z :
                        for t in range(words[i].count(w)):
                            z.append(e)
                    elif str(w)==str(e) and e not in z and words[i]!=words[q] and words[i].count(w)==words[q].count(e):
                        z.append(e)

            if len(z)==len(words[i]) and words[q] not in l:
                if words.count(words[q])>1:
                    for g in range(words.count(words[q])):
                        l.append(words[q])
                        l2.append(words[q])
                else:
                    l.append(words[q])
                    l2.append(words[q])
                z.clear()
                if words[i] not in l:
                    l.append(words[i])
                    l2.append(words[i])
        
            z.clear()
        if len(l2)>0:
            need.append(l2)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if len(x) <= len(pivot)]
        greater = [x for x in arr[1:] if len(x) > len(pivot)]
        return quicksort(greater) + [pivot] + quicksort(less)

need = quicksort(need)


for w in need:
    for q in range(len(w)):
        for i in range(0,len(w)):
            if i+1< len(w) and w[i] >w[i+1]:
                w[i], w[i+1] = w[i+1],w[i]



norm = []
for i in need:
    for q in i:
        norm.append(q)


norm2 = []
for i in words:
    if i not in norm:
        norm2.append(i)

for q in range(len(norm2)):
    for i in range(0,len(norm2)):
        if i+1 <len(norm2) and norm2[i]>norm2[i+1]:
            norm2[i],norm2[i+1]=norm2[i+1],norm2[i]

print(' '.join(norm+norm2))