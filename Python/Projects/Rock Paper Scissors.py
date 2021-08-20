import random

player_point = 0
computer_point = 0

options = ["rock", "paper", "scissors"]

while True:
    rpsinput = input('Rock/Paper/Scissors or Q to quit: ')
    if rpsinput == 'q':
        break

    if rpsinput not in options:
        continue

    random_play = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_play = options[random_play]
    print("Computer picked", computer_play + '.')

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
    elif rpsinput == 'rock' and computer_play == 'rock':
        print('A tie, play again!')
        continue

    elif rpsinput == 'paper' and computer_play == 'paper':
        print('A tie, play again!')
        continue

    elif rpsinput == 'scissors' and computer_play == 'scissors':
        print('A tie, play again!')
        continue

    else:
        print('You lost!')
        computer_point += 1

print('You won', player_point, 'times.')
print('The computer won', computer_point, 'times.')
print('Bye!')
    
