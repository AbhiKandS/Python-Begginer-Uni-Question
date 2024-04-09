str2 = "This is my string"

#a
str1 = input("Find:")
x= str2.find(str1)
stringFound = 1 if(x>0) else 0
print("a. Search string Index: ", end="")

if stringFound:
    print(x)
else:
    print("Not Found")

#b
print("b. uppercase: "+str2.upper())

#c
print("c. length:", len(str2))

#d
print("d. max: ", max(str2), "min: ", min(str2))

#e
print("e. from index 1-5: ", str2[1:5])
