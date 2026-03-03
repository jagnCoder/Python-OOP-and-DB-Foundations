import threading
import random

class Dice(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__roll = 0
        self.__name = ""
        self.__average = 0.0

    # Setter methods
    def set_roll(self, roll):
        self.__roll = roll

    def set_name(self, name):
        self.__name = name

    # Getter method
    def get_average(self):
        return self.__average

    def run(self):
        total = 0
        for _ in range(self.__roll):
            total += random.randint(1, 6)
        self.__average = total // self.__roll
        print(f"The Average roll of {self.__name}: {self.__average}\n")


def main():
    # Player 1
    name1 = input("Enter the player name 1: ")
    roll1 = int(input("Enter the no. of roll: "))

    # Player 2
    name2 = input("Enter the player name 2: ")
    roll2 = int(input("Enter the no. of roll: "))

    d1 = Dice()
    d1.set_name(name1)
    d1.set_roll(roll1)

    d2 = Dice()
    d2.set_name(name2)
    d2.set_roll(roll2)

    d1.start()
    d2.start()

    d1.join()
    d2.join()


if __name__ == "__main__":
    main()
