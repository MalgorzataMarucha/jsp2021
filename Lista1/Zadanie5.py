import math
print(5//2) #Dzielenie bez reszty (5//2) zaokrągla wynik zawsze do całości ingorując dalszą część po przecinku(zamiast 2.5 pokazuje tylko 2)
print(math.floor(7/2)) #Zaokrąglanie liczby zmiennoprzecinkowej za pomocą floor() zawsze zaokrągla nam wynik w dół.
print(round(11/3))
print(round(5/2)) #Zaokrąglanie liczby zmiennoprzecinkowej za pomocą round(): Jeśli część całkowita wyniku dzielenia jest parzysta to Python zaokrągla ją w dół. Jeśli część całkowita wyniku dzielenia jest nieparzysta - jest zaokrąglane w góre.