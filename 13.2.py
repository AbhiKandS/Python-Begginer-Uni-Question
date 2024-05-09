import isReal


def fib(a, b, c, i):
    if a <= c:
        print(f"{a}, ", end="")
        i = i + 1
        fib(b, a+b, c, i)
    else:
        print(i)


fibbonacciTill = isReal.getPositiveRealNumber("Print Fibbonacci till: ")
fib(0, 1, fibbonacciTill, 0)
