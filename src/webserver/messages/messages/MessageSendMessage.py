# -*- coding: utf-8 -*-

from src.webserver.messages import GameMessage


class MessageSendMessage(GameMessage):

    sid: str
    player_sid: str
    text: str

    def parse_data(self, data):
        self.sid = data["sid"]
        self.player_sid = data["player_sid"]
        self.text = data["text"]
