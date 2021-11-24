def program(n):
    silnia = 1
    for i in range(1,n+1):
        silnia*=i
    return silnia
n=int(input("Podaj liczbę, z której chcesz otrzymać silnie:"))
print(program(n))