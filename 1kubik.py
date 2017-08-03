from tkinter import *
from random import randint

def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(12,33)))
window = Tk()
text = Text(window, width=2, height=1)

buttonA = Button(window, text='Press to 1roll!', command=roll)
buttonB = Button(window, text='Press to 2roll!', command=roll)
buttonC = Button(window, text='Press to 3roll!', command=roll)
buttonD = Button(window, text='Press to 4roll!', command=roll)

text.pack()
buttonA.pack()
buttonB.pack()
buttonC.pack()
buttonD.pack()

