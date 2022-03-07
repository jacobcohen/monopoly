from location_set import LocationSet
from player_set import PlayerSet


class GameBoard:
    def __init__(self, player_set: PlayerSet, location_set: LocationSet):
        self.locations = location_set.locations
        #self.locations[0].add_players(player_set.players)


if __name__ == "__main__":
    gb = GameBoard()
