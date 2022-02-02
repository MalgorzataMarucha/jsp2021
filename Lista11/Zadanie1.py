from email import header
import urllib.request as ur
url=input("Podaj link do wybranej strony: ")
try:
    ur.urlopen(url)
    print("Strona istnieje!")
except:
    print("Strona nie istnieje!")