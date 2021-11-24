def NWD(a,b):
    if(a > b):
        if(a%b == 0):
            return b
        else:
            while b>0:
                x = a%b
                a = b
                b = x
            return a
    else:
        y = a
        a = b
        b = y
        if(a%b == 0):
            return b
        else:
            while b>0:
                x = a%b
                a = b
                b = x
            return a
a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
print(NWD(a,b))
