import time

print('Hello there! Welcome to the Pytholympics!')

time.sleep(2.4)

name = input('\nPlease enter your name to begin: ')

print('\nWelcome ' + name + '! Let us begin this Pytholympics journey!')

time.sleep(2.4)

print('\nYou walk along a path and you reach the centre of the Pytholympics park.')

time.sleep(2.4)

print('\nTeam Red')
print('Team Blue')
print('Team Yellow')
print('Team Green')

team_select = input('\nIt is time to choose a team! Select one: ')

if team_select == 'Team Red':
    print("\n" + name + ", you have selected Team Red. Let's continue with our journey!")
elif team_select == 'Team Blue':
    print("\n" + name + ", you have selected Team Blue. Let's continue with our journey!")
elif team_select == 'Team Yellow':
    print("\n" + name + ", you have selected Team Yellow. Let's continue with our journey!")
elif team_select == 'Team Green':
    print("\n" + name + ", you have selected Team Green. Let's continue with our journey!")

time.sleep(2.4)

print('\nThere are many activities for you to do in the Pytholympics park.')
time.sleep(2.4)
print('\nThe activities are divided into 7 islands.')
time.sleep(2.4)

print('\nKyriyos Island')
print('Papoloc Island')
print('Kuusama Island')
print('Tykore Island')
print('Asanaimo Island')
print('Yolasi Island')
print('Cullomi Island')

island_select = input('\nSelect an island to go to: ')

if island_select == 'Kyriyos Island':
    print('\nWelcome to Kyriyos Island. The game you will play is called Catch the Murderer!')
    time.sleep(3)
    print("You are a detective who has been called to a scene of a murder that had taken place.")
    time.sleep(3)
    print("The victim's name is Achi Ohilyo. She is a 32 year old woman who worked as a gardener")
    time.sleep(3)
    print("at a client's house for 7 years. The client's name is Dahra Hisman, a 45 year old businessman")
    time.sleep(3)
    print("who works for a company named Guysman Inc.")
    


