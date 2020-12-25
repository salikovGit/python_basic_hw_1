"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
with open('hw_5_5.txt', 'w+') as my_file:
    text = []
    sum = 0
    for i in range(int(random.random()*100)):
        num = random.random()*100
        sum += num
        num = str(num)
        my_file.writelines(num[0:5:] + " ")
        text.append(num)
print(f"Сумма чисел в файле hw_5_5 равна: {sum}")
