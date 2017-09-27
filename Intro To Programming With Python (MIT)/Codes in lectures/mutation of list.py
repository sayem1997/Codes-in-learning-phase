list1 = [1,2,3,4,5,6,7]
list2 = [5,6,7,8,9,10]
list1_copy = list1[:]
for element in list1_copy: #here if list1 is been used it will not remove 6, because
                            #here index get changed when we remove any number from any list
    if element in list2:
        list1.remove(element)

print(list1)
## Check this in pythontutuor.com