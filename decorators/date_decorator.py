import datetime

from decorators import MessageDecorator
from interfaces.message import Message


class DateDecorator(MessageDecorator):
    """Добавление даты"""

    def __init__(self, date: datetime.date, message: Message):
        super().__init__(message)
        self._message = message
        self._date = date.strftime("%d.%m.%Y")

    def get_message(self):
        return f"{self._message.get_message()}\n{self._date}"
