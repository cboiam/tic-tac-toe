# -*- coding: utf-8 -*-

from src.webserver.messages import GameMessage


class GameMovementSendMessage(GameMessage):

    sid: str
    player_sid: str
    row: int
    column: int

    def parse_data(self, data):
        self.sid = data["sid"]
        self.player_sid = data["player_sid"]
        self.row = data["row"]
        self.column = data["column"]
