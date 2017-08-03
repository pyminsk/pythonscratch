#программа инопланетянин
# можно менять цвета и размеры деталей
from tkinter import * 
window = Tk()
window.title('Alien')
c = Canvas(window, height=300, width=400) #размеры поля
c.pack()

body = c.create_oval(100, 150, 300, 250, fill='green')
eye = c.create_oval(170, 70, 230, 130, fill='white')
eyeball =c.create_oval(190, 90, 210, 110, fill='black')
mouth =c.create_oval(150, 220, 250, 240, fill='red')
neck = c.create_line(200, 150, 200, 130, fill='purple')
hat = c.create_polygon(170, 75, 230, 75, 200, 20, fill='blue')

def mouth_open(): # в консоли >>> набирать mouth_open() >>> mouth_close()
    c.itemconfig(mouth, fill='black')
def mouth_close():
    c.itemconfig(mouth, fill='red')

def blink(): # >>> blink()  >>>unblink()
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN) 
def unblink():
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL) 
    
words = c.create_text(200, 280, text='I am an alien')
def steal_hat(): # >>> steal_hat() исчезает шляпа
    c.itemconfig(hat, state=HIDDEN)
    c.itemconfig(words, text='Give my hat back!')

def blink2(event):
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN)
def unblink2(event):
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL)
c.bind_all('<KeyPress-a>', blink2) # keys a and s make blink() unblink()
c.bind_all('<KeyPress-s>', unblink2)

def eye_control(event): # keys up down left right for movies eyeball
    key = event.keysym
    
    if key == "Up":
        c.move(eyeball,  0, -1)
        
    elif key == "Down":
        c.move(eyeball,  0,  1)

    elif key == "Left":
        c.move(eyeball, -1,  0)
        
    elif key == "Right":
        c.move(eyeball,  1,  0)

c.bind_all('<Key>', eye_control)
        
    
    
                 
