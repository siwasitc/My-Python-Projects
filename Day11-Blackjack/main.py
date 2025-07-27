import random
from art import logo

# TODO: Create the shuffled standard DECK of cards and SCORE dictionary
def create_decks(num_of_decks):
    """
    Create a shuffled deck of standard playing cards and a score dictionary.
    :param num_of_decks: (int) Number of standard 52-card decks to include.
    :return:
        tuple: A tuple containing:
        - decks (list): A shuffled list of card ranks (no suits).
        - score_dict (dict): A dictionary mapping each card rank to its Blackjack value.
    """
    # suits = ["♥️", "♦️", "♣️", "♠️"]
    ranks = [str(i) for i in range(2,11)] + ["J", "Q", "K", "A"]
    decks = []
    for suit in range(4):
        for rank in ranks:
            decks.append(rank)
    decks *= num_of_decks   # The higher decks, the higher chance to win of the House Edge
    random.shuffle(decks)    # To shuffle the deck

    # Create a dictionary to store score of each card
    score_dict = {}
    for i in ranks:
        if i == "J" or i == "Q" or i == "K":
            score_dict[i] = 10
        elif i == "A":
            score_dict[i] = 11
        else:
            score_dict[i] = int(i)
    # print(f"Score Dictionary: {score_dict}")
    return decks, score_dict

# TODO: Create a function to calculate total score
def calculate_score(cards):
    """
    Calculates the total Blackjack score for a given hand of cards.
    Face cards (J, Q, K) are worth 10 points, Aces are worth 11 or 1 (depending on total score).
    :param cards: (list) A list of card ranks (e.g., ['A', '10', 'J']).
    :return:
        int: The total calculated score for the hand.
    """
    total_score = sum(SCORE[i] for i in cards)
    aces = cards.count("A")
    while total_score > 21 and aces:
        total_score -= 10
        aces -= 1
    return total_score

# TODO: Create a function for the player to play
def player_turn(player, dealer):
    """
    Handles the player's turn in the game.
    Displays the current hand and asks the player whether to hit (draw) or stand (pass).
    Stops when the player busts, hits Blackjack, or choose to pass.
    :param player: (list) The player's current hand.
    :param dealer: (list) The dealer's current hand (only first card is shown to player).
    :return:
        int: The final score of the player's hand.
    """
    total_score = calculate_score(player)
    print(f"     Your cards: {player}, current score: {total_score}")
    print(f"     Dealer's first cards: {dealer[0]}")
    while True:
        if total_score > 21:
            print("BUST!")
            break
        elif total_score == 21 and len(player) == 2:
            print("BLACKJACK!")
            break
        elif total_score == 21:
            break
        else:
            wants_to_draw = input("Type 'y' to get another card, or type anything to pass: ").lower()
            if wants_to_draw == "y":
                player.append(DECK.pop())
                total_score = calculate_score(player)
                print(f"     Your cards: {player}, current score: {total_score}")
                print(f"     Dealer's first cards: {dealer[0]}")
            else:
                total_score = calculate_score(player)
                return total_score
    return total_score

# TODO: Create a function for the dealer to play
def dealer_turn(dealer, play_score):
    """
    Handles the dealer's turn according to Blackjack rules.
    Dealer draws cards until their total score is 17 or more.
    Dealer stops if the player has busted.
    :param dealer: (list) The dealer's current hand.
    :param play_score: (list) The final score of the player.
    :return:
        int: The final score of the dealer's hand.
    """
    total_score = calculate_score(dealer)
    while total_score < 17 and play_score <= 21:
        dealer.append(DECK.pop())
        total_score = calculate_score(dealer)
    return total_score

# TODO: Compare scores and print the result
def compare_score(dealer, deal_score, player, play_score):
    """
    Compares the final scores of the player and the dealer to determine the result.
    Print out the game result: win, lose, or draw.
    :param dealer: (list) The dealer's final hand.
    :param deal_score: (int) The dealer's final score.
    :param player: (list) The player's final hand.
    :param play_score: (int) The player's final score.
    :return:
        none
    """
    # Compare scores between the player and the dealer
    if deal_score == 21 and len(dealer) == 2:
        if play_score == 21 and len(player) == 2:
            print("DRAW")
        else:
            print("YOU LOSE! Dealer has Blackjack!")
    elif play_score == 21 and len(player) == 2:
        print("YOU WIN!")
    elif play_score > 21:
        print("You went over. YOU LOSE!")
    elif deal_score > 21:
        print("The dealer went over. YOU WIN!")
    elif deal_score == play_score:
        print("DRAW")
    elif deal_score > play_score:
        print("YOU LOSE!")
    else:
        print("YOU WIN!")

def play_game():
    """
    Runs a single round of Blackjack.
    Deals initial cards, executes the player and dealer turns,
    displays final hands and scores, and announces the result.
    """
    print(logo)

    # Draw 2 cards for each player
    player_cards = []
    dealer_cards = []
    for card in range(2):
        player_cards.append(DECK.pop())
        dealer_cards.append(DECK.pop())

    player_score = player_turn(player_cards, dealer_cards)
    dealer_score = dealer_turn(dealer_cards, player_score)

    print(f"     Your final hand: {player_cards}, final score: {player_score}")
    print(f"     Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    compare_score(dealer=dealer_cards, deal_score=dealer_score, player=player_cards, play_score=player_score)

################# GAME RUNS HERE #################
DECK, SCORE = create_decks(8)   # Input the number of deck
minimum_cards = 10

player_continue = True
while player_continue:
    wants_to_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if wants_to_continue == "y":
        if len(DECK) < minimum_cards:
            DECK, SCORE = create_decks(8)
        play_game()
    else:
        player_continue = False