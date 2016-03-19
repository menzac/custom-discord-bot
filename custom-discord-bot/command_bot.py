# -*- coding: utf-8 -*-

import asyncio
from stats import Stats, MemberException

def command(func):
    func.command = None
    return func

class CommandBot():

    def __init__(self, stats_, config):
        self.config = config
        self.stats_ = stats_
        self.commands = []
        for k, v in CommandBot.__dict__.items():
            if hasattr(v, 'command'):
                self.commands.append(k)

    def on_message(self, msg):
        self.stats_.set_members(msg.server.members)

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
            return func(msg, arg)
        except MemberException as e:
            return [("send_message",(msg.channel, e), {})]

    def on_ready(self):
        print('Command bot running!')

    def _is_in_our_group(self, msg):
        return msg.server.id == self.config["server_id"] and \
            msg.channel.name in self.config["channels"]

    @command
    def bodik(self, msg, arg):
        if arg is not None:
            if msg.author.name.lower() != arg:
                self.stats_[arg]["bodik"] += 1
            else:
                return [("send_message",(msg.channel, "Sám si dát bodík nemůžeš :("), {})]
        else:
            return [("send_message",(msg.channel, "Potřebuji jméno komu mám dat bodik"), {})]

    @command
    def stats(self, msg, arg):
        if arg is not None:
            return [("send_message",(msg.channel, self.stats_.get_user_stats_str(arg)),{})]
        else:
            return [("send_message",(msg.channel, self.stats_.get_all_stats_str()),{})]

    @command
    def react(self, msg, arg):
        arg = arg.replace(".","").replace("/","")
        file_name = self.config["images_location"].format(arg)
        return [("send_file", (msg.channel, file_name), {"content":msg.author.name}),
                ("delete_message", (msg,), {})]
