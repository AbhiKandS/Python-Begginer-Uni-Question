def filterMultiples5(array1):
    return list(filter(lambda x: x % 5 == 0, array1))


list1 = (1, 25, 50, 34, 35, 101)
filteredList = filterMultiples5(list1)
print(filteredList)
