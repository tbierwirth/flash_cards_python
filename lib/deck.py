class Deck(object):
    def __init__(self, cards):
        self.cards = cards

    def count(self):
        return len(self.cards)

    def cards_in_category(self, category):
        match = []
        for card in self.cards:
            if card.category == category:
                match.append(card)
        return match
