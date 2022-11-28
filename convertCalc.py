from convertTypes import *


def run_calculator():
    while True:
        print("Конвертер температур")
        print("Поддерживает следующие значения:")
        print_list_convert()
        temp = int(input("Введите температуру: "))
        dimension_change = input("Введите систему измерения температуры: ")
        dimension_final = input("Введите итоговую систему изерения температуры: ")

        if dimension_change == "C" and dimension_final == "F":
            print(float(temp * (9 / 5) + 32))
        if dimension_change == "F" and dimension_final == "C":
            print(float((temp - 32) * (5 / 9)))
        if dimension_change == "C" and dimension_final == "K":
            print(float(temp + 273.15))
        if dimension_change == "K" and dimension_final == "C":
            print(float(temp - 273.15))
        if dimension_change == "F" and dimension_final == "K":
            print(float((temp - 32) * (5/9) + 273.15))
        if dimension_change == "K" and dimension_final == "F":
            print(float((temp - 273.15) * (9/5) + 32))
        if dimension_change == dimension_final:
            print(f' {dimension_change} = {dimension_final} and {temp} = {temp}')

        if dimension_change not in convertTypes or dimension_final not in convertTypes:
            print("----------------------------")
            print("Неверные входные данные!")
            print("----------------------------")
            continue
        if input("Вы хотите выйти из конвертера? Введите Y или N: ") == "Y":
            break
