"""Game class."""

class Game:
    """Game class."""

    def __init__(self, name: str):
        """Initialize game object."""
        self.__name = name

    def get_name(self):
        """Return the name of the game."""
        self.__name