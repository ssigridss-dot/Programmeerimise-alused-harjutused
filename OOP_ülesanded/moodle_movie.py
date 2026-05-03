"""Movie."""


class Movie:
    """Movie class, do not change."""

    def __init__(self, name: str, year: int, genres: list):
        """Movie constructor."""
        self.name = name
        self.year = year
        self.genres = genres


def create_movie(name_with_year: str, genre1: str, genre2: str):
    """
    Create a new movie from name and 2 genres.

    Name is in format "name some thing (2019)".
    Year is inside parenthesis and always 4 digits.
    Everything before parenthesis is a name.
    Return None, if:
    - year is below 1900 and above 2020 ("blah (1200)", "blah (3000)")
    - name is empty ("(1933)")
    Otherwise create a new movie and return it.

    Year has to be int.
    Remove trailing space from name.
    "film (1999)" => should give "film" 1999
    """
    # leia sulgude asukohad
    start = name_with_year.find("(")
    end = name_with_year.find(")")

    if start == -1 or end == -1:
        return None

    name = name_with_year[:start].strip()
    year_str = name_with_year[start + 1:end]

    # kontroll: nimi ei tohi olla tühi
    if name == "":
        return None

    # kontroll: aasta peab olema number
    if not year_str.isdigit():
        return None

    year = int(year_str)

    # kontroll: aasta vahemik
    if year < 1900 or year > 2020:
        return None

    return Movie(name, year, [genre1, genre2])


def get_ordered_movies(movies: list) -> list:
    """
    Return sorted movies by year (desc, newer first) and count of genres (asc).

    If both year and count of genres are the same, keep the original order.
    """
    return sorted(movies, key=lambda m: (-m.year, len(m.genres)))


def add_genres(movies: list, genres: list) -> None:
    """
    Modify the movies in the list by adding genres.

    A genre is added if it does not already exist.
    """
    for movie in movies:
        for genre in genres:
            if genre not in movie.genres:
                movie.genres.append(genre)


def remove_movies_by_genre(movies: list, genre: str) -> list:
    """
    Return a new list where all the movies with the given genre are removed.

    The order of movies should remain the same.
    The original movies list should remain unchanged.
    """
    result = []
    for movie in movies:
        if genre not in movie.genres:
            result.append(movie)
    return result


if __name__ == '__main__':
    m1 = create_movie("Matrix (1999)", "action", "sci-fi")
    m2 = create_movie("Titanic (1997)", "drama", "romance")
    m3 = create_movie("Avatar (2009)", "action", "fantasy")
    m4 = create_movie("(2000)", "test", "test")  # None

    movies = [m for m in [m1, m2, m3, m4] if m is not None]

    print("Algne nimekiri:")
    for m in movies:
        print(m.name, m.year, m.genres)

    print("\nLisa genre 'adventure':")
    add_genres(movies, ["adventure"])
    for m in movies:
        print(m.name, m.genres)

    print("\nSorteeritud filmid:")
    sorted_movies = get_ordered_movies(movies)
    for m in sorted_movies:
        print(m.name, m.year, len(m.genres))

    print("\nEemalda 'romance' žanriga filmid:")
    filtered = remove_movies_by_genre(movies, "romance")
    for m in filtered:
        print(m.name, m.genres)
