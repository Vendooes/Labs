nm = list(map(int,input().split()))
n = list(map(int, input().split()))
m = nm[1]
ln = nm[0]
count = [0]*m
time = 0

for i in range(ln):
    mini = min(count)
    num = count.index(mini)
    if i <m:
            count[i] = n[i]
    else:
        count[num]+=n[i]
    time = max(time,count[num])

print(time)
