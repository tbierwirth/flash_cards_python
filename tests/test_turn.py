import unittest
from lib.card import Card
from lib.turn import Turn

class TurnClass(unittest.TestCase):
    def test_it_exists(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        turn = Turn("Juneau", card)
        self.assertIsInstance(turn, Turn)
