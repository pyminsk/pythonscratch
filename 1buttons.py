
from tkinter import *
def bAaction():
    print('Thank you!')
def bBaction():
    print('Ouch! That hurt!')
def bCaction():
    print('Botton 3!')
def bDaction():
    print('Botton D4!')    
window = Tk()
buttonA = Button(window, text='Press me!',     command=bAaction)
buttonB = Button(window, text='Don\'t press!', command=bBaction)
buttonC = Button(window, text='It button 3!',  command=bCaction)
buttonD = Button(window, text='It button D4!',  command=bDaction)
buttonA.pack()
buttonB.pack()
buttonC.pack()
buttonD.pack()
