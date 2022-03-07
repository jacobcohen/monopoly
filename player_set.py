from location import Location
from player import Player
import random


class PlayerSet:
    NAME_CHOICES = [
        "Car",
        "Horse",
        "Bean Bag",
        "Jelly Bean",
        "Black Bean",
        "Turtle",
        "The Color Yellow",
        "Cheese?",
        "War: the concept",
        "Jonathan",
    ]

    def __init__(self, num_of_players: int, first_location: Location):
        temp_name_choices = list(self.NAME_CHOICES)
        self._players = [Player(first_location, temp_name_choices.pop()) for _ in range(num_of_players)]
        self._shuffle_players()

    def _shuffle_players(self):
        random.shuffle(self._players)

    @property
    def players(self):
        return self._players