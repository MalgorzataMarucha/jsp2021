import math
a=input("Wpisz a:")
b=input("Wpisz b:")
a=int(a)
b=int(b)
if b<a:
    Z = b % a
    Z*=Z+3
    print(Z)
else:
    print("b musi być mniejsze od a")