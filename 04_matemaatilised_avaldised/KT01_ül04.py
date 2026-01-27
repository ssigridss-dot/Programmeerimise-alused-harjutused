"""
KT 1. ülesanne 4.
1.       Küsi kasutaja sugu ja vanus
2.       Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
3.       Korda tervitust ea suurendamisega kuni tervitus vahetub või 10 korda.
"""
def greet_user(age: int, gender: str) -> str:
    repetitions = 0
    while repetitions < 10:
        if age < 18:
            if gender == "m":
                greeting = "Tere, poiss!"
            else:
                greeting = "Tere, tüdruk!"
        elif age < 65:
            if gender == "m":
                greeting = "Tere, härra!"
            else:
                greeting = "Tere, proua!"
        else:
            if gender == "m":
                greeting = "Tere, vanahärra!"
            else:
                greeting = "Tere, vanaproua!"
        print(f"{greeting}")

        next_age = age + 1
        if next_age < 18:
            if gender == "m":
                next_greeting = "Tere, poiss!"
            else:
                next_greeting = "Tere, tüdruk!"
        elif next_age < 65:
            if gender == "m":
                next_greeting = "Tere, härra!"
            else:
                next_greeting = "Tere, proua!"
        else:
            if gender == "m":
                next_greeting = "Tere, vanahärra!"
            else:
                next_greeting = "Tere, vanaproua!"
        if next_greeting != greeting:
            break
        age += 1
        repetitions += 1


if __name__ == '__main__':
    age = int(input("Kui vana sa oled? "))
    gender = input("Sisesta sugu m/n: ").lower()
    greet_user(age, gender)
