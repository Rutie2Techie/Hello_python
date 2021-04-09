#using reduce find addition of numbers



from functools import reduce   #imported library to use reduce function
numbers=[2,4,5,6]
summed=reduce(lambda a,b:a+b,numbers)
print(summed)