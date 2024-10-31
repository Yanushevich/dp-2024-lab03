class Message:
    """Интерфейс базового сообщения"""

    def __init__(self, message: str):
        """Инициализация сообщения"""
        self._message = message

    def get_message(self):
        """Возвращает значение"""
        return self._message

    def print(self) -> None:
        """Вывод сообщения в консоль"""
        print(self.get_message())
