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

	def setup_game(self):
		"""Sets up blackjack game. The game will exit here if user does not want to play

		Returns no value """

		play_game = input("Hello, welcome to Las Vegas! Would you care to pl"
					"ay some blackjack? It's a one on one! (y/n) ")
		if play_game.lower() == "y" or play_game.lower() == "yes":

			print("Okay, then let's play!")
		
		if play_game.lower() == "n" or play_game.lower() == "no":
			print("Alright, come play whenever you want!")
			sys.exit()

		else:
			play_game = input("I didn't quite get that. Could you answer once more? ")

	def deal_round(self):
		""" Deals a round of blackjack to players in round

		Attr: deck is the current deck of cards that will be used to distribute cards

		players is the players in the round signified as a list of Player objects

		Returns: list of Player objects with a new hand """

		for player in self.players:
			for card in range(2):
				self.deck.deal_one_card(player)

	def show_player_cards_(self):
		""" This function returns no value.

		It only prints out the raw_value of the Card objects in the players hands 

		"""


		dealer = self.players[0]
		player_1 = self.players[len(self.players) - 1]
		print("Hey " + player_1.name + "! Your cards are "
			+ player_1.hand[0].raw_card + " " + player_1.hand[1].raw_card)
		card_value = player_1.hand[0].value + player_1.hand[1].value

		print("Your hand value is ");print(card_value)
		print("The dealer has a " + dealer.hand[1].raw_card + " showing")

	def get_value_of_hand(self, player):
		player_hand = player.hand
		hand_value = 0

		for card in player_hand:
			hand_value += card.value

		return hand_value

	def hit_or_stay(self):
		""" Facilitates the hit/stay round

		This modifies the player_1 object and will return that player"""
		player_1 = self.players[len(self.players) - 1]
		hand_value = 0

		if hand_value >= 21:
			round_over = True

		else:
			will_hit_or_stay = input("Would you like to hit or stay? (hit/stay) ")
		

			if will_hit_or_stay.lower() == "hit" or will_hit_or_stay.lower() == "h":
				deck.deal_one_card(player_1)
				hand_value += player_1.hand[len(player_1.hand)-1].value
				print("Your new total is ");print(self.get_value_of_hand(player_1))
				return player_1

			elif will_hit_or_stay.lower() == "stay" or will_hit_or_stay.lower() == "s":
				return player_1

			else:
				print("I didn't get that. Could you say it again?")
