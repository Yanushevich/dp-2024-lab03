import unittest
import datetime

import decorators.date_decorator
import interfaces.message


class TestDate(unittest.TestCase):
    """Проверка добавления даты"""

    def setUp(self):
        """Первоначальные значения"""
        self.message = interfaces.message.Message("Test message")
        self.date = datetime.date.today()
        self.message_with_date = (
            f"Test message\n{datetime.date.today().strftime('%d.%m.%Y')}"
        )
        self.message_with_date_decorator = decorators.date_decorator.DateDecorator(
            self.date, self.message
        )

    def test_header(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(
            self.message_with_date, self.message_with_date_decorator._get_content()
        )


if __name__ == "__main__":
    unittest.main()
