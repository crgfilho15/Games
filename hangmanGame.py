import random


def play():
    print_opening_message()

    secret_word = choose_secret_word()

    correct_letters = initialize_correct_letters(secret_word)
    print(correct_letters)

    correct = False
    hanged = False
    error = 0

    while not hanged and not correct:
        shot = shot_letter()

        if shot in secret_word:
            correct_shot(secret_word, shot, correct_letters)
        else:
            error += 1
            draw_hangedman(error)

        correct = "_" not in correct_letters
        hanged = error == 6
        print(correct_letters)

    if correct:
        win_message()
    else:
        lose_message(secret_word, error)


def print_opening_message():
    print("####################################")
    print("Welcome to Hangman Game!")
    print("Hint: It's a fruit!")
    print("####################################")


def choose_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def initialize_correct_letters(word):
    return ["_" for letter in word]


def shot_letter():
    shot = input("Choose one letter: ")
    return shot.strip().upper()


def correct_shot(secret_word, shot, correct_letters):
    index = 0
    for letter in secret_word:
        if shot == letter:
            correct_letters[index] = letter
        index = index + 1


def win_message():
    print("Congratulations, you won the game!")
    print(":) :) :) :) :) :) :) :) :) :) :) :) ")


def lose_message(secret_word, error):
    print("Game over, you lost the game! The word it was {}".format(secret_word))
    draw_hangedman(error)


def draw_hangedman(error):
    print("________")
    print("|/      |")

    if error == 1:
        print("        O")
    if error == 2:
        print("        O")
        print("       /")
    if error == 3:
        print("        O")
        print("       /|")
    if error == 4:
        print("        O ")
        print("       /|\ ")
    if error == 5:
        print("        O ")
        print("       /|\ ")
        print("       /   ")
    if error == 6:
        print("        O ")
        print("       /|\ ")
        print("       / \ ")


if __name__ == "__main__":
    play()
