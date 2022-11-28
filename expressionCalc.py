from mathTypes import print_list_math_opers


def run_calculator():
    # Описание калькулятора
    # print("Калькулятор примеров")
    # print("Поддерживает следующие команды:")
    print_list_math_opers()
    # калькулятор
    while True:
        num1 = input("Введите пример: ")
        try:
            print(f'{num1} = {eval(num1)}')
        except Exception as e:
            print(f'Ошибка вычисления примера: {e}')
        print("----------------------------")

        if input("Вы хотите выйти из калькулятора примеров? Введите Y или N: ") == "Y":
            break
