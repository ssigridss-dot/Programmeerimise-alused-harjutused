numbers = [1, 2, 3, 4, 5]

another_numbers = numbers

separate_numbers = numbers[:]

def plus_one(numbers: list[int]) -> list[int]:
    result = numbers[:]
    for i in range(len(numbers)):
        result[i] += 1
    return result

print(numbers)
increased_numbers = plus_one(numbers)
plus_one(numbers)
print(numbers)

numbers[0] = 6
print(numbers)
print(another_numbers)
print(separate_numbers)