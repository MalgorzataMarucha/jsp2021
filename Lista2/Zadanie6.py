lista = ["Kasia","Basia","Marek","Darek"]
lista.append("Józek")
lista.extend(["Ania","Basia"])
lista.sort()
print(lista[3])
print(lista[0:2])
print(lista[-2:])
n=lista.count("Basia")
for i in range(n):
    lista.remove("Basia")
print(lista)
print(len(lista))
print(tuple(lista))