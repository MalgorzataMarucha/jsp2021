import SzyfrCezara
wybierz=int(input("Wybierz czynność: 1 - szyfrowanie, 2 - deszyfrowanie: "))
tekst=input("Podaj tekst: ")
klucz=int(input("Podaj klucz: "))
if(wybierz==1):
    SzyfrCezara.szyfr(tekst,klucz)
if(wybierz==2):
    SzyfrCezara.deszyfr(tekst,klucz)
