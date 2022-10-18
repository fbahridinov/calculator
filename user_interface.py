# Мозг
import model_addition as ma
import model_division as md
import model_exponentiation as mx
import model_multiplication as mm
import model_subtraction as ms

import view

def select_menu(a):
    if a == 1:
        ma.fn_addition(view.get_numbers_a(), view.get_numbers_b())
    elif a == 2:
        md.fn_division(view.get_numbers_a(), view.get_numbers_b())
    elif a == 3:
        mx.fn_model_exponentiation(view.get_numbers_a(), view.get_numbers_b())
    elif a == 4:
        mm.fn_model_multiplication(view.get_numbers_a(), view.get_numbers_b())
    elif a == 5:
        ms.fn_model_subtraction(view.get_numbers_a(), view.get_numbers_b())
    elif a > 5:
        print('Нет такой операции!!!')

