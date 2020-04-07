"""
Пример программы для работы с ООП

Данные класса
- имя
- фамилия
- возраст
"""


class Person:
    first_name: str
    last_name: str
    age: int


user = Person()
user.first_name = "John"
user.last_name = "Doe"
user.age = 30

print(user.first_name, user.last_name, user.age)
