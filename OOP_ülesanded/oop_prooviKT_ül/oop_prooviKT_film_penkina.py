class Movie:
    """
    Represents a movie.
    """

    count = 0

    def __init__(self, title, duration):
        """
        Constructor.
        """
        self.title = title
        self.duration = duration
        Movie.count += 1

    def play(self):
        """
        Plays movie.
        """
        return "Playing movie"

    def info(self):
        """
        Movie info.
        """
        return f"{self.title}, {self.duration} min"


class CinemaMovie(Movie):
    """
    Inherited Movie class.
    """

    def __init__(self, title="Film", duration=120, genre="Drama"):
        """
        Default constructor.
        """
        super().__init__(title, duration)
        self.genre = genre

    def genre_info(self):
        """
        Returns genre.
        """
        return f"Genre: {self.genre}"


if __name__ == "__main__":
    m = CinemaMovie()
    print(m.play())
    print(m.info())
    print(m.genre_info())
    print(Movie.count)