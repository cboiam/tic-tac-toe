# -*- coding: utf-8 -*-

from src.webserver.messages import Message
from src.webserver.handlers import Handler


class Event:

    def __init__(self, message: Message, handler: Handler):
        self.message = message
        self.handler = handler

    def process(self, data):
        self.message.parse_data(data)
        return self.handler.handle(self.message)
