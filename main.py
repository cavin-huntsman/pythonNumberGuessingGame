import methods
import time


def main():
    methods.startGame()
    lives = methods.setLives()
    num = methods.setNumber()
#    guess = methods.getNumber()
    methods.compareNumber(num, lives)
    time.sleep(1)


while True:
    main()

#def main():
#    print('__________Welcome to "Guess That Number!"__________')
#    while True:
#        games = input('Enter 1 to play - Enter 0 to quit')
#        games = int(games)
#        if games == 1:
#            number_guess()
#        elif games == 0:
#            break
#    print('__________Thanks for playing!__________')


if __name__ == "__main__":
    main()
