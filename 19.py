def filterMultiples5(array1):
    array2 = list(filter(lambda x: x % 5 == 0, array1))
    return array2


list1 = (1, 25, 50, 34, 35, 101)
list1 = filterMultiples5(list1)
print(list1)
