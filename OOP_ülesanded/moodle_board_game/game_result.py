"""Board game."""


class GameResult:
    """Game result class."""

    def __init__(self, result_type: str, value):
        """GameResult class constructor.
        :param result_type: points / places / winner
        :param values: tulemused (list)"""
        self.__type = result_type  # points/places/winner
        self.__value = value

    def get_type(self):
        """Get game type."""
        return self.__type

    def get_value(self):
        """Get the result value of the game."""
        return self.__value