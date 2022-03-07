


from game_board import GameBoard
from game_engine import GameEngine
from location_set import LocationSet
from player_set import PlayerSet


class IOC:
    NUM_OF_LOCATIONS = 40
    NUM_OF_PLAYERS = 8

    def __init__(self):
        location_set = LocationSet(self.NUM_OF_LOCATIONS)
        first_location = location_set.locations[0]
        player_set = PlayerSet(self.NUM_OF_PLAYERS, first_location)
        game_board = GameBoard(player_set, location_set)
        self.game_engine = GameEngine(game_board, player_set)

    def play(self):
        self.game_engine.play()


if __name__ == "__main__":
    ioc = IOC()
    ioc.play()