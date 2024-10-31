import unittest
import base64

import decorators.base64_decorator
import interfaces.message


class TestBase64(unittest.TestCase):
    """Проверка кодирования в Base64"""

    def setUp(self):
        """Первоначальные значения"""
        self.message = interfaces.message.Message("Test message")
        self.message_with_base64 = base64.b64encode(
            "Test message".encode("utf-8")
        ).decode("utf-8")
        self.message_with_base64_decorator = (
            decorators.base64_decorator.Base64Decorator(self.message)
        )

    def test_header(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(
            self.message_with_base64, self.message_with_base64_decorator.get_message()
        )


if __name__ == "__main__":
    unittest.main()
