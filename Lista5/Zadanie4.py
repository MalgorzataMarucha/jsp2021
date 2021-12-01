klucz={"a" : "y","e" : "i","i" : "o","o" : "a","y" : "e"}
klucz2={"y" : "a","i" : "e","o" : "i","a" : "o","e" : "y"}
def szyfr(n):
    napis = ""
    for x in n:
        if x in klucz.keys():
            napis += klucz[x]
        else:
            napis += x
    return napis
n = input("Podaj tekst do zaszyfrowania: ")
print(szyfr(n))
def deszyfr(n):
    napis = ""
    for x in n:
        if x in klucz2.keys():
            napis += klucz2[x]
        else:
            napis += x
    return napis
n = input("Podaj tekst do deszyfrowania: ")
print(deszyfr(n))
