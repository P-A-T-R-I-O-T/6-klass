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

from invalid_menu import invalid_menu_item, cleaning # Предупреждение о неправильном вводе меню и Очистка терминала
from obraz.use_functions import menu_selection # Выделение нижнего пункта меню
from decorator import border_siporaters # Выделение верхнего пункта меню
from faker import Faker # Формирование имён, в нашем случае, имя для компьютера
import random

fake = Faker('ru-RU') # Русские имена

@border_siporaters
def menu_cards():
    while True:
        print("""
    Игра по карточкам
    
    1. Один игрок портив компютера
    2. 2 игрока
    3. 2 компютера
    4. Назад,в предыдущее меню
    5. Выход    
    """)
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
            first_menu()
            pass
        elif item_number == '5':
            exit()
        else:
            invalid_menu_item('Неверный пункт меню')

@border_siporaters
def ticket_menu():
    while True:
        print("""
    Игра по билетам

    1. Один игрок портив компютера
    2. 2 игрока
    3. 2 компютера
    4. Назад,в предыдущее меню
    5. Выход    
    """)
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
            first_menu()
            pass
        elif item_number == '5':
            exit()
        else:
            invalid_menu_item('Неверный пункт меню')
@border_siporaters
def first_menu():
    while True:
        print("""
    Главное меню

    1. Игра по карточкам
    2. Игра по белетам
    3. Выход    
    """)
        menu_selection()
        item_number = input('В какой вариант игры Вы хотите сыграть? \n Введите пункт меню: ')
        cleaning()
        if item_number == '1':
            menu_cards()
            pass
        elif item_number == '2':
            ticket_menu()
            pass
        elif item_number == '3':
            exit()

        else:
            invalid_menu_item('Неверный пункт меню')


first_menu()