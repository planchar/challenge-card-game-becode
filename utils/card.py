""" This module provides three classes to help play a basic card game.
    There is a Symbol class that contains information on the card's suit,
    a Card class that inherits from Symbol, and a Deck class that represents
    a classic deck of 52 unique playing cards.

    The game is an exercise to learn basics of OOP in Python, and is part
    of a training program at BeCode Antwerp.
"""

# Import to shuffle a Deck
from random import shuffle

# list of icon strings
iconList = ["♥", "♦", "♣", "♠"]

# create a list of value strings (split to reformat provided data)
valueList = ["A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K"][0].split(", ")


class Symbol:
    """ A Symbol class to hold information on the card suits.

        :color: a string attribute for the card suit's color.
        :icon: a single character string to represent the suit.
    """

    # create a dictionary to look up an icon's color
    iconColorDict = {"♥": "Red", "♦": "Red", "♣": "Black", "♠": "Black"}

    def __init__(self, icon):
        """ TODO:  add comment """

        self.icon = icon

        # match the icon with it's color by using the dictionary
        self.color = self.iconColorDict[icon]

    def __str__(self):
        """ TODO:  add comment """
        return f"Symbol({self.icon}, {self.color})"


class Card(Symbol):
    """ A Card class that inherits from Symbol and combines it with a value.

        :value: a string representing the card's rank.
        :icon: inherited from Symbol
        :color: inherited from Symbol
    """

    def __init__(self, value, icon):
        super().__init__(icon)
        self.value = value

    def __str__(self):
        return f"Card({self.color}, {self.value}, {self.icon})"

    def __repr__(self):
        return f"Card(color={self.color}, value={self.value}, icon={self.icon})"


class Deck:
    """ A class to represent a classic deck of 52 playing cards.

        Some methods provide basic functionality, like filling the deck,
        shuffling the cards, and distributing the cards among the players.

        :cards: a list of Card objects representing the deck's contents.
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        return f"Deck({self.cards})"

    def fill_deck(self):
        """ A method that uses nested for loops to generate a card for
            each unique combination of icon (suit) and value (rank).

            This results in a deck of 52 unique cards.
        """
        for icon in iconList:
            for value in valueList:
                card = Card(value, icon)
                self.cards.append(card)

    def shuffle():
        """ A method to shuffle the cards in the deck. """
        shuffle(self.cards)

    def distribute(self, players):
        """ This method evenly deals all cards in the deck to a list of
            players.

            The method uses a while loop that stops after the last card
            has been delt to someone.

            To iterate over the list of players, a formula has been used to
            calculate a number each time a card is delt, and matches that
            number with a player's index in the list of players.
            This should work with variable sizes of player lists, although
            it hasn't been properly tested yet.

            :param players: A list of players to distribute the cards over.
            :return players: A list of players that has been dealt cards.
        """

        # count how many players are in the list
        playerCount = len(players)

        # while there are cards in the deck, give one to the next player
        # and remove it from the deck.
        while card in self.cards:

            # 1. calculate next player's index
            index = (playerCount - 1) - (len(self.cards) % playerCount)

            # 2. update his cards with the current card in the loop
            player[index].cards.append(self.cards[0])

            # 3. remove the card from the deck
            self.cards.pop(0)

        return players
