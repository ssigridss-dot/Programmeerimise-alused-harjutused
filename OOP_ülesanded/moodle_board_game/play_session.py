"""Board games."""


from player import Player
from game import Game


class PlaySession:
    """Play session class."""

    def __init__(self, game: Game):
        """Initialze session."""
        self.__game = game
        self.__players: list[Player] = []
        self.__results = None

    def add_player(self, player: Player):
        """Add player."""
        self.__players.append(player)

    def set_result(self, result):
        """Show results of the game."""
        self.__results = result

    def get_game(self):
        """Show the name of the game."""
        return self.__game

    def get_players(self):
        """Show players of the game."""
        return self.__players

    def get_result(self):
        """Show the result of the game."""
        return self.__results