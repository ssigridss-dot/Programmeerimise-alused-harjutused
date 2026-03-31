"""Close far."""


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """

    def is_close(x, y):
        return abs(x - y) <= 1

    def is_far(x, y):
        return abs(x - y) >= 2

    case1 = is_close(a, b) and is_far(a, c) and is_far(b, c)
    case2 = is_close(a, c) and is_far(a, b) and is_far(b, c)

    return case1 or case2


if __name__ == '__main__':
    print(close_far(1, 2, 10))
    print(close_far(1, 2, 3))
    print(close_far(4, 1, 3))
