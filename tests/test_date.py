import unittest
import datetime
from decorator import message_decorator


class TestDate(unittest.TestCase):
    def setUp(self):
        self.message = message_decorator.Message("Test message")
        self.date = datetime.date.today()
        self.message_with_date = (
            f"Test message\n{datetime.date.today().strftime('%d.%m.%Y')}"
        )
        self.message_with_date_decorator = message_decorator.DateDecorator(
            self.date, self.message
        )

    def test_header(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(
            self.message_with_date, self.message_with_date_decorator.get_message()
        )


if __name__ == "__main__":
    unittest.main()
