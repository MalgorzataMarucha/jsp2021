class lista:
    def __init__(self,lista1):
        self.lista1=lista1
        self.lista1.sort()
    def podlisty(self):
        self.lista3=[]
        for a in range(len(self.lista1)):
            for b in range(len(self.lista1)):
                for c in range(len(self.lista1)):
                    if(self.lista1[a]+self.lista1[b]+self.lista1[c]==0):
                        self.lista3.append([self.lista1[a],self.lista1[b],self.lista1[c]])
        return self.lista3
print(lista([-2,-1,0,1,2,3]).podlisty())