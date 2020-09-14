# -*- coding: utf-8 -*-

from flask_socketio import emit
from src.webserver.messages.invites import InviteMessage
from src.webserver.handlers import Handler
from src.webserver.models import lobby


class InviteDeclineHandler(Handler):
    def handle(self, message: InviteMessage):
        emit("invite_declined", message.sid, room=lobby.name)
