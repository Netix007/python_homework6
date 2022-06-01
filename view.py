from tkinter import *
from tkinter.font import *
from win_win import *

step_x = True
step = [' ' for i in range(9)]
pole = [9]
variant = 0

def cl_start(z):
    global variant
    variant = z
    return variant
    
def start():
    f_wind = Tk()
    f_wind.title('крестики-нолики 2022')
    fontStyle = Font(family="Lucida Grande", size=30)
    w = int(f_wind.winfo_screenwidth()/2)
    h = int(f_wind.winfo_screenheight()/2)
    x = int(w - 200)
    y = int(h - 100)
    f_wind.geometry(f'400x200+{x}+{y}')
    btn1 = Button(text='Игра вдвоем', font=fontStyle, command = (lambda: [cl_start(1), f_wind.destroy()]))
    btn1.pack(padx=20, pady=10)
    btn2 = Button(text='Игра с ботом', font=fontStyle, command = (lambda: [cl_start(2), f_wind.destroy()]))
    btn2.pack(padx=20, pady=10)
    f_wind.mainloop()
    return variant

def click_button(i):
    global step_x, step
    if step[i] == ' ' and not is_win(step):
        if step_x:
            pole[i].config(text='X')
            step[i] = 'X'
        else:
            pole[i].config(text='O')
            step[i] = 'O'
        step_x = not step_x
        
        print(is_win(step))

def game_xo():
    global pole 
    game = Tk()
    fontStyle = Font(family="Lucida Grande", size=80)
    w = game.winfo_screenwidth()
    h = game.winfo_screenheight()
    button_size = int(h/6)
    window_size = 3*button_size 
    x = int(w/2 - window_size/2)
    y = int(h/2 - window_size/2)
    game.title('крестики-нолики 2022')
    game.geometry('{}x{}+{}+{}'.format(window_size, window_size, x, y))
    for i in range(3):
        game.columnconfigure(index=i, weight=1)
        game.rowconfigure(index=i, weight=1)
    pixel = PhotoImage(width=button_size, height=button_size)
    pole = [Button(image=pixel, text=' ', font=fontStyle, compound='c',\
            command = (lambda z = 3*i + j: click_button(z))) for i in range(3) for j in range(3)]
    for i in range(9):
        pole[i].grid(column=i%3, row=i//3)
    game.mainloop()