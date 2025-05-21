n = int(input())
w = list(map(str,input().split()))
def p_s(num_1,num_2):
    maxi = min(len(num_1),len(num_2))
    fin=0
    for i in range(1,maxi+1):
        if num_1[len(num_1)-i:] ==num_2[:i]:
            fin=i
    return fin

res = w[0]
for q in w[1:]:
    cut = p_s(res,q)
    res += q[cut:]
print(res)


