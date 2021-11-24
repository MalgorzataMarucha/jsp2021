import math
def zamiana(x,y):
    if x=="radiany":
        wynik = y * (math.pi/180)
    elif x=="stopnie":
        wynik = y * (180/math.pi)
    else:
        print("Wybierz opcję!")
    return wynik
y=float((input("Podaj swoj kat:")))
x=(input("Na co chcesz zamienic dany kat? Wpisz radiany lub stopnie:"))
print("Twoj wynik: ",zamiana(x,y))