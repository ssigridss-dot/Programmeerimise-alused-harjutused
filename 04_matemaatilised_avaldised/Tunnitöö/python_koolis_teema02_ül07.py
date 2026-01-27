from datetime import datetime
"""
Eestis kasutatav isikukood koosneb üheteistkümnest numbrist. Tutvu isikukoodi struktuuriga
(https://et.wikipedia.org/wiki/Isikukood) ja kirjuta programm, mis analüüsib isikukoode ja väljastab võimalikult
rohkem infot selle kohta (sünnikuupäev, sugu jne). Isikukoodi käsitlege kui sümbolite kogumit ehk sõnet (kuigi see
koosneb numbritest), analüüsimiseks kasutage sõneoperatsioone (vt. käsiraamat). Kuna isikukoode on keeruline
testimise ajal korduvalt sisestada, on alguses mõistlik sisestada erinevad isikukoodid ning kommenteerida vastavalt
vajadusele ülearused välja, näiteks järgnevalt kasutatakse teisel real olevat isikukoodi:

#isikukood = "60201302715"
isikukood = "48008082727"
#isikukood = "31212230156"
[...]
Hiljem võib lisada isikukoodi küsimise kasutajalt.

Täiendusi:
Vastavalt toodud isikukoodi tutvustavale artiklile võrdle esimest kümmet numbrit ja viimast numbrit
(nn. kontrollnumbrit), et teha selgeks, kas isikukood on üldse kehtiv. Kuna isikukoodi võtame kui sõnet,
aga seal olevaid arve on vaja korrutada, peame tegema tüübiteisenduse: sõnena oleva arvu peame teisendama
täisarvuks (funktsioon "int()").
Koosta funktsioon, mis ise automaatselt koostab kehtivaid isikukoode. Võimatud on näiteks isikukoodid vale
kontrollnumbriga, kuid ka sellised, mis viitavad olematule kuupäevale
(algusega "3950230...", mis tähendaks 30. veebruari) vms. Vali kas "ohutu" tee (ette on antud piirid, mis
kehtivad igal juhul) või loo sisemised sõltuvused (stiilis "kui kuu on aprill, siis maksimaalsete päevade arv on 30").
"""


def has_correct_checksum(id_code: str) -> bool:
    return get_check_sum(id_code) == int(id_code[-1])


def is_valid(id_code: str) -> bool:
    return len(id_code) == 11 and id_code.isdigit() and has_correct_checksum(id_code)


def get_century(id_code: str) -> int:
   first_number = get_first_number(id_code)
   if first_number <= 2:
       return 1800
   elif first_number <= 4:
       return 1900
   elif first_number <= 6:
       return 2000
   elif first_number <= 8:
       return 2100
   return -1


def get_century_match(id_code: str) -> int:
    first_number = get_first_number(id_code)
    result = 0
    match first_number:
        case 1 | 2:
            result = 1800
        case 3 | 4:
            result = 1900
        case 5 | 6:
            result = 2000
        case 7 | 8:
            result = 2100
        case _:
            result = -1
    return result


def get_century_dict(id_code: str) -> int:
    century = {"1":1800,"2":1800,"3":1900,"4":1900,"5":2000,"6":2000,"7":2100,"8":2100}
    return century.get(id_code[0], -1)


def get_first_number(id_code: str):
    return int(id_code[0])


def get_gender(id_code: str) -> str:
    first_number = get_first_number(id_code)
    if first_number % 2 == 0:
        return "naine"
    return "mees"


def get_numbers(id_code: str, start: int, count: int) -> int:
    return int(id_code[start:start+count])


def get_year(id_code: str, century: int) -> int:
    year = century
    year += get_numbers(id_code, start=1, count=2)
    return year


def get_month(id_code: str) -> int:
    return get_numbers(id_code, start=3, count=2)


def get_day(id_code: str) -> int:
    return get_numbers(id_code, start=5, count=2)


def get_date(year: int, month: int, day: int) -> datetime:
    return datetime(year, month, day)


def get_date_string(date: datetime) -> str:
    return date.strftime("%A %d %B %Y")


def get_product_sum(id_code: str, weights: list[int]) -> int:
    result_sum = 0
    for index, weight in enumerate(weights):
        id_number = int(id_code[index])
        product = id_number * weight
        result_sum += product
    return result_sum


def get_check_sum(id_code: str) -> int:
    level_one_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    level_two_weights = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    product_sum = get_product_sum(id_code, level_one_weights)
    remainder = product_sum % 11
    if remainder < 10:
        return remainder
    product_sum = get_product_sum(id_code, level_two_weights)
    remainder = product_sum % 11
    if remainder < 10:
        return remainder
    return 0


def decode_id_code(id_code: str) -> None:
    if is_valid(id_code):
        century = get_century(id_code)
        gender = get_gender(id_code)
        year = get_year(id_code, century)
        month = get_month(id_code)
        day = get_day(id_code)
        birth_date = get_date(year, month, day)
        print(f"Sinu sugu: {gender},\nSünni kuupäev: {get_date_string(birth_date)}.")
    else:
        print(f"Viga sisestatud isikukoodis: {id_code}")


if __name__ == '__main__':
    # isikukood = "60201302715"
    isikukood = "48008082727"
    # isikukood = "31212230156"
    decode_id_code(isikukood)