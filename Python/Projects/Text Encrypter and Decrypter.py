
def main():
    
    while True:

        selector = input('Do you wish to encrypt or decrypt the word (encrypt => e or E, decrypt => d or D)? Press q or Q to quit.')

        if selector == 'E' or selector == 'e':
            wordEncrypt = input('Please type the word you would like to encrypt: ')
            key = int(input('Input the key (0 - 25)'))

            message_encrypted = encrypt(wordEncrypt, key)
            print(f'Encrypted message: {message_encrypted}')

        elif selector == 'D' or selector == 'd':

            wordDecrypt = input('Please type the encrypted word you would like to decrypt: ')
            key = int(input('Input the key (0 - 25), but please ensure that it is the same key that you had used to orignally encrypt the message otherwise the encrypted word wil be decrypted incorrectly: '))

            message_decrypted = decrypt(wordDecrypt, key)
            print(f'Decrypted message: {message_decrypted}')

        elif selector == 'Q' or selector == 'q':
            break

        else:
            print('Invalid mode. Please try again!')

if __name__ == "__main__":
    main()
    

