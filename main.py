import datetime
from decorator import message_decorator


def print_separator():
    print("------------------------------")


if __name__ == "__main__":
    print_separator()
    """Вывод сообщения"""
    message = message_decorator.Message("С наступающим новым годом!")
    message.print()
    print_separator()
    """Добавление к сообщению заголовка"""
    message_header = message_decorator.HeaderDecorator("Добрый день,", message)
    message_header.print()
    print_separator()
    """Добавление к сообщению подписи"""
    message_footer = message_decorator.FooterDecorator("Дед Мороз", message_header)
    message_footer.print()
    print_separator()
    """Добавление к сообщению даты"""
    message_date = message_decorator.DateDecorator(
        datetime.date.today(), message_footer
    )
    message_date.print()
    print_separator()
    """Кодирование всего сообщения в Base64"""
    message_base64 = message_decorator.Base64Decorator(message_date)
    message_base64.print()
    print_separator()
