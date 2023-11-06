import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_find_top_scorer(self):
        top_scorers = self.stats.top(1)
        self.assertEqual(top_scorers[0].name, "Gretzky")

    def test_find_top_goals(self):
        top_scorers = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(top_scorers[0].name, "Lemieux")

    def test_find_top_assists(self):
        top_scorers = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(top_scorers[0].name, "Gretzky")

    def test_search_for_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_for_not_existing_player(self):
        player = self.stats.search("Hyyry")
        self.assertEqual(player, None)

    def test_find_players_of_team(self):
        players_of_team = self.stats.team("EDM")
        self.assertEqual(len(players_of_team), 3)