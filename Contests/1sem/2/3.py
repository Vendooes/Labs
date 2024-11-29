friends = input().split()
norm = [int(i) for i in friends]
k = 0
l=[]
for i in range(len(norm)):
    for q in norm[i+1::]:
        if q>norm[i]:
            k+=1
            norm[i] = q
    l.append(k)
    k=0
end =[]
for i in l:
    end.append(str(i))
print(' '.join(end))
