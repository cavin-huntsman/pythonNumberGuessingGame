import random
import time

# methods for base game
# startGame(), setNumber(), setLives(), compareNumber(num, lives)


def startGame():
    print('__________Welcome to "Guess That Number!"__________\n ')
    games = input('Enter 1 to play - Enter 0 to quit\n ')
    games = int(games)
    if games == 0:
        exit()


def setNumber():
    print("I've selected a random number between 1 and 10! Can you guess it before you run out of lives??")
    num = random.randint(1, 10)
    num = int(num)
    return num


def setLives():
    lives = input('How many lives do you want?\n ')
    lives = int(lives)
    return lives


def compareNumber(num, lives, mode, round):
    if lives >= 10:
        print('__________Everyone needs a freebie now and then__________\n ')
    while lives > 0:
        guess = input('What do you think the number is?\n ')
        guess = int(guess)
        if guess == num:
            if mode == 1:
                print('__________Correct! YOU WIN!__________\n \n \n ')
                break
            elif mode == 2:
                print('__________Correct!__________\n \n \n ')
                print(f"Round {round} completed!")
                lives = addLives(lives, round)
                round += 1
                print(f"Now starting round {round}")
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
        if mode == 2:
            print(f'You survived until round {round}!\n ')
    return lives
# need to break out smaller methods or split into 2


# methods for perpetual mode
# chooseMode(), addLives(), roundCount(), ??


def chooseMode():
    print("What game mode would you like to play?")
    mode = input("Enter 1 for Normal or 2 for Perpetual\n(Enter 3 for more information)")
    mode = int(mode)
    if mode == 3:
        print("\n \nNormal Mode:")
        print("In normal mode your lives reset each round. You will be asked how many lives you want, and then guess")
        print("until you run out of lives or win that round!\n ")
        print("Perpetual Mode:")
        print("in perpetual mode you set your lives once, and then see how many rounds you can survive.")
        print("There is no winning in perpetual mode... but it does track your high score (of this session)")
        print("so you can play against yourself!\n \n ")
        mode = chooseMode()
    return mode


def play():
    round = 1
    mode = chooseMode()
    lives = setLives()
    while True:
        if mode == 1:
            num = setNumber()
            compareNumber(num, lives, mode, round)
            break
        elif mode == 2:
            while lives > 0:
                num = setNumber()
                lives = compareNumber(num, lives, mode, round)
                round += 1
            break


def addLives(lives, round):
    if round <= 3:
        lives += 3
        print(f"Lives increased to {lives}")
    elif round <= 5:
        lives += 2
        print(f"Lives increased to {lives}")
    elif round > 5:
        lives += 1
        print(f"Lives increased to {lives}")
    return lives



# methods for score keeping
# setHighScore(), increaseScore(), resetScore(), scoreForRound()
