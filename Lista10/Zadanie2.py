import itertools
class lista:
    def __init__(self,lista1):
        self.lista1=lista1
    def podlista(self):
        self.lista2=[]
        for x in range(len(self.lista1)+1):
            for y in itertools.combinations(self.lista1,x):
                self.lista2.append(list(y))
        return self.lista2
print(lista([1,2,3,4]).podlista())
        