lista=[1,2,3,4,"c","a","b"]
lista2=[]
for x in lista:
    if isinstance(lista,str):
        print("Nie ma tutaj liczb")
    if type(x) == int:
        lista2.append(x)
    else:
        pass
a=max(lista2)
b=min(lista2)
if (a==b):
    print("Max i min są takie same!")
elif(lista2.count(a)>1 or lista2.count(b)>1):
    print("Najmniejszy element listy: ",b)
else:
    print("Największy element listy: ",a)
    print("Najmniejszy element listy: ",b)
