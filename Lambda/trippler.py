#Function inside a function to double and thrice a number

def myfun(n):
  return lambda a: a*n
mydoubler=myfun(2)
mytrippler=myfun(3)

print(mydoubler(12))
print(mytrippler(23))