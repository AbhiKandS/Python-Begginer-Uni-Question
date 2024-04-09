import isReal

a = isReal.getInt("Enter an integer: ")
n= isReal.getWhole("Enter Table length: ")
for i in range(1, n+1):
    print(f"{a} x {i} = {a*i}")
