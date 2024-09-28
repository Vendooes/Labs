a = input()
mir = ['3', 'L', '2', '5','E', 'J', 'S', 'Z']
inme = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
l = []
for i in inme:
    if a.count(i) == 2 and a[0]!=a[1]:
        print(a,'is a regular palindrome.')

for q in inme:
    if a.find(q) != -1:
       l.append(q)
    if a[0]!=a[1] and len(l)==len(a):
        print(a,'is a mirrored palindrome.')
        break

for q in mir:
    if a.find(q) != -1:
       l.append(q)
if 1<len(l)<=len(a):
    print(a,'is a mirrored string.')

v = []
for w in inme:
    if ''.join(inme).find(w) == -1:
        v.append(w)
        if len(v)!= len(a):
            print(a,'is not a palindrome.')
            break



