"""
ticket= 0 # билет
card = 0 # карточка
line = 0 # строка
column = 0 # столб
cell = 0 # ячейка
object = 0 # объект

ticket = card * 2 == line * 6 == column * 9 == cell * 54 == object * 30
card = line * 3 == column * 9 == cell * 27 == object * 15
line = column * 9 == object * 5
column = cell * 3 == object
"""

from invalid_menu import invalid_menu_item, cleaning
from obraz.use_functions import top_menu, menu_selection
from decorator import border_siporaters
import random

@border_siporaters
def menu():
    while True:
        text_menu = """
    Главное меню
    
    1. Один игрок портив компютера
    2. 2 игрока
    3. 2 компютера
    4. Выход    
    """
        print(text_menu)
        menu_selection()
        item_number = input('Как вы хотите сыграть? \n Введите пункт меню: ')
        cleaning()

        if item_number == '1':

            pass
        elif item_number == '2':

            pass
        elif item_number == '3':

            pass
        elif item_number == '4':
            break
        else:
            invalid_menu_item('Неверный пункт меню')

menu()