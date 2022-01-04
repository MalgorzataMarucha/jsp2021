import SzyfrCezara
import datetime
import os
n = input("Podaj ścieżkę do pliku: ")
klucz=int(input("Podaj klucz: "))
while klucz<1 or klucz>10:
    klucz=int(input("Podaj klucz z zakresu 1-10: "))
try:
    plik=open(n,"r")
except FileNotFoundError:
    n = input("Taki plik nie istnieje, podaj poprawną ścieżkę: ")
    plik=open(n,"r")
tekst=plik.read()
tekst = SzyfrCezara.szyfr(tekst,klucz)
plik.close()
miejsce = input("Gdzie chcesz zapisać plik? ")
miejsce2 = miejsce
czas = datetime.datetime.now()
miejsce+="/plik_zaszyfrowany{}_{}{}{}.txt".format(klucz,czas.strftime("%Y"),czas.strftime("%m"),czas.strftime("%d"))
try:
    plik2=open(miejsce,"w")
    plik2.write(tekst)
    plik2.close()
except FileNotFoundError:
    os.mkdir(miejsce2)
    plik2=open(miejsce,"w")
    plik2.write(tekst)
    plik2.close()
