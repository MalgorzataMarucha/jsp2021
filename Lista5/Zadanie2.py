def zapis(n):
    lista = {
        0:"",
        1:"Jeden",
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
        60:"Szescdziesiat",
        70:"Siedemdziesiat",
        80:"Osiemdziesiat",
        90:"Dziewiecdziesiat",
        100:"Sto",
        200:"Dwiescie",
        300:"Trzysta",
        400:"Czterysta",
        500:"Piecset",
        600:"Szescset",
        700:"Siedemset",
        800:"Osiemset",
        900:"Dziewiecset",
        1000:"Tysiac",
    }
    x = 100
    counter = len(n)-1
    napis = ""
    i=0
    j=0
    while counter-2 >= 0:
        if n[len(n)-2]=='1' and j==0:
            napis+=lista[int(n[-2:])] + " "
            j=1
        elif i==0 and j==0:
            napis+=lista[10*int(n[len(n)-2])] + lista[int(n[len(n)-1])] + " "
            i=1
        
        napis+=lista[x * int(n[counter-2])] + " "
        counter -= 1
        x *= 10
    if(len(n)==2):
        if n[len(n)-2]=='1':
            napis+=lista[int(n[-2:])] 
            return napis
        else:
            napis+=lista[int(n[0])*10] + " " + lista[int(n[1])]
            return napis
    if(len(n)==1):
        napis+=lista[int(n[0])]

    napis2 = napis.split(" ")
    napis2.reverse()
    return " ".join(napis2)


n = input("Podaj liczbe z zakresu 1-1999: ")
print(zapis(n))