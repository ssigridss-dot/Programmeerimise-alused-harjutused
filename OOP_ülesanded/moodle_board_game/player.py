"""Board games."""


class Player:
    """Player class."""

    def __init__(self, name: str):
        """Initialze player."""
        self.__name = name
        self.__games = []  # (game_name, result_type, value, players_list)
        self.__wins = 0

    def add_game(self, game_name: str):
        """Add played game."""
        self.__games.append(game_name)

    def add_win(self):
        """Add win."""
        self.__wins += 1

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
        if not self.__games:
            return None

        counts = {}
        for g in self.__games:
            counts[g] = counts.get(g, 0) + 1

        return max(counts, key=counts.get)

    def get_won_game_count(self) -> int:
        """
        Return count of games won by player.

        "/player/{name}/won" - tagastab int-i, mis kirjeldab,
        mitu mängu mängija nimega player_name on võitnud.
        """
        return self.__wins

    def get_name(self):
        """Return name of player."""
        return self.__name