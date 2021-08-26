import time

print("Welcome to Thomas' Mad Libs Generator")
time.sleep(2.4)

print('\nStory Number 1')
print('Story Number 2')
print('Story Number 3')

while True:
    story_select = input('\nPlease enter the story: ')

    if story_select == 'Story Number 1':
        print('\nWelcome to Story Number 1')
        break
    elif story_select == 'Story Number 2':
        print('\nWelcome to Story Number 2')
        break
    elif story_select == 'Story Number 3':
        print('\nWelcome to Story Number 3')
        break
    else:
        print('\nInvalid input, please try again!')
