# -*- coding: utf-8 -*-

import json
from flask import request
from flask_socketio import emit
from src.webserver.messages.invites import InviteMessage
from src.webserver.handlers import Handler
from src.webserver.models import lobby


class InviteAcceptHandler(Handler):
    def handle(self, message: InviteMessage):
        inviter = lobby.get_player(message.players, message.sid)
        invited = lobby.get_player(message.players, request.sid)

        players = {
            "inviter": inviter.to_dict(),
            "invited": invited.to_dict()
        }

        emit("game_create", json.dumps(players), room=lobby.name)
