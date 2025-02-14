class Vektor:
    def __init__(self,x,y,z):
        assert isinstance(x, (int, float)), "x-число"
        assert isinstance(y, (int, float)), "y-число"
        assert isinstance(z, (int, float)), "z-число"
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,Vektor):
            return self.x + Vektor.x,self.y + Vektor.y,self.z + Vektor.z
    def __sub__(self,Vektor):
            return self.x - Vektor.x,self.y - Vektor.y,self.z - Vektor.z
    def __mul__(self,oth):
        if isinstance(oth, Vektor):
            return self.x * oth.x+ self.y * oth.y + self.z * oth.z
        if isinstance(oth, (int, float)):
            return Vektor(self.x * oth, self.y * oth, self.z * oth)
    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'
vektor1 = Vektor(1,2,3)
vector2 = Vektor(9,5,6)
sum = vektor1+vector2
a = 0
for i in sum:
     a+=i
CM = a/6
print(f'Центр масс =  {CM}')
