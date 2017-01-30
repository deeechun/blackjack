from card import Card
# floor method is used to round down a decimal Ex: 51.9999 will return 51
from math import floor
# random method is used to generate a value between 0 and 1
from random import random

class Deck(object):
    """
    This class represents a deck of cards
    """

    def __init__(self, cards):
        """
        :param: cards list of Card objects
        """
        self.cards = cards


# ........................................................................... #
    def get_one_card(self):
        """
        Randomly chooses an index between 0 and the length of the list 
        and pops off the entry at that index. The return type should be of Card
        but there are no restrictions placed 

        :return: dealt_card the card that was taken popped off of the deck
        attribute of self
        :rtype: Card
        """
        
        # generates an index between 0 and length of the list, then pops off
        # the entry at that list index and stores in dealt_card namespace
        number_cards = len(cards)
        random_card_index = floor(random() * number_cards)
        dealt_card = self.cards.pop(random_card_index)
        return dealt_card


# ........................................................................... #
    @staticmethod
    def create_deck_of_cards(values, suits):
        """
        Creates a deck of cards given a list of values and suits. Values and
        suits must be strings

        :param values list of string values e.g. ['1','2','foo']
        :param suits list of string values  e.g. ['spades', 'diamonds', 's',
        'd'] 

        :return: list_of_cards

        Ex: if values = ['1','2','q'] and suits = ['foo','bar'], method will
        return [Card('1 of foo'), Card('2 of foo'), Card('q of foo'),
        Card('1 of bar'), Card('2 of bar'), Card('q of bar')]
        """
        # Create an empty list 
        list_of_cards = []

        # loops through 'values' list
        # loops through 'suits' list
        # creates an instance of a Card using each value and suit
        # adds card to the list 'list_of_cards'
        for value in values:
            for suit in suits:
                card = Card(value, suit)
                list_of_card_objects.append(card)


        return list_of_cards