import isreal

list1=[]
list2=[]
n = isreal.getInt("Enter length of lists: ") 

for i in range(2):
    for j in range(n):
        elementOfList = input(f"Enter {j} element of list{i+1}: ")
        list1.append(elementOfList) if (i==0) else list2.append(elementOfList)

print("a. adding two list: ", list1+list2)

print("b. both lists are same") if list1==list2 else print("both lists are different")

print("c. length of lists: ", len(list1))

print("d. sorted list\n", list1.sort(), "\n", list2.sort())

print("e. reversed list\n", list1.reverse(), "\n", list2.reverse())
