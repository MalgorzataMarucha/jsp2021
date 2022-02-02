import urllib.request as ur
url=input("Podaj link do wybranej strony: ")
try:
    ur.urlopen(url)
    if(url[-1]=="/"):
        nazwa="index.html"
    else:
        nazwa=url.split("/")
        print(nazwa)
        nazwa=nazwa[-1]
    ur.urlretrieve(url,nazwa)
except:
    print("Strona nie istnieje!")
