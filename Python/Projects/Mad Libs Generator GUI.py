from tkinter import *

# This is the main window for the menu of the Mad Libs Generator.
# Initialises and opens a new window upon starting the program. This window 
# does not utilise the resizable function as it is not necessary to resize 
# a menu window when the only things showing on the menu are the title 
# and the buttons leading to the 3 stories in the program and the QUIT
# button.

win = Tk()
win.geometry('300x300')
win.title("Thomas' Mad Libs Generator")
win.resizable(False, False)
Label(win, text = "Welcome to Thomas'\n Mad Libs Generator!", font = 'arial 20 bold').pack()
Label(win, text = 'Select a story: ', font = 'arial 15 bold').place(x = 77, y = 80)

# Each function below contains the inner workings for the story inputs and outputs. In each function,
# a new window is initialised and created for the user to input their words of choice for the mad lib
# story they chose in the menu. This works by initialising several labels and entry functions for each
# noun, verb or any other word that is given as option for the user to input. The place method determines
# position of the labels and entry field boxes in the window upon its initialisation and creation. Upon
# clicking on the CONFIRM button, the entry values inputted by the user are displayed respectively in the output function,
# showing the final generated story with the user's input. This process is done via the command parameter of the button, which
# performs the command upon pressing the button. Usually the command parameter is normally a function without parameters,
# but since it is taking in entry values as parameters, the lambda keyword is used to facilitate this process.

def story1():
    def story1out(nameEntry,placeEntry,place1Entry,entityEntry,entityNameEntry,methodEntry,feelingEntry):
        win1out = Tk()
        win1out.geometry('900x250')
        win1out.title('The Samurai')
        win1out.config(bg = 'Gold')
        Label(win1out, text = "The Samurai", font = 'arial 20 bold', bg = 'Gold').pack()

        Label(win1out, text = 
        f'''\nLong ago, there was a samurai warrior named {str(nameEntry).capitalize()}, \nwho once lived in the Japanese countryside in {str(placeEntry).capitalize()}.
One day, he went into the {str(place1Entry).capitalize()} and fought a {str(entityEntry)} called {str(entityNameEntry).capitalize()}.
The {str(entityEntry)} was {str(methodEntry)} in battle and the citizens were {str(feelingEntry)}. 
The Samurai left the {str(place1Entry).capitalize()} heading onto the next mission.''', font = 'arial 20', bg = 'Gold').pack()
    
    win1 = Tk()
    win1.geometry('480x275')
    win1.title('The Samurai - Mad Libs')

    Label(win1, text = "The Samurai", font = 'arial 20 bold').pack()

    nameLabel = Label(win1, text = "Give a name for main character: ")
    nameLabel.place(x=0, y=40)
    nameEntry = Entry(win1)
    nameEntry.place(x=350, y=42)
    placeLabel = Label(win1, text = "Give a name for the place in Japan: ")
    placeLabel.place(x=0, y=64)
    placeEntry = Entry(win1)
    placeEntry.place(x=350, y=66)
    place1Label = Label(win1, text = "Give a name for a location in the place given in previous field: ")
    place1Label.place(x=0, y=86)
    place1Entry = Entry(win1)
    place1Entry.place(x=350, y=88)
    entityLabel = Label(win1, text = "Give the type of entity (e.g. monster):  ")
    entityLabel.place(x=0, y=108)
    entityEntry = Entry(win1)
    entityEntry.place(x=350, y=110)
    entityNameLabel = Label(win1, text = "Name the entity:  ")
    entityNameLabel.place(x=0, y=130)
    entityNameEntry = Entry(win1)
    entityNameEntry.place(x=350, y=132)
    methodLabel = Label(win1, text = "Give the method of how entity was dealt with: ")
    methodLabel.place(x=0, y=153)
    methodEntry = Entry(win1)
    methodEntry.place(x=350, y=153)
    feelingLabel = Label(win1, text = "Give the feeling of how the people felt in the aftermath: ")
    feelingLabel.place(x=0, y=175)
    feelingEntry = Entry(win1)
    feelingEntry.place(x=350, y=175)

    Button(win1, text = 'QUIT', font = 'arial 15', command = quit, bg = 'red').place(x = 150, y = 220)
    Button(win1, text = 'CONFIRM', font = 'arial 15', \
        command = lambda:story1out(nameEntry.get(),placeEntry.get(),place1Entry.get(),entityEntry.get(),\
            entityNameEntry.get(),methodEntry.get(),feelingEntry.get()), bg = 'green').place(x = 250, y = 220)

