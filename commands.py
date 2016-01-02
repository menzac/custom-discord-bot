# -*- coding: utf-8 -*-

from exceptions import ChatException

def bodik(command, message, bodiky):
    members = [member.name.lower() for member in message.server.members]
    try:
        if command[1] in members:
            bodiky[command[1]] = bodiky.get(command[1], 0) + 1
            client.send_message(message.channel, str(bodiky.get(command[1], 0)))
        else:
           raise ChatException("Tento uživatel neexistuje")
    except IndexError:
        raise ChatException("Potřebuji jméno komu mám dat bodik")

def stats(command, message, bodiky):
    members = [member.name.lower() for member in message.server.members]
    try:
        if command[1] in members:
            client.send_message(message.channel, str(bodiky.get(command[1], 0)))
        else:
            raise ChatException("Tento uživatel neexistuje")
    except IndexError:
        raise ChatException("Potřebuju jméno či statistiky mám zobrazit")
