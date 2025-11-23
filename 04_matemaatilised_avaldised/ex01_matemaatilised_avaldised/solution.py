import math
"""Math exercises."""


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b.
    :rtype: tuple
    """
    addition_result = num_a + num_b
    difference = num_a - num_b
    return addition_result, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average =(num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = radius ** 2 * math.pi
    return round(circle_area,2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = math.sqrt(3) / 4 * side_length ** 2
    return round(triangle_area)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = 1
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt((a ** 2 + b ** 2))
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt((c ** 2 - a ** 2))
    return b

if __name__ == '__main__':
    addition_result, difference = sum_and_difference(5, 6)

    assert  addition_result == 11
    assert difference == -1

    float_division_result = float_division(10,2)
    assert 4.99 < float_division_result < 5.01
    assert isinstance(float_division_result, float)

    integer_division_result = integer_division(10,10)
    assert isinstance(integer_division_result, int)
    assert integer_division_result == 1

    integer_division_result = integer_division(10,2)
    assert integer_division_result == 5

    multiplication, power, remainder = powerful_operations(3,4)
    assert multiplication == 12
    assert power == 81
    assert remainder == 3

    multiplication, power, remainder = powerful_operations(10, 2)
    assert multiplication == 20
    assert power == 100
    assert remainder == 0

    area_of_a_circle_result = area_of_a_circle(3)
    assert 28.269 <area_of_a_circle_result < 28.271

