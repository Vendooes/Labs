a = input().split()
amo = int(a[0])
sym = [a[1]]
def t(amo,sym):
    if amo%2 ==0:
        p = int(amo)/2
        for q in range (1,int(p-1)+2):
            print(''.join(sym*q))
        for i in reversed(range(1,int(p-1)+2)):
            print(''.join(sym*i))
    else:
        k= amo-1
        for q in range (1,int((k/2)+2)):
            print(''.join(sym*q))
        for i in reversed(range(1,int((k/2)+1))):
            print(''.join(sym*i))
t(amo,sym)
