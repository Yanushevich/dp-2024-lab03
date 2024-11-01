import unittest

import interfaces.message


class TestMessage(unittest.TestCase):
    """Проверка создания сообщения"""

    def setUp(self):
        """Первоначальные значения"""
        self.message = "Test message"
        self.message_decorator = interfaces.message.Message(self.message)

    def test_creating_message(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(self.message_decorator._get_content(), self.message)


if __name__ == "__main__":
    unittest.main()
