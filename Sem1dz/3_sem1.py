a = input('Введите числа:').split()
b = len(a)
s = 1
for i in a:
    s=s*int(i)
geometry = s**(1/int(b))
print(geometry)