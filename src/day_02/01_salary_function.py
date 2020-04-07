"""
Пример программы для работы с функциями (аналог файла 01_hours_salary.py)

Аргументы
- стоимость часа в руб
- количество дней в руб

Сделать
- функцию, которая вернет размер зарплаты в руб
"""


def salary(hour_cost: int, day_quantity: int):
    total = (hour_cost * 8) * day_quantity
    final = total - (total * .13)

    return final


a = salary(100, 1)
b = salary(100, 2)

print(a, b)
