import unittest

class Test_Deck(unittest.TestCase):

	def _makeOne(self):
		
		"""Create an instance of the Deck class for uses in the test class"""

		from ..deck import Deck
		deck = Deck()
		return deck

	def test_deck_has_52_cards(self):
		expected_value = 52
		return_value = len(self._makeOne().deck)
		self.assertEqual(expected_value, return_value)

if __name__ == "__main__":
	unittest.main()