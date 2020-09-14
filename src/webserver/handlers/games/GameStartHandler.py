# -*- coding: utf-8 -*-

from flask_socketio import join_room
from src.webserver.messages.games import GameStartMessage
from src.webserver.handlers import Handler
from src.webserver.models import game_lobby, Game, Chat
from src.core.entities import TicTacToe, Player


class GameStartHandler(Handler):
    def handle(self, message: GameStartMessage):
        game = GameStartHandler._create_game(message)
        game_lobby.add_game(message.games, game)

        join_room(game.sid)

        return game.to_dict()

    @staticmethod
    def _create_game(message: GameStartMessage):
        inviter = Player.from_dict(message.inviter)
        invited = Player.from_dict(message.invited)

        game_id = f"{inviter.sid}{invited.sid}"

        return Game(game_id, TicTacToe(inviter, invited), Chat())
