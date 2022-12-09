import random


def play():
    print("####################################")
    print("Welcome to Guessing Game!!!")
    print("####################################")

    secret_number = round(random.randrange(1, 101))
    total_try = 0
    points = 100

    print("What's the of difficulty level?")
    print("(1) Easy / (2) Medium / (3) Hard")

    level = int(input("Choose a level: "))

    if level == 1:
        total_try = 20
    if level == 2:
        total_try = 10
    if level == 3:
        total_try = 5

    for rodada in range(1, total_try + 1):
        print("**********")
        print("Try {} of {}".format(rodada, total_try))
        shot = int(input("Enter a number between 1 and 100: "))

        if shot < 1 or shot > 100:
            print("Choose a number between 1 and 100!")
            continue

        print("You chose the number {}".format(shot))

        won = shot == secret_number
        bigger = shot > secret_number
        smaller = shot < secret_number

        if won:
            print("You won!")
            break
        else:
            if bigger:
                print("You made a mistake, you entered a bigger value!")
            elif smaller:
                print("You made a mistake, you entered a smaller value!")
            lost_points = abs(secret_number - shot)
            points = points - lost_points
    print("Game Over! The number was {} and you scored {} points".format(secret_number, points))


if __name__ == "__main__":
    play()
