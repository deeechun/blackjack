from card import Card

class Deck(object):
    """
    This class represents a deck of cards

    It consists of 52 cards

    A card consists of a suit and a value

    There are 4 suits and 13 value in a deck """


    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def create_deck_of_card_objects(values, suits):
        """ Given a list of values and suits, this method will create a list
        of Card objects using those values and suits

        Args: values: an array of string values e.g. ['1','2','foo']

        suits: an array of string values  e.g. ['spades', 'diamonds', 's', 'd'] 

        Returns: array of Card objects 

        Ex: if values = ['1','2','q'] and suits = ['foo','bar'], method will return
        [<card.Card object at 0x7f330bc173c8>, <card.Card object at 0x7f330bc174e0>, 
        <card.Card object at 0x7f330bc17518>, <card.Card object at 0x7f330bc176a0>, 
        <card.Card object at 0x7f330bc176d8>, <card.Card object at 0x7f330bc175c0>]
        """

        array_of_card_objects = []

        for value in values:
            for suit in suits:
                card = Card(value, suit)
                array_of_card_objects.append(card)

        return array_of_card_objects

    def deal_one_card(self):
        """ Randomly chooses an index between 0 and the length of the array 
        and pops off the entry at that index

        Returns: The card that was popped off as dealt_card
        """
        # floor method is used to round down a decimal Ex: 51.9999 will return 51
        from math import floor
        from random import random
        # random method is used to generate a value between 0 and 1
        
        # generates an index between 0 and length of the array, then pops off the entry at that array
        # and stores in dealt_card namespace
        dealt_card = self.cards.pop(floor(random()*len(self.cards)))
        return dealt_card
