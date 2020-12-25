"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
my_file = open ('hw_5_2.txt', 'r')
print(f"Количество строк в файле: {len(my_file.readlines())}")
my_file = open ('hw_5_2.txt', 'r')
strings = my_file.readlines()
my_file = open ('hw_5_2.txt', 'r')
for i in range(len(my_file.readlines())):
    print(f'Количество символов в {i + 1} строке {len(strings[i])}')
my_file.close()
