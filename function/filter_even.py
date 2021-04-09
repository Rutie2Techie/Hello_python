#find even and odd number from list of numbers using filter function

numbers=[1,2,3,4,5,6,7,8,9,10]
#here we are using list to print values in output
even=list(filter(lambda x:x%2==0,numbers))
odd=list(filter(lambda x:x%2==1,numbers))

print(even)
print(odd)