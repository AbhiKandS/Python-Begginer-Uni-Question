import math, re

isFloat =r'^[-+]?[0-9]+(\.[0-9]+)?([eE][-+]?[0-9]+)?$'
isPositiveFloat =r'^[+]?[0-9]+(\.[0-9]+)?([eE][-+]?[0-9]+)?$'
isInt =r'^[-+]?[0-9]+(\.[0]+)?$'

def isValid(ValidationType, s):
    s = str(s)
    ValidationType = str(ValidationType)
    ValidationType = ValidationType.lower()

    if ValidationType in ("f","float", "1"):
        return bool(re.match(isFloat, s))
    
    elif ValidationType in ("pf","+float", "2"):
        return bool(re.match(isPositiveFloat,s))
    
    elif ValidationType in ("i", "int", "3"):
        return bool(re.match(isInt, s))





def getInt(s):
    while 1:
        outputString = input(s)
        if isValid("i", outputString):
            return int(round(float(outputString)))

def getWhole(s):
    while 1:
        outputString = input(s)
        if outputString.isnumeric():
            return int(outputString)

def getFloat(s):
    while 1:
        outputString = input(s)
        if isValid("f", outputString):
            return float(outputString)

def getPositiveRealNumber(userPrompt):
    while 1:
        outputString = input(userPrompt)
        if isValid("pf", outputString):
            return float(outputString)

def modulus(s):
    s = float(s)
    return math.sqrt(s*s)
