from math import factorial
def trojkat_pascala(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for x in range(i+1):
            print(factorial(i)//(factorial(x)*factorial(i-x)),end=" ")
        print()
n = int(input("Podaj liczbę wierszy:"))
trojkat_pascala(n)