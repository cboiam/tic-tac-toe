import json
from flask import request
from flask_socketio import join_room, leave_room, emit
from src.webserver.events import Event
from src.webserver.handlers.players import *
from src.webserver.messages.players import *

_lobby_players = []
_lobby_name = "lobby"


def player_enter(data: str):
    json_data = json.loads(data)
    event = Event(PlayerEnterMessage(), PlayerEnterHandler())
    player = event.process(json_data)

    join_room(_lobby_name)
    _lobby_players.append(player)
    emit("player_connect", json.dumps(_lobby_players), room=_lobby_name)

    return json.dumps(player)


def player_leave(sid: str):
    leave_room(_lobby_name)

    player = list(filter(lambda x: x["sid"] == sid, _lobby_players))[0]
    _lobby_players.remove(player)

    emit("player_disconnect", sid, room=_lobby_name)


def player_invite_send(sid: str):
    player = list(filter(lambda x: x["sid"] == request.sid, _lobby_players))[0]

    invitation = {
        "sid": sid,
        "player": player
    }

    emit("player_invite_receive", json.dumps(invitation), room=_lobby_name)
