from deck import Deck
from player import Player
from blackjack import Blackjack


import sys

play_game = input("Hello, welcome to Las Vegas! Would you care to pl"
					"ay some blackjack? It's a one on one! (y/n) ")
	
if play_game.lower() == "y" or play_game.lower() == "yes":

	player_name = input("Okay, let's play! Let's start with your name. "
						"I don't want to be rude! ")
	dealer = Player(name = "dealer", dealer = True)
	player_1 = Player(name = player_name)
	deck = Deck()
	player_array = []
	player_array.extend((dealer, player_1))
	blackjack = Blackjack(deck = deck, players = player_array)

	print("Alright then! Let's begin ~")
	print("* swipe swipe swipe swipe swipe *")

	blackjack.deal_round()
	blackjack.show_player_cards()
	blackjack.hit_or_stay_round()
	

	sys.exit()


if play_game.lower() == "n" or play_game.lower() == "no":
	print("Alright, come play whenever you want!")
	game_over = True

else:
	play_game = input("I didn't quite get that. Could you answer once more? ")
