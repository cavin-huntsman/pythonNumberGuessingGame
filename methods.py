import random


def startGame():
    print('__________Welcome to "Guess That Number!"__________\n ')
    games = input('Enter 1 to play - Enter 0 to quit\n ')
    games = int(games)
    if games == 0:
        exit()


def setNumber():
    num = random.randint(1, 10)
    int(num)
    return num


def setLives():
    lives = input('How many lives do you want?\n ')
    lives = int(lives)
    return lives


def compareNumber(num, lives):
    if lives >= 10:
        print('__________Really...?__________\n ')
    while lives > 0:
        guess = input('What do you think the number is?\n ')
        guess = int(guess)
        if guess == num:
            print('__________Correct! YOU WIN!__________\n \n \n ')
            break
        elif guess < num:
            print('__________The number you guessed is too low.__________')
            lives -= 1
            print(f"__________Remaining Lives: {lives}__________\n ")
        elif guess > num:
            print('__________The number you guessed is too high.__________')
            lives -= 1
            print(f"__________Remaining Lives: {lives}__________\n ")
    if lives == 0:
        print('__________YOU LOSE__________\n \n \n ')
