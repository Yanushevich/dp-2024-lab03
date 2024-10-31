import unittest

import decorators.header_decorator
import interfaces.message


class TestHeader(unittest.TestCase):
    """Проверка добавления заголовка"""

    def setUp(self):
        """Первоначальные значения"""
        self.header = "Header"
        self.message = interfaces.message.Message("Test message")
        self.message_with_header = "Header\nTest message"
        self.message_with_header_decorator = (
            decorators.header_decorator.HeaderDecorator(self.header, self.message)
        )

    def test_header(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(
            self.message_with_header, self.message_with_header_decorator._get_content()
        )


if __name__ == "__main__":
    unittest.main()
