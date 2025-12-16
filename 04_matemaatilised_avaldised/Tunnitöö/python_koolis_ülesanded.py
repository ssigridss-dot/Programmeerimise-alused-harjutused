def compute_rectangle():
    """Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala."""
    length = float(input("Sisesta ristküliku pikkus: "))
    width = float(input("Sisesta ristküliku laius: "))
    area = width * length
    circumference = 2 * (width + length)
    print(f"Antud ristküliku pindala on {area}")
    print(f"Ümbermõõt on {circumference}")


def greet_by_name(name: str) -> str:
    """Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise tervituse koos tekstiga,
    mis ütleb, kas tegemist on 7-18-aastase inimesega."""
    return f"Tervist {name}!"

def verify_age(age: int) -> str:
    if 7 <= age >= age:
        return "Oled 7-18aastane"
    return "Oled noorem või vanem kui 7-18aastane"


def calculate(num1, num2, operation) -> str:
    """
    Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega. Näiteks:

    Sisestage esimene arv: 2
    Sisestage teine arv: 3
    Sisestage tehe: +
    Tulemus: 2+3=5
    """
    result = ""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "//":
        result = num1 // num2
    elif operation == "%":
        result = num1 % num2
    if result == "":
        return f"Tundmatu tehe: {operation}"
    return f"{num1}+{num2}={result}"


def dog_calculate(num1: float, num2: float, operation: str) -> str:
    """Eelmise ülesande alusel koostage programm M-Koer (Matemaatiline Koer), millele antakse samuti ette kaks arvu ja tehtemärk, kuid vastus ei kirjutata mitte arvulisel kujul, vaid esitatakse "haukudes". Igaks juhuks: tsükleid pole vaja kasutada, me pole neid veel õppinud.

    Sisestage esimene arv: 2
    Sisestage teine arv: 3
    Sisestage tehe: +
    Tulemus: auh auh auh auh auh"""
    result = ""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "//":
        result = num1 // num2
    elif operation == "%":
        result = num1 % num2
    if result == "":
        return f"URRRR GRRRRR"
    return f"{round(result)*"auh"}"


def convert_to_fahrenheit(celsius_temperature: float) -> float:
    """Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse
    kraadides ja väljastab tulemuse Fahrenheiti kraadides. Kuidas muuta programmi nii,
    et võimalik oleks teisendamine nii üht- kui teistpidi?"""
    return celsius_temperature * 1.8 + 32


def convert_to_celsius(fahrenheit_temperature: float) -> float:
    """Convert given Fahrenheit temperature to Celsius"""
    return (fahrenheit_temperature - 32) / 1.8


def calculate_discriminant(a: float, b: float, c: float) -> float:
    """Loo programm, mis küsib kasutajalt ruutvõrrandi liikmete (ruutliige,
    lineaarliige, vabaliige) kordajad ning arvutab nende põhjal diskriminandi ja
    väljastab selle põhjal ruutvõrrandi lahendid. Nagu tead, võib lahendeid vastavalt diskriminandi
    väärtusele olla üks või kaks, kuid lahendid võivad ka puududa."""
    return b ** 2 - 4 * a * c


def solve_quadratic_equation(a, b, useAddition):
    import math
    if useAddition:
        top = -b + math.sqrt(discriminant)
    else:
        top = -b - math.sqrt(discriminant)
    bottom = 2 * a
    return top / bottom


if __name__ == '__main__':
    compute_rectangle()

    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus aastates täisarvuna: "))
    greeting = greet_by_name(name)
    age_text = verify_age(age)
    print(greeting, age_text, sep="\n")

    num1 = int(input("Sisestage esimene arv: "))
    num2 = int(input("Sisestage teine arv:"))
    operation = input("Sisestage tehe: ")
    print(f"Vastus: {calculate(num1, num2, operation)}")

    unit = input("Määra sisestatava temperatuuri ühik (C/F): ")
    if unit.upper() == "C":
        temperature_celsius = float(input("Sisesta temperatuur Celsiuse kraadides: "))
        temperature_fahrenheit = convert_to_fahrenheit(temperature_celsius)
        print(f"{temperature_celsius}C on {temperature_fahrenheit:.2f}F kraadi.")
    elif unit.upper() == "F":
        temperature_fahrenheit = float(input("Sisesta temperatuur Fahrenheiti kraadides: "))
        temperature_celsius =  convert_to_celsius(temperature_fahrenheit)
        print(f"{temperature_fahrenheit}F on {temperature_celsius:.2f}C kraadi.")
    else:
        print(f"Sisestasid tundmatu temperatuuriühiku - {unit}")
        print("Programm toetab C - Celsius ja F - Fahrenheiti kraade.")


    print("Arvutame ruutvõrrandit!")
    a = float(input("Sisesta ruutliige: "))
    if a == 0:
        print("Ruutliige ei tohi olla null.")
    else:
        b = float(input("Sisesta lineaarliige: "))
        c = float(input("Sisesta vabaliige: "))
        discriminant = calculate_discriminant(a, b, c)
        if discriminant < 0:
            print("Lahendid puuduvad")
        elif discriminant == 0:
            solution = solve_quadratic_equation(a, b, discriminant, True)
            print(f"Lahendid on võrdsed: {solution}")
        else:
            solution1 = solve_quadratic_equation(a, b, discriminant, True)
            solution2 = solve_quadratic_equation(a, b, discriminant, False)
            print(f"Lahendeid on kaks: {solution1} ja {solution2}")
