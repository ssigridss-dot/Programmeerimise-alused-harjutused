"""Koosta programm telefoniraamatu loomiseks."""
def phonebook() -> dict:
    result = {}
    key = int(input("Sisesta telefoninumber: "))
    value = list[input("Sisesta nimi: ")]
    for key, value in result.items():
        result[key].append(value)
    return result

def write_phonebook_csv():
    pass


if __name__ == '__main__':
    phonebook()