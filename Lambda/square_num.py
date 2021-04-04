#create a  list1 with elements raning from 10 to 20
#create a lambda function to find square of number
#and using this lambda function, find the square of each number that we have in list1

list1=list(range(10,20))
sqr_lam=lambda x: x**2
list2=list(map(sqr_lam,list1))
print(list1)
print(list2)

