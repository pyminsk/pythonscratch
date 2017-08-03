#igra pro ribku
#1
from tkinter import *
HEIGHT = 500 # razmer okna
WIDTH = 800  # razmer okna
window = Tk() # vizov funkcii okna iz modulia tkinter
window.title('Bubble Blaster') #nazvanie igri
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue') #holst temno-siniy
c.pack()
#2
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red') #treugolnik
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')      #kontur kruga
SHIP_R = 15 # razmer lodki
MID_X = WIDTH / 2  # koordinats seredini ekrana
MID_Y = HEIGHT / 2 # koordinats seredini ekrana
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
#3
SHIP_SPD = 15 # sdvig lodki pri push key
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    elif event.keysym == 'Left': 
        c.move(ship_id,  -SHIP_SPD, 0)
        c.move(ship_id2,  -SHIP_SPD, 0)        
    elif event.keysym == 'Right':
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)
c.bind_all('<Key>', move_ship) # funkciya move_ship pri liuboi klavishe
#4
from random import randint
bub_id = list()    #
bub_r = list()     #
bub_speed = list() # spiski imia radius speed kazdogo puzira
MIN_BUB_R = 10 # 
MAX_BUB_R = 40 # min i max radius puzira
MAX_BUB_SPD = 10 
GAP = 100
def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT) # poz puzira na holste
    r = randint(MIN_BUB_R, MAX_BUB_R) # randome r puzira
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white') # stroka risuet puzir
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD)) # imya radius skorost puzira v spiski
#5
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)
#6
#7
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y
#8
def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]
#9
def clean_up_bubs():
    for i in range(len (bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
          del_bubble(i)        
#10        
#11        
from math import sqrt
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
#12
def collision():
    points = 0
    for bub in range (len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points
#13
#14
c.create_text(50, 30, text='TIME', fill='white' )
c.create_text(150, 30, text='SCORE', fill='white' )
time_text = c.create_text(50, 50,  fill='white' )
score_text = c.create_text(150, 50, fill='white' )
def show_score(score):
    c.itemconfig(score_text, text=str(score))    
def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))
#15    
from time import sleep, time
BUB_CHANCE = 15
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT
#16
###############MAIN GAME LOOP######################
while time() < end:
 if randint(1, BUB_CHANCE) == 1:
        create_bubble()
 move_bubbles()
 clean_up_bubs()
 score += collision()
 if (int(score / BONUS_SCORE)) > bonus:
     bonus += 1
     end += TIME_LIMIT
 show_score(score)
 show_time(int(end - time()))
 window.update()
 sleep(0.01)
#17
c.create_text(MID_X, MID_Y, \
    text='GAME OVER', fill='white', font=('Helvetica',30))
c.create_text(MID_X, MID_Y + 30, \
    text='Score: '+ str(score), fill='white')
c.create_text(MID_X, MID_Y + 45, \
    text='Bonus time: '+ str(bonus*TIME_LIMIT), fill='white')                                               
# END END END
