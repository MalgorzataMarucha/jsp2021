import os
import sys
def funkcja(napis):
    napis=napis.lower()
    for i in napis:
        if(i == "," or i=="." or i=="?" or i=="!" or i==" "):
            napis = napis.replace(i,"")     
    print(napis)
    slownik = {}
    for i in napis:
        if i in slownik:
            slownik[i]+=1
        else:
            slownik[i]=1
    for keys,values in slownik.items():
        print(keys," ",values)
print("Nazwa twojego pliku: ",sys.argv[0])
nazwa = sys.argv[1]
try:
    plik = open(nazwa,"r")
except FileNotFoundError:
    print("Taki plik nie istnieje!")
tekst=plik.read()
print(funkcja(tekst))
plik.close()