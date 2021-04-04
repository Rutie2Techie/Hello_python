# create list1 with elements ranging from 50 to 200 with step 3
# create lambda function to check whether number is divisible by 4 or not
# using lambda function created above filter the elemements from list1 which are divible by 4 and store them into list 2
# create a lambda function to find square root of a number
# using the above created lambda function
# find the square root all the elements on list2 and store the result into list3
from typing import Any, Callable, Union

list1 = list(range(50, 200, 3))
div_4 = lambda x: x % 4 == 0
list2 = list(filter(div_4, list1))
print(list2)
sqrt = lambda x: x ** (1 / 2)
list3 = list(map(sqrt, list2))
print(list3)
