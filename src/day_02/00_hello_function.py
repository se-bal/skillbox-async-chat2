"""
Пример программы для работы с функциями

Сделать
- функцию hello, которая выводит текст приветствия клиенту
"""


def user_hello(user: str):
    print(f"Hello, {user}")


clients = ['John', 'David', 'Kate', 'Alex']

for user in clients:
    user_hello(user)

clients_two = ['Edward']

for user in clients_two:
    user_hello(user)
