# Sphinx/RST Python code syntax
# http://www.sphinx-doc.org/en/1.5.1/domains.html#the-python-domain

from deck import Deck
from player import Player
from blackjack import Blackjack




# ............................................................................ #
def reveal_player_cards(player):
    """
    Reveals cards of one player by printing to the terminal

    :param: player instance of Player class
    """
    player_cards = player.get_hand()
    player_raw_cards = (card.raw_card for card in player_cards)
    player_name = player.name
    print(player_name + ", you have a " + (' and a ').join(player_raw_cards))



# ............................................................................ #
def reveal_dealer_card(blackjack):
    """
    Reveals the initial face-up dealer card in blackjack to user by printing through the terminal
    
    :param: blackjack instance of Blackjack class
    """
    revealed_dealer_card = blackjack.get_revealed_dealer_card()
    print("The dealer is showing a " + revealed_dealer_card.raw_card)


# ............................................................................ #
def reveal_dealer_hand(blackjack):
    """
    Reveals entire dealer's hand to user

    :param: blackjack instance of Blackjack class
    """

    dealer = blackjack.dealer
    dealer_hand = dealer.get_hand()
    dealer_new_revealed_card = dealer_hand[0]
    dealer_already_revealed_card = dealer_hand[1]

    print("The dealer flips...")
    print("*~*~*~FLIP~*~*~*")

    print("The dealer's hidden card was the.... " + \
           dealer_new_revealed_card.raw_card)

    print("The dealer's hand is the " + \
          dealer_already_revealed_card.raw_card + \
          " and the " + dealer_new_revealed_card.raw_card)

    print("The dealer's hand value is ", end = "")
    print(dealer.get_value_of_hand())




# ............................................................................ #
def dealer_round(blackjack):
    """
    Performs the dealer's round. Nothing will happen is all of the players have
    busted
    """

    # Loops through blackjack.players and checks to see if any instances have busted = True
    # :return: True if any instance has busted == True
    # :return: False if all instances have busted == False
    all_players_busted = all(player.busted == True for player in 
                            blackjack.players)
    if all_players_busted == False:
        blackjack.dealer_hit_round()
        reveal_final_dealer_hand_value(blackjack)
    else:
        pass   


# ............................................................................ #
def reveal_user_outcomes(blackjack):
    """
    Reveals the outcomes of the players. Each of the player's outcomes will be
    printed out into the terminal

    :param: blackjack the game of blackjack that the players are a part of
    """
    for player in blackjack.players:
        if player.won_round == True:
            print(player.name + ", you won! Congrats!")
        elif player.won_round == False:
            print("You lost " + player.name + ". Better luck next time!")
        else:
            print(player.name + " , you tied")


# ............................................................................ #
def check_round_winners(blackjack):
    """
    Checks to see which players won in the round of blackjack. Player won_round
    attribute will change if they won
    """

    # This function loops through all the players list in Blackjack if the
    # dealer busted and sets all Players won_round to True if they did
    # not bust
    blackjack_players = blackjack.get_players()
    dealer_busted = blackjack.dealer.check_bust()
    if dealer_busted == True:
        for player in blackjack_players:
            if player.busted == False:
                player.set_won_round(True)
            else:
                pass
    else:
        dealer_hand_value = blackjack.dealer.get_value_of_hand()
        for player in blackjack_players:
            player_hand_value = player.get_value_of_hand()
            if player.busted == True:
                pass
            elif player_hand_value > dealer_hand_value:
                player.set_won_round(True)
            elif player_hand_value < dealer_hand_value:
                pass
            else:
                player.set_won_round(None)


# ............................................................................ #
def player_round(blackjack):
    blackjack_players = blackjack.get_players()
    for player in blackjack_players:
        reveal_player_cards(player)
        player_has_blackjack = player.check_for_blackjack()
        if player_has_blackjack == True:
            print("BLACKJACK! Congrats!")
        else:
            player_hand_value = player.get_value_of_hand()
            user_will_hit = ask_user_yes_or_no("Would you like to hit? ")
            while user_will_hit == True:
                player_hit_card = blackjack.player_hit_round(player, will_hit =
                                                             user_will_hit)
                if player_hit_card != None:
                    player_raw_card = player_hit_card.raw_card
                    player_hand_value = player.get_value_of_hand()
                    print("You got a " + player_raw_card)
                    print("Your new hand value is ", end = "")
                    print(player_hand_value)
                    player_bust = player.check_bust()
                    if player_bust == True:
                        break
                user_will_hit = ask_user_yes_or_no("Would you like to hit? ")


# ............................................................................ #
def reveal_final_dealer_hand_value(blackjack):
    """
    Reveals dealer's final hand value to user in terminal

    :param: blackjack instance of Blackjack class
    """
    dealer = blackjack.get_dealer()
    dealer_hand_value = dealer.get_value_of_hand()
    print("The dealer's final total is ", end = "")
    print(dealer_hand_value)


# ............................................................................ #
def reset_players(blackjack):
    blackjack.dealer.reset_player()
    for player in blackjack.players:
        player.reset_player()


