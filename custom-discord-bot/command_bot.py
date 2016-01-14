# -*- coding: utf-8 -*-

from discord import Client, utils
from stats import Stats

def command(func):
    func.command = None
    return func


class CommandBot(Client):

    def __init__(self, stats, config):
        Client.__init__(self)
        self.config = config
        self.stats = stats
        self.commands = []
        for k, v in CommandBot.__dict__.items():
            if hasattr(v, 'command'):
                self.commands.append(k)

    def on_message(self, msg):
        self.stats.set_members(msg.server.members)

        if msg.channel.is_private: return
        if not self._is_in_our_group(msg): return
        if not msg.content.startswith(self.config['trigger']): return

        line = msg.content[len(self.config['trigger']):].lower()
        if ' ' in line:
            cmd, arg = line.split(' ', 1)
        else:
            cmd, arg = line, None

        if cmd not in self.commands: return
        func = getattr(self, cmd)
        try:
            func(msg, arg)
        except MemberException as e:
            self.send_message(msg.channel, e)

    def on_ready(self):
        print('Command bot connected!')
        print('Username: ' + self.user.name)
        print('ID: ' + self.user.id)

    def _is_in_our_group(self, msg):
        return msg.server.id == "132560448775127041" and \
               msg.channel.name in ("lol", "test") and \
               not msg.channel.is_private

    @command
    def bodik(self, msg, arg):
        if arg is not None:
            if msg.author.name.lower() != arg:
                self.stats[arg]["bodik"] += 1
            else:
                self.send_message(msg.channel, "Sám si dát bodík nemůžeš :(")
        else:
            self.send_message(msg.channel, "Potřebuji jméno komu mám dat bodik")

    @command
    def stats(self, msg, arg):
        if arg is not None:
            self.send_message(message.channel, self.stats.get_user_stats_str(arg))
        else:
            self.send_message(message.channel, self.stats.get_all_stats_str())
