# -*- coding: utf-8 -*-

import discord
import pickle

import commands
from exceptions import ChatException

MY_SERVER = "132560448775127041"
bodiky = {}

client = discord.Client()
client.login('vojtin.j@gmail.com', '1UsJt2kuMZfybArRkYtI')

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
          try:
              execute_command(parse_command(text[1:]), message)
          except ChatException as e:
              send_message("Error: " + e.value, message.channel)

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
    commands.client = client
    if command[0] == "bodik":
        commands.bodik(command, message, bodiky)
    elif command[0] == "stats":
        commands.stats(command, message, bodiky)


client.run()
