def zapis(n):
    lista = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    x = len(n) - 1
    i=0
    zmieniona_liczba = 0
    while i < x:
        if lista[n[i]] >= lista[n[i+1]]:
            zmieniona_liczba += lista[n[i]]
            i+=1
        elif lista[n[i]] < lista[n[i+1]]:
            zmieniona_liczba += lista[n[i+1]] - lista[n[i]]
            i+=2
    if lista[n[x]] <= lista[n[x-1]]:
        zmieniona_liczba += lista[n[x]]
        return zmieniona_liczba
    else:
        return zmieniona_liczba
n = input("Podaj liczbę rzymską: ")
print(zapis(n))