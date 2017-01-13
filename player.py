

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