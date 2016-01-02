# -*- coding: utf-8 -*-

from exceptions import ChatException

def bodik(command, message, data):
    try:
        if command[1] in members:
            data[command[1]]["bodik"] = data.get(data.get(command[1]), 0) + 1
            client.send_message(message.channel, str(data.get(command[1], 0)))
        else:
           raise ChatException("Tento uživatel neexistuje")
    except IndexError:
        raise ChatException("Potřebuji jméno komu mám dat bodik")

def stats(command, message, data):
    try:
        if command[1] in members:
            client.send_message(message.channel, str(data.get(command[1], 0)))
        else:
            raise ChatException("Tento uživatel neexistuje")
    except IndexError:
        raise ChatException("Potřebuju jméno či statistiky mám zobrazit")