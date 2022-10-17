# Запросить информацию и показать информацию

def online_calc_massage():
    print('\nКалькулятор онлайн \n')


def choose_operation_massage():
    print('Выберите операцию')


def show_menu():
    menu = {
        1: 'Сложение',
        2: 'Деление',
        3: 'Возведение в степень',
        4: 'Умножение',
        5: 'Вычитание \n'
    }
    return menu


def get_numbers_a():
    number_a = input('Число А: ')
    if number_a.find('.') == True:
        number_a = float(number_a)
    else:
        number_a = int(number_a)
    return number_a


def get_numbers_b():
    number_b = input('Число Б: ')
    if number_b.find('.') == True:
        number_b = float(number_b)
    else:
        number_b = int(number_b)
    return number_b
