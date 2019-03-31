def fib(n,k):
    f1=f2=1
    for i in range (2,n):
        f1,f2=f2,f1*k+f2
    print(f2)

fib(29,5)
