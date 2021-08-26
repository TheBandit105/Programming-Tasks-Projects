from tkinter import *

win = Tk()
win.geometry('300x300')
win.title("Thomas' Mad Libs Generator")
Label(win, text = "Welcome to Thomas'\n Mad Libs Generator!", font = 'arial 20 bold').pack()
Label(win, text = 'Select a story: ', font = 'arial 15 bold').place(x = 80, y = 80)

def story1():
    win1 = Tk()
    win1.geometry('300x300')
    win1.title('Story Number 1')

    Button(win1, text = 'QUIT', font = 'arial 15', bg = 'white').place(x = 70, y = 290)

Button(win, text = 'Story Number 1', font = 'arial 15', command = story1, bg = 'white').place(x = 70, y = 120)
Button(win, text = 'Story Number 2', font = 'arial 15', bg = 'white').place(x = 70, y = 180)
Button(win, text = 'Story Number 3', font = 'arial 15', bg = 'white').place(x = 70, y = 240)
