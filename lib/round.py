from lib.turn import Turn

class Round(object):
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.number_correct = 0

    def current_card(self):
        return self.deck.cards[len(self.turns)]

    def take_turn(self, guess):
        turn = Turn(guess, self.current_card())
        self.turns.append(turn)
        if turn.is_correct():
            self.number_correct += 1
        return turn

    def number_correct_by_category(self, category):
        correct = 0
        for turn in self.turns:
            if (turn.is_correct() == True) and (turn.card.category == category):
                correct +=1
        return correct

    def percent_correct(self):
        return (self.number_correct / len(self.turns)) * 100.0

    def percent_correct_by_category(self, category):
        correct = 0
        incorrect = 0
        for turn in self.turns:
            if (turn.is_correct() == False) and (turn.card.category == category):
                incorrect += 1
            if (turn.is_correct() == True) and (turn.card.category == category):
                correct += 1

        return (correct / (correct + incorrect)) * 100.0
