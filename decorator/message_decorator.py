import datetime
import base64


class Message:
    """Создание базового сообщения"""

    def __init__(self, message: str, **kwargs):
        self._message = message

    def get_message(self):
        return self._message

    def print(self) -> None:
        print(self.get_message())


class MessageDecorator(Message):
    """Создание базового декоратора"""

    def __init__(self, message: Message):
        super().__init__(message.get_message())
        self._message = message

    def get_message(self):
        return self._message.get_message()


class HeaderDecorator(MessageDecorator):
    """Добавление заголовка"""

    def __init__(self, header: str, message: Message):
        super().__init__(message)
        self._message = message
        self._header = header

    def get_message(self):
        return f"{self._header}\n{self._message.get_message()}"


class FooterDecorator(MessageDecorator):
    """Добавление подписи"""

    def __init__(self, footer: str, message: Message):
        super().__init__(message)
        self._message = message
        self._footer = footer

    def get_message(self):
        return f"{self._message.get_message()}\n{self._footer}"


class DateDecorator(MessageDecorator):
    """Добавление даты"""

    def __init__(self, date: datetime.date, message: Message):
        super().__init__(message)
        self._message = message
        self._date = date.strftime("%d.%m.%Y")

    def get_message(self):
        return f"{self._message.get_message()}\n{self._date}"


class Base64Decorator(MessageDecorator):
    """Кодирование в Base64"""

    def __init__(self, message: Message):
        super().__init__(message)
        self._message = message
        self._base64 = base64.b64encode(self._message.get_message().encode("utf-8")).decode('utf-8')

    def get_message(self):
        return self._base64
