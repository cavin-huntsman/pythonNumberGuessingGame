import methods
import time


def main():
    methods.startGame()  # do you want to start yes or no?
    methods.play()  # play the game
    time.sleep(1.5)


while True:
    main()


#def main2():
#    methods.startGame()
#    mode = methods.chooseMode()
#    num = methods.setNumber()
#    round = 1
#    lives = methods.setLives()
#    methods.compareNumber(num, lives, mode, round)
#    time.sleep(1.5)