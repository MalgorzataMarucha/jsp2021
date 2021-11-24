def szereg(n):
    suma = 0
    for i in range(1,n+1):
        suma+=1/i
    return suma
n=int(input("Podaj liczbę wyrazów:"))
print(szereg(n))
