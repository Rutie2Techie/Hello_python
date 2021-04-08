#calculate square of numbers using map function

def calsquare(num):
  return num*num

number=[2,4,6,8]
result=map(calsquare,number)
print(result)
#converting map object to tuple
numsquare=tuple(result)
print(numsquare)