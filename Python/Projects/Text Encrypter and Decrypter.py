
selector = input('Do you wish to encrypt or decrypt the word (encrypt => e or E, decrypt => d or D)? Press q or Q to quit.')

if selector == 'E' or selector == 'e':

    wordEncrypt = input('Please type the word you would like to encrypt: ')

elif selector == 'D' or selector == 'd':

    wordDecrypt = input('Please type the encrypted word you would like to decrypt: ')

elif selector == 'Q' or selector == 'q':
    quit
else:

