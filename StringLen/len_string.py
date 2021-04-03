# This is program is to count number of characters in string without using len function

def len_counter(source_string):
    count = 0
    for i in source_string:
        count += 1
    return count


input_string = "This is Ruite"
print(len(input_string))
print(len_counter(input_string))
