import isreal
evenArray = [None]*8

for i in range(8):
    evenArray[i]=2*(i)

print("a.", evenArray)
print("b. length of array: ", len(evenArray))

while 1:
    deletionIndex = getInt("Enter index of string to delete: ") 
    if deletionIndex in range(len(evenArray)):
        previouItem = evenArray
        previousIndex = deletionIndex-1

        evenArray[previousIndex].next()= evenArray[deletionIndex].next()
        print(evenArray)
        break
    else:
        print("Index out of Range\n")
