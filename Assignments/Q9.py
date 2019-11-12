                            #QUESTION 9

# Write a program with a function that accepts a string as an argument and returns the number of vowels that the string contains. The application should have another function that accepts a string as an argument and returns the number of consonants that the string contains. The application should let the user enter a string, and should display the number of vowels and the number of consonants it contains.

def calculate_vowels(string):
    vowels = 'aeiou'
    number_of_vowels= 0
    for i in string:
        if i.lower() in vowels:
            number_of_vowels +=1
    return number_of_vowels


def calculate_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    number_of_consonants = 0
    for j in string:
        if j.lower() in consonants:
            number_of_consonants +=1
    return number_of_consonants

user_input = input("Enter a string of characters")

vowels = calculate_vowels(user_input)
consonants = calculate_consonants(user_input)

print("The number of vowels are " + str(vowels)  +  " and" + " " + "The number of consonants are " + str(consonants))

