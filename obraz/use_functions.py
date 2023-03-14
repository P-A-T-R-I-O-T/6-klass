"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
from invalid_menu import invalid_menu_item, cleaning
from decorator import border_siporaters
import os, pickle

HISORY_FILE = 'history_file'
def menu_selection(): #Выделение пунктов меню
    print('.'*30, '\n' *2)

def top_menu(): # Верхняя граница меню
    print('*' *30, '\n' *2)

def replenishment_of_funds(cash): # 1_меню (пополнение счёта)
    print('Меню пополнение счёта')
    menu_selection()
    amount = input('Пополните счёт: ')
    cleaning()
    while not amount.isdecimal() or not int(amount)>0:
        cleaning()
        invalid_menu_item('Не корректная сумма пополнения счёта!')
        top_menu()
        print('Меню пополнение счёта')
        menu_selection()
        amount = input('Пополните счёт: ')
    cash.append(('Пополнение счёта', int(amount)))
    cleaning()

def purchase(cash): # 2_Меню (Покупка)
    personal_cash = sum([trans[1] for trans in cash])
    if personal_cash == 0:
        invalid_menu_item('У Вас не хватает средств! Пополните свой баланс!')
    else:
        print('Произведите покупку')
        menu_selection()
        amount = input('Введите стоимость товара: ')
        cleaning()
        while not amount.isdecimal() or int(amount)< 1:
            cleaning()
            invalid_menu_item('Не корректная стоимость товара!')
            top_menu()
            print('Произведите покупку')
            menu_selection()
            amount = input('Введите стоимость товара: ')
        if not int(amount) > personal_cash:
            cleaning()
            top_menu()
            print('Произведите покупку')
            menu_selection()
            print('Введите стоимость товара: ', amount)
            name_product = input('Введите наименование продукта: ')
            cleaning()
            cash.append(('Покупка ' + name_product, -int(amount)))
        else:
            cleaning()
            invalid_menu_item('У Вас не хватает денег! Пополните свой баланс')

def history(cash):
    cleaning()
    if len(cash) == 0:
        invalid_menu_item('У Вас нет истории')
    else:
        top_menu()
        print('Ваша история покупок')
        menu_selection()
        for name, amount in cash:
            print(f'> {name} :  {amount}')
            input('\nНажмите Enter чтобы продолжить ')
            cleaning()
@border_siporaters
def menu():
    cash = [] # Деньги
    if os.path.exists(HISORY_FILE):
        with open(HISORY_FILE, 'rb') as f:
            cash = pickle.load(f)
    while True: # Основное меню
        personal_cash = sum([trans[1] for trans in cash])
        print('Ваши средства:', personal_cash, '\n')
        print('Главное меню')
        print('1. пополнение счета: ')
        print('2. покупка: ')
        print('3. история покупок: ')
        print('4. сохранить историю')
        print('5. выход из программы ')
        menu_selection()
        choice = input('Выберите пункт меню:  ')
        cleaning()

        if choice == '1':
            replenishment_of_funds(cash)
            pass
        elif choice == '2':
            purchase(cash)
            pass
        elif choice == '3':
            history(cash)
            pass
        elif choice == '4':
            with open(HISORY_FILE, 'wb') as f:
                pickle.dump(cash, f)
            pass
        elif choice == '5':
            break
        else:
            invalid_menu_item('Неверный пункт меню')

menu()