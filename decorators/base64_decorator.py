import base64

from decorators import MessageDecorator
from interfaces.message import Message


class Base64Decorator(MessageDecorator):
    """Декоратор кодирования сообщения в Base64"""

    def __init__(self, message: Message):
        """
        Инициализация декоратора

        Args:
            message (Message): Объект сообщения
        """
        super().__init__(message)
        self._message = message
        self._base64 = self._get_base64()

    def _get_content(self) -> str:
        """Возвращает сообщение"""
        return self._base64

    def _get_base64(self) -> str:
        """Кодирование в Base64"""
        return base64.b64encode(self._message._get_content().encode("utf-8")).decode(
            "utf-8"
        )
