# -*- coding: utf-8 -*-

import pickle
import collections
from unidecode import unidecode

class Stats(collections.MutableMapping):
    def __init__(self, file_location, *args, **kwargs):
        self.file_location = file_location
        self._deserialize_object()
        self._members = {}
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        key = self._translate_key(key)
        if key not in self.users:
            self.users[key] = UserStats(self)
        return self.users[key]

    def __setitem__(self, key, value):
        self.users[self._translate_key(key)] = value
        self._serialize_object(file_location)

    def __delitem__(self, key):
        del self.users[self._translate_key(key)]

    def __iter__(self):
        return iter(self.users)

    def __len__(self):
        return len(self.users)

    def _translate_key(self, key):
        key = unidecode(key).lower()
        if key in self._members:
            return self._members[key]["id"]
        else:
            raise MemberException("Není členem místnosti")

    def set_members(self, members):
        self._members = { unidecode(member.name).lower():{"id": member.id,
                                                    "name": member.name}
                          for member in members}

    def get_all_stats_str(self):
        text = "```python\n"
        for user in self._members:
            text += "{0}: \n{1} \n".format(
                        self._members[user]["name"],
                        self.__getitem__(user)._get_stats_str())
        text += "```"
        return text

    def get_user_stats_str(self, user):
        text = "```python\n"
        text += self.users[self._translate_key(user)]._get_stats_str()
        text += "```"
        return text

    def serialize_object(self):
        with open(self.file_location, 'wb') as f:
            pickle.dump(self.users, f)

    def _deserialize_object(self):
        try:
            with open(self.file_location, 'rb') as f:
                self.users = pickle.load(f, encoding="utf-8")
        except IOError:
            self.users = dict()


class UserStats(collections.MutableMapping):
    def __init__(self, parent, *args, **kwargs):
        self.stats = dict()
        self.parent = parent
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        if key in self.stats:
            return self.stats[key]
        else:
            return 0

    def __setitem__(self, key, value):
        self.stats[key] = value
        self.parent.serialize_object()

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
