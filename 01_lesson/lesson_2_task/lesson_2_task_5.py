
#Напишите функцию
# month_to_season(), которая принимает один аргумент — номер месяца
# — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима».


month = input("Введите номер месяца 1-- 12: ")

def month_to_season(month):

    m = int(month)
    if m == 1 or m == 2 or m == 12:
        print("Зима")

    elif m == 3 or m == 4 or m == 5:
        print("Весна")

    elif m == 6 or m == 7 or m == 8:
        print("Лето")

    else:  # месяцы 9, 10, 11
        print("Осень")


month_to_season(month)
