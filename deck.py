class Deck(object):
    """
    This class represents a deck of cards

    It consists of 52 cards

    A card consists of a suit and a value

    There are 4 suits and 13 value in a deck """


    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["D", "C", "H", "S"]

    def __init__(self, values = values, suits = suits):
        self.values = values
        self.suits = suits
        self.deck = [value + suit for suit in self.suits for value in self.values]


    """ How do I properly use properties?

    @property
    def deck(self):
        return self.deck

    @deck.setter
    def deck(self, deck):
        self.deck = deck"""