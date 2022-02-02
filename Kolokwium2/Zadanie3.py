from modul import convert
import sys
klucz = sys.argv[1]
il=0
for x in klucz:
    if ord(x)>47 and ord(x)<58:
        il+=1
if(il==16):
    klucz2=convert(klucz)
    klucz21 = int(klucz2[0:4])
    klucz22 = int(klucz2[5:9])
    klucz23 = int(klucz2[10:14])
    klucz24 = int(klucz2[15:19])
    print(klucz21,klucz22,klucz23,klucz24)
    if klucz21%3==0 and klucz22%3==0 and klucz23%3==0 and klucz24%3==0:
        print("Klucz jest prawidlowy")
        print(klucz2)
    else:
        print(("Klucz jest nieprawidlowy"))
else:
    print("Wprowadzone dane sa niepoprawne")