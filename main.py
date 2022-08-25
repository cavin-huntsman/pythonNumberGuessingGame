import methods
import time


def main():
    methods.startGame()
    lives = methods.setLives()
    num = methods.setNumber()
    methods.compareNumber(num, lives)
    time.sleep(1)


while True:
    main()
