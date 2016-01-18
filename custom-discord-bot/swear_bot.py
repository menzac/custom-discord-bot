# -*- coding: utf-8 -*-

from discord import Client, utils
from stats import Stats, MemberException

class SwearBot(Client):

    def __init__(self, stats_):
        Client.__init__(self)
        self.stats_ = stats_
        self.swear_words = self.build_swear_list()

    def on_message(self, msg):
        self.stats_.set_members(msg.server.members)

        if msg.channel.is_private: return
        if not self._is_in_our_group(msg): return

        try:
            count = sum((msg.content.count(word) for word in self.swear_words))
            if count > 0:
                self.stats_[msg.author]["sproste zpravy"] = 1
                self.stats_[msg.author]["sproste slova"] += count
        except MemberException as e:
            self.send_message(msg.channel, e)

    def on_ready(self):
        print('Swear bot connected!')
        print('Username: ' + self.user.name)
        print('ID: ' + self.user.id)

    def _is_in_our_group(self, msg):
        return msg.server.id == "132560448775127041" and \
               msg.channel.name in ("lol", "test") and \
               not msg.channel.is_private

    def build_swear_list(self):
        with open("../swear/cs", encoding="utf-8") as cs, \
             open("../swear/en", encoding="utf-8") as en:
              return cs.read().strip().split("\n") + \
                     en.read().strip().split("\n")
