# -*- coding: utf-8 -*-

import asyncio

class LogingBot():

    def __init__(self, config):
        self.config = config

    def on_message(self, msg):
        if msg.channel.is_private: return
        if not self._is_in_our_group(msg): return

    def on_ready(self):
        print('Loging bot running!')

    def _is_in_our_group(self, msg):
        return msg.server.id == self.config["server_id"]
