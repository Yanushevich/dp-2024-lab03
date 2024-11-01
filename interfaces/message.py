class Message:
    """Интерфейс базового сообщения"""

    def __init__(self, message: str):
        """
        Инициализация сообщения

        Args:
            message (str): Сообщение
        """
        self._message = message

    def _get_content(self) -> str:
        """Возвращает значение объекта"""
        return self._message

    def print(self) -> None:
        """Вывод сообщения в консоль"""
        print(self._get_content())
