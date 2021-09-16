import time

def madlib1():
    print('\nThe Samurai')

    name = input('\nGive a name for main character: ')
    place = input('Give a name for the place in Japan: ')
    place1 = input('Give a name for a location in ' + place + ': ')
    entity = input('Give the type of entity (e.g. monster): ')
    entname = input('Name the entity: ')
    method = input('Give the method of how entity was dealt with: ')
    feeling = input('Give the feeling of how the people felt in the aftermath: ')

    print('\nLong ago, there was a samurai warrior named ' + name + ', who once lived in the Japanese countryside in ' + place + '. One day, he went into the ' + place1 + ' and fought a ' + entity + ' called ' + entname + '. The ' + entity + ' was ' + method + ' in battle and the citizens were ' + feeling + '. The Samurai left the ' + place1 + ' heading onto the next mission.')
    
def madlib2():
    print('\nIn Love and Hate')

    town_name = input('\nGive a name for the town: ')
    boy_name = input('Give the name for the boy: ')
    boy_name_two = input('Give the name for the second boy: ')
    girl_name = input('Give the name for the girl: ')
    adjective = input('Describe the adjective for the girl: ')
    adjectiveTwo = input('Describe the adjective for the business: ')
    place = input('Give a name for a place to meet up: ')
    obj = input('Give a name for an object: ')
    speech = input('Write some speech for the girl: ')
    
    print('\nIn the sleepy town of ' + town_name + ', there was a young man named ' + boy_name + ' and he was longing to find the ' + adjective + ' girl. One day, while he was carrying his ' + obj + ' home, he accidently bumped into the girl. ' + boy_name + ' apologised and the girl responded , "' + speech + '". ' + boy_name + ' asked for her name and she said her name was ' + girl_name + '. Upon hearing her name, ' + boy_name + ' realised that this was the girl he was madly in love with. ' + boy_name + ' then asked ' + girl_name + ' if she would like to go out to the ' + place + ' just to get to know each other and be friends and ' + girl_name + ' said yes.\n')
    print(boy_name + ' and ' + girl_name + ' met up at the ' + place + ' as promised and they had a fantastic time together. It was revealed by ' + girl_name + ' that her family had a very ' + adjectiveTwo + ' business and were subsequently rich. However, she was only interested living a life that did not involve golddiggers. ' + boy_name + ' mustered up the courage and told her that he genuinely loved her before they met and the he would care for her now. ' + girl_name + ' was moved by this notion and decided to accept his proposal. However, ' + boy_name_two + ' bursted into the ' + place + ' and was very angry. He walked up to ' + boy_name + ' and shouted at him that he wanted ' + girl_name + '.\n')
    print('It turned out that ' + boy_name_two + ' was the best friend of ' + boy_name + ', but unfortunately had his eyes set on ' + girl_name + ' as well. After learning that ' + girl_name + ' had chosen ' + boy_name + ' over him, he began to hate ' + boy_name + ' with such passion. ' + boy_name_two + ' then challenges ' + boy_name + ' to a fight and said that whoever wins this fight will get ' + girl_name + '. ' + boy_name + ' accepted the challenge, despite ' + girl_name + ' pleading to ' + boy_name_two + ' not to do this. Eventually, ' + boy_name + ' beats ' + boy_name_two + ' in the fight and everyone parts way for the day.\n')
    print(boy_name + ' and ' + girl_name + ' then happily married and lived ever after. ')

def madlib3():
    print('\nThe Lightning Bolt')

    print('\n

print("Welcome to Thomas' Mad Libs Generator")
time.sleep(2.4)

print('\nThe Samurai')
print('In Love and Hate')
print('The Lightning Bolt')

while True:
    story_select = input('\nPlease enter the story: ')

    if story_select == 'The Samurai':
        madlib1()
        break
    elif story_select == 'In Love and Hate':
        madlib2()
        break
    elif story_select == 'The Lightning Bolt':
        madlib3()
        break
    else:
        print('\nInvalid input, please try again!')
