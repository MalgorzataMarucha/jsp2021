a=input("Podaj napis:")
pl = a[0]
napis = a[1:]
napis=napis.replace(pl,"$")
print(pl+napis)