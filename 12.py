import isReal

def fact(a):
    return 1 if a<=1 else a*fact(a-1)
    
userInput = isReal.getWhole("Enter a whole number: ") 
print(fact(userInput))