def story2():
    def story2out(townNameEntry, boyNameEntry, boyNameTwoEntry, girlNameEntry, adjectiveEntry,\
         adjectiveTwoEntry, placeEntry, objEntry, speechEntry):
        win2out = Tk()
        win2out.geometry('1000x550')
        win2out.title('In Love and Hate')
        win2out.config(bg = 'RoyalBlue2')
        Label(win2out, text = "In Love and Hate", font = 'arial 20 bold', bg = 'RoyalBlue2').pack()

        Label(win2out, text = 
        f'''\nIn the sleepy town of {townNameEntry.capitalize()}, there was a young man named {boyNameEntry.capitalize()} and he was longing to find the {adjectiveEntry} girl.
        One day, while he was carrying his {objEntry} home, he accidently bumped into the girl.
        {boyNameEntry.capitalize()} apologised and the girl responded, "{speechEntry}". 
        {boyNameEntry.capitalize()} asked for her name and she said her name was {girlNameEntry.capitalize()}. 
        Upon hearing her name, {boyNameEntry.capitalize()} realised that this was the girl he was madly in love with.
        {boyNameEntry.capitalize()} then asked {girlNameEntry.capitalize()} if she would like to go out to the {placeEntry} just to get to know each other and be friends and {girlNameEntry.capitalize()} said yes.
        {boyNameEntry.capitalize()} and {girlNameEntry.capitalize()} met up at the {placeEntry} as promised and they had a fantastic time together.
        It was revealed by {girlNameEntry.capitalize()} that her family had a very {adjectiveTwoEntry} business and were subsequently rich.\nHowever, she was only interested living a life that did not involve golddiggers.\
        \n{boyNameEntry.capitalize()} mustered up the courage and told her that he genuinely loved her before they met and the he would care for her now.
        
        \n{girlNameEntry.capitalize()} was moved by this notion and decided to accept his proposal.\nHowever, {boyNameTwoEntry.capitalize()} bursted into the {placeEntry} and was very angry.
        He walked up to {boyNameEntry.capitalize()} and shouted at him that he wanted {girlNameEntry.capitalize()}.
        It turned out that {boyNameTwoEntry.capitalize()} was the best friend of {boyNameEntry.capitalize()}, but unfortunately had his eyes set on {girlNameEntry.capitalize()} as well.
        After learning that {girlNameEntry.capitalize()} had chosen {boyNameEntry.capitalize()} over him, he began to hate {boyNameEntry.capitalize()} with such passion.\
        \n{boyNameTwoEntry.capitalize()} then challenges {boyNameEntry.capitalize()} to a fight and said that whoever wins this fight will get {girlNameEntry.capitalize()}.\
        \n{boyNameEntry.capitalize()} accepted the challenge, despite {girlNameEntry.capitalize()} pleading to {boyNameTwoEntry.capitalize()} not to do this. 
        Eventually, {boyNameEntry.capitalize()} beats {boyNameTwoEntry.capitalize()} in the fight and everyone parts way for the day.\
        \n{boyNameEntry.capitalize()} and {girlNameEntry.capitalize()} then happily married and lived ever after. ''', font = 'arial 14', bg = 'RoyalBlue2').pack()

    win2 = Tk()
    win2.geometry('350x300')
    win2.title('In Love and Hate')

    Label(win2, text = "In Love and Hate", font = 'arial 20 bold').pack()

    townNameLabel = Label(win2, text = "Give a name for the town: ")
    townNameLabel.place(x=0, y=44)
    townNameEntry = Entry(win2)
    townNameEntry.place(x=210, y=44)
    boyNameLabel = Label(win2, text = 'Give the name for the boy: ')
    boyNameLabel.place(x=0, y=64)
    boyNameEntry = Entry(win2)
    boyNameEntry.place(x=210, y=66)
    boyNameTwoLabel = Label(win2, text ='Give the name for the second boy: ')
    boyNameTwoLabel.place(x=0, y=86)
    boyNameTwoEntry = Entry(win2)
    boyNameTwoEntry.place(x=210, y=88)
    girlNameLabel = Label(win2, text = 'Give the name for the girl: ')
    girlNameLabel.place(x=0, y=108)
    girlNameEntry = Entry(win2)
    girlNameEntry.place(x=210, y=110)
    adjectiveLabel = Label(win2, text = 'Describe the adjective for the girl: ')
    adjectiveLabel.place(x=0, y=130)
    adjectiveEntry = Entry(win2)
    adjectiveEntry.place(x=210, y=132)
    adjectiveTwoLabel = Label(win2, text = 'Describe the adjective for the business: ')
    adjectiveTwoLabel.place(x=0, y=153)
    adjectiveTwoEntry = Entry(win2)
    adjectiveTwoEntry.place(x=210, y=153)
    placeLabel = Label(win2, text = 'Give a name for a place to meet up: ')
    placeLabel.place(x=0, y=175)
    placeEntry = Entry(win2)
    placeEntry.place(x=210, y=175)
    objLabel = Label(win2, text = 'Give a name for an object: ')
    objLabel.place(x=0, y=197)
    objEntry = Entry(win2)
    objEntry.place(x=210, y=197)
    speechLabel = Label(win2, text = 'Write some speech for the girl: ')
    speechLabel.place(x=0, y=219)
    speechEntry = Entry(win2)
    speechEntry.place(x=210, y=219)

    Button(win2, text = 'QUIT', font = 'arial 15', command = quit, bg = 'red').place(x = 70, y = 250)
    Button(win2, text = 'CONFIRM', font = 'arial 15', \
        command = lambda:story2out(townNameEntry.get(), boyNameEntry.get(), boyNameTwoEntry.get(),\
            girlNameEntry.get(), adjectiveEntry.get(), adjectiveTwoEntry.get(),\
                placeEntry.get(), objEntry.get(), speechEntry.get()), bg = 'green').place(x = 175, y = 250)

