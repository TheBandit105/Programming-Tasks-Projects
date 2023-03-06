import random
import string

# The function generate_password calls in 3 parameters. The first, min_Length
# is a compulsory parameter, which returns the password of that length. The other two
# parameters, numbers and special characters, are optional, but have been set to
# True as default unless specified otherwise.

def generate_password(min_Length, numbers=True, special_characters=True):
    
    # By importing the string module, all the ascii letters (letters from a-z in both lower and upper caps), 
    # the numerical digits (0-9) and the special characters, which refers to the punctuation characters 
    # on the QWERTY keyboard, can be accessed.
     
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Since letters are always going to be in the password,
    # no matter what the password is, so the characters variable
    # is going to contain the letters variable.

    characters = letters

    # If either numbers or special_characters or both have been 
    # set to True, this will allow the program to be able to
    # access the numbers or special characters or both by
    # concatenating them to the characters variable during the 
    # password generation.

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_Length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True 

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd

min_length = int(input('Enter the minimum length: '))
has_number = input('Do you want to include numbers? (y/n): ').lower() == 'y'
has_special = input('Do you want to include special characters? (y/n): ').lower() == 'y'

pwd = generate_password(min_length, has_number, has_special)
print(pwd)
