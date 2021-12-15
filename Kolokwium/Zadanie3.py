from math import pi
def funkcja(r,jed):
    Pole = pi*(r**2)
    if(jed == "m"):
        print("Pole twojego koła wynosi: ",Pole," m^2")
    elif(jed == "cm"):
        print("Pole twojego koła wynosi: ",Pole," cm^2")
    elif(jed == "mm"):
        print("Pole twojego koła wynosi: ",Pole," mm^2")
    return ""
r=float(input("Podaj r: "))
jed = input("Podaj jednostkę(m,cm,mm): ")
print(funkcja(r,jed))

