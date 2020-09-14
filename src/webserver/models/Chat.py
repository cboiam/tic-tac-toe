# -*- coding: utf-8 -*-

from src.webserver.models import Message


class Chat:

    def __init__(self):
        self._messages = []

    def add_message(self, message: Message):
        self._messages.append(message)

    def to_dict(self):
        messages = []

        for message in self._messages:
            messages.append(message.to_dict())

        return messages
