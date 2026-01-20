"""Koosta vähemalt kümnest elemendist koosnev järjend arvudest. Koosta programm, mis küsib kasutajalt tegurit
 ja korrutab kõik algses järjendis olnud arvud sellega läbi ning väljastab tulemuse ekraanile.

Sisesta tegur: 3
45 * 3 = 135
7 * 3 = 21
...
267 * 3 = 801"""
from random import randint

def generate_number_list(smallest: int, largest: int) -> list[int]:
    result = []
    for i in range(10):
        random_number = randint(smallest, largest)
        result.append(random_number)
    return result

def ask_user_int(question: str) -> int:
    user_input = input(question)
    while not user_input.isdigit():
        print("Input not an integer. Please try again.")
        user_input = input(question)
    return int(user_input)

def multiply_list(numbers: list[int], multiplier: int) -> list[int]:
    result = []
    for number in numbers:
        result.append(number * multiplier)
    return result

def show_result(original_numbers: list[int], multiplier: int, resulting_numbers:list[int]) -> None:
    for i in range(len(original_numbers)):
        print(f"{original_numbers[i]} * {multiplier} = {resulting_numbers[i]}")


if __name__ == '__main__':
    numbers_list = generate_number_list(1,10)
    print(numbers_list)
    multiplier = ask_user_int("Please insert multiplier: ")
    print(f"{multiplier=}")
    multiplied_list = multiply_list(numbers_list, multiplier)
    print(multiplied_list)
    show_result(numbers_list, multiplier, multiplied_list)