"""
KT 1. ülesanne 3.
1.       Küsi kasutaja vanust ja nime
2.       Tervita kasutajat nime pidi niimitu korda kui mitu aastat ta on täisealine olnud (Kordus)
3.       Kirjuta ekraanile nime lõpust 3 tähte.
"""
def greet_user(name: str, age: int) -> str:
    agelimit = 18
    for i in range(max(0, age - agelimit)):
        print(f"Tere, {name}!")
    return name

def last_chars(name):
    print(name[-3:])


if __name__ == '__main__':
    name = input("Mis on sinu nimi? ")
    age = int(input("Kui vana sa oled? "))
    greet_user(name, age)
    last_chars(name)