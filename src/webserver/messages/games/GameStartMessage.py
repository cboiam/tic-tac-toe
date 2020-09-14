# -*- coding: utf-8 -*-

from src.webserver.messages import GameMessage


class GameStartMessage(GameMessage):

    inviter: dict
    invited: dict

    def parse_data(self, data):
        self.inviter = data["inviter"]
        self.invited = data["invited"]
