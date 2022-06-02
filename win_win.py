

def is_win(list_cell):  #проверка на победу
    diag1, diag2 = '', ''
    for i in range(3):
        col, row = '', ''
        for j in range(3):
            col += list_cell[3*j + i]
            row += list_cell[3*i + j]
            if i == j:
                diag1 += list_cell[4*i]
                diag2 += list_cell[2*i + 2]
        if col in ['XXX', 'OOO'] or row in ['XXX', 'OOO']:
            return True
    if diag1 in ['XXX', 'OOO'] or diag2 in ['XXX', 'OOO']:
        return True
    return False