"""Count odds and evens."""


def count_odds_and_evens(numbers: list) -> str:
    r"""
    Return how many odd and even numbers are in the list.

    The task is to count how many odd and even numbers does the given list contain.
    Result should be displayed as string "ODDS: {number of odds}
                                          EVENS: {number of evens}"

    (the second line does not have any spaces before EVENS)

    count_odds_and_evens([1, 2, 3]) => "ODDS: 2\nEVENS: 1" (\n represents new line)
    count_odds_and_evens([1, 3]) => "ODDS: 2\nEVENS: 0" (\n represents new line)

    :param number: int
    :return: str
    """
    odds = 0
    evens = 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"ODDS: {odds}\nEVENS: {evens}")


if __name__ == '__main__':
    count_odds_and_evens([1, 2, 3])
    count_odds_and_evens([1, 3])
