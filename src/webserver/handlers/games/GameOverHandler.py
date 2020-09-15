# -*- coding: utf-8 -*-

from flask_socketio import leave_room
from src.webserver.messages.games import GameOverMessage
from src.webserver.handlers import Handler
from src.webserver.models import game_lobby


class GameOverHandler(Handler):
    def handle(self, message: GameOverMessage):
        game_lobby.remove_game(message.games, message.sid)
        leave_room(message.sid)
