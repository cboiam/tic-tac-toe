# -*- coding: utf-8 -*-

from src.core.entities import TicTacToe
from src.webserver.models import Chat


class Game:

    def __init__(self, sid: str, game: TicTacToe, chat: Chat):
        self.sid = sid
        self.game = game
        self.chat = chat

    def to_dict(self):
        game = self.game.to_dict()
        game["sid"] = self.sid
        game["chat"] = self.chat.to_dict()

        return game
