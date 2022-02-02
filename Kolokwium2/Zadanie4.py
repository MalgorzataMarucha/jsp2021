class Time:
    def __init__(self,ile,jednostka):
        self.ile=ile
        self.jednostka=jednostka
    def __add__(self,i):
        return Time(self.ile+i.ile,'s')
    def __sub__(self,i):
        return Time(self.ile-i.ile,'s')
    def konwersja(self,how):
        sekundy=0
        if(how == "ms"):
            if(self.jednostka=="s"):
                sekundy+= self.ile
            elif(self.jednostka=="m"):
                sekundy+=(self.ile*60)
        elif(how == "hms"):
            if(self.jednostka=="s"):
                sekundy+= self.ile
            elif(self.jednostka=="m"):
                sekundy+=(self.ile*60)
            elif(self.jednostka=="h"):
                sekundy+=(self.ile*60*60)
        sek=sekundy
        sek2m = 60
        sek2h = 60*60
        godziny = sek//sek2h
        minuty = (sek-(godziny*sek2h))//sek2m
        sekundy = (sek-(godziny*sek2h)-(minuty*sek2m))
        if(how == "ms"):
            print(minuty,"m",sekundy,"s")
        elif(how == "hms"):
            print(godziny,"h",minuty,"m",sekundy,"s")
x = Time(10,"s")
y = Time(1,"m")
z = Time(0.5,"h")
w=z-y+x
print(w.konwersja("hms"))

