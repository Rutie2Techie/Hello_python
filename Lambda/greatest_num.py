# find lambda function to check gretest number out of 2

from functools import reduce

find_greater = lambda x, y: x if x > y else y
print(find_greater(23, 45))
list4 = [23, 54, 45, 56]
reduce(find_greater, list4)
list7=[34,56,43,53]
reduce(find_greater,list7)
