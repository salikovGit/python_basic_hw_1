"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
import typing


def salary_count(hours, hour_payment, bonus):
    sal = hours * hour_payment + bonus
    return sal

if len(argv) != 4:
    print("Ошибка ввода параметров! Введите Выработку в часах, ставку в час и премию")
    exit()

params = []

for param in argv[1:]:
    try:
        param = int(param)
        params.append(param)
    except ValueError:
        print("введите целочисленные значения")
    if len(params) == 3:
        salary = salary_count(*params)
        print(salary)
