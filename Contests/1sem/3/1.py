class Heap:
    
    def __init__(self, a):
        self.array = a
        for i in range(len(self.array)//2, -1, -1):
            self.findD(i)
    
    def findD(self, i):
        while 2 * i + 1 < len(self.array):
            maxi = 2 * i + 1
            if 2 * i + 2 < len(self.array) and self.array[2 * i + 1] < self.array[2 * i + 2]:
                maxi = 2 * i + 2
            if self.array[i] > self.array[maxi]:
                break
            self.array[i], self.array[maxi] = self.array[maxi], self.array[i]
            i = maxi
        return
    
    def plus(self, value):
        self.array.append(value)
    
    def pop(self):
        result = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.findD(0)
        return result

n, k = list(map(int, input().split()))
seq = list(map(int, input().split()))
h = Heap(seq[:k])
for val in seq[k:]:
    if val < h.array[0]:
        h.pop()
        h.plus(val)
    
h.array.sort()
print(" ".join(map(str, h.array)))
