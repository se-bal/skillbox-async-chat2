"""
Пример программы для работы с ООП

Сделать
- класс User от класса Person
- добавить поле для пароля
- добавить метод проверки пароля
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


class User(Person):
    password: str

    def check_password(self, user_password):
        return self.password == user_password


user = User("John", "Doe", 30)
user.info()
user.say("Hello")

user.password = "123123"
print(user.check_password("456456"))
print(user.check_password("123123"))
