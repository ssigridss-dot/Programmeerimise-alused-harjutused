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

    def __get_game_sessions(self, game_name: str):
        """Return game session."""
        return [s for s in self.__play_sessions if s.get_game().get_name() == game_name]

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

        if path == "/games":
            return [g.get_name() for g in self.__games]

        if path == "/total":
            return len(self.__play_sessions)

            # player endpoints
        if path.startswith("/player/"):
            parts = path.split("/")
            name = parts[2]
            action = parts[3]

            for p in self.__players:
                if p.get_name() == name:
                    if action == "amount":
                        return p.get_played_game_count()
                    if action == "favourite":
                        return p.get_favourite_game_name()
                    if action == "won":
                        return p.get_won_game_count()

            # GAME endpoints
        if path.startswith("/game/"):
            parts = path.split("/")
            game_name = parts[2]
            action = parts[3]

            sessions = self.__get_game_sessions(game_name)

            # kui pole mänge
            if not sessions:
                return None

            # amount
            if action == "amount":
                return len(sessions)

            # player-amount (unikaalsed mängijad)
            if action == "player-amount":
                players = set()
                for s in sessions:
                    for p in s.get_players():
                        players.add(p.get_name())
                return len(players)

            # most-wins
            if action == "most-wins":
                win_count = {}
                for s in sessions:
                    result = s.get_result()
                    if result.get_type() == "winner":
                        w = result.get_values()[0]
                        win_count[w] = win_count.get(w, 0) + 1

                return max(win_count, key=win_count.get) if win_count else None

            # most-frequent-winner
            if action == "most-frequent-winner":
                win_rate = {}
                total = {}

                for s in sessions:
                    result = s.get_result()
                    if result.get_type() == "winner":
                        w = result.get_values()[0]
                        total[w] = total.get(w, 0) + 1
                        win_rate[w] = win_rate.get(w, 0) + 1

                best = None
                best_rate = -1

                for p in win_rate:
                    rate = win_rate[p] / total[p]
                    if rate > best_rate:
                        best_rate = rate
                        best = p

                return best

            # most-losses (places only)
            if action == "most-losses":
                losses = {}

                for s in sessions:
                    result = s.get_result()
                    if result.get_type() == "places":
                        last = result.get_values()[-1]
                        losses[last] = losses.get(last, 0) + 1

                return max(losses, key=losses.get) if losses else None

            # most-frequent-loser
            if action == "most-frequent-loser":
                total = {}
                losses = {}

                for s in sessions:
                    result = s.get_result()
                    if result.get_type() == "places":
                        last = result.get_values()[-1]
                        for p in s.get_players():
                            name = p.get_name()
                            total[name] = total.get(name, 0) + 1
                            if name == last:
                                losses[name] = losses.get(name, 0) + 1

                best = None
                best_rate = -1

                for p in losses:
                    rate = losses[p] / total[p]
                    if rate > best_rate:
                        best_rate = rate
                        best = p

                return best

            # record-holder (points game)
            if action == "record-holder":
                best_player = None
                best_score = -1

                for s in sessions:
                    result = s.get_result()
                    if result.get_type() == "points":
                        values = result.get_values()
                        players = s.get_players()

                        for i in range(len(values)):
                            if values[i] > best_score:
                                best_score = values[i]
                                best_player = players[i].get_name()

                return best_player

        return None