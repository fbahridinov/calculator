# Мозг
import model_addition as ma
import model_division as md
import view


def select_menu(a):
    if a == 1:
        ma.fn_addition(view.get_numbers_a(), view.get_numbers_b())
    elif a == 2:
        md.fn_division(view.get_numbers_a(), view.get_numbers_b())