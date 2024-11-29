N = int(input())
l=[]
def calk(N):
    if N==1:
        return 0
    if N/3==1:
        return 0
    if N%3==0:
        return 1+calk(N/3)
    elif N%2==0:
        return 1+calk(N/2)
    else:
        return 1+calk(N-1)
l.append(calk(N))
def calk3(N):
    if N==1:
        return 0

    elif N%3!=0:
        return 1+calk3(N-1)
    elif N%3==0:
        return 1+calk3(N/3)
l.append(calk3(N))
sum=0
for q in str(N):
    sum+=int(q)
if sum%3==2:
    N=N-2
    def calk0(N):
        if N==1:
            return 0
        if N/3==1:
            return 0
        if N%3==0:
            return 1+calk0(N/3)
        elif N%2==0:
            return 1+calk0(N/2)
        else:
            return 1+calk0(N-1)
    l.append(calk0(N)+1)
print(min(l))

