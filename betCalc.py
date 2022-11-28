def run_calculator():
    while True:
        print("Калькулятор доходности вклада")
        print("*Программа начислеят проценты на вклад")
        print("Программа поддерживает периодичности капитализации:")
        print("- 1 месяц")
        print("- 3 месяца (1 квартал)")
        print("- 12 месяцев (1 год)")
        print("----------------------------")

        capital = float(input("Введите сумму вклада: "))
        time = int(input("Введите срок вклада (в месяцах): "))
        bet_percent = float(input("Введите процентную ставку (число): "))
        regularity = int(input("Введите периодичность капитализации (месяц):"))

        if regularity == 1:
            print(int(capital))
            for i in range(0, time):
                bet_percent_month = bet_percent / 12
                capital = capital + (capital / 100 * bet_percent_month)
                print(int(capital))
        elif regularity == 3:
            print(int(capital))
            for i in range(0, time // 3):
                bet_percent_month = bet_percent / 12
                bet_percent_quarter = bet_percent_month * 3
                capital = capital + (capital / 100 * bet_percent_quarter)
                print(int(capital))
        elif regularity == 12:
            print(int(capital))
            for i in range(0, time // 12):
                capital = capital + (capital / 100 * bet_percent)
                print(int(capital))
        else:
            print("Некорректные данные!")

        print("--" * 10)

        if input("Вы хотите выйти из калькулятора доходности вклада? Введите Y или N: ") == "Y":
            break
