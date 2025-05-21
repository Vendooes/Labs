k=5000
K=[k**i for i in range(5000)]
def hash(s,k=30,p=2**63-1):
    h=0
    for i in range(len(s)):
        h+=((ord(s[i])-ord('a')+1)*K[i])%p

    return h

def rev_hash(s,k=30,p=2**63-1):
    h=0
    for i in range(len(s)):
        h+=((ord(s[i])-ord('a')+1)*K[len(s)-i-1])%p

    return h

print(hash('aaba'))