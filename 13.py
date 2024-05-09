def feibonnaci(c):
    int(c)
    return {
        c <= 1: 0,
        c == 2: 1,
        c > 2: feibonnaci(c - 1) + feibonnaci(c - 2),
    }[True]


c = int(input("Fibbonacci sequence till number: "))
print(feibonnaci(c))
