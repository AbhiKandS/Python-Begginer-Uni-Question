import math, isReal

float1 = isReal.getWhole("Enter a whole Number: ")
p = isReal.getFloat("Enter a power: ")
x = math.ceil(float1)

#a
print("a. Rounding to int:", x)

#b
print("b. Sqrt:", math.sqrt(float1))


#c
print("c. power", math.pow(float1, p))

#d
print("d. factorial", math.factorial(x))
