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
            return [("send_message",(msg.channel, e))]
 
    def on_ready(self):
        print('Command bot running!')
 
    def _is_in_our_group(self, msg):
        return msg.server.id == "132560448775127041" and \
               msg.channel.name in ("lol", "test") and \
               not msg.channel.is_private
 
    @command
    def bodik(self, msg, arg):
        if arg is not None:
            if msg.author.name.lower() != arg:
                self.stats_[arg]["bodik"] += 1
            else:
                return [("send_message",(msg.channel, "Sám si dát bodík nemůžeš :("))]
        else:
            return [("send_message",(msg.channel, "Potřebuji jméno komu mám dat bodik"))]
 
    @command
    def stats(self, msg, arg):
        if arg is not None:
            return [("send_message",(msg.channel, self.stats_.get_user_stats_str(arg)))]
        else:
            return [("send_message",(msg.channel, self.stats_.get_all_stats_str()))]
 
    @command
    def franta(self, msg, arg):
        return [("send_message", (msg.channel, "http://goo.gl/NpHh9C")),
                ("delete_message", (msg,))]
 
    @command
    def kappa(self, msg, arg):
        return [("send_message", (msg.channel, "http://i.imgur.com/cpzYXCI.png?1")),
                ("delete_message", (msg,))]
 
    @command
    def kreygasm(self, msg, arg):
        return [("send_message", (msg.channel, "https://pp.vk.me/c7002/v7002292/cf67/EfLPiAfA_B4.jpg")),
                ("delete_message"), (msg,))]
 
    @command
    def pepe(self, msg, arg):
        return [("send_message", (msg.channel, "http://puu.sh/nIOFn/afcd16e232.jpg")),
                ("delete_message"), (msg,))]
 
    @command
    def pogchamp(self, msg, arg):
        return [("send_message", (msg.channel, "http://puu.sh/nIOHH/e25c7f9dc5.jpg")),
                ("delete_message"), (msg,))]
 
    @command
    def elegiggle(self, msg, arg):
        return [("send_message", (msg.channel, "http://media.steampowered.com/steamcommunity/public/images/avatars/57/57cb8df9bf154d2f169530862383fda6cf823bec_full.jpg")),
                ("delete_message"), (msg,))]
 
    @command
    def failfish(self, msg, arg):
        return [("send_message", (msg.channel, "http://cs622222.vk.me/v622222801/4f53e/3hxQvNmWAxQ.jpg")),
                ("delete_message"), (msg,))]
 
    @command
    def harold(self, msg, arg):
        return [("send_message", (msg.channel, "https://pbs.twimg.com/profile_images/673560564895846400/eOjzhHQl.png")),
                ("delete_message"), (msg,))]
