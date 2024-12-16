class Fenwikcod:
    def __init__(self,maxi=10**5):
        self.maxi = maxi
        self.basetree =[0]*(self.maxi+1)

    def fenwikup(self, ind, value):
        while ind<=self.maxi:
            self.basetree[ind]+=value
            ind +=ind &-ind

    def fenwiks(self,ind):
        result=0
        while ind >0:
            result +=self.basetree[ind]
            ind -= ind&-ind
        return result

    def fin(self,count):
        toomuch =0
        for dist in count:
            little = self.fenwiks(dist-1)
            toomuch +=little
            self.fenwikup(dist, dist)
        return toomuch

t = int(input())
res = []
for i in range(t):
    n = int(input())
    count = list(map(int,input().split()))
    Fen = Fenwikcod()
    result = Fen.fin(count)
    res.append(result)
for i in res:
    print(i)





