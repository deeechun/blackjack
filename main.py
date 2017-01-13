from deck import Deck
from player import Player
from blackjack import Blackjack

def setup_game(deck):
        """Sets up blackjack game. The game will exit here if user does not want to play
        
        This is a static method because there is no reference to self

        Creates Blackjack object with two Player objects: one dealer and one player

        Returns Blackjack object """

        
        will_play_game = input("Hello, welcome to Las Vegas! Would you care to pl"
                    "ay some blackjack? It's a one on one! (y/n) ")
        if will_play_game.lower() == "y" or will_play_game.lower() == "yes":
            player_name = input("Okay, let's play! Let's start with your name. "
                                 "I don't want to be rude! ")
            dealer = Player(name = "dealer", dealer = True)
            player = Player(name = player_name)
            player_array = []
            player_array.extend((dealer, player))
            blackjack = Blackjack(deck = deck, players = player_array)
            return blackjack
            
        elif will_play_game.lower() == "n" or will_play_game.lower() == "no":
            import sys
            print("Alright, come play whenever you want!")
            sys.exit()

        else:
            setup_game(deck)

if __name__ == '__main__':
    values = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['D','C','H','S']
    list_of_card_objects = Deck.create_deck_of_card_objects(values, suits)
    deck = Deck(list_of_card_objects)
    blackjack = setup_game(deck)
    blackjack.start_game()