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

    # A while loop is called here to generate a new random 
    # character for the password and store them in the pwd variable 
    # per iteration of the while loop. This loop will continue until 
    # the criteria has been met (e.g. the password contains a number or a 
    # special character or both) and/or the password's minimum length has been reached or exceeded.

    # The pwd variable will be what the final password that is generated and ultimately printed out.
    # At the moment, meets_criteria is set to False by default and will change to True once the
    # password meets the criteria (e.g. has a number or a special character or both) and this will
    # be based on what is initially inputted into the generate_password function at the start.
    # has_number will tell us if the password has a number and has_special will tell us if the
    # password has a special character.

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_Length:
        
        # New random character generation by using random.choice(characters).
        # Essentially, this will select a random element (character) from the string of
        # letters that we initialised earlier using string.ascii_letters. Once
        # a random element is selected, it is concatenated to the pwd variable.
         
        new_char = random.choice(characters)
        pwd += new_char

        # If the new character added is in the digits variable, then the has_number
        # variable will be set to True. If the new character added is in the special
        # variable, then the has_special variable will also be set to True.

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Here meets_criteria is set to True before the if statements. The if
        # statements that follow will try prove that the meets_criteria is False and
        # will set meets_criteria to False if it should be False. If numbers is included
        # as a requirement for generating the password, then the meets_criteria will be
        # set to whatever the value of the has_number variable is. If has_number is True, then
        # the criteria is met, but if it is set to False, then meets_criteria will be False.
        # 
        # Afterwards, regardless of whether the numbers if statement returns True of False, if 
        # special characters is included as a requirement for generating the password, then
        # meets_criteria will be determined by the previously called meets_criteria variable and the
        # has_special variable. This means that one or both of the variables in this chained condition must be
        # BOTH TRUE for the meets_criteria to remain True, otherwise the value returned will be False. 

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    # Upon meets_criteria being met, the while loop is terminated and the generated password
    # is returned as the output of this function.

    return pwd

# The information require to generate the password is given by the user through inputting their
# values to the variables min_length, has_number and has special accordingly and the values in these
# variables are passed as parameters for the generated_password function. Finally, the output of the
# function is returned and printed out for the user.

min_length = int(input('Enter the minimum length: '))
has_number = input('Do you want to include numbers? (y/n): ').lower() == 'y'
has_special = input('Do you want to include special characters? (y/n): ').lower() == 'y'

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
