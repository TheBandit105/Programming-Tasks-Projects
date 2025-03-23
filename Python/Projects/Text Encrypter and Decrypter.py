def encrypt_and_decrypt(wordEncryptDecrypt, key):
    
    """
    Encrypts and then decrypts a given word using a Caesar cipher.

    This function takes a word, encrypts it using the provided key,
    and then decrypts the encrypted word back to its original form.
    It preserves the case of letters and leaves non-alphabetic characters unchanged.

    Parameters:
    wordEncryptDecrypt (str): The word to be encrypted and then decrypted.
    key (int): The shift value for the Caesar cipher (0-25).

    Returns:
    str: A formatted string containing both the encrypted and decrypted messages.
    """

    encryptedWord = ''
    decryptedWord = ''

    for letter in wordEncryptDecrypt:
        if letter.isalpha():
            if letter.islower():
                encryptedWord += chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
            else:
                encryptedWord += chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
        else:
            encryptedWord += letter

    for letter in encryptedWord:
        if letter.isalpha():
            if letter.islower():
                decryptedWord += chr((ord(letter) - ord('a') - key) % 26 + ord('a'))
            else:
                decryptedWord += chr((ord(letter) - ord('A') - key) % 26 + ord('A'))
        else:
            decryptedWord += letter

    return f'\nEncrypted message: {encryptedWord} \nDecrypted message: {decryptedWord}\n'

def encrypt(wordEncrypt, key):

    """
    Encrypts a given word using a Caesar cipher.

    This function takes a word and encrypts it using the provided key.
    It preserves the case of letters and leaves non-alphabetic characters unchanged.

    Parameters:
    wordEncrypt (str): The word to be encrypted.
    key (int): The shift value for the Caesar cipher (0-25).

    Returns:
    str: The encrypted word.
    """

    encryptedWord = ''

    for letter in wordEncrypt:
        if letter.isalpha():
            if letter.islower():
                encryptedWord += chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
            else:
                encryptedWord += chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
        else:
            encryptedWord += letter

    return encryptedWord

def decrypt(wordDecrypt, key):

    """
    Decrypts a given word using a Caesar cipher.

    This function takes an encrypted word and decrypts it using the provided key.
    It preserves the case of letters and leaves non-alphabetic characters unchanged.

    Parameters:
    wordDecrypt (str): The encrypted word to be decrypted.
    key (int): The shift value for the Caesar cipher (0-25).

    Returns:
    str: The decrypted word.
    """

    decryptedWord = ''

    for letter in wordDecrypt:
        if letter.isalpha():
            if letter.islower():
                decryptedWord += chr((ord(letter) - ord('a') - key) % 26 + ord('a'))
            else:
                decryptedWord += chr((ord(letter) - ord('A') - key) % 26 + ord('A'))
        else:
            decryptedWord += letter

    return decryptedWord

def main():

    """
    The main() function serves as the entry point of the program and runs an interactive loop
    that allows the user to encrypt, decrypt, or both encrypt & decrypt a word using a 
    Caesar cipher-like approach.
    
    1. The function starts an infinite loop using `while True:` to continuously prompt the user for input.
    The loop will only terminate when the user explicitly chooses to quit.
    
    2. The user is prompted to enter a choice (`selector`) to determine what action they want to perform:
    - 'E' or 'e' for encryption
    - 'D' or 'd' for decryption
    - 'ed' or 'ED' for both encryption and decryption
    - 'Q' or 'q' to quit the program
    
    3. If the user selects encryption ('E' or 'e'):
    - The program prompts the user to input the word they want to encrypt (`wordEncrypt`).
    - It then asks for a numeric key (`key`) between 0 and 25, which determines the shift for encryption.
    - If the key is out of the valid range (0-25), the program informs the user and asks them to try again.
    - Otherwise, it calls the `encrypt()` function (assumed to be defined elsewhere) to encrypt the word.
    - The encrypted message is displayed to the user.
    
    4. If the user selects decryption ('D' or 'd'):
    - The program prompts the user to input the encrypted word they want to decrypt (`wordDecrypt`).
    - It then asks for a numeric key (`key`), reminding the user that it should match the key used for encryption.
    - If the key is out of range (0-25), an error message is displayed.
    - Otherwise, the `decrypt()` function is called to decrypt the message, and the result is displayed.
    
    5. If the user selects both encryption & decryption ('ed' or 'ED'):
    - The user is asked to input a word (`wordEncryptDecrypt`) that will be encrypted and then decrypted.
    - They must also provide a valid key (0-25).
    - If the key is invalid, an error message is displayed.
    - Otherwise, the function `encrypt_and_decrypt()` is called, and the final result is displayed.
    
    6. If the user selects 'Q' or 'q', the program prints a newline (`\n`) and exits the loop using `break`, 
    which ends the program.
    
    7. If the user enters an invalid input (anything other than the expected options), an error message is displayed,
    and the program prompts them to try again.
    
    8. The script includes the standard Python check:
    `if __name__ == "__main__":` 
    - This ensures that `main()` is executed only when the script is run directly and not when imported as a module.
    """

    while True:

        selector = input('Do you wish to encrypt, decrypt or do both at the same time to the word (encrypt => e or E, decrypt => d or D, encrypt & decrypt => ed or ED)? Press q or Q to quit. ')

        if selector == 'E' or selector == 'e':
            wordEncrypt = input('\nPlease type the word you would like to encrypt: ')
            key = int(input('Input the key (0 - 25): '))

            if key > 25 or key < 0:
                print('Invalid key, must be in the range 0 - 25, please try again.')
            else:
                message_encrypted = encrypt(wordEncrypt, key)
                print(f'\nEncrypted message: {message_encrypted}\n')

        elif selector == 'D' or selector == 'd':

            wordDecrypt = input('\nPlease type the encrypted word you would like to decrypt: ')
            key = int(input('Input the key (0 - 25), but please ensure that it is the same key that you had used to orignally encrypt the message otherwise the encrypted word wil be decrypted incorrectly: '))

            if key > 25 or key < 0:
                print('Invalid key, must be in the range 0 - 25, please try again.')
            else:
                message_decrypted = decrypt(wordDecrypt, key)
                print(f'\nDecrypted message: {message_decrypted}\n')
        
        elif selector == 'ed' or selector == 'ED':

            wordEncryptDecrypt = input('\nPlease type the word you would like to encrypt, then decrypt after: ')
            key = int(input('Input the key (0 - 25): '))

            if key > 25 or key < 0:
                print('Invalid key, must be in the range 0 - 25, please try again.')
            else:
                message_encrypted_and_decrypted = encrypt_and_decrypt(wordEncryptDecrypt, key)
                print(message_encrypted_and_decrypted)

        elif selector == 'Q' or selector == 'q':
            print('\n')
            break

        else:
            print('\nInvalid mode. Please try again!\n')

if __name__ == "__main__":
    main()
    

