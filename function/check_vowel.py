#Print your name without vowels using function


def checkvowelinname(name):
    name=name.lower()

    for letter in name:
        if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
            continue                #continue statement skips the statement after it
        else:
            print(letter,end=" ")

checkvowelinname('Rutuja Patil')