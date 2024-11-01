from interfaces.message import Message


class MessageDecorator(Message):
    """Базовый декоратор"""

    def __init__(self, message: Message):
        """
        Инициализация декоратора

        Args:
            message (Message): Объект сообщения
        """
        super().__init__(message._get_content())
        self._message = message

    def _get_content(self) -> str:
        """Возвращает сообщение"""
        return self._message._get_content()
