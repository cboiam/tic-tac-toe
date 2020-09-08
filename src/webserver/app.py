# -*- coding: utf-8 -*-

from flask import Flask, request
import eventlet
from flask_socketio import SocketIO
from src.webserver.events.players import player_events

server = Flask(__name__)
websocket = SocketIO(server, cors_allowed_origins="*")
server.config["DEBUG"] = True


@websocket.on('connect')
def connect():
    print("connected", request.sid)


@websocket.on('disconnect')
def disconnect():
    player_events.player_leave(request.sid)
    print('disconnected', request.sid)


websocket.on_event("player_enter", player_events.player_enter)
websocket.on_event("player_leave", player_events.player_leave)
websocket.on_event("player_invite_send", player_events.player_invite_send)


if __name__ == '__main__':
    websocket.run(server)
