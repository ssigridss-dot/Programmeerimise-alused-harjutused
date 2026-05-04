"""Board games."""


class Statistics:
    """Board games statistics class."""

    def __init__(self, filename):
        """Initialize statistics."""
        self.players: list[Player] = []
        self.games: list[Game] = []
        self.game_sessions: list[GameSession] = []

        self.get_data(filename)

    def get(self, path: str):
        """
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
        p = path.strip("/").split("/")
        if not p:
            return None

        p0 = p[0].lower()
        stats = self.game_sessions

        handlers = {
            "players": lambda: [p.name for p in self.players],
            "games": lambda: [g.name for g in self.games],
            "total": lambda: self.handle_total(p, stats),
            "player": lambda: self.handle_player(p, stats),
            "game": lambda: self.handle_game(p, stats)
        }

        handler = handlers.get(p0)
        return handler() if handler else None

    def handle_total(self, p, stats):
        """Return path handling for total requests."""
        if len(p) == 1:
            return len(stats)
        return sum(1 for r in stats if r.result_type == p[1])

    def handle_player(self, p, stats):
        """Return path handling for specified player requests."""
        name, action = p[1], p[2]
        player = next((pl for pl in self.players if name == pl.name), None)
        if not player:
            return None

        options = {
            "amount": lambda: len(player.games_played),
            "favourite": lambda: player.favourite_game(),
            "won": lambda: player.total_wins(stats)
        }
        return options[action]() if action in options else None

    def handle_game(self, p, stats):
        """Return path handling for specified game requests."""
        name, action = p[1], p[2]
        game = next((g for g in self.games if name == g.name), None)
        if not game:
            return None

        options = {
            "amount": lambda: game.total_sessions(stats),
            "player-amount": lambda: game.most_frequent_player_count(stats),
            "most-wins": lambda: game.most_win_loss_count(stats, "win"),
            "most-frequent-winner": lambda: game.most_frequent_win_loss(stats, "win"),
            "most-losses": lambda: game.most_win_loss_count(stats, "loss"),
            "most-frequent-loser": lambda: game.most_frequent_win_loss(stats, "loss"),
            "record-holder": lambda: game.high_score_holder(stats)
        }
        return options[action]() if action in options else None

    def get_data(self, filename):
        """Get data from file."""
        with open(filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue
                g_name, p_names, res_type, res = line.split(";")
                players = p_names.split(",")
                results = [int(r) if res_type == "points" else r for r in res.split(",")]

                game_obj = Game(g_name, res_type)
                g_add = True
                for g_obj in self.games:
                    if g_obj.name == g_name:
                        game_obj = g_obj
                        g_add = False
                if g_add:
                    self.games.append(game_obj)

                obj_players = []
                for player in players:  # kontrolli kas mängijate objekt eksisteerib, kui ei siis loo, kui jah, siis lisa sellele mängitud mäng
                    player_obj = Player(player)
                    p_add = True
                    for p_obj in self.players:
                        if p_obj.name == player:
                            player_obj = p_obj
                            p_add = False
                    if p_add:
                        self.players.append(player_obj)
                    player_obj.add_games(game_obj)
                    obj_players.append(player_obj)

                session = GameSession(game_obj, obj_players, res_type, results)
                self.game_sessions.append(session)


class Player:
    """Player class."""

    def __init__(self, name):
        """Initialize player."""
        self.name = name
        self.games_played = []

    def total_sessions(self):
        """Return total count of game sessions played."""
        return len(self.games_played)

    def favourite_game(self):
        """Return game most played."""
        return max(set(self.games_played),
                   key=self.games_played.count).name  # teeb järjendist hulga ja siis järjestab enim mängitud järjestusse

    def total_wins(self, stats: list):
        """Return amount of games won."""
        return sum(1 for g in stats if g.winner == self.name)

    def add_games(self, game):
        """Add games to played games list."""
        return self.games_played.append(game)

    def __repr__(self):
        """Return player name."""
        return self.name


class Game:
    """Game class."""

    def __init__(self, name, result_type):
        """Initialize game."""
        self.name = name
        self.result_type = result_type

    def total_sessions(self, stats):
        """Return total times played a game."""
        return sum(1 for g in stats if g.game.name == self.name)

    def most_frequent_player_count(self, stats):
        """Return most frequent player count in a game."""
        player_counts = [len(g.players) for g in stats if g.game.name == self.name]
        if not player_counts:
            return 0
        return max(set(player_counts), key=player_counts.count)

    def win_or_loss(self, stats, win_loss):
        """Return list of game session winners or losers."""
        return [(g.winner if win_loss == "win" else g.lost) for g in stats if g.game.name == self.name]

    def make_unique_list(self, list):
        """Return list of winners or losers unique objects."""
        unique_list = []
        for p in list:
            if p not in unique_list:
                unique_list.append(p)
        return unique_list

    def most_win_loss_count(self, stats, win_lost):
        """Return player name with most wins or losses in the game."""
        win_loss = self.win_or_loss(stats, win_lost)
        u_win_loss = self.make_unique_list(win_loss)
        return max(u_win_loss, key=win_loss.count)

    def most_frequent_win_loss(self, stats, win_lost):
        """Return player with highest rate of wins or losses in the game."""
        win_loss = self.win_or_loss(stats, win_lost)
        unique_list = self.make_unique_list(win_loss)[::-1]

        result_player = None
        max_rate = -1

        for p in unique_list:
            win_count = win_loss.count(p)
            times_played = sum(1 for g in stats if g.game.name == self.name and any(p == pl.name for pl in g.players))
            if times_played == 0:
                continue
            rate = win_count / times_played
            if rate > max_rate:
                max_rate = rate
                result_player = p
        return result_player

    #  zip aitab sorteerida nimekirju koos, range(len on vajalik, et oleks sorteerimise unikaalsus, kuna pythonile ei meeldi objekte võrrelda.

    def high_score_holder(self, stats):
        """Return points game high_score holder, in case same score, return latest."""
        last_hi_score = 0
        hi_score_holder = ""
        if self.result_type == "points":
            for g in stats:
                if g.game.name == self.name:
                    hi_score = max(g.results)
                    if hi_score > last_hi_score:
                        last_hi_score = hi_score
                        hi_score_holder = g.players[g.results.index(hi_score)].name
            return hi_score_holder
        return None

    def __repr__(self):
        """Return game name."""
        return self.name


class GameSession:
    """Game session class."""

    def __init__(self, game, players, result_type, results):
        """Initialize game session."""
        self.game = game
        self.players = players
        self.result_type = result_type
        self.results = results
        self.winner = self.get_session_winner()
        self.lost = self.get_session_loser()

    def get_session_winner(self):
        """Return winner of game session."""
        res_type = self.result_type.lower()
        if res_type == "winner" or res_type == "places":
            return self.results[0]
        if res_type == "points":
            max_points = max(self.results)
            return self.players[self.results.index(max_points)].name
        return None

    def get_session_loser(self):
        """Return loser of game session."""
        res_type = self.result_type.lower()
        if res_type == "places":
            return self.results[-1]
        if res_type == "points":
            min_points = min(self.results)
            return self.players[self.results.index(min_points)].name
        return None


if __name__ == '__main__':
    stats1 = Statistics("test_file.csv")

    """print(stats1.get("/players"))
    print(stats1.get("/games"))
    print(stats1.get("/total"))
    print(stats1.get("/total/winner"))
    print(stats1.get("/player/riho/amount"))
    print(stats1.get("/player/riho/favourite"))
    print(stats1.get("/player/hans/won"))
    print(stats1.get("/game/terraforming mars/amount"))
    print(stats1.get("/game/terraforming mars/player-amount"))
    print(stats1.get("/game/terraforming mars/most-wins"))"""
    print(stats1.get("/game/terraforming mars/most-frequent-winner"))
    # print(stats1.get("/game/terraforming mars/most-losses"))
    print(stats1.get("/game/terraforming mars/most-frequent-loser"))
    # print(stats1.get("/game/terraforming mars/record-holder"))