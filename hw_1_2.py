time_in_sec = input("Введите время в секундах >>> ")
hours = int(time_in_sec) // 3600
minutes = int(time_in_sec) % 3600 // 60
seconds = int(time_in_sec) - hours*3600 - minutes*60
time = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(time)
