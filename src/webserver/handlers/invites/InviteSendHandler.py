# -*- coding: utf-8 -*-

import json
from flask import request
from flask_socketio import emit
from src.webserver.handlers import Handler
from src.webserver.messages.invites import InviteSendMessage
from src.webserver.models import lobby


class InviteSendHandler(Handler):
    def handle(self, message: InviteSendMessage):
        player = lobby.get_player(message.players, request.sid)

        invite = {
            "sid": message.sid,
            "player": player.to_dict()
        }

        emit("invite_receive", json.dumps(invite), room=lobby.name)
