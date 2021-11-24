lista = []
n=int(input("Podaj dlugosc listy:"))
print("Podaj liczby, ktore maja byc zawarte w liscie:")
for _ in range(0,n):
    a=int(input())
    lista.append(a)
iloczyn=1
suma = 0
for x in lista:
    suma+=x
for y in lista:
    iloczyn*=y
print("Suma twoich liczb: ",suma)
print("Iloczyn twoich liczb: ",iloczyn)