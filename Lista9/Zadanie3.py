import matplotlib.pyplot as plt
import numpy as np
import math
import random
v0=float(input("Podaj prędkość początkową: "))
kat=float(input("Podaj kąt rzutu w stopniach: "))
Vox = v0 * math.cos(math.radians(kat))
Voy = v0 * math.sin(math.radians(kat))
Hmax=((v0**2)*(math.sin(math.radians(kat)))**2)/(2*9.81)
print("Maksymalna wysokość jaką osiągnie dany rzut: ",Hmax)
zasieg=(2*(v0**2)*math.sin(math.radians(kat))*math.cos(math.radians(kat)))/9.81
print("Zasięg jaki osiągnie dany rzut: ",zasieg)
czas=(2*v0*math.sin(math.radians(kat)))/9.81
print("Czas lotu rzutu: ",czas)
t=np.linspace(0.0,czas,100)
x = np.linspace(0.0,zasieg,100)
y = (Voy*t)-((9.81*(t**2))/2)
plt.subplot(3,1,1)
plt.plot(x,y)
plt.xlabel("Dystans")
plt.ylabel("Wysokość")
plt.title("Wykres toru rzutu ukośnego")
Vy = v0*math.sin(math.radians(kat)) - 9.81*t
Vx = np.ones_like(t)*Vox
plt.subplot(3,1,2)
plt.plot(t,Vx)
plt.plot(t,Vy)
plt.title("Wykres prędkości chwilowej")
plt.legend(["Vx","Vy"])
plt.subplot(3,1,3)
plt.plot(t,x)
plt.xlabel("Czas")
plt.ylabel("Położenie")
plt.title("Wykres toru położenia w funkcji czasu")
plt.show()

