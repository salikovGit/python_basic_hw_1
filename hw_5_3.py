"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
try:
    with open('hw_5_3.txt', 'r', encoding='UTF-8') as my_file:
        person = []
        salary = []
        my_list = my_file.read().split('\n')
        for i in my_list:
            i = i.split()
            print(i)
            if int(i[1]) < 20000:
                person.append(i[0])
            salary.append(i[1])
except IndexError:
    print("Уберите пустую строку в конце файла")
print(f'\nОклад меньше 20000 у следующих:\n{person};\nСредний оклад составляет: {sum(map(int, salary)) / len(salary)} р.')
