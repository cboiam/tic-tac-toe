# -*- coding: utf-8 -*-

from src.webserver.messages.players import PlayerLeaveMessage
from src.webserver.handlers import Handler
from src.webserver.models import lobby
from flask_socketio import emit, leave_room


class PlayerLeaveHandler(Handler):
    def handle(self, message: PlayerLeaveMessage):
        leave_room(lobby.name)
        lobby.remove_player(message.players, message.sid)

        emit("player_disconnect", message.sid, room=lobby.name)
