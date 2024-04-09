a=0
b=1
tmp = a

c=int(input("Fibbonacci sequence till number: "))
print(f"{a}, ")
while b<=c:
    print(f"{b}, ")
    tmp = b
    b=b+a
    a=tmp
