#from calendar import c
from tkinter import *
from tkinter.font import *

step_x = True
step = ['' for i in range(9)]

def click_button(i):
    global step_x, step
    if step[i] == '':
        if step_x:
            pole[i].config(text='X')
            step[i] = 'X'
        else:
            pole[i].config(text='O')
            step[i] = 'O'
        step_x = not step_x


root = Tk()
fontStyle = Font(family="Lucida Grande", size=100)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
button_size = int(h/6)
window_size = 3*button_size 
x = int(w/2 - window_size/2)
y = int(h/2 - window_size/2)
root.title('крестики-нолики 2022')
root.geometry('{}x{}+{}+{}'.format(window_size, window_size, x, y))
pixel = PhotoImage(width=1, height=1)
pole = [Button(image=pixel, text=' ', font=fontStyle, height=button_size, width=button_size, compound='c',\
        command = (lambda z = 3*i + j: click_button(z))) for i in range(3) for j in range(3)]
for i in range(9):
    pole[i].grid(column=i%3, row=i//3)
root.mainloop()