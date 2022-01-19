import math
class Koło:
    def __init__(self,r):
        self.r=r
    def obwod(self):
        self.obw=2*math.pi*self.r
        return self.obw
    def pole(self):
        self.pol=math.pi*(self.r**2)
        return self.pol
print(Koło(15).obwod())
print(Koło(15).pole())