import itertools
lista = []
n=int(input("Podaj dlugosc listy:"))
print("Podaj liczby, ktore maja byc zawarte w liscie:")
for _ in range(0,n):
    a=int(input())
    lista.append(a)
def permutacje(x):
    x=list(itertools.permutations(lista))
    return x
print("Permutacje elementow z twojej listy: ",permutacje(lista))