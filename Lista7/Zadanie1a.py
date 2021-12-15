import time
czas1=time.time_ns()
def fib(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return fib(N-1)+fib(N-2)
N=int(input("Podaj liczbę wyrazów ciągu Fibonacciego:"))
fibo=[fib(a) for a in range(N)]
print(fibo)
czas2=time.time_ns()
print("Tak długo wykonywała się funkcja: ",(czas2-czas1)/(10**9),"sec")