import unittest
from lib.card import Card
from lib.turn import Turn

class TurnClass(unittest.TestCase):
    def test_it_exists(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        turn = Turn("Juneau", card)
        self.assertIsInstance(turn, Turn)

    def test_correct_guess(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        turn = Turn("Juneau", card)
        self.assertEqual(turn.card, card)
        self.assertEqual(turn.guess, "Juneau")
        self.assertTrue(turn.is_correct())
        self.assertEqual(turn.feedback(), "Correct!")

    def test_incorrect_guess(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        turn = Turn("Topeka", card)
        self.assertEqual(turn.card, card)
        self.assertEqual(turn.guess, "Topeka")
        self.assertFalse(turn.is_correct())
        self.assertEqual(turn.feedback(), "Incorrect")

if __name__ == '__main__':
    unittest.main()
