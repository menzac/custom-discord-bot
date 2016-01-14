# -*- coding: utf-8 -*-

import unittest

from stats import Stats, UserStats

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
        self.assertEqual("  neco = 8\n" in user_stats._get_stats_str(), True)

    def test_stats(self):
        stats_ = Stats()
        stats_.set_members(["Jidřich"])
        stats_["jindrich"]["bodiky"] += 1
        self.assertEqual(isinstance(stats_["Jindrich"], UserStats), True)
        self.assertEqual(stats_["Jindrich"]["bodiky"], 1)
        stats_["jindrich"]["bodiky"] += 1
        self.assertEqual(stats_["Jindrich"]["bodiky"], 2)
        stats_["jindrich"]["tenisák"] += 2
        self.assertEqual(stats_["Jindrich"]["tenisák"], 2)

    def test_stats_formating(self):
        stats_ = Stats()
        stats_["on"]["bodiky"] += 1
        expected = "```python\n  bodiky = 1\n```"
        self.assertEqual(stats_.get_user_stats_str("On"), expected)
        stats_["on"]["n"] += 8
        self.assertEqual("  n = 8\n" in stats_.get_user_stats_str("On"), True)
        self.assertEqual("```" in stats_.get_user_stats_str("On"), True)
        stats_["teo"]["bodiky"] += 9
        self.assertEqual("Teo:" in stats_.get_all_stats_str(), True)
        self.assertEqual("  bodiky = 9" in stats_.get_all_stats_str(), True)


if __name__ == '__main__':
    unittest.main()
