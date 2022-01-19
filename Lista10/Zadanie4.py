import xml.etree.ElementTree as et
class Kursy:
    def __init__(self, gdzie):
        self.gdzie = gdzie
    def lista(self):
        tree = et.parse(self.gdzie)
        root = tree.getroot()
        print("Wszystkie waluty: ")
        for x in root.findall("pozycja"):
            print(x[0].text)
        return ""
    def PLN(self):
        tree = et.parse(self.gdzie)
        root = tree.getroot()
        waluta=input("Podaj walutę: ")
        opcja=int(input("Z PLN na twoją walutę (wciśnij 1), z twojej waluty na PLN (wciśnij 2): "))
        if(opcja==1):
            ile=float(input("Podaj kwotę PLN: "))
            for x in root.findall("pozycja"):
                if(x[0].text == waluta):
                    nazwa=x[2].text
                    kurs_sredni=x[3].text.replace(",", ".")
                    przelicznik=ile*float(x[1].text)/float(kurs_sredni)
                    print(przelicznik,"",nazwa)
        if(opcja==2):
            ile=float(input("Podaj kwotę swojej waluty: "))
            for x in root.findall("pozycja"):
                if(x[0].text == waluta):
                    kurs_sredni=x[3].text.replace(",", ".")
                    przelicznik=ile/float(x[1].text)*float(kurs_sredni)
                    print(przelicznik," PLN")
        return ""
    def konwersja(self):
        tree = et.parse(self.gdzie)
        root = tree.getroot()
        waluta1=input("Podaj walutę, z której chcesz przeliczyć: ")
        waluta2=input("Podaj walutę, na którą chcesz przeliczyć: ")
        ile=float(input("Podaj kwotę: "))
        for x in root.findall("pozycja"):
            if(x[0].text == waluta1):
                kurs_sredni1=x[3].text.replace(",", ".")
                przelicznik1=x[1].text
            if(x[0].text == waluta2):
                kurs_sredni2=x[3].text.replace(",", ".")
                przelicznik2=x[1].text
                nazwa=x[2].text
        przelicznik = (ile/float(przelicznik1)*float(kurs_sredni1))*float(przelicznik2)/float(kurs_sredni2)
        print(przelicznik,"",nazwa)
        return ""

kursy = Kursy("waluty.xml")
print(kursy.lista())
print(kursy.PLN())
print(kursy.konwersja())