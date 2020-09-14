# -*- coding: utf-8 -*-

from abc import abstractmethod
from src.webserver.messages import Message


class GameMessage(Message):

    def __init__(self, games: list):
        self.games = games

    @abstractmethod
    def parse_data(self, data):
        pass
