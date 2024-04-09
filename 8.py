import isReal

while(1):
    m=isReal.getFloat("Enter grade: ")

    if 100>=m>90:
        g="A"
    elif(90>=m>80):
        g="B"
    elif(80>=m>70):
        g="C"
    elif(70>=m>60):
        g="D"
    elif(60>=m>50):
        g="E"
    elif(50>=m>=0):
        g="F"
    else:
        print("Error: marks from 0-100")
        continue

    print(g, "grade")
    break
