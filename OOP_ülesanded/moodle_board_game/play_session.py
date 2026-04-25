"""Board games."""


from player import Player
from game import Game


class PlaySession:
    """Play session class."""

    def __init__(self, game: Game):
        """Initialze statistics."""
        self.__results:  dict[Player, int] = {}
        self.__games: Game = game