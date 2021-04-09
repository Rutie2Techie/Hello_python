#print vowels from list of letters

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def check_vowel(letter):
     vowels=['a','e','i','o','u']
     if(letter in vowels):
         return True
     else:
        return False


# function that filters vowels

filteredVowels = list(filter(check_vowel, letters))
for vowel in filteredVowels:
    print(vowel)
#print(filteredVowels)





