class Message:
    """Интерфейс базового сообщения"""

    def __init__(self, message: str):
        """Инициализация сообщения"""
        self._message = message

    def _get_content(self):
        """Возвращает значение объекта"""
        return self._message

    def print(self) -> None:
        """Вывод сообщения в консоль"""
        print(self._get_content())
