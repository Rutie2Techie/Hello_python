#find factorial of number

def factorial(x):
     if x<=1:
         return 1
     else:
         return x*factorial(x-1)    #recursive function used here
num=4
print("factorial of ",num,"is:",factorial(num))
