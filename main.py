from deck import Deck
from player import Player

import sys

game_over = False

play_game = input("Hello, welcome to Las Vegas! Would you care to pl"
					"ay some blackjack? It's a one on one! (y/n) ")

while game_over == False:
	
	if play_game.lower() == "y" or play_game.lower() == "yes":

		player_name = input("Okay, let's play! Let's start with your name. "
							"I don't want to be rude! ")

		players_in_game_array = []
		dealer = Player(name = "dealer", dealer = True)
		player_1 = Player(name = player_name)
		players_in_game_array.extend((dealer, player_1))

		deck = Deck()

		print("Alright " + player_1.name + "! Let's begin ~")
		print("* swipe swipe swipe swipe swipe *")

		for player in players_in_game_array:
			for card in range(2):
				deck.deal_one_card(player)
		print("Okay, here are your cards! " + player_1.hand[0], player_1.hand[1])
		

		while game_over == False:
		
			hit_or_stay = input("Would you like to hit or stay? (hit/stay) ")
			if hit_or_stay.lower() == "hit" or hit_or_stay.lower() == "h":
				deck.deal_one_card(player)

				print("Your new total is")

			game_over = True

		sys.exit()


	if play_game.lower() == "n" or play_game.lower() == "no":
		print("Alright, come play whenever you want!")
		game_over = True

	else:
		play_game = input("I didn't quite get that. Could you answer once more? ")