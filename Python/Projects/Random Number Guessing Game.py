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

while True:
    guesses += 1
    in_guess = input('Guess the number: ')

    if int(in_guess) > max_num:
            print('Invalid guess, due to input given being bigger than the max number set.\
 Input a guess between 0 and the max number that was set and try again.')
            guesses -=1

    if in_guess.isdigit():
        in_guess = int(in_guess)
    else:
        print('Please type a number and try again.')
        continue

    if in_guess == randnum:
        print("\nWell done! You've guessed my number!")
        break
    elif in_guess > randnum:
        print("Your guess was above the chosen number!\n")
    else:
        print("Your guess was below the chosen number!\n")

print('\nYou achieved the guess in', guesses, 'guesses.')
