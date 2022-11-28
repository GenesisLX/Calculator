from prettytable import PrettyTable

convertTypes = {
    "K": "Кельвины",
    "F": "Фаренгейты",
    "C": "Цельсии"
}


def print_list_convert():
    mytable_oper = PrettyTable()
    # имена полей таблицы
    mytable_oper.field_names = ["Обозначение", "Что означает?"]
    # добавление данных по одной строке за раз
    for typ in convertTypes:
        mytable_oper.add_row([typ, convertTypes[typ]])
    # вывод таблицы в терминал
    print(mytable_oper)
