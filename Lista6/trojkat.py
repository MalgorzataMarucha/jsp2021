from math import sqrt
def obwod(a,b,c):
    obwod=a+b+c
    return obwod
def pole(a,b,c):
    p=(a+b+c)/2
    pole=sqrt(p*(p-a)*(p-b)*(p-c))
    return pole
def sprawdz1(a,b,c):
    if(a==b==c):
        print("Trójkąt jest równoboczny!")
    if(a==b !=c or a==c !=b or b==c !=a):
        print("Trójkąt jest równoramienny!")
    else:
        print("Trójkąt jest różnoboczny!")
    return print
def sprawdz2(a,b,c):
    if(c>b and c>a):
        if(a**2+b**2==c**2):
            print("Trójkąt jest prostokątny!")
        if(a**2+b**2>c**2):
            print("Trójkąt jest ostrokątny!")
        if(a**2+b**2<c**2):
            print("Trójkąt jest rozwartokątny!")
    if(b>c and b>a):
        if(a**2+c**2==b**2):
            print("Trójkąt jest prostokątny!")
        if(a**2+c**2>b**2):
            print("Trójkąt jest ostrokątny!")
        if(a**2+c**2<b**2):
            print("Trójkąt jest rozwartokątny!")
    if(a>b and a>c):
        if(c**2+b**2==a**2):
            print("Trójkąt jest prostokątny!")
        if(c**2+b**2>a**2):
            print("Trójkąt jest ostrokątny!")
        if(c**2+b**2<a**2):
            print("Trójkąt jest rozwartokątny!")