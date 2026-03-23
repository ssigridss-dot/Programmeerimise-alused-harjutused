"""Tests for students_study, lottery and fruit_order."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False
    assert students_study(1, True) is False
    assert students_study(2, True) is False
    assert students_study(4, True) is False


def test__students_study__night_without_coffee__no_studying():
    """During night without coffee students do not study."""
    assert students_study(3, False) is False
    assert students_study(1, False) is False
    assert students_study(2, False) is False
    assert students_study(4, False) is False


def test__students_study__evening_with_coffee__studying():
    """During evening with coffee students study."""
    assert students_study(18, True) is True
    assert students_study(21, True) is True
    assert students_study(24, True) is True


def test__students_study__evening_without_coffee__studying():
    """During evening without coffee students study."""
    assert students_study(18, False) is True
    assert students_study(21, False) is True
    assert students_study(24, False) is True


def test__students_study__day_with_coffee__studying():
    """During day with coffee students study."""
    assert students_study(5, True) is True
    assert students_study(11, True) is True
    assert students_study(17, True) is True


def test__students_study__day_without_coffee__no_studying():
    """During day without coffe students don't study."""
    assert students_study(5, False) is False
    assert students_study(11, False) is False
    assert students_study(17, False) is False


def test_lottery_all_equal():
    """Lottery a is b is c, value 5 returns 10, else 5."""
    assert lottery(5, 5, 5) == 10
    assert lottery(1, 1, 1) == 5
    assert lottery(10, 10, 10) == 5
    assert lottery(-1, -1, -1) == 5
    assert lottery(0, 0, 0) == 5


def test_lottery_a_not_b_or_c():
    """Lottery a is not b or c, returns 1."""
    assert lottery(1, 2, 3) == 1
    assert lottery(1, 3, 3) == 1


def test_lottery_a_is_b_or_c():
    """Lottery a is b or c, returns 0."""
    assert lottery(1, 2, 1) == 0
    assert lottery(1, 1, 3) == 0


def test_fruit_order__large_equal():
    """Big_basket weight equal to ordered_amount."""
    assert fruit_order(10, 2, 10) == 0
    assert fruit_order(1, 3, 15) == 0
    assert fruit_order(0, 3, 15) == 0
    assert fruit_order(9, 2, 10) == 0
    assert fruit_order(0, 400, 2000) == 0
    assert fruit_order(9, 400, 2000) == 0


def test_fruit_order__large_less():
    """Big_basket weight less than ordered_amount."""
    assert fruit_order(10, 1, 10) == 5
    assert fruit_order(5, 1, 15) == -1
    assert fruit_order(0, 2, 25) == -1
    assert fruit_order(7, 1, 12) == 7
    assert fruit_order(2, 2, 7) == 2
    assert fruit_order(6, 2, 17) == -1
    assert fruit_order(1000, 200, 2000) == 1000


def test_fruit_order__large_more():
    """Big_basket weight more than ordered_amount."""
    assert fruit_order(10, 3, 10) == 0
    assert fruit_order(5, 3, 12) == 2
    assert fruit_order(0, 6, 25) == 0
    assert fruit_order(0, 6, 4) == -1
    assert fruit_order(3, 6, 4) == -1
    assert fruit_order(4, 6, 5) == 0
    assert fruit_order(100, 402, 2000) == 0
    assert fruit_order(100, 404, 2001) == 1
    assert fruit_order(1000, 1000, 4000) == 0
    assert fruit_order(3, 1001, 4004) == -1


def test_fruit_order__large_zero():
    """Big_basket weight zero than ordered_amount."""
    assert fruit_order(0, 0, 10) == -1
    assert fruit_order(5, 0, 5) == 5
    assert fruit_order(6, 0, 5) == 5
    assert fruit_order(6, 0, 6) == 6
    assert fruit_order(4, 0, 7) == -1
    assert fruit_order(6, 0, 7) == -1
    assert fruit_order(2000, 0, 2000) == 2000


def test_fruit_order_zero():
    """Ordered_amount equal to zero."""
    assert fruit_order(0, 1, 0) == 0
    assert fruit_order(1, 0, 0) == 0
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(1, 1, 0) == 0
