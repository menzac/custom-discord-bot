# -*- coding: utf-8 -*-

from exceptions import ChatException
import stats_formatter as stats_f

def bodik(command, message, data):
    try:
        if command[1] in members and message.author.name.lower() != command[1]:
            data[command[1]] = data.get(command[1], {})
            data[command[1]]["bodik"] = data[command[1]].get("bodik", 0) + 1
        else:
           raise ChatException("Tento uživatel neexistuje")
    except IndexError:
        raise ChatException("Potřebuji jméno komu mám dat bodik")

def stats(command, message, data):
    try:
        if command[1] in members:
            client.send_message(message.channel, stats_f.get_stats_for_user(data, command[1]))
        else:
            raise ChatException("Tento uživatel neexistuje")
    except IndexError:
        stats_f.members = members
        client.send_message(message.channel, stats_f.get_all_stats(data))
