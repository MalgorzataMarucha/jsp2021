def words2numbers(n):
    konwersja={     1:"Jeden",
                    2:"Dwa",
                    3:"Trzy",
                    4:"Cztery",
                    5:"Piec",
                    6:"Szesc",
                    7:"Siedem",
                    8:"Osiem",
                    9:"Dziewiec",
                    10:"Dziesiec",
                    11:"Jedenascie",
                    12:"Dwanascie",
                    13:"Trzynascie",
                    14:"Czternascie",
                    15:"Pietnascie",
                    16:"Szesnascie",
                    17:"Siedemnascie",
                    18:"Osiemnascie",
                    19:"Dziewietnascie",
                    20:"Dwadziescia",
                    30:"Trzydziesci",
                    40:"Czterdziesci",
                    50:"Piecdziesiat",
    }
    konwersja = {v:k for k,v in konwersja.items()}
    if "Dwadziescia" in n and len(n) > 11:
        words = n.split(" ")
        return konwersja[words[0]] + konwersja[words[1]]
    elif "Trzydziesci" in n and len(n) > 11:
        words = n.split(" ")
        return konwersja[words[0]] + konwersja[words[1]]
    elif "Czterdziesci" in n and len(n) > 12:
        words = n.split(" ")
        return konwersja[words[0]] + konwersja[words[1]]    
    elif "Piecdziesiat" in n and len(n) > 12:
        words = n.split(" ")
        return konwersja[words[0]] + konwersja[words[1]]
    return konwersja[n]
n=(input("Podaj liczbę: "))
print(words2numbers(n))
