current_result = input("Введите текущий результат пробежки: >>> ")
current_result = int(current_result)
target_result = input("Введите целевой результат пробежки: >>> ")
target_result = int(target_result)
day = 1
if current_result < target_result:
    while current_result < target_result:
        print(f"{day}-й день: {current_result:.2f} км")
        day += 1
        current_result *= 1.1
    print(f"{day}-й день: {current_result:.2f} км")
    print(f"Ответ: на {day}-й день спортсмен достиг результата - не менее {target_result} км")
else:
    print("Цель достигнута!")
