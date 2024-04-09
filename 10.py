import isReal, math

userNumber = isReal.getWhole("Enter a Whole Numer: ")

temp = str(userNumber)
lengthOfNumber = len(temp)
sum = 0
for i in range(lengthOfNumber):
    sum = sum + math.pow(int(temp[i]), lengthOfNumber)
if sum == userNumber:
    print(userNumber, "is an armstrong number")
else:
    print(userNumber, "is not an armstrong number")
