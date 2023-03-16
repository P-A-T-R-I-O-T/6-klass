"""
Делаю программу Лото.

"""
from invalid_menu import invalid_menu_item
from obraz.use_functions import top_menu, menu_selection
from decorator import border_siporaters

"""def menu():
    text_menu = 
    Главное меню
    1. Один игрок портив компютера
    2. 2 игрока
    3. 2 компютера
    4 Выход    
    
    print(text_menu)
    item_number = input('Как вы хотите сыграть? \n Введите пункт меню')
    return int(item_number)

menu()"""

text_menu = """
    Главное меню
    1. Один игрок портив компютера
    2. 2 игрока
    3. 2 компютера
    4 Выход    
    """
print(text_menu)
item_number = input('Как вы хотите сыграть? \n Введите пункт меню')