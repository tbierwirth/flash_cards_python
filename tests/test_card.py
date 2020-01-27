import unittest
from lib.card import Card

class CardClass(unittest.TestCase):
    def test_it_exists(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        self.assertIsInstance(card, Card)

    def test_attributes(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        self.assertEqual(card.question, "What is the capital of Alaska?")
        self.assertEqual(card.answer, "Juneau")
        self.assertEqual(card.category, "Geography")
