from deck import Deck
from player import Player
from blackjack import Blackjack

if __name__ == '__main__':
	
	blackjack = Blackjack.setup_game()
	blackjack.start_game()