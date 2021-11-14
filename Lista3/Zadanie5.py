import re
print("Twoje hasło musi posiadać: małą i dużą literę oraz znak specjalny ($#@).")
print("Twoje hasło musi mieć długość od 6 do 16 znaków.")
haslo=input("Podaj haslo:")
min_dlugosc=6
max_dlugosc=16
ml= re.search(r"(?=.*[a-z])",haslo)
if re.search(r"(?=.*[a-z])",haslo) == None:
    print("Hasło nie posiada małej litery!")
elif re.search(r"(?=.*[A-Z])",haslo) == None:
    print("Hasło nie posiada dużej litery!")
elif re.search(r"(?=.*[$#@])",haslo) == None:
    print("Hasło nie posiada, któregoś z danych znaków: $#@!")
elif len(haslo) < int(min_dlugosc):
    print("Hasło jest za krótkie!")
elif len(haslo) > int(max_dlugosc):
    print("Hasło jest za długie!")

    