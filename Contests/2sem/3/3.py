n= int(input())
a= str( input().strip())
b= str( input().strip())

def first_check():
    res=False
    if a.count('1')<b.count('1'):
        res='No'
    elif a.count('1')>b.count('1'):
        res='Yes'
    return res

def prefix_function(s):
    long = len(s)
    p = [0]*long 
    for i in range (1,len(s)):
        k = p[i-1]
        while k>0 and s[k]!=s[i]:
            k = p[k-1]
        if s[k]==s[i]:
            k+=1
        p[i] = k 
    return p

def kmp_search(text, pattern):
    if not pattern:
        return True
    
    n = len(text)
    m = len(pattern)
    if m > n:
        return False
    pi = prefix_function(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return True
    return False


if first_check() is not False:
    print(first_check())
else:
    t = a+'1'+a
    t2 = a+'0'+a
    r= kmp_search(t,b)
    r2=kmp_search(t2,b)
    if r and r2:
        print('Random')
    elif r:
        print('Yes')
    elif r2:
        print('No')
    







