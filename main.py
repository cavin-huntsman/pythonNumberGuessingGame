import random
lives = None
games = None
num = None
guess = None


def number_guess():
    num = random.randint(1, 10)
    lives = input('How many lives do you want?')
    lives = int(lives)
    if lives >= 10:
        print('__________Really...?__________')
    while lives > 0:
        guess = input('What do you think the number is?')
        guess = int(guess)
        if guess == num:
            print('__________Correct! YOU WIN!__________')
            break
        elif guess < num:
            print('__________The number you guessed is too low.__________')
            lives -= 1
            print(f"__________Remaining Lives: {lives}__________")
        elif guess > num:
            print('__________The number you guessed is too high.__________')
            lives -= 1
            print(f"__________Remaining Lives: {lives}__________")
    if lives == 0:
        print('__________YOU LOSE__________')


def main():
    print('__________Welcome to "Guess That Number!"__________')
    while True:
        games = input('Enter 1 to play - Enter 0 to quit')
        games = int(games)
        if games == 1:
            number_guess()
        elif games == 0:
            break
    print('__________Thanks for playing!__________')


if __name__ == "__main__":
    main()
