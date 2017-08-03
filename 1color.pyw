from random import *
from tkinter import *

size = 600
size1 = 1366
size2 = 768

window = Tk()
canvas = Canvas(window, width=size1, height=size2)
canvas.pack()

while True:
    col = choice(['pink', 'orange', 'purple', 'yellow', 'red', 'green', 'blue', 'pink', 'purple', 'purple', 'pink' ])
    x0 = randint(0, size1)
    y0 = randint(0, size2)
    d = randint(5, size/6)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=col)
    window.update()

    
