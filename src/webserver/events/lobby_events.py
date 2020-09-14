# -*- coding: utf-8 -*-

import json
from flask_socketio import join_room, leave_room, emit, SocketIO
from src.webserver.events import Event
from src.webserver.handlers.players import *
from src.webserver.messages.players import *
from src.webserver.handlers.invites import *
from src.webserver.messages.invites import *

_players = []


def player_enter(data: str):
    json_data = json.loads(data)
    event = Event(PlayerEnterMessage(_players), PlayerEnterHandler())
    player = event.process(json_data)

    return json.dumps(player)


def player_leave(sid: str):
    event = Event(PlayerLeaveMessage(_players), PlayerLeaveHandler())
    event.process(sid)


def invite_send(sid: str):
    event = Event(InviteMessage(_players), InviteSendHandler())
    event.process(sid)


def invite_accept(sid: str):
    event = Event(InviteMessage(_players), InviteAcceptHandler())
    event.process(sid)


def invite_decline(sid: str):
    event = Event(InviteMessage(_players), InviteDeclineHandler())
    event.process(sid)


def register_lobby_events(websocket: SocketIO):
    websocket.on_event("player_enter", player_enter)
    websocket.on_event("player_leave", player_leave)
    websocket.on_event("invite_send", invite_send)
    websocket.on_event("invite_decline", invite_decline)
    websocket.on_event("invite_accept", invite_accept)
