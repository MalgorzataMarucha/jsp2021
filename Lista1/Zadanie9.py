import cmath
z=complex(input("Wpisz liczbę zespoloną:"))
modul=cmath.sqrt((z.real**2)+(z.imag**2))
print(modul)
arg=cmath.phase(z)
print(arg)
spr=z.conjugate()
print(spr)