from player import Player
from deck import Deck
from card import Card

import sys

class Blackjack(object):

    """ Class created to run a game of blackjack. All you need to provide
    is the number of players in the game
    """


# ........................................................................... #
    def __init__(self, players, dealer, deck):
        """
        :param: players list of Player objects
        :param: dealer instance of Player class
        :param: deck instance of Deck
        """        
        self.players = players
        self.dealer = dealer
        self.deck = deck

# ........................................................................... #
    def get_dealer(self):
        return self.dealer


# ........................................................................... #
    def get_players(self):
        return self.players


# ........................................................................... #
    def get_deck(self):
        return self.deck


# ........................................................................... #
    def get_revealed_dealer_card(self):
        """
        Gets the revealed card of the dealer after the deal. Set it so the \
        card is in index 1 for the dealer

        :return: the revealed card that the dealer possesses in hand
        :rtype Card
        """
        dealer_hand = self.dealer.get_hand()
        revealed_dealer_card = dealer_hand[1]
        return revealed_dealer_card


# ........................................................................... #
    def deal_round(self):
        """
        Deals cards for one round of blackjack

        :param: blackjack the blackjack game that you want to deal a round for
        """
        for card_number in range(2):
            dealer_dealt_card = self.deck.get_one_card()
            self.dealer.add_card_to_hand(dealer_dealt_card)
            for player in self.players:
                player_dealt_card = self.deck.get_one_card()
                player.add_card_to_hand(player_dealt_card)


# ........................................................................... #
    def player_hit_round(self, player, will_hit = False):
        """
        Facilitates the player's hit round in blackjack. Default value for hit is False

        :param: player instance of Player object
        :param: will_hit boolean to signify whether a player will hit or not

        :return: hit_card Card object that the Player just hit
        """
        hand_value = player.get_value_of_hand()
        player_name = player.name
        if will_hit == True:
            hit_card = self.hit(player)
            return hit_card
        else:
            self.stay(player)


# ........................................................................... #
    def dealer_hit_round(self):
        """
        The dealer will continue to hit (function below) until the hand value is greater than 17
        """
        dealer_cards = self.dealer.get_hand()
        dealer_hand_value = self.dealer.get_value_of_hand()
        while dealer_hand_value < 17:
            self.hit(self.dealer)
            dealer_hand_value = self.dealer.get_value_of_hand()
        return dealer_hand_value


# ........................................................................... #
    def check_player_beats_dealer(self, player):
        """
        Checks to see if Player in self.players list numerical hand value beats
        dealer's hand in blackjack game
        

        """
        dealer_hand_value = self.dealer.get_value_of_hand()
        for player in self.players:
            player_hand_value = player.get_value_of_hand
            if player.get_busted_value() == True:
                return False
            elif player_hand_value > dealer_hand_value:
                return True
            elif player_hand_value == dealer_hand_value:
                return None


# ........................................................................... #
    def hit(self, player):
        """
        Adds card to hand - acts as 'hit' in blackjack'

        :param: player instance of Player class
        """
        hit_card = self.deck.get_one_card()
        player.add_card_to_hand(hit_card)
        return hit_card


# ........................................................................... #
    def stay(self, player):
        """
        No function - acts as 'stay' in blackjack
        """
        pass


# ........................................................................... #
    def double_down(self, player):
        pass


# ........................................................................... #
    def split(self, player):
        pass