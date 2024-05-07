
class Hangman():
    GUESSES = 6
    ATTEMPTS = 10

    def __init__(self, secret_word: str, max_guesses=GUESSES, max_attempts=ATTEMPTS):
        self.secret_word = secret_word
        self.max_guesses = max_guesses
        self.max_attempts = max_attempts
        self.guesses = 0
        self.attempts = 0
        self.correct_guesses = []
        self.incorrect_guesses = []
        self.game_over = False
        self.game_won = False


    def to_dict(self) -> dict:
        return {
            "secret_word": self.secret_word,
            "guesses": self.guesses,
            "attempts": self.attempts,
            "correct_guesses": self.correct_guesses,
            "incorrect_guesses": self.incorrect_guesses,
            "game_state": self.game_state()
        }
    

    def check_guess(self, guess: str) -> None:
        if guess.isalpha():
            if len(guess) == 1:
                if guess in self.correct_guesses or guess in self.incorrect_guesses:
                    pass
                elif guess in self.secret_word:
                    self.correct_guesses.append(guess)
                    self.attempts += 1
                    self.check_game_over()
                    self.check_game_won()    
                else:
                    self.incorrect_guesses.append(guess)
                    self.attempts += 1
                    self.guesses += 1
                    self.check_game_over()
            else: 
                self.check_whole_word(guess)

    def check_game_over(self) -> bool:
        if self.attempts == self.max_attempts or self.guesses == self.max_guesses:
            self.game_over = True
            return self.game_over

    def check_game_won(self) -> bool:
        if set(self.correct_guesses) == set(self.secret_word):
            self.game_won = True
            return self.game_won

    def get_masked_word(self) -> str:
        masked_word = ""
        for letter in self.secret_word:
            if letter in self.correct_guesses:
                masked_word += f" {letter} "
            else:
                masked_word += " __ "
        return masked_word
    
    def get_remaining_letters(self) -> str:
        remaining_letters = ""
        available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in available_letters:
            if letter not in self.correct_guesses and letter not in self.incorrect_guesses:
                remaining_letters += " " + letter + " "
        return remaining_letters

    def check_whole_word(self, guessed_word: str) -> None:
        if guessed_word.upper() == self.secret_word:
            self.game_won = True
        else:
            self.attempts += 1
            self.check_game_over()

    def game_state(self) -> str:
        if self.game_over:
            return "LOST"
        elif self.game_won:
            return "WON"
        else:
            return "PLAYING"

    def get_game_status(self) -> str:
        if self.game_over:
            return "GAME OVER! The word was: " + self.secret_word
        elif self.game_won:
            return "CONGRATULATIONS! YOU WON!"
        else:
            return f"\nAttempts left: {str(self.max_attempts - self.attempts)} \nGuesses left: {str(self.max_guesses - self.guesses)}"
