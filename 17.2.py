import isReal

def deleteArray(array, deletionIndex)

evenArray = [None]*8
arrayLength = len(evenArray)

for i in range(arrayLength):
    evenArray[i] = i*2

print("a.: ", evenArray)
print("b. length of array: ", arrayLength)

while(1):
    deletionIndex = isReal.getWhole(f"Enter a index from 0-{arrayLength-1} to be deleted: ")
    
    if deletionIndex in range(arrayLength):
        break

i = deletionIndex
while i < (arrayLength-1):
    evenArray[i] = evenArray[i+1]
    i= i+1

evenArray[arrayLength-1] = None

print(evenArray)
