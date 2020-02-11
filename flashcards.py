from lib.card import Card
from lib.deck import Deck
from lib.round import Round
from lib.turn import Turn

card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
cards = [card_1, card_2, card_3]

deck = Deck(cards)
round = Round(deck)

print(f"Welcome! You're playing with {len(cards)} cards.")
print("-------------------------------------")

for card in cards:
    print(f"This is card number {i} out of {len(cards)}")
    print(f"Question: {card.question}")
    guess = input("")
    turn = round.take_turn(guess)
    print(turn.feedback())
