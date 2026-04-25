"""Board games."""


class Player:
    """Player class."""

    def __init__(self, name: str):
        """Initialze player."""
        self.__name = name
        self.__games = []

    def get_played_game_count(self) -> int:
        """
        Return the amount of games played.

        "/player/{name}/amount" - tagastab int-i, mis kirjeldab, mitu mängu on mängija nimega player_name mänginud.
        """
        return len(self.__games)

    def get_favourite_game_name(self) -> str:
        """
        Return the name of the game most played.

        "/player/{name}/favourite" - tagastab mängu (str, kus on mängu nimi), mida mängija nimega player_name
        on enim mänginud
        """
        pass

    def get_won_game_count(self) -> int:
        """
        Return count of games won by player.

        "/player/{name}/won" - tagastab int-i, mis kirjeldab, mitu mängu mängija nimega player_name on võitnud.
        """

    def get_name(self):
        """Return name of player."""
        return self.__name