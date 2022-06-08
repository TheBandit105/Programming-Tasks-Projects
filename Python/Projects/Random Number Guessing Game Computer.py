import random

max_num = input('Set the max number: ')

if max_num.isdigit():
    max_num = int(max_num)

    if max_num <= 0:
        print('Please type a number bigger than 0 and try again.')
        quit()
else:
    print('Please type a number and try again.')
    quit()

chose_num = input('Input your number between 0 and set max number: ')

if chose_num.isdigit():
    chose_num = int(chose_num)

if chose_num <= 0:
    print('Please type a number bigger than 0 and try again.')
    quit()
elif chose_num > max_num:
    print('Please type a number smaller than or equal to ' + str(max_num) + ' and try again.')
    quit()
    
low = 0
high = max_num
feedback = ''
while feedback != 'c':
    if low != high:
        guess = random.randint(low, high)
    else:
        guess = low
    feedback = input(f'Is {guess} too high (h), too low (l) or correct (c)? ')
    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1

print('Awesome! Computer guessed your number ' + str(guess) + ' correctly! ')
