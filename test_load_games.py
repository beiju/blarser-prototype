import unittest

from parameterized import parameterized
from blaseball_mike import chronicler

from load_games import test_game


def games_to_test():
    return chronicler.get_games(season=12, count=30, cache_time=None)


class TestAllGames(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxDiff = None

    @parameterized.expand([(g['gameId'],) for g in games_to_test()])
    def test_s12_game(self, game_id):
        game = test_game(self, game_id)
        self.assertIsInstance(game, dict)


if __name__ == '__main__':
    unittest.main()
