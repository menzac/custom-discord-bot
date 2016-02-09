# -*- coding: utf-8 -*-

from command_bot import CommandBot
from swear_bot import SwearBot
from bots import Bots
from stats import Stats


stats = Stats("/home/slepice1/data.data")
command_bot = CommandBot(stats, {"trigger":"!"})
swear_bot = SwearBot(stats)
bots = Bots([command_bot, swear_bot])

with open("login.data", 'r') as f:
    email, password = f.read().strip().split("\n")


bots.run(email, password)
