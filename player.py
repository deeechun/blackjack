class Player(object):
	
	""" Class that defines a blackjack player
	"""
	# counter to keep track of number of players
	_counter = 0
	def __init__(self, name = "", is_dealer = False, blackjack = False, 
		won_round = False, busted = False):
		"""
		:param: name string that defines the player's name
		:param: dealer boolean that's True if you are dealer; defaults False
		:param: hand list that represents hand of player; defaults to an empty list
		:param: blackjack boolean that's True on blackjack; defaults False
		:param: won_round boolean that's True on winning round; defaults False
		"""
		Player._counter += 1
		self._name = name
		self._is_dealer = is_dealer
		self.hand = []
		self._blackjack = blackjack
		self._won_round = won_round
		self._busted = busted


# ........................................................................... #
	@property
	def name(self):
		return self._name


# ........................................................................... #
	@property
	def is_dealer(self):
		return self._is_dealer


# ........................................................................... #
	@property
	def blackjack(self):
		return self._blackjack


# ........................................................................... #
	@blackjack.setter
	def blackjack(self, has_blackjack):
		blackjack = self._blackjack
		blackjack = has_blackjack

		
# ........................................................................... #
	@property
	def won_round(self):
		return self._won_round


# ........................................................................... #
	@won_round.setter
	def won_round(self, did_win_round):
		self.won_round = did_win_round


# ........................................................................... #
	@property
	def busted(self):
		return self._busted


# ........................................................................... #
	@busted.setter
	def busted(self, is_busted):
		busted = self._busted
		busted = is_busted


# ........................................................................... #
	def get_hand(self):
		return self.hand


# ........................................................................... #
	def get_value_of_hand(self):
		"""
		Get numerical value of hand. Uses the hand attribute in player. 
		:return: hand_value numerical value of hand

		Ex: If hand = ['10 of Spades', '2 of Diamonds'], returns 12
		"""
		
		hand_value = 0
		
		for card in self.hand:
			card_value = card.get_numerical_value_of_card()
			hand_value += card_value
		return hand_value


# ........................................................................... #
	def check_for_blackjack(self):
		"""
		Checks to see if numerical value of Player hand is 21

		:return: True if value of hand is 21
		:return: False if value of hand is anything but 21
		:rtype: bool
		"""
		player_hand_value = self.get_value_of_hand()
		if player_hand_value == 21:
			self.blackjack = True
			self.won_round = True
			return True
		else:
			return False


# ........................................................................... #
	def check_bust(self):
		"""
		Checks to see if numerical value of hand is greater than 21. Uses the
		hand attribute of self
		"""
		player_hand_value = self.get_value_of_hand()
		if player_hand_value > 21:
			self.busted = True
		return self.busted


# ........................................................................... #
	def add_card_to_hand(self, card):
		"""
		Adds a card to the hand of the player. The card should be a Card object
		but will accept any type. The program may throw an error if another
		type is used when you call another function.

		:param: card instance of Card object

		:return: card instance of Card that was appended to hand
		"""
		self.hand.append(card)

# ........................................................................... #
	def reset_player(self):
		"""
		Resets hand, blackjack, won_round, and busted attribute back to their
		defaults
		"""

		self.hand = []
		self.blackjack = False
		self.won_round = False
		self.busted = False
