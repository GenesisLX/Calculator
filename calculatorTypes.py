from prettytable import PrettyTable

from simpleCalc import run_calculator as run_simple_calc
from expressionCalc import run_calculator as run_expression_calc
from convertCalc import run_calculator as run_convert_calc
from betCalc import run_calculator as run_bet_calc
from notationCalc import run_calculator as run_notation_calc
from guiCalc import run_calculator as run_gui_calc

calculatorTypes = {
    "1": {"handler": run_simple_calc, "name": "Простой калькулятор"},
    "2": {"handler": run_expression_calc, "name": "Вычисление примеров"},
    "3": {"handler": run_convert_calc, "name": "Конвертер температур"},
    "4": {"handler": run_bet_calc, "name": "Расчёт доходности вклада"},
    "5": {"handler": run_notation_calc, "name": "Перевод в 10-ую систему счисления"},
    "6": {"handler": run_gui_calc, "name": "GUI-калькулятор"}
}


def print_menu(field_names: list):
    menu_items = PrettyTable()
    # формируем наименования полей таблицы
    # menu_items.field_names = ["Номер вида калькулятора", "Название"]
    menu_items.field_names = field_names
    # формируем данные таблицы
    for key in calculatorTypes:
        menu_items.add_row([key, calculatorTypes[key]["name"]])
    # вывод таблицы в терминал
    print(menu_items)
