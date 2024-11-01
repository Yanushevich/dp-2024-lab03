import unittest

import decorators.footer_decorator
import interfaces.message


class TestFooter(unittest.TestCase):
    """Проверка добавления подписи"""

    def setUp(self):
        """Первоначальные значения"""
        self.message = interfaces.message.Message("Test message")
        self.footer = "Footer"
        self.message_with_footer = "Test message\nFooter"
        self.message_with_footer_decorator = (
            decorators.footer_decorator.FooterDecorator(self.footer, self.message)
        )

    def test_header(self):
        """Сравнение содержимого сообщений"""
        self.assertEqual(
            self.message_with_footer, self.message_with_footer_decorator._get_content()
        )


if __name__ == "__main__":
    unittest.main()
