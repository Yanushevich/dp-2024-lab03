import datetime
import decorators
import interfaces


def print_separator():
    print("------------------------------")


if __name__ == "__main__":
    print_separator()
    """Вывод сообщения"""
    message = interfaces.message.Message("С наступающим новым годом!")
    message.print()
    print_separator()
    """Добавление к сообщению заголовка"""
    message_header = decorators.header_decorator.HeaderDecorator(
        "Добрый день,", message
    )
    message_header.print()
    print_separator()
    """Добавление к сообщению подписи"""
    message_footer = decorators.footer_decorator.FooterDecorator(
        "Дед Мороз", message_header
    )
    message_footer.print()
    print_separator()
    """Добавление к сообщению даты"""
    message_date = decorators.date_decorator.DateDecorator(
        datetime.date.today(), message_footer
    )
    message_date.print()
    print_separator()
    """Кодирование всего сообщения в Base64"""
    message_base64 = decorators.base64_decorator.Base64Decorator(message_date)
    message_base64.print()
    print_separator()
