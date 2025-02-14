a = int(input())
b = input().split()
for i in range (0,a-1):
    for q in range (i+1,a-1):
        if b[i]>b[q]:
            b[i], b[q] = b[q],b[i]
s = b[int((a-1)/2)]
print(''.join(s))
