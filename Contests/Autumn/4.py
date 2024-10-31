text = input()
find = input()
count = int(input())
count_sym_f = len(find)
count_sym_t = len(text)
slize=[]
l = []
p = 0
f=[]
chisla = []
while count_sym_f<count_sym_t+1:
    for i in text[p:count_sym_f]:
        slize.append(i)
    yeah = 0
    l.append(''.join(slize))#
    for t in find:
        f.append(t)
    for q in f:
        c =  slize.count(q)
        if c>0:
            slize.remove(q)
            f.remove(str(q))
        yeah+=c
        c = 0
    l.append(yeah)
    chisla.append(yeah)
    # l.append(''.join(slize))
    count_sym_f+=1
    p+=1
    slize.clear()
    f.clear()
maxi = max(chisla)
gg = max(chisla)

z = l.index(maxi)
slovo = l[z-1]
n = []
for g in slovo:
    n.append(g)
pp=[]
for qq in find:
    pp.append(qq)
for ww in n:
    if n.count(ww)>pp.count(ww) and maxi==len(find):
        mm = n.count(ww) - pp.count(ww)
        maxi-=mm
first = n[0]
second = n[1]
for j in text:
    if j==first and second == text[text.index(j)+1]:
        oe = text.index(j)

txt=[]
for op in text:
    txt.append(op)
# chisla.remove(maxi)
# maxi2 = max(chisla)
# print(l)
# print(slovo)

y=0
sk = 0
for u in n:
    if u != pp[y] and y<len(find):
        sk+=1
    y+=1

if sk>count:
    chisla.remove(gg)
    # del chisla[chisla.index(maxi)]
    l.remove(str(slovo))
    maxi2 = max(chisla)
    z1 = l.index(maxi2)
    slovo = l[z1+1]
    n1 = []

    for g1 in slovo:
        n1.append(g1)
    pp1=[]
    for qq1 in find:
        pp1.append(qq1)
    for ww1 in n1:
        if n1.count(ww1)>pp1.count(ww1) and maxi2==len(find):
            mm1 = n1.count(ww1) - pp1.count(ww1)
            maxi2-=mm1
    first1 = n1[0]
    second1 = n1[1]
    third = n1[2]
    ll=1
    for j1 in range(0,len(txt)-1):
        ll=j1
        ll2 = j1+1
        ll3 = j1+2
        if txt[ll]==first1 and txt[ll2]==second1 and txt[ll3]==third :
            oe1 =ll
            # print(txt[ll])
            # print(txt[ll2])
    # print(sk)
    print(f'{oe1} {maxi2-1}')
    # print(chisla)
else:
    # print(sk)
    print(f'{oe} {maxi}')
