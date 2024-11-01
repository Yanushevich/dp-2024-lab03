from decorators.message_decorator import MessageDecorator
from interfaces.message import Message


class HeaderDecorator(MessageDecorator):
    """Декоратор добавления заголовка в начало сообщения"""

    def __init__(self, header: str, message: Message):
        """
        Инициализация декоратора

        Args:
            header (str): Заголовок
            message (Message): Объект сообщения
        """
        super().__init__(message)
        self._message = message
        self._header = header

    def _get_content(self) -> str:
        """Возвращает сообщение"""
        return f"{self._header}\n{self._message._get_content()}"
