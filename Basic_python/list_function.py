#Difference between append and extend function

#add 2 elements to a list


list1=[23,56,43,87]
list1.append([65,89])
print(list1)
print('----------*----------')
list1.extend([23,76])
print(list1)

list1.reverse()      #reversed the list
print(list1)

list1.pop()  #removed last element from list
