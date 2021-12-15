import random
import time
def sortowanie(lista1,n):
    for x in range(n):
        element=lista1[x] 
        y=x-1
        while y>=0 and element<lista1[y]: 
            lista1[y+1]=lista1[y] 
            y-=1 
            lista1[y+1] = element 
    #print(lista1)
lista100 = []
lista200 = []
lista300 = []
for i in range(100):
    lista100.append(random.randint(0,20))
for i in range(200):
    lista200.append(random.randint(0,20))
for i in range(300):
    lista300.append(random.randint(0,20))
czas1 = time.time_ns()
sortowanie(lista100,100)
czas2 = time.time_ns()
print("Tak długo trwało sortowanie listy100: ", (czas2-czas1)/(10**9),"sec")
czas1 = time.time_ns()
sortowanie(lista200,200)
czas2 = time.time_ns()
print("Tak długo trwało sortowanie listy200: ", (czas2-czas1)/10**9,"sec")
czas1 = time.time_ns()
sortowanie(lista300,300)
czas2 = time.time_ns()
print("Tak długo trwało sortowanie listy300: ", (czas2-czas1)/(10**9),"sec")