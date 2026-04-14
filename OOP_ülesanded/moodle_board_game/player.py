"""Player class."""


class Player:
    """Player class."""

    def __init__(self, name: str):
        self.__name = name
        self.__games = []


    def get_player_name_count(self) -> int:
        """Return the amount of game played."""
        return len(self.__games)

    def get_favourite_game_name(self) -> str:
        """Return the name of the game most played."""

    pass

    def get_won_game_count(self) -> int:
        """Return the number of games won."""