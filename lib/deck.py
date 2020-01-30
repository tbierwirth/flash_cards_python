class Deck(object):
    def __init__(self, cards):
        self.cards = cards

    def count(self):
        return len(self.cards)
