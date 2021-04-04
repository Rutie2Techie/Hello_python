# Create a list and name it as list1 with elements ranging from 100 to 200 with step 4
# create lambda function to find number is divisible by 5 or not
# using lambda function   filter number divisible by 5 from list1 and store them in list2

list1 = list(range(100, 200, 4))
div_5 = lambda a: a % 5 == 0
list2 = list(filter(div_5, list1))
print(list1)
print(list2)
