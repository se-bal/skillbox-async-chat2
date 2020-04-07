#
# Серверное приложение для соединений
#
import asyncio
from asyncio import transports


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes):
        print(data)

        decoded = data.decode().replace("\r\n", "")

        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("login:"):
                login = decoded.replace("login:", "")
                if self.login_used(login):
                    self.transport.write(f"Логин {login} занят, попробуйте другой\n".encode())
                    print(f"Сессия клиента завершена при попытке установить логин {login}")
                    self.transport.close()
                else:
                    self.login = login
                    self.transport.write(
                        f"Привет, {self.login}!\n".encode()
                    )
                    self.send_history()
            else:
                self.transport.write("Неправильный логин\n".encode())

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("Пришел новый клиент")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("Клиент вышел")

    def send_message(self, content: str):
        message = f"{self.login}: {content}\n"

        for user in self.server.clients:
            if user is self:
                continue
            user.transport.write(message.encode())

        self.server.message_history.append(message)
        while len(self.server.message_history) > 10:
            del self.server.message_history[0]

    def login_used(self, login: str):
        for user in self.server.clients:
            if user.login == login:
                return True
        return False

    def send_history(self):
        self.transport.write("Сейчас обсуждают:\n".encode())
        for message in self.server.message_history:
            self.transport.write(f"{message}".encode())


class Server:
    clients: list
    message_history: list

    def __init__(self):
        self.clients = []
        self.message_history = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )

        print("Сервер запущен ...")

        await coroutine.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
