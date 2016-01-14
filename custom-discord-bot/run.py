# -*- coding: utf-8 -*-

import pickle

from swear import count_swear_words
from . import CommandBot


client = CommandBot()

with open("login.data", 'r') as f:
    email, password = f.read().strip().split("\n")
    client.login(email, password)


def serialize_object(object_, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(object_, f)

def deserialize_object(file_name):
    try:
        with open(file_name, 'rb') as f:
            return pickle.load(f, encoding="utf-8")
    except IOError:
        return {}

def execute_command(command, message):
    commands.members = [member.name.lower() for member in message.server.members]
    commands.client = client
    if command[0] == "bodik":
        commands.bodik(command, message, data)
        serialize_object(data, "data.data")
    elif command[0] == "stats":
        commands.stats(command, message, data)

client.run()
