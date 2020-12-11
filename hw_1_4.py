user_digit = input("Введите число >>> ")
user_digit = int(user_digit)
biggest = 0
while user_digit > 10:
    remainder = user_digit % 10
    if remainder > biggest:
        biggest = remainder
    user_digit //= 10
if user_digit > biggest:
    biggest = user_digit
print(f"Наибольшая цифра в числе - {biggest}")
