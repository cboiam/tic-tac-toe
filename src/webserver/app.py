# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_socketio import SocketIO
from src.webserver.events import lobby_events, game_events

server = Flask(__name__)
websocket = SocketIO(server, cors_allowed_origins="*")
server.config["DEBUG"] = True


@websocket.on('connect')
def connect():
    print("connected", request.sid)


@websocket.on('disconnect')
def disconnect():
    lobby_events.player_leave(request.sid)
    print('disconnected', request.sid)


lobby_events.register_lobby_events(websocket)
game_events.register_game_events(websocket)


if __name__ == '__main__':
    websocket.run(server)