# ............................................................................ #
def ask_user_yes_or_no(player_prompt):
    """
    Checks to see if user will play. Uses check_prompt_response function above
    Prompted question changes if True or False is not returned the first time

    :return: True if user wants to play
    :rtype: bool
    :return: False if user does NOT want to play
    :rtype: bool
    """
    player_response = False
    repeat_text = "Didn't quite get that. Could you repeat yourself please? "
    while True:
        try:
            player_response = prompt_player(player_prompt)
            break
        except Exception as e:
            player_prompt = repeat_text

    return player_response


# ............................................................................ #

def prompt_player(prompt_text):

    """
    Checks to see if user-generated string response is 'y'/'yes'/'n'/'no' and is 
    case-insensitive

    :param: response the response that the user generated indicating whether
    they choose to 'hit' or 'stay' and is case insensitive (i.e. 'y','Y','Yes',
    'yEs')
    :type: str

    :return: True when response is 'y' or 'yes'
    :return: False when response is 'n' or 'no'
    :return: None when response is none of four options
    """
    response = input(prompt_text)
    lowercase_response = response.lower()
    if lowercase_response in ['y', 'yes']:
        return True
    elif lowercase_response in ['n','no']:
        return False
    else:
        raise Exception('Invalid player response')


# ............................................................................ #
def setup_blackjack_game():
    """
    Sets up the blackjack game only if the user wants to play. 
    """
    player_number = get_player_number()
    player_names = get_player_names(player_number)
    dealer = init_dealer()
    players = init_players(player_names = player_names)
    deck = create_standard_deck_of_cards()
    blackjack = create_blackjack_game(players = players, dealer = dealer,
                                        deck = deck)
    return blackjack

# ............................................................................ #
def get_player_number():
    """
    Gets the number of players playing for the user. If the user gives a non-
    numeric response, the prompt will change and loop until a valid response
    is given

    :return: player_number
    :rtype: int
    """
    player_number_string = input("Cool, how many players are playing? ")
    # isnumeric is True if all characters in string are numerical
    if player_number_string.isnumeric() == True:
        player_number = int(player_number_string)
    else:
        while True:
            player_number_string = input("That's not a number! Could you say \
                it again in numeric format? ")
            if player_number_string.isnumeric() == True:
                player_number = int(player_number_string)
                break
            else:
                pass
    return player_number


# ............................................................................ #
def get_player_names(player_number):
    """
    Prompts user to provide the names for each user playing. The number of names
    that the user needs to provide is based on the number of player that will
    be playing. The prompt will change after the first 

    :return: player_names list that represents player names
    """
    player_names = []
    player_name = input("Awesome! Well I don't want to be rude, let's start with the first player's name: ")
    player_names.append(player_name)
    for index in range(1, player_number):
        player_name = input("Okay, what's the next player's name? ")
        player_names.append(player_name)
    return player_names


# ............................................................................ #
def init_dealer():
    """
    Initializes a dealer that we will use for the Blackjack instance we create.
    We use the Player class and set the dealer attribute to True to create a 
    dealer

    :return: dealer instance of Player class
    """
    dealer = Player(name = 'dealer', is_dealer = True)
    return dealer


# ............................................................................ #
def init_players(player_names):
    """
    Initializes two player objects using their names that are provided by
    another function. The names are provided in a list

    :param: player_name string to represent name of player

    :return: player_list list of players with dealer at index 0
    """
    player_list = []
    for name in player_names:
        player = Player(name = name)
        player_list.append(player)
    return player_list


# ............................................................................ #
def create_standard_deck_of_cards():
    """
    Creates a standard 52 card deck

    :return: deck the deck that will be used in  
    :rtype: Deck
    """
    values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    suits = ['Diamonds','Clubs','Hearts','Spades']
    list_of_cards = Deck.create_deck_of_cards(values, suits)
    deck = Deck(list_of_cards)
    return deck


# ............................................................................ #
def create_blackjack_game(players, dealer, deck):
    """
    Creates a game of blackjack with players and a deck by creating a Blackjack 
    object

    :param: the players playing in the blackjack game
    :type: list holding the numbers of players
    :param: the deck to be used in the blackjack game

    :return: the newly created blackjack game
    :rtype: Blackjack
    """
    blackjack = Blackjack(deck = deck, dealer = dealer, players = players)
    return blackjack


# ............................................................................ #
def game_introduction():
    """
    Function does nothing but print to terminal
    """
    print("Alright then, let's begin!")
    print("~*~swipe swipe swipe swipe ~*~*~")


# ............................................................................ #
def main():
    """
    The main function of the game. Will run the entire game by calling
    functions previously defined in this script
    """
    blackjack = None
    while True:
        user_will_play = ask_user_yes_or_no("Would you like to play a game of blackjack? ")
        if user_will_play:
            if blackjack == None:
                blackjack = setup_blackjack_game()
            game_introduction()
            blackjack.deal_round()
            reveal_dealer_card(blackjack)
            player_round(blackjack)
            reveal_dealer_hand(blackjack)
            dealer_round(blackjack)
            check_round_winners(blackjack)
            reveal_user_outcomes(blackjack)
        else:
            break
    print("Goodbye.")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
if __name__ == '__main__':
    main()
