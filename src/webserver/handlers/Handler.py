# -*- coding: utf-8 -*-

from abc import abstractmethod
from src.webserver.messages import Message


class Handler:

    @abstractmethod
    def handle(self, message: Message):
        pass
