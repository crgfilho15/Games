import hangmanGame
import guessingGame


def choose_game():
    print("###############################")
    print("Welcome, choose your game!")
    print("###############################")

    print("(1) Hangman Game / (2) Guessing Game")

    game = int(input("What's the game? "))

    if game == 1:
        print("Playing Hangman Game...")
        hangmanGame.play()
    elif game == 2:
        print("Playing Guessing Game...")
        guessingGame.play()


if __name__ == "__main__":
    choose_game()
