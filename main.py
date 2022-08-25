import methods
import time


def main():
    methods.startGame()
    num = methods.setNumber()
    lives = methods.setLives()
    methods.compareNumber(num, lives)
    time.sleep(1.5)


while True:
    main()
