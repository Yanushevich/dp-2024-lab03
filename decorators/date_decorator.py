import datetime
from decorators import MessageDecorator
from interfaces.message import Message


class DateDecorator(MessageDecorator):
    """Декоратор добавления даты в конец сообщения"""

    def __init__(self, date: datetime.date, message: Message):
        """
        Инициализация декоратора

        Args:
            date (datetime.date): Дата
            message (Message): Объект сообщения
        """
        super().__init__(message)
        self._message = message
        self._date = self._get_date(date)

    def _get_date(self, date: datetime.date) -> str:
        """
        Приведение даты к формату

        Args:
            date (datetime.date): Дата
        """
        return date.strftime("%d.%m.%Y")

    def _get_content(self) -> str:
        """Возвращает сообщение"""
        return f"{self._message._get_content()}\n{self._date}"
