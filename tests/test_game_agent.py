"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = sample_players.GreedyPlayer()
        self.game = isolation.Board(self.player1, self.player2, width=7, height=7)
        print(self.game.to_string())

    def time_left_function(self):
        return 10
    """
    def test_legal_moves(self):
        self.game.apply_move((1,1))
        print(self.game.to_string())
        print("Active player is: ", self.game.active_player)
        assert len(self.game.get_legal_moves()) == 8
    """

    def test_example(self):
        # TODO: All methods must start with "test_"
        self.player1.time_left = self.time_left_function
        self.player1.get_move(self.game, self.player1.time_left)
        self.fail("Hello, World!")


if __name__ == '__main__':
    unittest.main()
