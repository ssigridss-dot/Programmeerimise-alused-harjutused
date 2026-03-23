"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    try:
        if time >= 18 and time <= 24:
            return True
        elif time >= 5 and time <= 17 and coffee_needed is True:
            return True
        elif time >= 1 and time <= 4:
            return False
        return False
    except TypeError:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == a == c:
        return 10
    elif a == b == c:
        return 5
    elif a != b and a != c:
        return 1
    elif b != c and b == a or c == a:
        return 0
    return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if ordered_amount == 0:
        return 0
    big_used = min(big_baskets, ordered_amount // 5)
    remaining_order = ordered_amount - big_used * 5
    if remaining_order == 0:
        return 0
    elif remaining_order - small_baskets > 0:
        return -1
    return remaining_order
