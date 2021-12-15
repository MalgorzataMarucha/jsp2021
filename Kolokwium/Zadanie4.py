n=1234.56
lista1=[]
lista2=[]
przed,po = divmod(n, 1)
lista1.append(przed)
lista2.append(po)
print(lista1)
print(lista2)
slownik1 = {}
slownik2 = {}
for i in lista1:
    if i in slownik1:
        slownik1[i]+=1
    else:
        slownik1[i]=1
for a in lista2:
    if a in slownik2:
        slownik2[i]+=1
    else:
        slownik2[i]=1
for keys,values in slownik1.items():
    print(keys," ",values)
for x,y in slownik2.items():
    print(x," ",y)



