"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_file = []
with open('hw_5_4.txt', 'r', encoding='UTF-8') as eng_file:
    for elem in eng_file:
        elem = elem.split(' ', 1)
        rus_file.append(rus[elem[0]] + ' ' + elem[1])
with open('hw_5_4_rus.txt', 'w', encoding='UTF-8') as russian:
    russian.writelines(rus_file)
