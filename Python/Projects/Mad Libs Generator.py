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

    print('\nLong ago, there was a samurai warrior named ' + name.capitalize() + ', who once lived in the Japanese countryside in ' + place.capitalize() \
          + '. One day, he went into the ' + place1.capitalize() + ' and fought a ' + entity + ' called ' + entname.capitalize() + '. The ' + entity + \
          ' was ' + method + ' in battle and the citizens were ' + feeling + '. The Samurai left the ' + place1.capitalize() + ' heading onto the next mission.')
    
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
    
    print('\nIn the sleepy town of ' + town_name.capitalize() + ', there was a young man named ' + boy_name.capitalize() + \
          ' and he was longing to find the ' + adjective + ' girl. One day, while he was carrying his ' + obj + \
          ' home, he accidently bumped into the girl. ' + boy_name.capitalize() + ' apologised and the girl responded , "' + speech + \
          '". ' + boy_name.capitalize() + ' asked for her name and she said her name was ' + girl_name.capitalize() + '. Upon hearing her name, ' + \
          boy_name.capitalize() + ' realised that this was the girl he was madly in love with. ' + boy_name.capitalize() + ' then asked ' + girl_name.capitalize()\
          + ' if she would like to go out to the ' + place + ' just to get to know each other and be friends and ' + girl_name.capitalize() \
          + ' said yes.\n')
    print(boy_name.capitalize() + ' and ' + girl_name.capitalize() + ' met up at the ' + place + ' as promised and they had a fantastic time together. It was revealed by ' + girl_name.capitalize() \
          + ' that her family had a very ' + adjectiveTwo + ' business and were subsequently rich. However, she was only interested living a life that did not involve golddiggers. '\
          + boy_name.capitalize() + ' mustered up the courage and told her that he genuinely loved her before they met and the he would care for her now. ' + girl_name.capitalize() + \
          ' was moved by this notion and decided to accept his proposal. However, ' + boy_name_two.capitalize() + ' bursted into the ' + place + ' and was very angry. He walked up to ' + boy_name.capitalize()\
          + ' and shouted at him that he wanted ' + girl_name.capitalize() + '.\n')
    print('It turned out that ' + boy_name_two.capitalize() + ' was the best friend of ' + boy_name.capitalize() + ', but unfortunately had his eyes set on ' + girl_name.capitalize() + ' as well. After learning that ' + \
          girl_name.capitalize() + ' had chosen ' + boy_name.capitalize() + ' over him, he began to hate ' + boy_name.capitalize() + ' with such passion. ' + boy_name_two.capitalize() + ' then challenges ' + \
          boy_name.capitalize() + ' to a fight and said that whoever wins this fight will get ' + girl_name.capitalize() + '. ' + \
          boy_name.capitalize() + ' accepted the challenge, despite ' + girl_name.capitalize() + ' pleading to ' + \
          boy_name_two.capitalize() + ' not to do this. Eventually, ' + boy_name.capitalize() + ' beats ' + boy_name_two.capitalize() + ' in the fight and everyone parts way for the day.\n')
    print(boy_name.capitalize() + ' and ' + girl_name.capitalize() + ' then happily married and lived ever after. ')

def madlib3():
    print('\nLightning Bolt (a sample extract taken from Lightning Bolt and Blazer by Zanders and Lundin)')

    brother_name = input('\nGive a name for the brother of Lightning Bolt: ')
    verb_one = input('Give a verb to describe getting out quickly: ')
    room = input('Give the name of room Lightning Bolt escapes from: ')
    sound_one = input('Give an onomatopoeia to describe the movement given in the first verb: ')
    adjective_one = input("Give an adjective to describe Lightning's namesake: ")
    timeObject = input('Give a name of a device used to record the time elapsed: ')
    timeElapsed = input('Give the time recorded on the device mentioned preiovusly: ')
    adjective_two = input('Give another adjective that describes slow-moving behaviour: ')
    creature = input('Give a name for a scary creature, whether from outer space or on Earth: ')
    
    print('\n' + brother_name.capitalize() + ' heard his brother ' + verb_one + ' out the back exit of the ' + room + ' with a ' + sound_one + '.')
    print('Like his namesake he was ' + adjective_one + ', but ' + brother_name.capitalize() + ' was not why everything had to be a competition.')
    print('Lightning Bolt opened the door and jumped out like the ' + room + ' was on fire. \n"About time you showed up," his brother said. Lightning Bolt shouldered his way past.')
    print('"That was a record and you know it." \n' + brother_name.capitalize() + \
          ' tapped his ' + timeObject + '. "It looks like it took you ' + timeElapsed +' seconds. That is no record, and you know it."\
          \nLightning Bolt let it go. "Sitrep." "Sitrep? Seriously?"\nLightning Bolt was getting so ' + adjective_two + ' that he could not even say complete sentences. \
            \nWhat had the public done to him? ' + brother_name.capitalize() + ' wondered. They were at their limits.\nOne more giant ' + creature + ', and they were going to explode from exhaustion.'\
          '\n')

print("Welcome to Thomas' Mad Libs Generator")
time.sleep(2.4)

print('\nThe Samurai')
print('In Love and Hate')
print('Lightning Bolt')

while True:
    story_select = input('\nPlease enter the story: ')

    if story_select == 'The Samurai':
        madlib1()
        break
    elif story_select == 'In Love and Hate':
        madlib2()
        break
    elif story_select == 'Lightning Bolt':
        madlib3()
        break
    elif story_select == 'E' or story_select == 'e':
        break
    else:
        print('\nInvalid input, please try again!')
