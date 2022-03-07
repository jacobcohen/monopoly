from random import randint

class Dice:
    NUM_OF_SIDES = 6
    @classmethod
    def roll(cls):
        return randint(1,cls.NUM_OF_SIDES)