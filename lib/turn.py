class Turn(object):
    def __init__(self, guess, card):
        self.guess = guess
        self.card = card

    def is_correct(self):
        if self.guess == self.card.answer:
            return True
        else:
            return False

    def feedback(self):
        if self.is_correct():
            return "Correct!"
        else:
            return "Incorrect"
