# -*- coding: utf-8 -*-

import json
from flask_socketio import emit
from src.webserver.messages.messages import MessageSendMessage
from src.webserver.handlers import Handler
from src.webserver.models import game_lobby, Message


class MessageSendHandler(Handler):
    def handle(self, message: MessageSendMessage):
        if not message.text:
            return

        game = game_lobby.get_game(message.games, message.sid)
        message_sent = Message(message.player_sid, message.text)
        game.chat.add_message(message_sent)

        emit("game_message_sent", json.dumps(message_sent.to_dict()), room=message.sid)
