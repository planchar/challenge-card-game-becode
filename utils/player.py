""" This module contains a single class Player to use in a basic card game.

    The game is an exercise to learn basics of OOP in Python, and is part
    of a training program at BeCode Antwerp.
"""

from card.py import Card
from random import randint


class Player:
    """ TODO: docstring
    """

    def __init__(self, name):
        self.name = name
        self.turn_count = 0
        self.number_of_cards = 0
        self.cards = []
        self.history = []

    def __str__(self):
        return f"Player({self.name}, {self.turn_count}, {self.number_of_cards}, {self.cards}, {self.history})"

    def __repr__(self):
        return f"Player(name={self.name}, turn_count={self.turn_count}, number_of_cards={self.number_of_cards}, cards={self.cards}, history={self.history})"

    def play(self):
        """ A method to have a player play a card. """

        # check for cards
        if self.number_of_cards == 0:
            break

        elif self.number_of_cards >= 1:
            # select a random card to play
            cardIndex = randint(1, self.number_of_cards) - 1
            returnCard = self.cards[cardIndex]
            # print message
            value, icon = returnCard.value, returnCard.icon
            player, turn = self.name, self.turn_count
            text = "{player} {turn} played: {value} {icon}."
            print(text.format(player, turn, value, icon))
            # add it to history
            self.history.append(returnCard)
            # remove it from the cards list
            self.cards.pop(returnCard)
            # return it
            return returnCard
