import time
czas1=time.time_ns()
def fib(N):
    if(N==0):
        return 1
    if(N==1):
        return 1
    else:
        lista=[0,1]
        for x in range(N-2):
            nowa=lista[-1]+lista[-2]
            lista.append(nowa)
    print(lista)
N=int(input("Podaj liczbę wyrazów ciągu Fibonacciego: "))
fib(N)
czas2=time.time_ns()
print("Tak długo wykonywała się funkcja: ",(czas2-czas1)/(10**9),"sec")