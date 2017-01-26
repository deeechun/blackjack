class Card(object):
	""" This class represents a standard card in a deck

	Each card consists of two attributes: value and suit

	There are 4 unique suits and 13 values """

	def __init__(self, value, suit):

		"""
		:param value string that represents card value 
		:param suit string that represents the suit of a card
		:param raw_card string that combines value and suit (ex. 'Jack of Spades')
		"""
	
		self.value = value
		self.suit = suit
		self.raw_card = value + " of " + suit

	def get_raw_card(self):
		return self.raw_card

	def get_numerical_value_of_card(self):
		"""Given a card string in format "[value][suit]", it will return the value of the card
		Ex: "10S" represents 10 of spades and will return the value 10 

		:returns value numerical blackjack value of card
		"""
		face_cards = ["Jack","Queen","King"]
		value = self.value

		if value in face_cards:
			value = 10
		if value == "Ace":
			value = 11
		else:
			value = int(value)
		return value