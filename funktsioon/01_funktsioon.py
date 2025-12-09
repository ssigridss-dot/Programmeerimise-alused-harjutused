"""Function examples."""


def func():
    """Print out "I`m inside the function."""
    print("I´m inside the function")


def my_name_is(name):
    """Print out "My name is" with given name."""
    print("My name is", name)


def sum_six(num: int) -> int:
    """Return the sum of 6 and given number."""
    return 6 + num


def sum_numbers(a: int, b: int) -> int:
    """Return the sum of given numbers."""
    return a + b


def usd_to_eur(usd: int) -> float:
    """Convert USD to EUR."""
    return 0.8 * usd


func()
my_name_is("Mari")
print(sum_six(4))
print(sum_numbers(3, 5))
print(usd_to_eur(100))
