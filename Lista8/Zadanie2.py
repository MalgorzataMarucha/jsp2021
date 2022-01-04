import SzyfrCezara
import datetime
import os
n = input("Podaj ścieżkę do katalogu: ")
try:
    pliki = os.listdir(n)
except FileNotFoundError:
    n = input("Taki katalog nie istnieje, podaj poprawną ścieżkę: ")
    pliki = os.listdir(n)
zaszyfrowane = []
licznik = 1
for _ in pliki:
    if "plik_zaszyfrowany" in _:
        zaszyfrowane.append(_)
for _ in zaszyfrowane:
    czas = datetime.datetime.now()
    klucz = int(_[17])
    plik = open(n+"/"+_, "r")
    tekst = plik.read()
    tekst = SzyfrCezara.deszyfr(tekst, klucz)
    plik.close()
    licznik += 1
    nazwa = "/plik_deszyfrowany{}_{}{}{} nr {}.txt".format(klucz,czas.strftime("%Y"),czas.strftime("%m"),czas.strftime("%d"),licznik)
    plik2 = open(n+nazwa, "w")
    plik2.write(tekst)
    plik2.close()
