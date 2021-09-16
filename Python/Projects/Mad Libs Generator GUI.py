from tkinter import *

win = Tk()
win.geometry('300x300')
win.title("Thomas' Mad Libs Generator")
Label(win, text = "Welcome to Thomas'\n Mad Libs Generator!", font = 'arial 20 bold').pack()
Label(win, text = 'Select a story: ', font = 'arial 15 bold').place(x = 77, y = 80)

def story1():
    win1 = Tk()
    win1.geometry('300x300')
    win1.title('The Samurai')

    Label(win1, text = "The Samurai", font = 'arial 20 bold').pack()

    nameLabel = Label(win1, text = "Give a name for main character: ")
    nameLabel.pack(side = LEFT)
    nameEntry = Entry(win1)
    nameEntry.pack(side = LEFT)

    Button(win1, text = 'QUIT', font = 'arial 15', command = quit, bg = 'white').place(x = 70, y = 290)

def story2():
    win1 = Tk()
    win1.geometry('300x300')
    win1.title('In Love and Hate')

    Button(win1, text = 'QUIT', font = 'arial 15', command = quit, bg = 'white').place(x = 70, y = 290)

def story3():
    win1 = Tk()
    win1.geometry('300x300')
    win1.title('Story Number 3')

    Button(win1, text = 'QUIT', font = 'arial 15', command = quit, bg = 'white').place(x = 70, y = 290)

Button(win, text = 'The Samurai', font = 'arial 15', command = story1, bg = 'white').place(x = 80, y = 120)
Button(win, text = 'In Love and Hate', font = 'arial 15', command = story2, bg = 'white').place(x = 60, y = 180)
Button(win, text = 'Story Number 3', font = 'arial 15', command = story3, bg = 'white').place(x = 68, y = 240)
