import trojkat
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
c=float(input("Podaj c: "))
if(c>=a and c>=b):
    if(a+b>c):
        print("Obwód trójkąta wynosi: ",trojkat.obwod(a,b,c))
        print("Pole trójkąta wynosi: ",trojkat.pole(a,b,c))
        trojkat.sprawdz1(a,b,c)
        trojkat.sprawdz2(a,b,c)
    else:
        print("Nie ma trójkąta o podanych bokach!")
if(b>=a and b>=c):
    if(a+c>b):
        print("Obwód trójkąta wynosi: ",trojkat.obwod(a,b,c))
        print("Pole trójkąta wynosi: ",trojkat.pole(a,b,c))
        trojkat.sprawdz1(a,b,c)
        trojkat.sprawdz2(a,b,c)
    else:
        print("Nie ma trójkąta o podanych bokach!")
if(a>=b and a>=c):
    if(c+b>a):
        print("Obwód trójkąta wynosi: ",trojkat.obwod(a,b,c))
        print("Pole trójkąta wynosi: ",trojkat.pole(a,b,c))
        trojkat.sprawdz1(a,b,c)
        trojkat.sprawdz2(a,b,c)
    else:
        print("Nie ma trójkąta o podanych bokach!")