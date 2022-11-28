from prettytable import PrettyTable

mathTypes = {
    "+": "сложение",
    "-": "вычитание",
    "*": "умножение",
    "/": "деление с остатком",
    "//": "целочисленное деление",
    "%": "остаток от деления",
    "**": "возведение в степень"
}


def print_list_math_opers():
    mytable_oper = PrettyTable()
    # имена полей таблицы
    mytable_oper.field_names = ["Операция", "Что выполняет?"]
    # добавление данных по одной строке за раз
    for i in mathTypes:
        mytable_oper.add_row([i, mathTypes[i]])
    # вывод таблицы в терминал
    print(mytable_oper)
