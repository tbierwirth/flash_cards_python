import unittest
from lib.card import Card
from lib.deck import Deck
from lib.round import Round

class RoundClass(unittest.TestCase):
    def test_it_exists(self):
        card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
        card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
        card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
        cards = [card_1, card_2, card_3]
        deck = Deck(cards)
        round = Round(deck)
        self.assertIsInstance(round, Round)
        self.assertEqual(round.deck, deck)

    def test_current_card(self):
        card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
        card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
        card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
        cards = [card_1, card_2, card_3]
        deck = Deck(cards)
        round = Round(deck)
        self.assertEqual(round.current_card(), card_1)
