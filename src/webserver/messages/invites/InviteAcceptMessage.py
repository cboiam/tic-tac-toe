# -*- coding: utf-8 -*-

from src.webserver.messages import LobbyMessage


class InviteAcceptMessage(LobbyMessage):

    sid: str

    def parse_data(self, data: str):
        self.sid = data
