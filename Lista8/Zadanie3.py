import random

pesel = []
wagi = [1,3,7,9,1,3,7,9,1,3]
licznik = 0
suma = 0
plik = open("PESEL.txt", "w")
for _ in range(10):
    rok = random.randint(1800,2099)
    pesel.extend([str(rok)[-2:-1], str(rok)[-1]])
    miesiac = random.randint(1,12)
    if(miesiac in [1,3,5,7,8,10,12]):
        dzien = random.randint(1,31)
    elif(miesiac in [4,6,9,11]):
        dzien = random.randint(1,30)
    elif(miesiac == 2 and rok%4==0):
        dzien = random.randint(1,29)
    elif(miesiac == 2 and rok%4!=0):
        dzien = random.randint(1,28)
    if(rok in range(1800,1900)):
        miesiac+=80 
        pesel.extend([str(miesiac)[0], str(miesiac)[1]])
    elif(rok in range(2000,2100)):
        miesiac+=20 
        pesel.extend([str(miesiac)[0],str(miesiac)[1]])
    elif(rok in range(1900,2000)):
        if(len(str(miesiac)) == 1):
            pesel.extend(["0",str(miesiac)])
        elif(len(str(miesiac)) >= 1):
            pesel.extend([str(miesiac)[0], str(miesiac)[1]])
    if(dzien in range(1,10)):
        pesel.extend(["0",str(dzien)])
    elif(dzien in range(10,32)):
        pesel.extend([str(dzien)[0],str(dzien)[1]])
    for _ in range(4):
        pesel.append(str(random.randint(0,9)))
    for _ in wagi:
        if(len(str(_*int(pesel[licznik]))) > 1):
            suma += int(str(_*int(pesel[licznik]))[-1]) 
        else:
            suma += _*int(pesel[licznik])
        licznik+=1
    kontrolna = 10-int(str(suma)[-1])
    if(kontrolna == 10):
        kontrolna = 0
    pesel.append(str(kontrolna))
    plik.write("".join(pesel)+"\n")
    licznik = 0
    pesel = []
    suma = 0

plik.close()
    




