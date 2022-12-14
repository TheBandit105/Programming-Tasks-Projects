import random

# Initialise scores for the user and computer.
player_point = 0
computer_point = 0

# A list of possible moves in the game of Rock, Paper, Scissors.
options = ["rock", "paper", "scissors"]

# Game begins in this while loop.
while True:
    # If user wants to quit the game, simply type q.
    rpsinput = input('Choose Rock, Paper or Scissors or Q to quit (Note: Please make sure you type your input \nCORRECTLY\
 as even including a space after the input can lead to the input not being read):\n').lower()
    if rpsinput == 'q':
        break

    # This if if statement ensures that no invalid inputs can be passed into the game.
    if rpsinput not in options:
        continue

    # Using the random library, this variable generates a
    # random integer between 0 and 2. The integer is then
    # compared accordingly to the index position in the list above.
    # rock: 0, paper: 1, scissors: 2
    random_play = random.randint(0, 2)
    
    computer_play = options[random_play]
    print("Computer picked", computer_play + '.')

    # All the possible win scenarios.
    if rpsinput == 'rock' and computer_play == 'scissors':
        print('You won!')
        player_point += 1
        continue

    elif rpsinput == 'paper' and computer_play == 'rock':
        print('You won!')
        player_point += 1
        continue

    elif rpsinput == 'scissors' and computer_play == 'paper':
        print('You won!')
        player_point += 1
        continue
    
    # In case the computer tied with player, no points are awarded.

    # These elif statements were what I had used before I realised that these
    # could be simplified into one elif statement as provided below. For beginners,
    # who want to understand how that works, you are more than welcome to uncomment
    # the three elif statements AND comment out the simplified elif statement - it will
    # work in exactly the same way.

    #elif rpsinput == 'rock' and computer_play == 'rock':
    #    print('A tie, play again!')
    #    continue

    #elif rpsinput == 'paper' and computer_play == 'paper':
    #    print('A tie, play again!')
    #    continue

    #elif rpsinput == 'scissors' and computer_play == 'scissors':
    #    print('A tie, play again!')
    #    continue

    elif rpsinput == computer_play:
        print('A tie, play again!')
        continue
    
    else:
        print('You lost!')
        computer_point += 1

print('\nYou won', player_point, 'times.')
print('The computer won', computer_point, 'times.')
print('Bye!')
    
