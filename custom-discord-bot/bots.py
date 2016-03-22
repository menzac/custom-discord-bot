# -*- coding: utf-8 -*-

import asyncio
from discord import Client

class Bots(Client):

    def __init__(self, bots):
        Client.__init__(self)
        self.bots = bots
        operations = [self.send_message, self.send_file, self.delete_message]
        self.operations = {op.__name__:op for op in operations}

    @asyncio.coroutine
    def on_message(self, msg):
        for bot in self.bots:
            func = getattr(bot, "on_message", None)
            if callable(func):
                reactions = func(msg)
                if reactions is None: continue
                for reaction in reactions:
                    if len(reaction) < 3:
                        yield from self.operations[reaction[0]](*reaction[1])
                    else:
                        yield from self.operations[reaction[0]](*reaction[1], **reaction[2])

    @asyncio.coroutine
    def on_ready(self):
        for bot in self.bots:
            func = getattr(bot, "on_ready", None)
            if callable(func):
                func()
