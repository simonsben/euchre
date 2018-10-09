from utilities import suits, ranks
from card import card
from random import random


# Class to define deck
class deck:
    def __init__(self):
        self.fill_deck()
        self.shuffle()

    # Fills the deck with cards
    def fill_deck(self):
        self.cards = []

        for suit in suits:  # For every suit
            for rank in ranks:  # For every card value
                self.cards.append(card(suit, rank))

    # Shuffle the cards in the deck
    def shuffle(self):
        for card in self.cards:  # Assign random value to each card
            card.index = random()
        self.sort_deck()  # Order the cards based on the random values

        for i, card in enumerate(self.cards):  # Re-number the deck indexes
            card.index = i

    # Sort the deck (selection sort)
    def sort_deck(self):
        for i, _ in enumerate(self.cards):
            min = i
            for j in range(i, len(self.cards)):
                if self.cards[min].index > self.cards[j].index:
                    min = j

            if min != i:
                hold = self.cards[min]
                self.cards[min] = self.cards[i]
                self.cards[i] = hold

    # To string method
    def __str__(self):
        output = ''
        for i, card in enumerate(self.cards):
            output += str(i + 1) + ' ' + card.__str__() + '\n'

        return output
