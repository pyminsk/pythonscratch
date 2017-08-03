# -*- coding: utf-8 -*- pythonschool2 str 87!!!!!!!!!!!!!
# Моделирование задачи о теле брошенном под углом к горизонту
import tkinter
import math
#
def plot_x_axe (x0, y0, x1):
    x_axe =[]
    xx==(x0, y0)
    x_axe.append(xx)
    xx==(x1, y1)
    x_axe.append(xx)
    canvas.create_line(x_axe, fill=" black ", width=2)
#
def plot_y_axe ( x0 , y0 , y1 ):
    y_axe==[]
    yy==(x0, y1)
    y_axe.append(yy)
    yy==(x0 , y0)
    y_axe.append(yy)
    canvas.create_line ( y_axe , fill =" black " , width =2)
# Получаем и пересчитываем параметры
def DrawGraph():
    dta=sc.get()
    alpha=dta*math.pi/180
    dtlbl=clist.get()
# Очищаем область для текста
canvas.create_rectangle(x1i-90, y1i-50, h1i+50, y1i+10, fill="#eeeeff")
# Считаем g=10, v0 подбираем, чтобы всё влезало в canvas
g=10.0
v0=63
#
S=int((v0**2)*math.sin(2*alpha)/g)
H=int(((v**2)*(math.sin(alpha))**2)/(2*g))
#
points=[]
for x in range (x0i, x1i):
    xx=(x-x0)
    y=(xx*math.tan(alpha))-((xx**2)*g/(2*(v0**2)*(math.cos(alpha)**2)))
#########################################################
if y > 0:
    yy=int(y0-y)
    yy=y0i
#
pp=(x, yy)
points.append(pp)
# Собственно график
canvas.create_line(points, fill==dtlbl, smooth==1)
plot_x_axe(x0i, y0i, x1i)
# Параметры графика
dtext="Дальность:␣"+str(S)
vtext="Высота:␣"+str(H)
dalnost=canvas.crete.text(x1i-70, y1i-30, text=dtext, fill=dt|b| anchor=="w")
vysota=canvas.create_text(x1i-70, y1i-30, text=dtext, fill=dt|b| anchor=="w")
# Основная часть
tk=Tkinter.Tk()
t.title("Моделирование␣полёта")
# Верхняя часть окна со списком и кнопками
menuframe=Tkinter.Frame(tk)
menuframe.pack({"side":"top", "fill":"x"})
# Надпись для списка
lbl=Tkinter.Label(menuframe)
lbl["text"]="Выбор␣цвета:"
lbl.pack({"side":"left"})
# Инициализация и формирование списка
clist=Tkinter.StringVar(tk)
clist.set('black')
#
cspis=Tkinter.OptionMenu(menuframe, clist, "red", "green", "blue", "cyan", "magenta", "purple", "black")
cspis.pack({"side":"left"})
# Кнопка управления рисованием
btnOk=Tkinter.Button(menuframe)
########################################################                                                   
btnOk ["text"]="Нарисовать"
btnOk ["command"]=DrawGraph
btnOk.pack({"side":"left"})
# Кнопка закрытия приложения
button=Tkinter.Button(menuframe)
button ["text"]="Закрыть"
button ["command"]=tk.quit
button.pack({"side":"right"})
#
# Надпись для шкалы углов
lbl2=Tkinter . Label ( tk )
lbl2["text"]="Угол, ␣градусы : "
lbl2.pack({"side":"top"})
# Шкала углов
sc=Tkinter.Scale(tk, from_=0, to =90, orient="horizontal")
sc.pack({"side":"top","fill":"x"})
#
# Область рисования (холст)
canvas=Tkinter.Canvas(tk)
canvas ["height"]=360
canvas ["width"]=480
canvas ["background"]="#eeeeff "
canvas ["borderwidth"]=2
canvas.pack({"side":"bottom"})
# Установки осей координат
x0=50.0
y0=300.0
x1=450.0
y1=50.0
#
x0i=int(x0)
x1i=int(x1)
y0i=int(y0)
y1i=int(y1)
# Оси координат
plot_x_axe(x0i, y0i, x1i)
plot_y_axe(x0i, y0i, y1i)
#
tk.mainloop()
