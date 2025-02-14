n = int(input())
def destr(n):
    l = []
    for i in range(2,n+1):
        while n%i == 0:
            l.append(str(i))
            n = n/i
    return (str('*'.join(l)))
print(f'{destr(n)} = {n}')
