proceeds = input("Укажите выручку предприятия: >>> ")
proceeds = int(proceeds)
costs = input("Укажите издержки предприятия: >>> ")
costs = int(costs)

if proceeds > costs:
    profit = proceeds - costs
    print(f"Компания получила выручку: {profit}")
    print(f"Рентабельность выручки составляет: {profit / proceeds:.3f}")
    employes = input("Укажите численность сотрудников компании: >>> ")
    print(f"В расчете на одного сотрудника прибыль фирмы составляет: {profit / int(employes):.3f}")
elif proceeds == costs:
    print("Компания отработала в ноль")
else:
    print("Компания понесла убытки")
