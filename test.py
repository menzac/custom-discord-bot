# -*- coding: utf-8 -*-

import discord
import pickle

MY_SERVER = "132560448775127041"
bodiky = {}

client = discord.Client()
client.login('vojtin.j@gmail.com', 'Wn9z7EQq67rpUQFUZscY')

@client.event
def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
def on_message(message):
    text = message.content.strip()
    if is_in_our_group(message):
        if text.startswith('!'):
            execute_command(parse_command(text[1:]), message)

def is_in_our_group(message):
    return message.server.id == MY_SERVER and \
           message.channel.name in ("lol", "test") and \
           not message.channel.is_private

def parse_command(command):
    command = command.lower()
    while command.count("  "):
        command = command.replace("  ", " ")
    return command.split(" ")

def send_message(message, channel):
    client.send_message(channel, message)

def execute_command(command, message):
    members = [member.name.lower() for member in message.server.members]
    if command[0] == "bodik":
        try:
            if command[1] in members:
                bodiky[command[1]] = bodiky.get(command[1], 0) + 1
                client.send_message(message.channel, str(bodiky.get(command[1], 0)))
            else:
                client.send_message(message.channel, "Tento user tady neni")
        except IndexError:
            client.send_message(message.channel, "Potrebuju jmeno komu mam dat bodik")
    if command[0] == "stats":
        try:
            if command[1] in members:
                client.send_message(message.channel, str(bodiky.get(command[1], 0)))
            else:
        except IndexError:
            send_message("Potrebuju jmeno ci statistiky mam zobrazit", message.channel)


client.run()
