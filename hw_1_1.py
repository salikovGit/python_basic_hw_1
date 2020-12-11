variable_1 = 23
variable_2 = 304
print(f"{variable_1} {variable_2}")
user_string = input("Введите текст >>> ")
user_digit = input("Введите число >>> ")
if user_digit.isdigit():
    print(f"""
    Вы ввели следующее сообщение: {user_string}
    Вы ввели следующее число: {user_digit}
    """)
else:
    print(f""" 
    Вы ввели следующее сообщение: "{user_string}"
    Введенные данные не являются числом! Пожалуйста, повторите ввод
    """)
