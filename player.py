class Player(object):
	
	""" Class that defines a blackjack player

	Attr:

	name: a string that defines the player's name

	dealer: True if you are dealer, False if you are not

	hand: represents hand of player; defaults to an empty array """

	_counter = 0

	def __init__(self,name = "", dealer = False):
		
		Player._counter += 1
		self.name = name
		self.dealer = False
		self.hand = []

		"""I have some quick questions about init parameters"""

	def get_value_of_hand(self):
		""" Get numerical value of hand in hand attribute

		Ex: If hand = ['10S', '2D'], returns 12"""
		
		hand_value = 0
		
		for card in self.hand:
			card_value = card.get_numerical_value_of_card()
			hand_value += card_value
		return hand_value

	def clear_hand(self):
		"""Sets hand attribute to original empty array """
		self.hand = []