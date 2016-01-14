# -*- coding: utf-8 -*-

import collections

class Stats(collections.MutableMapping):
    def __init__(self, *args, **kwargs):
        self.users = dict()
        self._members = {}
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        if key not in self.users:
            if key in _members:
                self.users[key] = UserStats()
            else:
                raise MemberException("Není členem místnosti")
        return self.users[key]

    def __setitem__(self, key, value):
        self.users[key] = value

    def __delitem__(self, key):
        del self.users[key]

    def __iter__(self):
        return iter(self.users)

    def __len__(self):
        return len(self.users)

    def set_members(self, members):
        self._members = {member.lower():member for member in members}

    def get_all_stats_str(self):
        text = "```python\n"
        for user in self.users:
            text += "{0}: \n {1} \n".format(self._members[user],
                                            self.users[user]._get_stats_str())
        text += "```"
        return text

    def get_user_stats_str(self, user):
        text = "```python\n"
        text += self.users[user]._get_stats_str()
        text += "```"
        return text


class UserStats(collections.MutableMapping):
    def __init__(self, *args, **kwargs):
        self.stats = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        if key in self.stats:
            return self.stats[key]
        else:
            return 0

    def __setitem__(self, key, value):
        self.stats[key] = value

    def __delitem__(self, key):
        del self.stats[key]

    def __iter__(self):
        return iter(self.stats)

    def __len__(self):
        return len(self.stats)

    def _get_stats_str(self):
        text = ""
        for key in self.stats:
           text += "  {0} = {1}\n".format(key, str(self.stats[key]))
        return text

class MemberException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
