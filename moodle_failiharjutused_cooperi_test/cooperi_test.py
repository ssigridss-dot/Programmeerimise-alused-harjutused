"""Grade Cooper`s test`s results depending on gender and distance."""
def grade(distance: int, gender: str) -> str:
    if gender == "M":
        very_good_limit = 2800
        satisfactory_limit = 2000
    else:
        very_good_limit = 2600
        satisfactory_limit = 1800

    if distance >= very_good_limit:
        return "väga hea"

    elif distance < satisfactory_limit:
        missing = satisfactory_limit - distance
        return f"nõrk, järgmisest hindest puudu {missing} m"

    else:
        missing = very_good_limit - distance
        return f"rahuldav, järgmisest hindest puudu {missing} m"


filename = input("Sisestage failinimi: ")

sum_m = 0
count_m = 0
sum_n = 0
count_n = 0

with open(filename, "r") as f:
    for line in f:
        parts = line.strip().split()
        distance = int(parts[0])
        gender = parts[1]

        result = grade(distance, gender)
        print(f"{gender} {distance} m, {result}")

        if gender == "M":
            sum_m += distance
            count_m += 1
        else:
            sum_n += distance
            count_n += 1

print("Keskmised:")

if count_m > 0:
    avg_m = round(sum_m / count_m)
    print(f"M {avg_m} m, {grade(avg_m, 'M')}")

if count_n > 0:
    avg_n = round(sum_n / count_n)
    print(f"N {avg_n} m, {grade(avg_n, 'N')}")