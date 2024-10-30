from decorators import MessageDecorator
from interfaces.message import Message


class FooterDecorator(MessageDecorator):
    """Добавление подписи"""

    def __init__(self, footer: str, message: Message):
        super().__init__(message)
        self._message = message
        self._footer = footer

    def get_message(self):
        return f"{self._message.get_message()}\n{self._footer}"
