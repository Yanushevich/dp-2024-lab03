class Message:
    """Создание базового сообщения"""

    def __init__(self, message: str):
        self._message = message

    def get_message(self):
        return self._message

    def print(self) -> None:
        print(self.get_message())
