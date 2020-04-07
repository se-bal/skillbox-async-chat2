"""
Пример программы для работы с ООП

Сделать
- добавить метод для вывода сообщений с префиксом имени
- добавить метод для вывода информации об объекте
- добавить конструктор класса для формирования полей
"""


class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        print(f"{self.first_name} {self.last_name}, age: {self.age}")

    def say(self, content):
        print(f"<{self.first_name}>: {content}")


user = Person("John", "Doe", 30)
user.info()
user.say("Hello")
