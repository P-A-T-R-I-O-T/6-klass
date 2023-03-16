"""
Декоратор не работает должным образом (как мне хочется, чтобы он работал) функции menu()
"""
def border_siporaters(f):
    def inner():
        print('*' * 30)
        resultat = f()
        return resultat

    return inner