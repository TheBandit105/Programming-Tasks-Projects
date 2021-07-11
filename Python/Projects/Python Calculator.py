import math

print('Hello, welcome to the Python Calculator! \n')
print('Please select an operation below: \n')

print('Addition -> a')
print('Subtraction -> s')
print('Multiplication -> m')
print('Division -> d')
print('Floor Division -> f')
print('Ceiling Division -> c')
print('Modulus (Remainder) -> mod')
print('')


selection = input('\nInput: ')

if selection == 'a':
    print('\nPlease input two values to add: \n')
    a = float(input())
    b = float(input())
    print('\n', a + b)

elif selection == 's':
    print('\nPlease input two values to subtract: \n')
    a = float(input())
    b = float(input())
    print('\n', a - b)
          
elif selection == 'm':
    print('\nPlease input two values to multiply: \n')
    a = float(input())
    b = float(input())
    print('\n', a * b)
          
elif selection == 'd':
    print('\nPlease input two values to divide: \n')
    a = float(input())
    b = float(input())
    print('\n', a / b)

elif selection == 'f':
    print('\nPlease input two values to find the floor division: \n')
    a = float(input())
    b = float(input())
    print('\n', math.floor(a / b))

elif selection == 'c':
    print('\nPlease input two values to find the ceiling division: \n')
    a = float(input())
    b = float(input())
    print('\n', math.ceil(a / b))

elif selection == 'mod':
    print('\nPlease input two values to find the modulus: \n')
    a = float(input())
    b = float(input())
    print('\n', math.fmod(a, b))

elif selection == 'gcd':
    print('\nPlease input values to find the gcd: \n')
    a = int(input())
    b = int(input())

    print('\n', b)
    
    
elif selection == 'quit':
    exit()
