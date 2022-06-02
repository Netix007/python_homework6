from test import *

def start_game():
    is_end = False
    while not is_end:
        variant = start()
        is_end = game_xo(variant)
        