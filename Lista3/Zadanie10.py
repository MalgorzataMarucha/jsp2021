liczby = []
for liczba in range(100,401):
    jed = liczba%10
    dz = (liczba%100)//10
    se = (liczba%1000)//100
    if jed%2 == 0 and dz%2 == 0 and se%2 == 0:
        liczby.append(liczba)
print(liczby)