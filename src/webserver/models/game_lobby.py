# -*- coding: utf-8 -*-

from src.webserver.models import Game


def add_game(games: list, game: Game):
    games.append(game)


def remove_game(games: list, sid: str):
    game = get_game(games, sid)
    games.remove(game)


def get_game(games: list, sid: str):
    return list(filter(lambda x: x.sid == sid, games))[0]
