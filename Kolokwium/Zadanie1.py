a = [int(x) for x in input("Podaj listę: ").split()]
lista=[]
for x in a:
    if(x%2==0):
        pass
    else:
        lista.append(x)
print(lista)
