#  LIST METHODS 
#     clear method : This method removes all the items inside a list

list1 = [1,1,5.6,9,False]
list1.clear()
# print(list1)

# list count method :  This method returns the number of items with the value specified

check1 = list1.count(0)

# print(check1)

# list extend method : This method adds an item to the end of the current list or any other iterable

list2 = ["2",6.4,False,14,15]

# Extend list1 with list2

list1.extend(list2)

# print(newlst)

# List index method : This method is used to return the index of the first occurence of an item in a list or iterable

needle = list1.index(False)

# print(list1)
# print(needle)

# List remove method : This method is used to remove items at a specified index position

list3 = [1,2,3,4,5,6,7,8]

list3.remove(2)

# print(list3)

# List append method: This method appends an item to the end of a list

listX= [9,10]

list3.append(11)

# print(len(list3))

list3.extend(listX)
# list3.append(listX)

# print(list3)

#  List copy method : This method is used to make a copy of a list

new_list = list3.copy()

# print(new_list)

# List insert method : This method adds a new value to a specifice position

list3.insert(1,True)

print(list3)