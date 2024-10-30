import base64

from decorators import MessageDecorator
from interfaces.message import Message


class Base64Decorator(MessageDecorator):
    """Кодирование в Base64"""

    def __init__(self, message: Message):
        super().__init__(message)
        self._message = message
        self._base64 = base64.b64encode(
            self._message.get_message().encode("utf-8")
        ).decode("utf-8")

    def get_message(self):
        return self._base64
