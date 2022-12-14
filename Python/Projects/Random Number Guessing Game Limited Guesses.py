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

randnum = random.randint(0, max_num)
guesses = 0
guessctr = 3

while True:
    guesses += 1

    if guesses > 3:
        print("Game Over! Unlucky, you weren't able to guess the number!")
        print(f'\nThe number was {randnum}.')
        break
    
    in_guess = input('Guess ' + str(guessctr) + ' of the number: ')

    if int(in_guess) > max_num:
            print('Invalid guess, due to input given being bigger than the max number set.\
 Input a guess between 0 and the max number that was set and try again.')
            guesses -=1
            guessctr +=1

    if in_guess.isdigit():
        in_guess = int(in_guess)
    else:
        print('Please type a number and try again.')
        continue

    if in_guess == randnum:
        print("\nWell done! You've guessed my number!")
        print('\nYou achieved the guess in', guesses, 'guesses.')
        break
    elif in_guess > randnum:
        print("Your guess was above the chosen number!\n")
    else:
        print("Your guess was below the chosen number!\n")

    guessctr -= 1




