hights = input().split()
norm = [int(i) for i in hights]
l =[-1]
f = norm[0]
for i in range(len(norm)):
    if norm[i]>f:
        l.append(-1)
        f=norm[i]
    else:
        for q in range(i-1,-1,-1):
            if norm[q]>=norm[i]:
                l.append(q)
                break
end=[]
for i in l:
    end.append(str(i))
print(' '.join(end))

    

