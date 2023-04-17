"""
Создал карточки и правило игры,
осталось создать запуск формирование имен перед игрой в пунк 1 второго меню
"""

from invalid_menu import invalid_menu_item, cleaning # Предупреждение о неправильном вводе меню и Очистка терминала
from obraz.use_functions import menu_selection # Выделение нижнего пункта меню
from decorator import border_siporaters # Выделение верхнего пункта меню
from faker import Faker # Формирование имён, в нашем случае, имя для компьютера
from random import randint

fake = Faker('ru-RU') # Русские имена

@border_siporaters # 2 меню Игра по карточкам
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
            start_game()
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

@border_siporaters # 2 меню Инра по белетам
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

@border_siporaters # Главное меню
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


def generate_unique_numbers(count, minimal, max):
    objects = []
    while len(objects) < count:
        new = randint(minimal, max)
        if new not in objects:
            objects.append(new)
    return objects


# Цыкл доставания бачёнков
class Keg:
    __num = None

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)


# Формирование карточки
class Card:
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
    line = 3
    cell = 9
    object = 5
    data = None
    emptynum = 0
    crossednum = -1

    def __init__(self):
        uniques_count = self.object * self.line
        uniques = generate_unique_numbers(uniques_count, 1, 90)
        self.data = []
        for i in range(0, self.line):
            tmp = sorted(uniques[self.object * i: self.object * (i + 1)])
            empty_nums_count = self.cell - self.object
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self.emptynum)
            self.data += tmp

    def __str__(self):
        delimiter = '--------------------------'
        ret = delimiter + '\n'
        for index, num in enumerate(self.data):
            if num == self.emptynum:
                ret += '  '
            elif num == self.crossednum:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.cell == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter

    def __contains__(self, item):
        return item in self.data

    def cross_num(self, num):
        for index, item in enumerate(self.data):
            if item == num:
                self.data[index] = self.crossednum
                return
        raise ValueError(f'Номера нет в карточке: {num}')

    def closed(self) -> bool:
        return set(self.data) == {self.emptynum, self.crossednum}


class Game:
    __usercard = None
    __compcard = None
    __numkegs = 90
    __kegs = []
    __gameover = False

    def __init__(self):
        self.__usercard = Card()
        self.__compcard = Card()
        self.__kegs = generate_unique_numbers(self.__numkegs, 1, 90)

    def play_round(self) -> int:
        keg = self.__kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'-- Карточка игрока --- \n{self.__usercard}')
        print(f'-- Карточка компьютера ---\n{self.__compcard}')

        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if useranswer == 'y' and not keg in self.__usercard or \
           useranswer != 'y' and keg in self.__usercard:
            return 2

        if keg in self.__usercard:
            self.__usercard.cross_num(keg)
            if self.__usercard.closed():
                return 1
        if keg in self.__compcard:
            self.__compcard.cross_num(keg)
            if self.__compcard.closed():
                return 2

        return 0


def start_game():
    if __name__ == '__main__':
        game = Game()
        while True:
            score = game.play_round()
            if score == 1:
                print('Вы победили')
                break
            elif score == 2:
                print('Вы проиграли')
                break



first_menu()