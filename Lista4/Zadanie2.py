lista = []
n=int(input("Podaj dlugosc listy:"))
print("Podaj liczby, ktore maja byc zawarte w liscie:")
def usun(x):
    x.sort()
    x=list(set(lista))
    return x
for _ in range(0,n):
    a=int(input())
    lista.append(a)
print("Twoja lista: ",lista)
print("Twoja lista po usunieciu duplikatow: ", usun(lista))