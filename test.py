# -*- coding: utf-8 -*-

import discord
import pickle

import commands
from swear import count_swear_words
from exceptions import ChatException

MY_SERVER = "132560448775127041"

client = discord.Client()
with open("login.data", 'r') as f:
    email, password = f.read().strip().split("\n")
    client.login(email, password)

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
        else:
            swear_count = count_swear_words(message.content)
            if swear_count:
                author = message.author.name.lower()
                data[author] = data.get(author, {})
                data[author]["sprosté zprávy"] = data[author].get("sprosté zprávy", 0) + 1
                data[author]["sprostá slova"] = data[author].get("sprostá slova", 0) + swear_count
                serialize_object(data, "data.data")

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

def serialize_object(object_, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(object_, f)

def deserialize_object(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f, encoding="utf-8")

def execute_command(command, message):
    commands.members = [member.name.lower() for member in message.server.members]
    commands.client = client
    if command[0] == "bodik":
        commands.bodik(command, message, data)
        serialize_object(data, "data.data")
    elif command[0] == "stats":
        commands.stats(command, message, data)

data = deserialize_object("data.data")

client.run()
