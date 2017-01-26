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
        :param cards array of Card objects
        """
        self.cards = cards


# ........................................................................... #
    def get_one_card(self):
        """ Randomly chooses an index between 0 and the length of the array 
        and pops off the entry at that index

        :return: dealt_card Card object that is popped off self.cards
        """
        
        # generates an index between 0 and length of the array, then pops off
        # the entry at that array index and stores in dealt_card namespace
        number_cards = len(cards)
        random_card_index = floor(random() * number_cards)
        dealt_card = self.cards.pop(random_card_index)
        return dealt_card


# ........................................................................... #
    @staticmethod
    def create_deck_of_cards(values, suits):
        """ Given a list of values and suits, this method will create a list
        of Card objects using those values and suits

        :param values array of string values e.g. ['1','2','foo']
        :param suits array of string values  e.g. ['spades', 'diamonds', 's',
        'd'] 

        :return: array_of_Card_objects 

        Ex: if values = ['1','2','q'] and suits = ['foo','bar'], method will
        return [Card('1 of foo'), Card('2 of foo'), Card('q of foo'),
        Card('1 of bar'), Card('2 of bar'), Card('q of bar')]
        """

        array_of_card_objects = []

        for value in values:
            for suit in suits:
                card = Card(value, suit)
                array_of_card_objects.append(card)

        return array_of_card_objects