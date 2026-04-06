"""Koosta programm telefoniraamatu loomiseks.

1.       Peab saama sisestada nime ja telefoni numbrit
2.       Samal nimel võib olla ainult üks telefoni number
3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime
    a.       Kui vastet pole, siis peab võimaldama lisamist
4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)
5.       Lisa funktsioon terve raamatu kuvamiseks"""

import csv


def read_phonebook(filename: str) -> dict:
    contacts = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for name, nr in reader:
                contacts[name] = nr
    except FileNotFoundError:
        with open(filename, "w", encoding="utf-8"):
            pass
    return contacts


def save_phonebook(filename: str, contacts: dict) -> None:
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for name, nr in contacts.items():
            writer.writerow([name, nr])


def reverse_dict(d: dict) -> dict:
    reversed_dict = {}

    for key in d:
        value = d[key]
        reversed_dict[value] = key

    return reversed_dict


def add_contact(filename: str) -> None:
    contacts = read_phonebook(filename)

    name = input("Sisesta nimi: ").strip()
    if not name:
        print("Tühi nimi ei ole lubatud!")
        return

    if name in contacts:
        print("See nimi juba eksisteerib!")
        return

    number = input("Sisesta telefoninumber: ").strip()
    if not number:
        print("Tühi number ei ole lubatud!")
        return

    if number in contacts.values():
        print("See number on juba kasutusel!")
        return

    contacts[name] = number
    save_phonebook(filename, contacts)
    print("Kontakt lisatud!")


def find_contact(filename: str) -> None:
    contacts = read_phonebook(filename)
    reversed_contacts = reverse_dict(contacts)

    query = input("Sisesta nimi või number: ").strip()

    if query in contacts:
        print(f"{query}, {contacts[query]}")
    elif query in reversed_contacts:
        print(f"{query} kuulub: {reversed_contacts[query]}")
    else:
        print("Ei leitud!")
        if input("Kas lisada uus kontakt? (y/n): ").lower() == "y":
            add_contact(filename)


def print_phonebook(filename: str) -> None:
    contacts = read_phonebook(filename)

    print("\nTelefoniraamat:")
    print("-" * 30)
    for name, nr in contacts.items():
        print(f"{name:<15} | {nr}")
    print("-" * 30)


def choose_file() -> str:
    filename = input("Sisesta faili nimi: ").strip()
    if not filename:
        print("Faili nimi ei tohi olla tühi!")
        return choose_file()
    return filename


def main():
    filename = choose_file()

    while True:
        print("\n--- Telefoniraamat ---")
        print("1 - Otsi kontakt")
        print("2 - Lisa kontakt")
        print("3 - Kuva kõik")
        print("4 - Muuda faili")
        print("5 - Välju")

        choice = input("Valik: ")

        if choice == "1":
            find_contact(filename)
        elif choice == "2":
            add_contact(filename)
        elif choice == "3":
            print_phonebook(filename)
        elif choice == "4":
            filename = choose_file()
        elif choice == "5":
            print("Head aega!")
            break
        else:
            print("Vale valik!")


if __name__ == "__main__":
    main()