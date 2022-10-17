# Мозг
import model_addition as ma
import model_division as md
import model_subtraction as ms
import model_exponentiation as me
import model_multiplication as mm
import view

def select_menu(a):
    if a == 1:
        ma.fn_addition(view.get_numbers_a(), view.get_numbers_b())
    if a == 2:
        md.fn_division(view.get_numbers_a(), view.get_numbers_b())
    if a == 3:
        ms.fn_model_subtraction(view.get_numbers_a(), view.get_numbers_b())
    if a == 4:
        mm.fn_model_multiplication(view.get_numbers_a(), view.get_numbers_b())
    if a == 5:
        me.fn_model_exponentiation(view.get_numbers_a(), view.get_numbers_b())
    #else:
