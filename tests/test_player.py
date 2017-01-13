import unittest

class Test_Player_Hit_Function(unittest.TestCase):

	def _makeOne(self):
		""" Create an instance of the Player class to use in the test class """
		from ..player import Player
		player = Player()
		return player

	def test_hit_increases_hand_count(self):

		expected_value = 1
		returned_value = len(self._makeOne().hit("5S"))
		self.assertEqual(expected_value, returned_value)


class Test_Player(unittest.TestCase):

	def _makeOne(self):
		""" Create an instance of the Player class to use in the test class """
		from ..player import Player
		player = Player(dealer = True)
		return player

	def test_player_is_dealer(self):
		expected_value = True
		returned_value = self._makeOne()

if __name__ == "__main__":
	unittest.main()