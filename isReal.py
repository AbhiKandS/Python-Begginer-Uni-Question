import math

def isReal(s):
    import re
    s = str(s)
    p =r'^[-+]?[0-9]+(\.[0-9]+)?([eE][-+]?[0-9]+)?$'
    return True if re.match(p,s) else False

def isInt(s):
    import re
    s = str(s)
    p =r'^[-+]?[0-9]+$'
    return True if re.match(p,s) else False

def isPositiveReal(s):
    import re
    s = str(s)
    p =r'^[+]?[0-9]+(\.[0-9]+)?([eE][-+]?[0-9]+)?$'
    return True if re.match(p,s) else False







def getInt(s):
    while 1:
        outputString = input(s)
        if isInt(outputString):
            return int(outputString)

def getWhole(s):
    while 1:
        outputString = input(s)
        if outputString.isnumeric():
            return int(outputString)

def getFloat(s):
    while 1:
        outputString = input(s)
        if isReal(outputString):
            return float(outputString)

def getPositiveRealNumber(userPrompt):
    while 1:
        outputString = input(userPrompt)
        if isPositiveReal(outputString):
            return float(outputString)

def modulus(s):
    s = float(s)
    return math.sqrt(s*s)
