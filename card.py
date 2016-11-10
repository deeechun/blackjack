class Card(object):
	""" This class represents a standard card in a deck

	Each card consists of two attributes: value and suit

	There are 4 unique suits and 13 values """

	def __init__(self, raw_card, value = None, suit = None):
		self.raw_card = raw_card
		self.value = self.get_value()
		self.suit = suit

	def get_value(self):
		""" Given a card string in format "[value][suit]", it will return the value of the card

		Ex: "10S" represents 10 of spades and will return the value 10 """
		face_cards = ["J","Q","K"]
		ace = "A"

		value = self.raw_card[:len(self.raw_card) - 1]
		if value in face_cards:
			value = 10
		if value == "A":
			value = 11
		else:
			value = int(value)
		return value
