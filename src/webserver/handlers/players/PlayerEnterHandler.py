# -*- coding: utf-8 -*-

from src.webserver.messages.players import PlayerEnterMessage
from src.webserver.handlers import Handler
from src.core.entities import Player


class PlayerEnterHandler(Handler):
    def handle(self, message: PlayerEnterMessage):
        player = Player(message.sid, message.username)

        return {
            "sid": player.sid,
            "name": player.name
        }
