def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = gcd_extended(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y

while True:
    try:
        a, b = map(int, input().split())
        d, x, y = gcd_extended(a, b)
        print(x, y, d)
    except EOFError:
        break

