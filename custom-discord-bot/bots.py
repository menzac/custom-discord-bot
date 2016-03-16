# -*- coding: utf-8 -*-

import asyncio
from discord import Client

class Bots(Client):



    def __init__(self, bots):
        self.bots = bots
        Client.__init__(self)
        operations = [self.send_message, self.delete_message]
        self.operations = {op.__name__:op for op in operations}

    @asyncio.coroutine
    def on_message(self, msg):
        for bot in self.bots:
            func = getattr(bot, "on_message", None)
            if callable(func):
                reactions = func(msg)
                if reactions is None: return
                for reaction in reactions:
                    yield from self.operations[reaction[0]](*reaction[1])

    @asyncio.coroutine
    def on_ready(self):
        for bot in self.bots:
            func = getattr(bot, "on_ready", None)
            if callable(func):
                func()
