import base64
import datetime
import unittest

import decorators
import interfaces


class TestAllDecorators(unittest.TestCase):
    """Проверка полной цепочки декораторов"""

    def setUp(self):
        """Создание тестового сообщения"""
        self.test_message = "Заголовок\nСообщение\nПодпись\n31.12.2024"
        """Создание полной цепочки декораторов"""
        message = interfaces.message.Message("Сообщение")
        message_with_header = decorators.HeaderDecorator("Заголовок", message)
        message_with_header_footer = decorators.FooterDecorator(
            "Подпись", message_with_header
        )
        self.message_with_header_footer_date = decorators.DateDecorator(
            datetime.date(2024, 12, 31), message_with_header_footer
        )
        """Кодирование получившегося сообщения в Base64"""
        self.message_with_header_footer_date_base64 = decorators.Base64Decorator(
            self.message_with_header_footer_date
        )

    def test_all_decorators(self):
        """Проверка соответствия полной цепочки декораторов"""
        self.assertEqual(self.test_message, self.message_with_header_footer_date._get_content())
        """Проверка кодирования"""
        self.assertEqual(
            base64.b64encode(self.test_message.encode("utf-8")).decode("utf-8"),
            self.message_with_header_footer_date_base64._get_content(),
        )


if __name__ == "__main__":
    unittest.main()
