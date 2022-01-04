plik = open("PESEL.txt","r")
pesele = plik.readlines()
plik.close()
wagi = [1,3,7,9,1,3,7,9,1,3]
plik2 = open("PESEL_wynik.txt", "w")
for a in pesele:
    suma = 0
    licznik = 0
    a=a.strip()
    for _ in wagi:
        if(len(str(_*int(a[licznik]))) > 1):
            suma += int(str(_*int(a[licznik]))[-1])
        else:
            suma += _*int(a[licznik])
        licznik+=1
    kontrolna = 10-int(str(suma)[-1])
    if(kontrolna == 10):
        kontrolna = 0
        
    if(int(a[10])==kontrolna):
        miesiac = a[2:4]
        if(int(miesiac) in range(81,93)):
            rok = "18"+a[0:2]
            miesiac = int(miesiac) - 80
        elif(int(miesiac) in range(21,33)):
            rok = "20"+a[0:2]
            miesiac = int(miesiac) - 20
        elif(int(miesiac) in range(1,13)):
            rok = "19"+a[0:2]
        dzien = a[4:6]
        if(int(a[9])%2 == 0 or int(a[9])==0):
            plec = "kobieta"
        elif(int(a[9])%2 != 0 and int(a[9])!=0):
            plec = "mężczyzna"
        plik2.write("nr PESEL: {}\n data urodzenia {}-{}-{};\t płeć: {} \n".format(a, dzien, miesiac, rok, plec))
plik2.close()

        

