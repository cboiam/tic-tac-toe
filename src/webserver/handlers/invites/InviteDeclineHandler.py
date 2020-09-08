# -*- coding: utf-8 -*-

from flask_socketio import emit
from src.webserver.messages.invites import InviteDeclineMessage
from src.webserver.handlers import Handler
from src.webserver.models import lobby


class InviteDeclineHandler(Handler):
    def handle(self, message: InviteDeclineMessage):
        emit("invite_declined", message.sid, room=lobby.name)
