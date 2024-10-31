from interfaces.message import Message


class MessageDecorator(Message):
    """Базовый декоратор"""

    def __init__(self, message: Message):
        """Инициализация декоратора"""
        super().__init__(message.get_message())
        self._message = message

    def get_message(self):
        """Возвращает сообщение"""
        return self._message.get_message()
