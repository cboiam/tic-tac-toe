# -*- coding: utf-8 -*-

from src.core.entities import Player


name = "lobby"


def add_player(players: list, player: Player):
    players.append(player)


def remove_player(players: list, sid: str):
    player = get_player(players, sid)
    players.remove(player)


def get_player(players: list, sid: str):
    return list(filter(lambda x: x.sid == sid, players))[0]
