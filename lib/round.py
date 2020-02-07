from lib.turn import Turn

class Round(object):
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.number_correct = 0

    def current_card(self):
        return self.deck.cards[len(self.turns)]

    def take_turn(self, guess):
        return Turn(guess, self.current_card())
