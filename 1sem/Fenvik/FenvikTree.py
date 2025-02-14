class Fenvik:
    
    def __init__(self, size):
        self.size = size
        self.base = [0]*(size + 1)

    def update(self, i, value):
        while i <= self.size:
            self.base[i] += value
            i += i & -i

    def summa(self, i):
        sum = 0
        while i > 0:
            sum += self.base[i]
            i -= i & -i
        return sum

test = [12,54,7,3,45,9]
fenvikb = Fenvik(len(test))

for i in range(len(test)):
    fenvikb.update(i+1, test[i]) 

print(fenvikb.summa(3))  
fenvikb.update(2, 3)  
print(fenvikb.summa(3))


