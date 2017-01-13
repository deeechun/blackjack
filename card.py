class Card(object):
	""" This class represents a standard card in a deck

	Each card consists of two attributes: value and suit

	There are 4 unique suits and 13 values """

	def __init__(self, value, suit):

		"""Attrs:

		suit: represents the suit of a card, represented by the first letter of the suit
		Ex: 'S' represents spades

		raw_card: representative form of the Card object
		Ex: AS represents the Ace of Spades

		value: numerical value of the card
		Ex: 10S will return 10
		"""
	
		self.value = value
		self.suit = suit
		self.raw_card = value + suit

	def get_numerical_value_of_card(self):
		"""Given a card string in format "[value][suit]", it will return the value of the card

		Ex: "10S" represents 10 of spades and will return the value 10 """
		face_cards = ["J","Q","K"]
		ace = "A"

		value = self.value

		if value in face_cards:
			value = 10
		if value == "A":
			value = 11
		else:
			value = int(value)
		return value