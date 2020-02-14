from lib.card import Card

class CardGenerator(object):
    def __init__(self, file):
        self.file = open(file, "r")
        self.cards = []
        for line in self.file:
            card = line.split(",")
            self.cards.append(Card(card[0], card[1], card[2]))
