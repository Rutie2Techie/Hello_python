sum_lam = lambda a, b: a + b
sub_lam = lambda a, b: a - b
mul_lam = lambda a, b: a * b
div_lam = lambda a, b: a / b


def accept_inputs():
    op1 = float(input("enter 1st operand:"))
    op2 = float(input("enter 2nd operand:"))
    return


while True:
    op1 = float(input("enter 1st operand:"))
    op2 = float(input("enter 2nd operand:"))
    option = input("enter an option like +, - ,/ ,*")
    if option == '+':
        print("addition is:", sum_lam(op1, op2))
    elif option == '-':
        print("subtraction is:", sub_lam(op1, op2))
    elif option == '*':
        print("multiplication is:", mul_lam(op1, op2))
    elif option == '/':
        if op2 != 0:
            print("division is:", div_lam(op1, op2))
        else:
            print("div by zero error")
    else:
        break;

