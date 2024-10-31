import datetime
from decorators import MessageDecorator
from interfaces.message import Message


class DateDecorator(MessageDecorator):
    """Декоратор добавления даты в конец сообщения"""

    def __init__(self, date: datetime.date, message: Message):
        """Инициализация декоратора"""
        super().__init__(message)
        self._message = message
        self._date = self._get_date(date)

    def _get_date(self, date: datetime.date) -> str:
        """Приведение даты к формату"""
        return date.strftime("%d.%m.%Y")

    def get_message(self):
        """Возвращает сообщение"""
        return f"{self._message.get_message()}\n{self._date}"
