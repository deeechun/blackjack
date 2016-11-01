import unittest

class Test_Card_Value(unittest.TestCase):
	
	def _makeOne(self):

		# Create an instance of the Card class with attributes of value = 1 and suit = "s"
		from ..card import Card
		card = Card(1, "s")
		return card

	def test_card_returns_value_of_1(self):

		expected_value = 1
		returned_value = self._makeOne().value

		self.assertEqual(expected_value, returned_value)

	def test_card_does_not_value_of_2(self):

		expected_value = 2
		returned_value = self._makeOne().value
		self.assertNotEqual(expected_value, returned_value)

class Test_Card_Suit(unittest.TestCase):
	
	def _makeOne(self):

		# Create an instance of the Card class with attributes of value = 1 and suit = "s"
		from ..card import Card
		card = Card(1, "s")
		return card

	def test_card_suit_returns_suit_of_s(self):

		expected_value = "s"
		returned_value = self._makeOne().suit
		self.assertEqual(expected_value, returned_value)

	def test_card_suit_does_not_return_suit_of_d(self):

		expected_value = "d"
		returned_value = self._makeOne().suit
		self.assertNotEqual(expected_value, returned_value)

if __name__ == "__main__":
	unittest.main()