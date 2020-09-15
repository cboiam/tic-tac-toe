# -*- coding: utf-8 -*-

import json
from flask_socketio import SocketIO, emit
from src.webserver.events import Event
from src.webserver.handlers.games import *
from src.webserver.messages.games import *
from src.webserver.handlers.messages import *
from src.webserver.messages.messages import *

_games = []


def game_start(data):
    sids = json.loads(data)
    event = Event(GameStartMessage(_games), GameStartHandler())
    game = event.process(sids)

    return json.dumps(game)


def game_message_send(data):
    json_data = json.loads(data)
    event = Event(MessageSendMessage(_games), MessageSendHandler())
    event.process(json_data)


def game_movement_send(data):
    json_data = json.loads(data)
    event = Event(GameMovementSendMessage(_games), GameMovementSendHandler())
    event.process(json_data)


def game_over(sid):
    event = Event(GameOverMessage(_games), GameOverHandler())
    event.process(sid)

def register_game_events(websocket: SocketIO):
    websocket.on_event("game_start", game_start)
    websocket.on_event("game_message_send", game_message_send)
    websocket.on_event("game_movement_send", game_movement_send)
    websocket.on_event("game_over", game_over)
