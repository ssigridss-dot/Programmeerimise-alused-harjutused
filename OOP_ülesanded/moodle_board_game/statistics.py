"""Board games."""


from player import Player
from game import Game
from play_session import PlaySession
from game_result import GameResult


class Statistics:
    """Board games statistics class."""

    def __init__(self, filename):
        """Initialze statistics from file."""
        self.__players: list[Player] = []
        self.__games: list[Game] = []
        self.__play_sessions: list[PlaySession] = []

        self.__load_file(filename)

    def __get_or_create_player(self, name: str) -> Player:
        for p in self.__players:
            if p.get_name() == name:
                return p

        new_p = Player(name)
        self.__players.append(new_p)
        return new_p

    def __get_or_create_game(self, name: str) -> Game:
        for g in self.__games:
            if g.get_name() == name:
                return g

        new_g = Game(name)
        self.__games.append(new_g)
        return new_g

    def __load_file(self, filename):
        """Read the statistics file."""
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(";")

                game_name = parts[0]
                player_names = parts[1].split(",")
                result_type = parts[2]

                game = self.__get_or_create_game(game_name)
                session = PlaySession(game)

                players = []
                for name in player_names:
                    p = self.__get_or_create_player(name)
                    p.add_game(game_name)
                    session.add_player(p)
                    players.append(p)

                # RESULT PARSING
                if result_type == "points":
                    values = list(map(int, parts[3].split(",")))
                    result = GameResult("points", values)

                    # winner = max points
                    max_points = max(values)
                    winner_index = values.index(max_points)
                    players[winner_index].add_win()

                elif result_type == "places":
                    values = parts[3].split(",")
                    result = GameResult("places", values)

                    winner_name = values[0]
                    for p in players:
                        if p.get_name() == winner_name:
                            p.add_win()

                else:  # winner
                    winner_name = parts[3]
                    result = GameResult("winner", [winner_name])

                    for p in players:
                        if p.get_name() == winner_name:
                            p.add_win()

                session.set_result(result)
                self.__play_sessions.append(session)

    def get(self, path: str):
        """
        API
        REST style path to invoke an action.

        "/players"                          - tagastab listi mängijate nimedest (nimede järjekord pole oluline).
        "/games"                            - tagastab listi mängude nimedest (nimede järjekord pole oluline).
        "/total"                            - tagastab int-i, mis kirjeldab, mitu mängu on mängitud.
        "/total/{result_type}"              - kus {result_type} on string võimalike väärtustega points, places või winner, funktsioon peab tagastama, mitu seda tüüpi mängu on mängitud.
        "/player/{name}/amount"             - tagastab int-i, mis kirjeldab, mitu mängu on mängija nimega player_name mänginud.
        "/player/{name}/favourite"          - tagastab mängu (str, kus on mängu nimi), mida mängija nimega player_name on enim mänginud.
        "/player/{name}/won"                - tagastab int-i, mis kirjeldab, mitu mängu mängija nimega player_name on võitnud.
        "/game/{name}/amount"               - tagastab int-i, mis kirjeldab, mitu mängu nimega name on mängitud.
        "/game/{name}/player-amount"        - tagastab int-i, mis kirjeldab, mitme mängijaga mängu nimega game_name enim / kõige tihedamini mängitud on.
        "/game/{name}/most-wins"            - tagastab mängija string, kellel on mängus nimega game_name enim võite (seda funktsiooni võidakse kutsuda ükskõik, mis tüüpi mängu korral).
        "/game/{name}/most-frequent-winner" - tagastab mängija string, kelle võiduprotsent mängus nimega game_name on suurim (seda funktsiooni võidakse kutsuda ükskõik, mis tüüpi mängu korral).
        "/game/{name}/most-losses"          - tagastab mängija string, kellel on mängus nimega game_name enim kaotusi (viimasele kohale jäämisi) (seda funktsiooni kutsutakse vaid points või places mängu korral).
        "/game/{name}/most-frequent-loser"  - tagastab mängija string, kelle kaotuse protsent (protsent kordadest, kui mängija jäi viimasele kohale) mängus nimega game_name on suurim (seda funktsiooni kutsutakse vaid points või places mängu korral).
        "/game/{name}/record-holder"        - tagastab mängija (string), kes on mängus nimega game_name saanud enim punkte (ühe mängu jooksul), viigi korral tagastada see, kes selle tulemuse esimesena saavutas (seda funktsiooni kutsutakse vaid points mängu korral).
        """
        if path == "/players":
            return [p.get_name() for p in self.__players]

        elif path == "/games":
            return [g.get_name() for g in self.__games]

        elif path == "/total":
            return len(self.__play_sessions)

        elif path.startswith("/player/"):
            parts = path.split("/")
            name = parts[2]
            action = parts[3]

            for p in self.__players:
                if p.get_name() == name:
                    if action == "amount":
                        return p.get_played_game_count()
                    elif action == "favourite":
                        return p.get_favourite_game_name()
                    elif action == "won":
                        return p.get_won_game_count()

        return None