def check_even(number):
    even_lam = lambda a: a % 2 == 0
    return even_lam(number)


print(check_even(2))

