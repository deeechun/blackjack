import unittest

class Test_Card_Value(unittest.TestCase):
	
	def _makeOne(self):

		""" Create an instance of the Card class to use in the test class

		Attrs:

		value: set to 1

		suit: set to "s" (spades)"""

		from ..card import Card
		card = Card(1, "s")
		return card

	def test_card_returns_value_of_1(self):

		# Asserts that the value of the card is 1
		expected_value = 1
		returned_value = self._makeOne().value

		self.assertEqual(expected_value, returned_value)

	def test_card_does_not_value_of_2(self):

		# Asserts that the value of the card is not 2
		expected_value = 2
		returned_value = self._makeOne().value
		self.assertNotEqual(expected_value, returned_value)

class Test_Card_Suit(unittest.TestCase):
	
	def _makeOne(self):

		""" Create an instance of the Card class

		Attrs:

		value: set to 1

		suit: set to "s" (spades)

		We use this instance throughout our test cases """

		from ..card import Card
		card = Card(1, "s")
		return card

	def test_card_suit_returns_suit_of_s(self):

		# Asserts that the suit of the card is "s" (spades)
		expected_value = "s"
		returned_value = self._makeOne().suit
		self.assertEqual(expected_value, returned_value)

	def test_card_suit_does_not_return_suit_of_d(self):

		#Asserts that the suit of the card is not "d" (diamonds)
		expected_value = "d"
		returned_value = self._makeOne().suit
		self.assertNotEqual(expected_value, returned_value)

if __name__ == "__main__":
	unittest.main()