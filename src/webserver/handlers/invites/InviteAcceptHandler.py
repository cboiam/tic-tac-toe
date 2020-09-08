# -*- coding: utf-8 -*-

import json
from flask import request
from flask_socketio import emit
from src.webserver.messages.invites import InviteAcceptMessage
from src.webserver.handlers import Handler
from src.webserver.models import lobby


class InviteAcceptHandler(Handler):
    def handle(self, message: InviteAcceptMessage):
        sids = {
            "inviter": message.sid,
            "invited": request.sid
        }

        emit("game_create", json.dumps(sids), room=lobby.name)
