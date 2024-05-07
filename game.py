import logging
import logging.config
from image import image
import os
from hangman_game import Hangman
import random

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("Log")

def get_secret_word() -> str:
    file_path = open("words.txt", "r")
    words = [word.strip() for word in file_path.readlines()]
    secret_word = random.choice(words)
    file_path.close()
    return secret_word.upper()   

game = Hangman(secret_word= get_secret_word())

logger.info(f"Game started")
logger.info(f"Game status: {game.to_dict()}") 

os.system("clear")
while game.game_state() == "PLAYING":
    print(image[game.guesses])
    word = game.get_masked_word()
    print("\n" + word + "\n")
    print("\n" + game.get_remaining_letters() + "\n")
    print(f"Correct guesses: {game.correct_guesses}")
    print(f"Incorrect guesses: {game.incorrect_guesses}")
    guess = input("Guess a letter or a whole word: ")
    
    if guess.upper() in game.correct_guesses or guess.upper() in game.incorrect_guesses:
        print(f"You already guessed {guess.upper()}. Try again.")
    game.check_guess(guess.upper())
    print(f"Game status: {game.get_game_status()}")
    if game.game_state() == "LOST":
        print(image[game.guesses])
        print("\n" + word + "\n")
    elif game.game_state() == "WON":
        print(image[game.guesses])
        word = game.get_masked_word()
        print("\n" + word + "\n")
    logger.info(f"Game status: {game.to_dict()}")

logger.info(f"Game status: {game.to_dict()}")
logger.info(f"Game ended")