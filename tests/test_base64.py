import unittest
import base64
from decorator import message_decorator


class TestDate(unittest.TestCase):
    def setUp(self):
        self.message = message_decorator.Message("Test message")
        self.message_with_base64 = base64.b64encode(
            "Test message".encode("utf-8")
        ).decode("utf-8")
        self.message_with_base64_decorator = message_decorator.Base64Decorator(
            self.message
        )

    def test_header(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(
            self.message_with_base64, self.message_with_base64_decorator.get_message()
        )


if __name__ == "__main__":
    unittest.main()
