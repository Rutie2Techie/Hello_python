## Passing Multiple Iterators to map() Using Lambda
## In this example, corresponding items of two lists are added.

list1=[2,4,6,7]
list2=[4,6,2,8]
addition=list(map(lambda num1,num2:num1+num2,list1,list2))
print(addition)