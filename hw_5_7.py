"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой
компании, а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь
с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
"""
import json
with open('hw_5_7.txt', 'r', encoding='UTF-8') as file:
    profit = {}
    avg_profit = {}
    sum_profit= 0
    average_profit = 0
    i = 0
    for line in file:
        name, firm, income, losses = line.split()
        profit[name] = int(income) - int(losses)
        if profit.setdefault(name) >= 0:
            sum_profit+= profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = sum_profit/ i
        print(f'Средняя прибыль - {average_profit:.2f}')
    else:
        print(f'Все в минусе')
    avg_profit= {'Cредняя прибыль': round(average_profit)}
    profit.update(avg_profit)
    print(f'Прибыль каждой компании - {profit}')

with open('hw_5_7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')