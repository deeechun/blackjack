class Player(object):
	
	""" Class that defines a blackjack player
	"""
	# counter to keep track of number of players
	_counter = 0
	def __init__(self,name = "", is_dealer = False, blackjack = False, 
		won_round = False, busted = False):
		"""
		:param name string that defines the player's name
		:param dealer boolean that's True if you are dealer; defaults False
		:param hand array that represents hand of player; defaults to an empty array
		:param blackjack boolean that's True on blackjack; defaults False
		:param won_round boolean that's True on winning round; defaults False
		"""
		Player._counter += 1
		self.name = name
		self.is_dealer = False
		self.hand = []
		self.blackjack = False
		self.won_round = False
		self.busted = False

	def get_name(self):
		return self.name

	def get_is_dealer(self):
		return self.is_dealer

	def get_blackjack(self):
		return self.blackjack

	def get_won_round(self):
		return self.won_round

	def get_busted(self):
		return self.busted

	def get_hand(self):
		return self.hand

	def set_busted(self, is_busted):
		self.busted = is_busted

	def set_won_round(self, did_win_round):
		self.won_round = did_win_round

	def get_value_of_hand(self):
		""" Get numerical value of hand in hand attribute

		:returns hand_value numerical value of hand

		Ex: If hand = ['10 of Spades', '2 of Diamonds'], returns 12"""
		
		hand_value = 0
		
		for card in self.hand:
			card_value = card.get_numerical_value_of_card()
			hand_value += card_value
		return hand_value

	def check_for_blackjack(self):
		"""
		Checks to see if numerical value of Player hand is 21

		:returns True if value of hand is 21
		:returns False if value of hand is anything but 21
		"""
		player_hand_value = self.get_value_of_hand()
		if player_hand_value == 21:
			self.blackjack = True
			self.won_round = True
			return True
		else:
			return False

	def check_bust(self):
		"""
		Checks to see if numerical value of hand is greater than 21
		"""
		player_hand_value = self.get_value_of_hand()
		if player_hand_value > 21:
			self.busted = True
		return self.busted

	def add_card_to_hand(self, card):
		"""
		Appends a card to the Player hand array

		:param card instance of Card object

		:returns card instance of Card that was appended to hand
		"""
		self.hand.append(card)
		return card

	def reset_Player(self):
		"""
		Resets hand, blackjack, won_round, and busted attribute back to their
		defaults
		"""

		self.hand = []
		self.blackjack = False
		self.won_round = False
		self.busted = False
