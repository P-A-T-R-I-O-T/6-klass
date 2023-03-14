from decorator import border_siporaters
import time, os

def cleaning (): # Очистка терминала
    # os.system('cls' if os.name == 'nt' else 'clear') # Почему-то выходит строчка: TERM environment variable not set
    print('\n' * 100)
def invalid_menu_item(error = 'Неверный пункт меню', num_seconds = 3 ): # Рамка: Неверного пункт меню
    indent = ' '
    indent_2 = ' '
    if len(error) >= 37: # Работа с длинными предупреждениями
        error_1 = error[:len(error) // 2] # Делим на 2с равные части
        error_2 = error[len(error) //2:]
        
        for char1 in error_2[:5]:  # второую часть, начало строки (до максимального размера страки которая может войти в строку) проверяем на знаки припенания
            if char1 in [' ','.', ',', ':', ';', '!', '?']:
                search1 = error_2.find(char1) # Ищем данный символ в строке
                error_1 = error_1 + error_2[:search1:] #Слияние пер
                error_2 = error_2[search1:] # вычитание не нужных символов
        
    border = '|-|' 
    print(border * 13)    # Печатаем верхнюю рамки
    len(border +indent * 33 + border)
    print(border + indent * 33 + border)
    
    if len(error) >= 37: # В случаи когда главный параметр больше максимального значения, выравниваем по центру рамки
        if len(border + indent + error_1 + indent_2 + border) < 39:
            while len(border + indent + error_1 + indent_2 + border) <= 38:
                indent += ' '
                indent_2 += ' '
            if len(border + indent + error_1 + indent_2 + border) > 39:
                indent = indent[1:]
            print(border + indent + error_1 + indent_2 + border)
            indent = ' '
            indent_2 = ' '

        if len(border + indent + error_2 + indent_2 + border) < 39:
            while len(border + indent + error_2 + indent_2 + border) <= 38:
                indent += ' '
                indent_2 += ' '
            if len(border + indent + error_2 + indent_2 + border) > 39:
                indent = indent[1:]
            print(border + indent + error_2 + indent_2 + border)
    
    elif len(error) < 37:  # В случаи когда главный параметр маленькое значение, выравниваем по центру рамки
        indent = ' '
        indent_2 = ' '
        while len(border + indent + error + indent_2 + border) <= 38:
            indent += ' '
            indent_2 += ' '
        if len(border + indent + error + indent_2 + border) > 39:
                indent = indent[1:]
        print(border + indent + error + indent_2 + border)
    indent = ' '
    print(border + indent * 33 + border)
    print(border * 13)
    print('\n'* 2)
    time.sleep(num_seconds)
    cleaning()