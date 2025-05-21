n = int(input())
words = []
res=[]
for i in range(n):
    w = input()
    words.append(w)

for i in range(len(words)):
    for q in range(len(words)):
        if i!=q:
            if list(words[i]+words[q])==list(reversed(words[i]+words[q])):
                res.append([i+1,q+1])
            elif list(words[q]+words[i])==list(reversed(words[i]+words[q])):
                res.append([q+1,i+1])
print(len(res))
for i in range(len(res)):
    print(f'{res[i][0]} {res[i][1]}')
