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
        print(step)

root = Tk()
fontStyle = Font(family="Lucida Grande", size=80)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
button_size = int(h/6)
window_size = 3*button_size 
x = int(w/2 - window_size/2)
y = int(h/2 - window_size/2)
root.title('крестики-нолики 2022')
root.geometry('{}x{}+{}+{}'.format(window_size, window_size, x, y))
for i in range(3):
    root.columnconfigure(index=i, weight=1)
    root.rowconfigure(index=i, weight=1)
pixel = PhotoImage(width=button_size, height=button_size)
pole = [Button(image=pixel, text=' ', font=fontStyle, compound='c',\
        command = (lambda z = 3*i + j: click_button(z))) for i in range(3) for j in range(3)]
for i in range(9):
    pole[i].grid(column=i%3, row=i//3)
root.mainloop()