import unittest
from decorator import message_decorator


class TestFooter(unittest.TestCase):
    def setUp(self):
        self.message = message_decorator.Message("Test message")
        self.footer = "Footer"
        self.message_with_footer = "Test message\nFooter"
        self.message_with_footer_decorator = message_decorator.FooterDecorator(
            self.footer, self.message
        )

    def test_header(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(
            self.message_with_footer, self.message_with_footer_decorator.get_message()
        )


if __name__ == "__main__":
    unittest.main()
