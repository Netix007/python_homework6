from tkinter import *
from tkinter.font import *
from win_win import *
from random import choice

def cl_start(z): #настнойка кнопок начального меню
    global variant
    variant = z
    
def start(): #начальное меню
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

def click_button(i, variant): #кнопки игрового поля
    global pole, step, step_x, bot_step, game
    if step[i] == ' ' and not is_win(step):
        if variant == 1:
            if step_x:
                pole[i].config(text='X')
                step[i] = 'X'
            else:
                pole[i].config(text='O')
                step[i] = 'O'
            step_x = not step_x
            who_win(step, step_x)
        else:
            pole[i].config(text='X')
            step[i] = 'X'
            step_x = not step_x
            if is_win(step) or " " not in step:
                who_win(step, step_x)
            else:
                del bot_step[bot_step.index(i)]
                i = choice(bot_step)
                pole[i].config(text='O')
                step[i] = 'O'
                step_x = not step_x
                if is_win(step):
                    who_win(step, step_x)
                else:
                    del bot_step[bot_step.index(i)]

def game_xo(variant): #игровое поле
    global pole, step, step_x, bot_step, game, is_end
    pole = [9]
    step = [' ' for j in range(9)]
    bot_step = [i for i in range(9)]
    step_x = True
    is_end = False
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
            command = (lambda z = 3*i + j: click_button(z, variant))) for i in range(3) for j in range(3)]
    for i in range(9):
        pole[i].grid(column=i%3, row=i//3)
    game.mainloop()
    return is_end

def result(a):
    result_wind = Toplevel()
    if variant == 1:
        players = 'Игрок 1 vs Игрок 2'
    else:
        players = 'Игрок 1 vs Бот'
    result_wind.title(f'Результаты игры: {players}')
    fontStyle = Font(family="Lucida Grande", size=30)
    w = int(result_wind.winfo_screenwidth()/2)
    h = int(result_wind.winfo_screenheight()/2)
    x = int(w - 200)
    y = int(h - 100)
    result_wind.geometry(f'400x200+{x}+{y}')
    lab = Label(result_wind, text=a, font='Arial 14')
    lab.pack()
    btn1 = Button(result_wind, text='Сыграть ещё раз', font=fontStyle, command = (lambda: restart_game()))
    btn1.pack(padx=20, pady=10)
    btn2 = Button(result_wind, text='Выйти из игры', font=fontStyle, command = (lambda: end_game()))
    btn2.pack(padx=20, pady=10)
    result_wind.mainloop()

def who_win(step, step_x):
    if (is_win(step)):
        if step_x:
            result('Выиграл Игрок 2')
        else:
            result('Выиграл Игрок 1')
    elif ' ' not in step:
        result('Ничья')

def restart_game():
    game.destroy()

def end_game():
    global is_end
    is_end = True
    game.destroy()

    
