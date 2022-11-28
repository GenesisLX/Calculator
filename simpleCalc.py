from mathTypes import *


def run_calculator():
    # Описание калькулятора
    print("Простой калькулятор")
    print("Выполняет следующие команды:")
    print_list_math_opers()
    print("----------------------------")
    # калькулятор
    num1 = int(input("Введите первое число: "))
    while True:
        oper = input("Введите знак операции: ")
        if oper not in mathTypes:
            print("Некорректная операция")
            continue

        num2 = int(input("Введите второе число: "))

        if num2 == 0 and (oper == "/" or oper == "//"):
            print("Делить на ноль запрещено.")
            continue

        print("--------------------------------")
        print(f' {num1} {oper} {num2} = {eval(str(num1) + oper + str(num2))}')
        num1 = eval(str(num1) + oper + str(num2))
        print("--------------------------------")

        if input("Вы хотите выйти из калькулятора? Введите Y или N: ") == "Y":
            break
