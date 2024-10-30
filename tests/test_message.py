import unittest
from decorator import message_decorator


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = "Test message"
        self.message_decorator = message_decorator.Message(self.message)

    def test_creating_message(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(self.message_decorator.get_message(), self.message)


if __name__ == "__main__":
    unittest.main()
