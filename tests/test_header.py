import unittest
from decorator import message_decorator


class TestHeader(unittest.TestCase):
    def setUp(self):
        self.header = "Header"
        self.message = message_decorator.Message("Test message")
        self.message_with_header = "Header\nTest message"
        self.message_with_header_decorator = message_decorator.HeaderDecorator(
            self.header, self.message
        )

    def test_header(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(
            self.message_with_header, self.message_with_header_decorator.get_message()
        )


if __name__ == "__main__":
    unittest.main()
