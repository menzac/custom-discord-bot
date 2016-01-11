# -*- coding: utf-8 -*-

def get_all_stats(data):
    text = "```python\n"
    for user in members:
        text += get_user_stats(data, user)
    text += "```"
    return text

def get_stats_for_user(data, user):
    text = "```python\n"
    text += get_user_stats(data, user)
    text += "```"
    return text

def get_user_stats(data, user):
    data[user] = data.get(user, {})
    text = user + ":\n"
    for key in data[user].keys():
       text += "   " + str(key) + " = " + str(data[user][key]) + "\n"
    text += "\n"
    return text
