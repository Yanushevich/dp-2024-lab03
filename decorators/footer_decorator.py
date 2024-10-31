from decorators import MessageDecorator
from interfaces.message import Message


class FooterDecorator(MessageDecorator):
    """Декоратор добавления подписи в конец сообщения"""

    def __init__(self, footer: str, message: Message):
        """Инициализация декоратора"""
        super().__init__(message)
        self._message = message
        self._footer = footer

    def _get_content(self) -> str:
        """Возвращает сообщение"""
        return f"{self._message._get_content()}\n{self._footer}"
