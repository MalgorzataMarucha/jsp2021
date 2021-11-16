import cmath
z=cmath.sqrt(-1)
print("Część rzeczywista sin(z):", cmath.sin(z).real)
print("Część urojona sin(z):", cmath.sin(z).imag)
print("Część rzeczywista cos(z):", cmath.cos(z).real)
print("Część urojona cos(z):", cmath.cos(z).imag)
print("Czy zachodzi tutaj jedynka trygonometryczna?", (cmath.sin(z)**2)+(cmath.cos(z)**2))
#Odp. Zachodzi