#Find maximum number from list of numbers

values=[3,14,7,2,7,9]
from functools import reduce
max=reduce(lambda x,y:x if x>y else y,values)
print("maximum number from list is:",end=" ")
print(max)