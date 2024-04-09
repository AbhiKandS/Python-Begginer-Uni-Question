import isReal

def gcdOf(a,b):
    if b==0:
        return a
    else:
        return gcdOf(b,a%b)

a=isReal.getWhole("Enter 1st number: ")
b=isReal.getWhole("Enter 2nd number: ")

m=gcdOf(a,b)
print(m)


