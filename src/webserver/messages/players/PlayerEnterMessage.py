# -*- coding: utf-8 -*-

from src.webserver.messages import LobbyMessage


class PlayerEnterMessage(LobbyMessage):

    sid: str
    username: str

    def parse_data(self, data):
        self.sid = data["sid"]
        self.username = data["username"]
