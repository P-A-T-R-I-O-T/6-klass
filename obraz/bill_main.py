"""
Добавим 1. Открытие счета. 2. Счетов может быть несколько
3. Накопительный счет - с него нельзя снимать денги
"""
from bill03 import Bill, SavingBill

my_bills = {}
current_bill = None

while True:
    print('1. Положить')
    print('2. Покупка')
    print('3. История покупок')
    print('4. Выход')
    print('5. Открыть новый счет')
    print('6. Выбрать рабочий счет')
    print('7. Открыть накопительный счет')

    choise = input('Выберите пункт: ')
    if choise == '1':
        count = int(input('Количество денег: '))
        current_bill.add(count)
    elif choise == '2':
        count = int(input('Стоимость: '))
        if current_bill.can_by(count):
            name = input('Название покупки')
            current_bill.buy(count, name)
        else:
            if isinstance(current_bill, SavingBill):
                print('Счет накопительный')
            elif isinstance(current_bill, Bill):
                print('Не хватает денег')
            else:
                print('Какой то не такой счет')
    elif choise == '3':
        print(current_bill.history)
    elif choise == '4':
        break
    elif choise == '5':
        name = input('Введите имя счета')
        if name in my_bills:
            print('Такой счет уже есть')
        else:
            new_bill = Bill()
            my_bills[name] = new_bill
            # my_bills[name] = Bill()

    elif choise == '6':
        name = input('Введит имя счета')
        if name in my_bills:
            current_bill = my_bills[name]
        else:
            print('Такого счета нет')
    elif choise == '7':
        # TODO: Убрать дублирование с пунктом 5
        name = input('Введите имя счета')
        if name in my_bills:
            print('Такой счет уже есть')
        else:
            new_bill = SavingBill()
            my_bills[name] = new_bill
