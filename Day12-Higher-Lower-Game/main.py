import random
from art import logo, vs
from game_data import data

DEBUG_MODE = False

# TODO: Random choices A and B from data
def get_a_choice(data_input:list):
    """
    Shuffle the list and pop out the choice.
    :return: a choice and remaining data
    """
    random.shuffle(data_input)
    choice = data_input.pop()
    return choice, data_input

def get_a_valid_answer():
    """
    Limit the player's input only 'a' and 'b'. Ask again if invalid.
    :return: the player's guess
    """
    player_guess = ""
    while player_guess not in ["a", "b"]:
        player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if player_guess not in ["a", "b"]:
            print("Only 'A' or 'B' is acceptable.")
    return player_guess

# TODO: Create a function to check if the guess is correct
def right_answer(num_follower_a:int, num_follower_b:int, player_guess:str)->bool:
    """Check if the player's guess is correct"""
    if num_follower_a == num_follower_b:
        return True     # There is a case that they both have the same number.
    return (num_follower_a > num_follower_b and player_guess == "a") or \
           (num_follower_a < num_follower_b and player_guess == "b")

def start_game(data_input:list):
    """The main looping game is here.
    The game ends if the player can answer all correctly or give the wrong answer."""
    print(logo)
    choice_a, data_input = get_a_choice(data_input)
    score = 0
    while True:
        choice_b, data_input = get_a_choice(data_input)
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
        print(vs)
        print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

        if DEBUG_MODE:
            print(f"A: {choice_a['follower_count']} followers\n"
                  f"B: {choice_b['follower_count']} followers")
            print(f"Choices remain: {len(data_input)} names.")

        guess = get_a_valid_answer()

        if right_answer(choice_a['follower_count'], choice_b['follower_count'], guess):
            score += 1
            choice_a = choice_b # choice B becomes choice A of the next round
            if len(data_input) == 0:
                print(f"🎉 Congratulations! 🏆 You answers all correctly!\n"
                      f"Final score: {score}")
                break
            else:
                print(f"Nailed it!👍 Current score: {score}\n")
        else:
            print(f"Sorry, mate!😔 That's wrong.❌\nFinal score: {score}\n")
            break

player_continues = True
while player_continues:
    start_game(data)
    keep_playing = input("Let's see if you can beat yourself.💪\n"
                         "Type 'y' to continue, otherwise to exit the game: ").lower()
    if keep_playing != "y":
        player_continues = False