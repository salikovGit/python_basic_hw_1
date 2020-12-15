"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
"""
print('Вводите элементы для заполнения списка. Для разделения элементов используйте пробел \n>>> ')
user_list = list(input().split(' '))
print("Ваш список: ", user_list)
j = 0
if len(user_list) % 2 == 0:
    for i in range(int(len(user_list)/2)):
        user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
        j += 2
else:
    for i in range(int((len(user_list)-1)/2)):
        user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
        j += 2
print("Ваш список после обмена соседних значений: ", user_list)
