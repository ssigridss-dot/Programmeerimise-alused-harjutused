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