import re
tekst = input("Podaj tekst: ")
wynik = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",tekst)
print("Podane URL: {}",format(wynik))