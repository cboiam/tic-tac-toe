# -*- coding: utf-8 -*-

from abc import abstractmethod
from src.webserver.messages import Message


class LobbyMessage(Message):

    def __init__(self, players: list):
        self.players = players

    @abstractmethod
    def parse_data(self, data):
        pass
