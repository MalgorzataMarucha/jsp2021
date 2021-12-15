def ciag(n):
    ile=1
    s=""
    ciag=""
    if(n==1):
        print("1")
    if(n<=0):
        print("Podaj liczbę większą niż 0!")
    if(n==2):
        print("1")
        print("11")
    if(n==3):
        print("1")
        print("11")
        print("21")
    if(n>3):
        print("1")
        print("11")
        print("21")
        y=3
        s="21"
        while y < n:
            ile=1
            for x in range(len(s)):
                if(s[x] == s[x+1]):
                    ile+=1
                if(s[x] != s[x+1]):
                    ciag+=str(ile)+s[x]
                    ile=1
                if x+1==len(s)-1:
                    ciag+=str(ile)+s[x+1]
                    break
            print(ciag)
            s=ciag
            ciag=""
            y+=1

n=int(input("Podaj długość ciągu: "))
ciag(n)

