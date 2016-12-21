from player import Player
from deck import Deck
from card import Card

import sys

class Blackjack(object):

    """ Class created to run a game of blackjack. All you need to provide
    is the number of players in the game

    Attrs: players: represents an array of Player objects in game

    deck: the deck being used; represented by an instance of the Deck class
    An array is found in the object called deck, which contains suit/value pairs
    Ex: '10H' represents 10 of hearts """

    def __init__(self, players, deck):
        self.players = players
        self.deck = deck

    @staticmethod
    def setup_game():
        """Sets up blackjack game. The game will exit here if user does not want to play
        
        This is a static method because there is no reference to self

        Creates Blackjack object with two Player objects: one dealer and one player

        Returns Blackjack object """

        play_game = input("Hello, welcome to Las Vegas! Would you care to pl"
                    "ay some blackjack? It's a one on one! (y/n) ")
        if play_game.lower() == "y" or play_game.lower() == "yes":

            print("Okay, then let's play!")
            
            player_name = input("Okay, let's play! Let's start with your name. "
                            "I don't want to be rude! ")
            dealer = Player(name = "dealer", dealer = True)
            player = Player(name = player_name)
            deck = Deck()
            player_array = []
            player_array.extend((dealer, player))
            blackjack = Blackjack(deck = deck, players = player_array)
            return blackjack
            
        elif play_game.lower() == "n" or play_game.lower() == "no":
            print("Alright, come play whenever you want!")
            sys.exit()

        else:
            self.setup_game()
            
    def deal_one_card(self, player):
        """ Pops off a raw_value from the deck at a pseudo-random index and adds it to 
        player's hand as a Card object

        Args: player MUST represent an instance of the class Player

        Returns: player with new Card object appended to list """

        from card import Card
        import random
        from math import floor
        deck = self.deck.deck
        dealt_card = deck.pop(floor(random.random()*len(deck)))
        dealt_card = Card(dealt_card)
        player.hand.append(dealt_card)
        return player

    def deal_round(self):
        """ Deals a round of blackjack to players in round

        Attr: deck is the current deck of cards that will be used to distribute cards

        players is the players in the round signified as a list of Player objects

        Returns: list of Player objects with a new hand """

        for player in self.players:
            for card in range(2):
                self.deal_one_card(player)

    def show_player_cards(self):
        """ This function returns no value.

        It only prints out the raw_value of the Card objects in the players hands 

        """


        dealer = self.players[0]
        player = self.players[len(self.players) - 1]
        print("Hey " + player.name + "! Your cards are "
            + player.hand[0].raw_card + " " + player.hand[1].raw_card)
        player_hand_value = self.get_value_of_hand(player)

        print("Your hand value is ", end = ""), print(player_hand_value)
        if player_hand_value == 21:
            print("BLACKJACK! You win!")
            sys.exit()

    def get_value_of_hand(self, player):
        player_hand = player.hand
        hand_value = 0

        for card in player_hand:
            hand_value += card.value
        return hand_value

    def show_dealer_card(self):
        dealer = self.players[0]
        dealer_card = dealer.hand[1].raw_card
        print("The dealer is showing a " + dealer_card)

    def player_hit_or_stay(self, player):
        """ Facilitates the hit/stay round for Player object that has
        attribute dealer = False

        This modifies the Player object and will return that player

        Argss:

        player: This function takes in a Player object

        Returns: True if Player object chooses to hit; False if Player object 
        chooses to stay """

        hand_value = 0

        for card in player.hand:
            hand_value += card.value



        if hand_value >= 21:
            return True

        else:
            will_hit_or_stay = input("Would you like to hit or stay? (hit/stay) ")
        

            if will_hit_or_stay.lower() == "hit" or will_hit_or_stay.lower() == "h":
                self.deal_one_card(player)
                card = player.hand[len(player.hand)-1]
                hand_value += card.value
                print("You drew a "+ card.raw_card)
                print("Your new total is ", end = ""); print(self.get_value_of_hand(player))
                return False

            elif will_hit_or_stay.lower() == "stay" or will_hit_or_stay.lower() == "s":
                return True

            else:
                print("I didn't get that. Could you say it again?")


    def dealer_hit_or_stay(self, dealer):
        """ Facilitates the hit/stay round for Player object that has
        attribute dealer = False

        This modifies the Player object and will return that Player 

        dealer: This function takes in a Player object

        Returns: the same Player object taken as the argument"""

        hand_value = self.get_value_of_hand(dealer)
        print("The value of the dealer's hand is ", end = ""), print(hand_value)

        while hand_value < 17:
            self.deal_one_card(dealer)

            dealer_drawn_card = dealer.hand[len(dealer.hand) - 1].value

            print("The dealer has drawn a ", end = ""), print(dealer_drawn_card)
            hand_value = self.get_value_of_hand(dealer)
            print("The dealer's new total is ", end = ""), print(hand_value)
            if hand_value > 21:
                print("The dealer has bust! You win!")
                sys.exit()
        return dealer

    def compare_dealer_and_player_hand_values(self, dealer, player):
        """ Compares two Player object hands

        Args:

        dealer: a Player object with a dealer attribute = True

        player: a Player object with a dealer attribute = False

        Returns:

        -1: if dealer hand is greater than player hand

        0: if dealer hand equals player hand

        1: if player hand is greater than dealer hand """

        dealer_hand_value = self.get_value_of_hand(dealer)

        player_hand_value = self.get_value_of_hand(player)

        if dealer_hand_value == player_hand_value:
            return 0

        elif dealer_hand_value > player_hand_value:
            return -1

        else:
            return 1

    def start_game(self):
        """Facilitates round after set up

        Uses methods of this class to player one round of blackjack"""

        game_over = False
        dealer, player = self.players[0], self.players[1] 
        while game_over == False:
            round_over = False
            
            while round_over == False:
                print("Alright then! Let's begin ~")
                print("* swipe swipe swipe swipe *")

                self.deal_round()
                player_turn_over = False
                self.show_player_cards()
                self.show_dealer_card()
                while player_turn_over == False:
                    
                    if self.player_hit_or_stay(player) == False:
                        pass
                    else:
                        player_turn_over = True

                player_hand_value = self.get_value_of_hand(player)

                if player_hand_value > 21:
                    print("Oh, no! Bust!")
                    round_over = True

                elif player_hand_value <= 21:

                    self.dealer_hit_or_stay(dealer)
                    if self.compare_dealer_and_player_hand_values(dealer, player) == 0:
                        print("It's a draw!")

                    elif self.compare_dealer_and_player_hand_values(dealer, player) == 1:
                        print("You win!")

                    else:
                        print("You lose D:")
                    

                    round_over = True
            game_over = True
