import random
import string

def generate_password(min_Length, numbers=True, special_characters=True):
    
    # Obtains all the ascii letters (letters from a-z in both lower and upper caps), the numerical digits (0-9)
    # and the special characters, which refers to the punctuation characters on the QWERTY keyboard.
     
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

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

pwd = generate_password(10)
print(pwd)
