def fib(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return fib(N-1)+fib(N-2)
N=int(input("Podaj liczbę wyrazów ciągu Fibonacciego:"))
for a in range(0,N):
    print(fib(a))