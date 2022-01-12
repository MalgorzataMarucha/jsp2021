import sys
import numpy as np
print("Nazwa programu: ",sys.argv[0])
del sys.argv[0]
argumenty = sys.argv
print("Oto twoje dane pomiarowe: ",argumenty)
lista=[]
for _ in range(len(argumenty)):
    lista.append(int(argumenty[_]))
print("Twoja średnia: ",np.mean(lista))
print("Twoja wariancja: ",np.var(lista))
print("Twoje odchylenie standardowe: ",np.std(lista))