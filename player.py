

class Player(object):
	
	""" Class that defines a blackjack player

	Attr:

	name: a string that defines the player's name

	dealer: True if you are dealer, False if you are not

	hand: represents hand of player; defaults to empty list """

	def __init__(self, name = "", dealer = False, hand = []):
		
		self.name = name
		self.dealer = dealer
		self.hand = hand

	def hit(self, card):
		# Adds a card to the hand

		self.hand.append(card)
		return self.hand