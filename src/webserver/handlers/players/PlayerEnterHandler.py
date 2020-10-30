# -*- coding: utf-8 -*-

import json
from src.webserver.models import lobby
from flask_socketio import join_room, emit
from src.webserver.messages.players import PlayerEnterMessage
from src.webserver.handlers import Handler
from src.core.entities import Player


class PlayerEnterHandler(Handler):
    def handle(self, message: PlayerEnterMessage):
        player = Player(message.sid, message.username)

        join_room(lobby.name)
        lobby.add_player(message.players, player)
        players = list(map(lambda x: x.to_dict(), message.players))

        emit("player_connect", json.dumps(players), room=lobby.name)

        return player.to_dict()
