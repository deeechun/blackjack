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


    def show_player_cards(self):
        """ This function returns no value.

        It only prints out the raw_card of the Card objects in the players hands 

        """

        dealer = self.players[0]
        player = self.players[len(self.players) - 1]
        print("Hey " + player.name + "! Your cards are "
            + player.hand[0].raw_card + " " + player.hand[1].raw_card)
        player_hand_value = player.get_value_of_hand()

        print("Your hand value is ", end = ""), print(player_hand_value)
        if player_hand_value == 21:
            print("BLACKJACK! You win!")
            sys.exit()

    def check_for_blackjack(self, player):
        """ Checks initial hand for blackjack

        Args: player is a Player object

        Returns: True if the player has a blackjack

        False if the player has any other value """
        hand_value = player.get_value_of_hand()
        if hand_value = 21:
            return True
        else:
            return False

    def dealer_shown_card(self):
        """ Prints out dealer's flipped card onto the terminal """
        dealer = self.players[0]
        dealer_shown_card = dealer.hand[1]
        return dealer_shown_card

    def player_hit_or_stay(self, player):
        """ Facilitates the hit/stay round for Player object that has
        attribute dealer = False

        This modifies the Player object and will return that player

        Argss:

        player: This function takes in a Player object

        Returns: True if Player object chooses to hit; False if Player object 
        chooses to stay """

        # Uses method from Player class that returns the numerical value of the hand
        hand_value = player.get_value_of_hand()

        if hand_value >= 21:
            return True

        else:
            will_hit_or_stay = input("Would you like to hit or stay? (hit/stay) ")
        

            if will_hit_or_stay.lower() == "hit" or will_hit_or_stay.lower() == "h":
                player_dealt_card = self.deck.deal_one_card()
                player.hand.append(player_dealt_card)

                hand_value = player.get_value_of_hand()
                print("You drew a "+ player_dealt_card.raw_card)
                print("Your new total is ", end = ""); print(hand_value)
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
        
        dealer_cards = dealer.hand
        hand_value = dealer.get_value_of_hand()
        print("The dealer flips his other card... ")
        print("It's a " + dealer_cards[0].raw_card)
        print("The value of the dealer's hand is ", end = ""), print(hand_value)

        while hand_value < 17:
            dealer_dealt_card = self.deck.deal_one_card()
            dealer.hand.append(dealer_dealt_card)

            print("The dealer has drawn a ", end = ""), print(dealer_dealt_card.raw_card)
            hand_value = dealer.get_value_of_hand()
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

        dealer_hand_value = dealer.get_value_of_hand()

        player_hand_value = player.get_value_of_hand()

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

                # Loop through players twice and distribute hands to players
                for player_number in range(2):
                    for player in self.players:
                        dealt_card = self.deck.deal_one_card()
                        player.hand.append(dealt_card)


                player_turn_over = False
                self.show_player_cards()
                
                dealers_showing_card = self.dealer_shown_card()
                print("The dealer is showing " + dealers_showing_card.raw_card)
                while player_turn_over == False:
                    
                    if self.player_hit_or_stay(player) == False:
                        pass
                    else:
                        player_turn_over = True

                player_hand_value = player.get_value_of_hand()

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
           
            will_play_again = input("Would you like to play another round? ")
            if will_play_again.lower() == "y" or will_play_again.lower() == "yes":
                for player in self.players:
                    # Clears all player's hands
                    player.clear_hand()
            else:
                print("Alright then, good bye!")
                game_over = True
