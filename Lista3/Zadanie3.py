import math
print("Kalkulator równania kwadratowego")
a=int(input("Podaj a:"))
b=int(input("Podaj b:"))
c=int(input("Podaj c:"))
if a==0:
    print("To nie jest równanie kwadratowe, podaj inne a.")
else:
    delta=b*b-4*a*c
    if delta>0:
        delta=math.sqrt(delta)
        x1=(-b-delta)/(2*a)
        x2=(-b+delta)/(2*a)
        print("Są dwa pierwiastki równania:",x1,x2)
    else:
        if delta==0:
            x0=(-b)/(2*a)
            print("Jest jeden pierwiastek równania:",x0)
        else:
            print("Równanie nie ma pierwiastków.")
