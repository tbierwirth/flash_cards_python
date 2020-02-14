from lib.card import Card
from lib.deck import Deck
from lib.round import Round
from lib.turn import Turn
from lib.card_generator import CardGenerator

generator = CardGenerator("cards.txt")
cards = generator.cards
categories = []

deck = Deck(cards)
round = Round(deck)

print(f"Welcome! You're playing with {deck.count} cards.")
print("-------------------------------------")

i = 1
for card in cards:
    if card.category not in categories:
        categories.append(card.category)

    print(f"This is card number {i} out of {deck.count()}")
    print(f"Question: {card.question}")
    guess = input("")
    turn = round.take_turn(guess)
    print(turn.feedback())
    i += 1

print("****** Game over! ******")
print(f"You had {round.number_correct} out of {deck.count()} for a total score of {round.percent_correct()}%.")
for category in categories:
    print(f"{category} - {round.percent_correct_by_category(category)}% correct")
