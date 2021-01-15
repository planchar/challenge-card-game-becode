# TODO: add a nice module description
""" This module combines deck and players to create a game.
"""
from card.py import Deck
from player.py import Player


class Board:
    """ TODO: add description
    """

    def __init__(self):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def __str__(self):
        return f"Board({self.players}, {self.turn_count}, {self.active_cards}, {self.history_cards})"

    def __repr__(self):
        return f"Board(players={self.players}, turn_count={self.turn_count}, active_cards={self.active_cards}, history_cards={self.history_cards})"

    def start_game(self):
        #  the following code is a test to check if the code works
        #  it can be improved later if necessary
        daniel, sijal = Player("Daniel"), Player("Sijal")
        players = [daniel, sijal]

        #  fill a deck
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()

        #  distribute the cards
        deck.distribute(players)

        # start the game
        #
        # loop of turns until no cards are left
        # make each player play() 1 Card per turn
        # at the end of the turn, print (turn_count, list of active cards, list of history cards)
        #
        #
