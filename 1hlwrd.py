message = ("Hello word!")
pi = 3.1415
n = 177

print (message)
print (n)
print (12)
print (pi)


import math
import tkinter
# import turtle

# import turtle
# print (math.__doc__)
print (tkinter.__doc__)
print (math.pi)

import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="####Hello, World#####")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()
