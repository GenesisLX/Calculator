def run_calculator():
    print("Переводчик в 10-ую систему счисления")
    while True:
        mutable_num = input("Введите число: ")
        base = int(input("Введите систему счисления: "))
        print("Результат:", int(mutable_num, base))

        if input("Вы хотите выйти из калькулятора 10-ой системы счисления? Введите Y или N: ") == "Y":
            break
