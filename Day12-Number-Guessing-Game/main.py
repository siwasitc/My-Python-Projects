from art import logo
import random

DEBUG_MODE = False

EASY_LEVEL_TURNS = 10
NORMAL_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5

def game_set_up()->int:
    """
    Initialises the number guessing game.
    Prints a welcome message and the game logo, then generate a random target number between 1 and 100 for the player to guess.
    Displays the number if DEBUG_MODE is enabled.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!\n"
          "Here you will guess the number I'm thinking of between 0-100.\n"
          "Are you READY???")
    number = random.randint(1,100)
    if DEBUG_MODE:
        print(f"\n###################################"
              f"\n# SPOILER ALERT! THE NUMBER IS {number} #\n"
              f"###################################\n")
    return number

def get_level_and_attempts()->int:
    """
    Prompts the player to choose a difficulty level.

    Available difficulty levels:
        - easy: 10 attempts
        - normal: 7 attempts
        - hard: 5 attempts

    Repeats the prompt until a valid input is given.
    :return: The number of attempts based on chosen difficulty.
    """
    while True:
        level = input("Choose your difficulty. Type 'easy', 'normal', or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "normal":
            return NORMAL_LEVEL_TURNS
        elif level == 'hard':
            return HARD_LEVEL_TURNS
        else:
            print("Invalid choice. Please type 'easy', 'normal', or 'hard'.\n")

def check_answer(user_guess:int, answer:int)->bool:
    """
    Compares the player's guess with the correct answer.
    If the guess is correct, congratulates the player. Otherwise, indicates whether the guess was too high or too low.
    """
    if user_guess == answer:
        print(f"\nYOU NAILED IT! THE NUMBER WAS {answer}!\n"
              f"YOU WIN!\n")
        return True
    else:
        print("TOO HIGH" if user_guess > answer else "TOO LOW")
        return False

def game_play(attempt:int, answer:int)->None:
    """
    Manages the main gameplay loop.

    Prompts the player to guess the number, gives feedback on each guess, and tracks the number of remaining attempts.
    Ends when the player guesses correctly or runs out of attempts.
    """
    while attempt > 0:    # Check if the attempts is more than zero
        print(f"\nYou have {attempt} attempts remaining to guess the number.")
        try:
            user_guess = int(input("Make a guess: "))
            if user_guess < 1 or user_guess > 100:
                print("Please enter the number between 1 and 100.")
                continue
            if check_answer(user_guess,answer):
                break

            attempt -= 1
            if attempt > 0:
                print("Guess again.")
        except ValueError:
            print("Invalid input. Please guess a number.")

    else:
        print("\nGAME OVER!\n"
              f"THE NUMBER WAS {answer}.\n")

keep_playing = True
while keep_playing:
    the_number = game_set_up()
    num_attempts = get_level_and_attempts()
    game_play(attempt=num_attempts, answer=the_number)
    user_continues = input("Isn't it fun?\n"
                           "Let's play it again! Type 'yes' or 'no': ").lower()
    if user_continues != 'yes':
        keep_playing = False