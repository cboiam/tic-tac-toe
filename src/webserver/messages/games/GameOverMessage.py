# -*- coding: utf-8 -*-

from src.webserver.messages import GameMessage


class GameOverMessage(GameMessage):

    sid: str

    def parse_data(self, data):
        self.sid = data
