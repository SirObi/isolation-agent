"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_example(self):
        # TODO: All methods must start with "test_"
        self.fail("Hello, World!")

    def test_custom_score(self):
        game = self.game
        player = self.player1
        evaluate_game = game_agent.custom_score(game, player)
        self.assertTrue(evaluate_game == 49)

    def test_minimax_get_move(self):
        # TODO: All methods must start with "test_"
        game = self.game
        player = game_agent.MinimaxPlayer()
        player.time_left = 10.
        print(player.minimax(game, 3))
        self.assertTrue(0==0)


if __name__ == '__main__':
    unittest.main()
