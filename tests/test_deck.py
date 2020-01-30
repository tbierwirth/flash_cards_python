import unittest
from lib.card import Card
from lib.deck import Deck

class DeckClass(unittest.TestCase):
    def test_it_exists(self):
        card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
        card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
        card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
        cards = [card_1, card_2, card_3]
        deck = Deck(cards)
        self.assertIsInstance(deck, Deck)

    def test_it_has_cards(self):
        card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
        card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
        card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
        cards = [card_1, card_2, card_3]
        deck = Deck(cards)
        self.assertEqual(len(deck.cards), 3)

if __name__ == '__main__':
    unittest.main()
