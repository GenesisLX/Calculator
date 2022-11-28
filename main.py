from calculatorTypes import print_menu, calculatorTypes

while True:
    # Виды калькулятора
    print("Калькулятор выражений")
    print("Меню")
    print("Виды калькулятора: ")
    print_menu(["Номер вида калькулятора", "Название"])
    calc_type = input("Выберите вид калькулятора: ")
    print("----------------------------")

    # print(calculatorTypes[calc_type]["handler"])
    calculatorTypes[calc_type]["handler"]()

    if input("Завершить работу? Введите Y или N: ") == 'Y':
        break
