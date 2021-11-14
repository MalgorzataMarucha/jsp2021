m = int(input("Podaj liczbę wierszy:"))
n = int(input("Podaj liczbę kolumn:"))
tablica = [[i*j for i in range(1,n+1)]for j in range(1,m+1)]
print(tablica)