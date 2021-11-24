n=int(input("Podaj liczbe wyrazow ciagu geometrycznego:"))
a1=float(input("Podaj pierwszy wyraz ciagu:"))
q=float(input("Podaj wartosc iloczynu ciagu:"))
def wyraz_ciagu(n,a1=1,q=2):
    return a1 * q**(n-1)
print("Ostatni wyraz ciagu wynosi: ",wyraz_ciagu(n,a1,q))