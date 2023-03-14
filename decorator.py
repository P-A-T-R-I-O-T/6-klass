"""
Декоратор не работает должным образом (как мне хочется, чтобы он работал) функции menu()
"""
def border_siporaters(f):
    def inner():
        print('*' * 30, '\n' * 2)
        resultat = f()
        return resultat

    return inner