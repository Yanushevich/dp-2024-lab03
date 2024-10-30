from interfaces.message import Message


class MessageDecorator(Message):
    """Создание базового декоратора"""

    def __init__(self, message: Message):
        super().__init__(message.get_message())
        self._message = message

    def get_message(self):
        return self._message.get_message()
