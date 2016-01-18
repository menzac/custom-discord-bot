# -*- coding: utf-8 -*-

import unittest

from stats import Stats, UserStats, MemberException

class User():
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def __str__(self):
        return name


class StatsTest(unittest.TestCase):

    def test_user_stats(self):
        user_stats = UserStats()
        user_stats["bodiky"] += 1
        self.assertEqual(user_stats["bodiky"], 1)

    def test_user_stats_formating(self):
        user_stats = UserStats()
        user_stats["bodiky"] += 1
        self.assertEqual(user_stats._get_stats_str(), "  bodiky = 1\n")
        user_stats["neco"] += 8
        self.assertIn("  neco = 8\n", user_stats._get_stats_str())

    def test_stats(self):
        stats_ = Stats()
        stats_.set_members([User("Jindřich", 1), User("Loe", 2), User("olej", 3)])
        self.assertEqual(stats_._members["jindrich"]["name"], "Jindřich")
        self.assertEqual(stats_._members["jindrich"]["id"], 1)

        stats_["jindrich"]["bodiky"] += 1
        self.assertTrue(isinstance(stats_["Jindrich"], UserStats))
        self.assertEqual(stats_["Jindřich"]["bodiky"], 1)
        stats_["JInDRICH"]["bodiky"] += 1
        self.assertEqual(stats_["Jindrich"]["bodiky"], 2)
        stats_["loe"]["tenisák"] += 2
        self.assertEqual(stats_["loe"]["tenisák"], 2)

        with self.assertRaises(MemberException):
            stats_["Oto"]["tenisák"] += 8

    def test_stats_formating(self):
        stats_ = Stats()
        stats_.set_members([User("On", 1), User("Teo", 2), User("olej", 3)])
        stats_["on"]["bodiky"] += 1
        expected = "```python\n  bodiky = 1\n```"
        self.assertEqual(stats_.get_user_stats_str("On"), expected)
        stats_["on"]["n"] += 8
        self.assertIn("  n = 8\n", stats_.get_user_stats_str("On"))
        self.assertIn("```", stats_.get_user_stats_str("On"))
        stats_["teo"]["bodiky"] += 9
        self.assertIn("Teo:", stats_.get_all_stats_str())
        self.assertIn("  bodiky = 9", stats_.get_all_stats_str())


if __name__ == '__main__':
    unittest.main()
