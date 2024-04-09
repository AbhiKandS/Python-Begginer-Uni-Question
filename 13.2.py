import isReal

def fib(a,b,c):
    if a<=c:
        print(f"{a}, ", end="")
        return fib(b, a+b, c)
    else:
        return 0

fibbonacciTill = isReal.getPositiveRealNumber("Print Fibbonacci till: ")
fib(0,1,fibbonacciTill)
