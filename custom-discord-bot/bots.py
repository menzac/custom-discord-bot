# -*- coding: utf-8 -*-

import asyncio
from discord import Client

class Bots(Client):

    def __init__(self, bots):
        self.bots = bots
        Client.__init__(self)

    @asyncio.coroutine
    def on_message(self, msg):
        for bot in self.bots:
            func = getattr(bot, "on_message", None)
            if callable(func):
                message = func(msg)
                if message is not None:
                    yield from self.send_message(msg.channel, message)

    @asyncio.coroutine
    def on_ready(self):
        for bot in self.bots:
            func = getattr(bot, "on_ready", None)
            if callable(func):
                func()
