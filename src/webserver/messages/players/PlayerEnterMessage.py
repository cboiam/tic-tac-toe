# -*- coding: utf-8 -*-

from src.webserver.messages import Message


class PlayerEnterMessage(Message):

    sid: str
    username: str

    def parse_data(self, data):
        self.sid = data["sid"]
        self.username = data["username"]
