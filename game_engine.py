from game_board import GameBoard
from player_set import PlayerSet


class GameEngine:
    def __init__(self,  game_board: GameBoard, player_set: PlayerSet):
        self.game_board = game_board
        self.player_set = player_set
        self.round = 0

    def play(self):
        pass