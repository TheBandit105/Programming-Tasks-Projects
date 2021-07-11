import random
num = random.randint(1,20)
flag = True
guess = 0
print('Guess any number between 1 and 20: ', end = ' ')
while flag == True :
    guess = input( )
    if not guess.isdigit() :
        print('Invalid! Enter only digits between 1 and 20')
        break
    elif int(guess) == num - 1:
        print('Still too low, but you are very close. Please try again: ', end = ' ')
    elif int(guess) < num:
        print('Too low, try again: ', end = ' ')
    elif int(guess) == num + 1:
        print('Still too high, but you are very close. Please try again: ', end = ' ')
    elif int(guess) > num:
        print('Too high, try again: ', end = ' ')
    else:
        print('Correct... My number is ' + guess)
        flag = False