def story3():
    def story3out(brotherNameEntry, verbOneEntry,roomEntry,soundOneEntry,adjectiveOneEntry,\
            timeObjectEntry, timeElapsedEntry, adjectiveTwoEntry, creatureEntry):

            win3out = Tk()
            win3out.geometry('1000x400')
            win3out.title('Lightning Bolt')
            win3out.config(bg = 'DarkOrange')
            Label(win3out, text = "Lightning Bolt", font = 'arial 20 bold', bg = 'DarkOrange').pack()
            Label(win3out, text = "(a sample extract taken from Lightning Bolt and Blazer by Zanders and Lundin)", font = 'arial 17 italic', bg = 'DarkOrange').pack()

            Label(win3out, text = 
            f'''\n{brotherNameEntry.capitalize()} heard his brother {verbOneEntry} out the back exit of the {roomEntry} with a {soundOneEntry}.
            Like his namesake he was {adjectiveOneEntry}, but {brotherNameEntry.capitalize()} was not why everything had to be a competition.
            Lightning Bolt opened the door and jumped out like the {roomEntry} was on fire. 
            "About time you showed up," his brother said. Lightning Bolt shouldered his way past. 
            "That was a record and you know it." {brotherNameEntry.capitalize()} tapped his {timeObjectEntry}.
            "It looks like it took you {timeElapsedEntry} seconds. That is no record, and you know it."
            Lightning Bolt let it go. "Sitrep." "Sitrep? Seriously?"
            Lightning Bolt was getting so {adjectiveTwoEntry} that he could not even say complete sentences.
            What had the public done to him? {brotherNameEntry.capitalize()} wondered. They were at their limits.
            One more giant {creatureEntry}, and they were going to explode from exhaustion.
            ''', font = 'arial 17', bg = 'DarkOrange').pack()

    win3 = Tk()
    win3.geometry('600x350')
    win3.title('Lightning Bolt')
    
    Label(win3, text = "Lightning Bolt", font = 'arial 20 bold').pack()

    brotherNameLabel = Label(win3, text ='Give a name for the brother of Lightning Bolt: ')
    brotherNameLabel.place(x=0, y=44)
    brotherNameEntry = Entry(win3)
    brotherNameEntry.place(x=450, y=44)
    verbOneLabel = Label(win3, text ='Give a verb to describe getting out quickly: ')
    verbOneLabel.place(x=0, y=68)
    verbOneEntry = Entry(win3)
    verbOneEntry.place(x=450, y=68)
    roomLabel = Label(win3, text ='Give the name of room Lightning Bolt escapes from: ')
    roomLabel.place(x=0, y=92)
    roomEntry = Entry(win3)
    roomEntry.place(x=450, y=92)
    soundOneLabel = Label(win3, text ='Give an onomatopoeia to describe the movement given in the first verb: ')
    soundOneLabel.place(x=0, y=116)
    soundOneEntry = Entry(win3)
    soundOneEntry.place(x=450, y=116)
    adjectiveOneLabel = Label(win3, text ="Give an adjective to describe Lightning's namesake: ")
    adjectiveOneLabel.place(x=0, y=140)
    adjectiveOneEntry = Entry(win3)
    adjectiveOneEntry.place(x=450, y=140)
    timeObjectLabel = Label(win3, text ='Give a name of a device used to record the time elapsed: ')
    timeObjectLabel.place(x=0, y=164)
    timeObjectEntry = Entry(win3)
    timeObjectEntry.place(x=450, y=164)
    timeElapsedLabel = Label(win3, text ='Give the time recorded on the device mentioned preiovusly: ')
    timeElapsedLabel.place(x=0, y=188)
    timeElapsedEntry = Entry(win3)
    timeElapsedEntry.place(x=450, y=188)
    adjectiveTwoLabel = Label(win3, text ='Give another adjective that describes slow-moving behaviour: ')
    adjectiveTwoLabel.place(x=0, y=212)
    adjectiveTwoEntry = Entry(win3)
    adjectiveTwoEntry.place(x=450, y=212)
    creatureLabel = Label(win3, text ='Give a name for a scary creature, whether from outer space or on Earth: ')
    creatureLabel.place(x=0, y=236)
    creatureEntry = Entry(win3)
    creatureEntry.place(x=450, y=236)

    Button(win3, text = 'QUIT', font = 'arial 15', command = quit, bg = 'red').place(x = 180, y = 290)
    Button(win3, text = 'CONFIRM', font = 'arial 15', command = lambda:story3out(\
        brotherNameEntry.get(), verbOneEntry.get(),roomEntry.get(),soundOneEntry.get(),adjectiveOneEntry.get(),\
            timeObjectEntry.get(), timeElapsedEntry.get(), adjectiveTwoEntry.get(), creatureEntry.get()), bg = 'green').place(x = 310, y = 290)

Button(win, text = 'The Samurai', font = ('Comic Sans MS',16), command = story1, bg = '#0BD67E').place(x = 80, y = 120)
Button(win, text = 'In Love and Hate', font = ('Comic Sans MS',16), command = story2, bg = '#0BD67E').place(x = 60, y = 180)
Button(win, text = 'Lightning Bolt', font = ('Comic Sans MS',16), command = story3, bg = '#0BD67E').place(x = 75, y = 240)
win.mainloop()