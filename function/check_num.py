#Check if the number is positive or negative or zero and display an appropriate message.

def checkNum(num):
    if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print("Negative number")


num = float(input("Enter a number: "))
checkNum(num)
