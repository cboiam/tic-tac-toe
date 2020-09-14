# -*- coding: utf-8 -*-

import json
from flask_socketio import emit
from src.webserver.messages.games import GameMovementSendMessage
from src.webserver.handlers import Handler
from src.webserver.models import game_lobby
from src.core.entities import Coordinate


class GameMovementSendHandler(Handler):
    def handle(self, message: GameMovementSendMessage):
        game = game_lobby.get_game(message.games, message.sid)

        coordinate = Coordinate(message.row, message.column)
        winner = game.game.make_move(message.player_sid, coordinate)

        response = {
            "winner": message.player_sid if winner else "",
            "board": game.game.board.to_dict(),
            "turn": game.game.player_turn.sid
        }

        emit("game_movement_sent", json.dumps(response), room=message.sid)
