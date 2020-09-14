# -*- coding: utf-8 -*-


class Message:

    def __init__(self, sid: str, text: str):
        self.sid = sid
        self.text = text

    def to_dict(self):
        return {
            "sid": self.sid,
            "text": self.text
        }
