# -*- coding: utf-8 -*-

from abc import abstractmethod


class Message:

    @abstractmethod
    def parse_data(self, data: dict):
        pass
