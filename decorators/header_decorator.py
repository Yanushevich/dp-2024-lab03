from decorators.message_decorator import MessageDecorator
from interfaces.message import Message


class HeaderDecorator(MessageDecorator):
    """Добавление заголовка"""

    def __init__(self, header: str, message: Message):
        super().__init__(message)
        self._message = message
        self._header = header

    def get_message(self):
        return f"{self._header}\n{self._message.get_message()}"
